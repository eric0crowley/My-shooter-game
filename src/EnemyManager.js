import * as THREE from 'three';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';
import { clamp, resolveCircleBoxes, segmentIntersectsBox } from './collision.js';
import { RECOVERED_ZOMBIE_ASSET } from './recoveredAssets.js';

const TRAINING_BOT = {
  health: 100,
  speed: 3.2,
  detectRange: 60,
  shootRange: 22,
  hitChance: 0.34,
  attackRange: 1.6,
  fireRate: 1.1,
  damage: 8,
};

export function zombieWavePlan(wave) {
  const level = Math.max(1, Math.floor(Number(wave) || 1));
  return {
    count: Math.min(36, 5 + level * 2),
    maxAlive: Math.min(10, 6 + Math.floor(level / 2)),
    health: 72 + (level - 1) * 11,
    speed: Math.min(3.8, 2.55 + (level - 1) * 0.11),
    damage: Math.min(28, 12 + (level - 1) * 1.5),
    attackRate: Math.max(0.62, 1.15 - (level - 1) * 0.035),
  };
}

function disposeMaterial(material) {
  if (Array.isArray(material)) material.forEach((part) => part.dispose());
  else material?.dispose();
}

export class Enemy {
  constructor(scene, spawn, manager, kind = 'bot', stats = {}) {
    this.scene = scene;
    this.manager = manager;
    this.kind = kind;
    this.netId = null;
    this.radius = kind === 'zombie' ? 0.48 : 0.5;
    this.alive = true;
    this.health = 100;
    this.maxHealth = 100;
    this.speed = 0;
    this.detectRange = 40;
    this.shootRange = 0;
    this.hitChance = 1;
    this.attackRange = 1.6;
    this.attackRate = 1;
    this.damage = 0;
    this.attackCooldown = 0;
    this.respawnAt = null;
    this.animationTime = Math.random() * Math.PI * 2;

    this.group = new THREE.Group();
    this.group.userData.enemy = this;
    this.makeModel();
    if (manager.recoveredZombieTemplate) this.setRecoveredVisual(manager.recoveredZombieTemplate);
    scene.add(this.group);
    this.spawnAt(spawn, stats);
  }

  makeModel() {
    const isZombie = this.kind === 'zombie';
    this.fallbackVisual = new THREE.Group();
    const bodyMaterial = new THREE.MeshStandardMaterial({
      color: isZombie ? 0x62734b : 0xcc4433,
      roughness: 0.78,
      metalness: 0.02,
    });
    const skinMaterial = new THREE.MeshStandardMaterial({
      color: isZombie ? 0x9b9a69 : 0xd7ab8d,
      roughness: 0.9,
    });
    const body = new THREE.Mesh(new THREE.CapsuleGeometry(0.4, 0.9, 4, 8), bodyMaterial);
    body.position.y = 0.9;
    body.castShadow = true;
    body.userData.part = 'body';
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.28, 12, 12), skinMaterial);
    head.position.y = 1.7;
    head.castShadow = true;
    head.userData.part = 'head';
    this.fallbackVisual.add(body, head);
    this.head = head;

    if (isZombie) {
      const armGeometry = new THREE.CapsuleGeometry(0.115, 0.58, 3, 6);
      const leftArm = new THREE.Mesh(armGeometry, skinMaterial);
      leftArm.position.set(-0.43, 1.1, 0.06);
      leftArm.rotation.z = -0.75;
      leftArm.castShadow = true;
      leftArm.userData.part = 'body';
      const rightArm = new THREE.Mesh(armGeometry, skinMaterial);
      rightArm.position.set(0.43, 1.1, 0.06);
      rightArm.rotation.z = 0.75;
      rightArm.castShadow = true;
      rightArm.userData.part = 'body';
      const eyeMaterial = new THREE.MeshBasicMaterial({ color: 0xf07d43 });
      const leftEye = new THREE.Mesh(new THREE.SphereGeometry(0.045, 6, 6), eyeMaterial);
      const rightEye = leftEye.clone();
      leftEye.position.set(-0.105, 1.73, 0.248);
      rightEye.position.set(0.105, 1.73, 0.248);
      this.fallbackVisual.add(leftArm, rightArm, leftEye, rightEye);
      this.leftArm = leftArm;
      this.rightArm = rightArm;
    }
    this.group.add(this.fallbackVisual);
  }

  setRecoveredVisual(template) {
    if (this.kind !== 'zombie' || this.recoveredVisual || !template) return;
    const visual = template.clone(true);
    visual.traverse((object) => {
      if (!object.isMesh) return;
      if (object.geometry) object.geometry = object.geometry.clone();
      if (Array.isArray(object.material)) {
        object.material = object.material.map((material) => material.clone());
      } else if (object.material) {
        object.material = object.material.clone();
      }
      object.userData.part = object.name.toLowerCase().includes('head') ? 'head' : 'body';
      object.castShadow = true;
      object.receiveShadow = true;
    });
    this.recoveredVisual = visual;
    this.group.add(visual);
    this.fallbackVisual.visible = false;
  }

  spawnAt(pos, stats = {}) {
    const defaults = this.kind === 'zombie' ? zombieWavePlan(1) : TRAINING_BOT;
    this.maxHealth = stats.health ?? defaults.health;
    this.health = this.maxHealth;
    this.speed = stats.speed ?? defaults.speed;
    this.detectRange = stats.detectRange ?? (this.kind === 'zombie' ? 44 : defaults.detectRange);
    this.shootRange = stats.shootRange ?? defaults.shootRange;
    this.hitChance = stats.hitChance ?? defaults.hitChance ?? 1;
    this.attackRange = stats.attackRange ?? (this.kind === 'zombie' ? 1.55 : defaults.attackRange);
    this.attackRate = stats.attackRate ?? (this.kind === 'zombie' ? defaults.attackRate : defaults.fireRate);
    this.damage = stats.damage ?? defaults.damage;
    this.attackCooldown = 0.35 + Math.random() * 0.55;
    this.respawnAt = null;
    this.animationTime = Math.random() * Math.PI * 2;
    this.group.position.set(pos.x, 0, pos.z);
    this.group.rotation.set(0, 0, 0);
    this.group.visible = true;
    this.alive = true;
  }

  takeDamage(amount) {
    if (!this.alive || amount <= 0) return;
    this.health -= amount;
    if (this.health <= 0) this.die();
  }

  die() {
    if (!this.alive) return;
    this.alive = false;
    this.group.visible = false;
    this.manager.onKill(this);
  }

  hasLineOfSight(target, colliders) {
    const from = this.group.position;
    for (const box of colliders) {
      if (segmentIntersectsBox(from.x, from.z, target.x, target.z, box)) return false;
    }
    return true;
  }

  moveToward(target, dt, colliders, bounds, distance) {
    const from = this.group.position;
    if (distance <= this.attackRange * 0.8) return;
    const baseAngle = Math.atan2(target.x - from.x, target.z - from.z);
    const offsets = [0, 0.55, -0.55, 1.05, -1.05, 1.6, -1.6];
    let best = { x: from.x, z: from.z, distance };

    for (const offset of offsets) {
      const angle = baseAngle + offset;
      let x = from.x + Math.sin(angle) * this.speed * dt;
      let z = from.z + Math.cos(angle) * this.speed * dt;
      [x, z] = resolveCircleBoxes(x, z, this.radius, colliders);
      x = clamp(x, -bounds + this.radius, bounds - this.radius);
      z = clamp(z, -bounds + this.radius, bounds - this.radius);
      const nextDistance = Math.hypot(target.x - x, target.z - z);
      if (nextDistance < best.distance - 0.0001) best = { x, z, distance: nextDistance };
    }

    from.x = best.x;
    from.z = best.z;
  }

  animate(dt) {
    if (!this.alive) return;
    this.animationTime += dt;
    if (this.kind === 'zombie' && this.leftArm) {
      this.leftArm.rotation.z = -0.75 + Math.sin(this.animationTime * 5.2) * 0.14;
      this.rightArm.rotation.z = 0.75 + Math.sin(this.animationTime * 5.2 + 1.2) * 0.14;
      this.group.position.y = Math.sin(this.animationTime * 5.2) * 0.025;
    }
  }

  update(dt, player, colliders, bounds) {
    if (!this.alive) return;
    this.animate(dt);

    const candidates = Array.isArray(player) ? player : [player];
    let targetPlayer = null;
    let target = null;
    let distance = Infinity;
    const from = this.group.position;
    for (const candidate of candidates) {
      if (!candidate?.camera?.position || candidate.alive === false) continue;
      const candidateDistance = Math.hypot(
        candidate.camera.position.x - from.x,
        candidate.camera.position.z - from.z
      );
      if (candidateDistance < distance) {
        targetPlayer = candidate;
        target = candidate.camera.position;
        distance = candidateDistance;
      }
    }
    if (!targetPlayer) return;

    const dx = target.x - from.x;
    const dz = target.z - from.z;
    this.group.rotation.y = Math.atan2(dx, dz);
    this.attackCooldown -= dt;
    if (distance > this.detectRange) return;

    const canSeeTarget = this.hasLineOfSight(target, colliders);
    if (this.kind === 'bot') {
      if (distance > this.shootRange || !canSeeTarget) {
        this.moveToward(target, dt, colliders, bounds, distance);
      }
      const shotDistance = Math.hypot(target.x - from.x, target.z - from.z);
      if (shotDistance > this.shootRange || this.attackCooldown > 0 || !canSeeTarget) return;

      this.attackCooldown = this.attackRate;
      const hit = Math.random() < this.hitChance;
      this.manager.spawnTracer(from, target, hit);
      if (hit) targetPlayer.damage(this.damage);
      return;
    }

    this.moveToward(target, dt, colliders, bounds, distance);
    const updatedDistance = Math.hypot(target.x - from.x, target.z - from.z);
    if (updatedDistance > this.attackRange || this.attackCooldown > 0 || !canSeeTarget) return;

    this.attackCooldown = this.attackRate;
    targetPlayer.damage(this.damage);
  }
}

export class EnemyManager {
  constructor(scene, spawns, colliders, bounds) {
    this.scene = scene;
    this.spawns = spawns;
    this.colliders = colliders;
    this.bounds = bounds;
    this.enemies = [];
    this.score = 0;
    this.kills = 0;
    this.mode = 'training';
    this.wave = 0;
    this.waveQueue = 0;
    this.maxZombiesAlive = 8;
    this.waveIntermission = 0;
    this.spawnCooldown = 0;
    this.elapsed = 0;
    this.tracers = [];
    this.nextNetId = 1;
    this.networkClient = false;
    this.onKillEvent = null;
    this.onWaveStart = null;
    this.recoveredZombieTemplate = null;
    if (typeof document !== 'undefined') void this.loadRecoveredZombieModel();
  }

  async loadRecoveredZombieModel() {
    try {
      const objectLoader = new OBJLoader();
      const textureLoader = new THREE.TextureLoader();
      const [importedModel, texture] = await Promise.all([
        objectLoader.loadAsync(RECOVERED_ZOMBIE_ASSET.model),
        textureLoader.loadAsync(RECOVERED_ZOMBIE_ASSET.texture),
      ]);
      texture.colorSpace = THREE.SRGBColorSpace;
      texture.anisotropy = 4;
      const sourceMesh = importedModel.getObjectByProperty('isMesh', true);
      if (!sourceMesh) throw new Error('Recovered ZombieC OBJ contains no mesh.');

      importedModel.updateMatrixWorld(true);
      const sourceBounds = new THREE.Box3().setFromObject(importedModel);
      const sourceSize = sourceBounds.getSize(new THREE.Vector3());
      const sourceHeight = sourceSize.y;
      if (!Number.isFinite(sourceHeight) || sourceHeight <= 0) {
        throw new Error('Recovered ZombieC mesh has no usable height.');
      }
      const material = new THREE.MeshStandardMaterial({
        map: texture,
        roughness: 0.9,
        metalness: 0,
        alphaTest: 0.45,
      });
      importedModel.traverse((object) => {
        if (!object.isMesh) return;
        object.material = material;
        object.userData.part = 'body';
        object.castShadow = true;
        object.receiveShadow = true;
      });

      // OBJ preserves the bind pose but not the rig. Keep a non-rendering head
      // hit volume so the existing headshot damage behavior still works.
      const hitboxMaterial = new THREE.MeshBasicMaterial({
        transparent: true,
        opacity: 0,
        colorWrite: false,
        depthWrite: false,
      });
      const headHitbox = new THREE.Mesh(
        new THREE.SphereGeometry(sourceHeight * 0.085, 10, 8),
        hitboxMaterial
      );
      headHitbox.name = 'ZombieC_HeadHitbox';
      headHitbox.userData.part = 'head';
      const sourceCenter = sourceBounds.getCenter(new THREE.Vector3());
      headHitbox.position.set(sourceCenter.x, sourceBounds.min.y + sourceHeight * 0.88, sourceCenter.z);
      importedModel.add(headHitbox);
      const model = importedModel;
      model.scale.setScalar(RECOVERED_ZOMBIE_ASSET.targetHeight / sourceHeight);
      model.updateMatrixWorld(true);
      const fittedBounds = new THREE.Box3().setFromObject(model);
      const fittedCenter = fittedBounds.getCenter(new THREE.Vector3());
      model.position.set(-fittedCenter.x, -fittedBounds.min.y, -fittedCenter.z);
      model.userData.recoveredAssetId = RECOVERED_ZOMBIE_ASSET.sourceMesh;
      model.updateMatrixWorld(true);

      this.recoveredZombieTemplate = model;
      for (const enemy of this.enemies) enemy.setRecoveredVisual(model);
    } catch (error) {
      // Keep the original procedural zombie if browser loading fails.
      console.warn('Could not load recovered ZombieC character model.', error);
    }
  }

  registerEnemy(enemy) {
    enemy.netId = this.nextNetId++;
    this.enemies.push(enemy);
    return enemy;
  }

  get aliveCount() {
    return this.enemies.reduce((count, enemy) => count + Number(enemy.alive), 0);
  }

  get remainingCount() {
    return this.mode === 'zombie' ? this.aliveCount + this.waveQueue : this.aliveCount;
  }

  getMeshes() {
    return this.enemies.map((enemy) => enemy.group);
  }

  clearActors() {
    for (const enemy of this.enemies) {
      this.scene.remove(enemy.group);
      enemy.group.traverse((object) => {
        object.geometry?.dispose();
        if (object.material) disposeMaterial(object.material);
      });
    }
    this.enemies = [];
    for (const tracer of this.tracers) {
      this.scene.remove(tracer.line);
      tracer.line.geometry.dispose();
      tracer.line.material.dispose();
    }
    this.tracers = [];
  }

  start(mode = 'training') {
    this.clearActors();
    this.mode = mode === 'zombie' ? 'zombie' : 'training';
    this.score = 0;
    this.kills = 0;
    this.elapsed = 0;
    this.wave = 0;
    this.waveQueue = 0;
    this.nextNetId = 1;
    this.networkClient = false;
    this.waveIntermission = 0;
    this.spawnCooldown = 0;

    if (this.mode === 'training') {
      for (let i = 0; i < 6; i++) {
        const spawn = this.spawns[i % this.spawns.length];
        this.registerEnemy(new Enemy(this.scene, spawn, this, 'bot'));
      }
      return;
    }

    this.beginWave(1);
  }

  beginWave(wave) {
    const plan = zombieWavePlan(wave);
    this.wave = wave;
    if (this.onWaveStart) this.onWaveStart(wave);
    this.waveQueue = plan.count;
    this.maxZombiesAlive = plan.maxAlive;
    this.spawnCooldown = 0.25;
  }

  chooseSpawn(target) {
    const candidates = this.spawns.filter((spawn) => Math.hypot(spawn.x - target.x, spawn.z - target.z) > 12);
    const options = candidates.length ? candidates : this.spawns;
    return options[Math.floor(Math.random() * options.length)];
  }

  spawnZombie(player) {
    const plan = zombieWavePlan(this.wave);
    const target = Array.isArray(player) ? player[0] : player;
    const spawn = this.chooseSpawn(target.camera.position);
    let zombie = this.enemies.find((enemy) => enemy.kind === 'zombie' && !enemy.alive);
    if (!zombie) {
      zombie = this.registerEnemy(new Enemy(this.scene, spawn, this, 'zombie', plan));
    } else {
      zombie.spawnAt(spawn, plan);
    }
    this.waveQueue--;
  }

  onKill(enemy) {
    if (this.networkClient) return;
    this.score++;
    this.kills++;
    if (this.onKillEvent) this.onKillEvent(enemy);
    if (this.mode === 'training') {
      enemy.respawnAt = this.elapsed + 1.5 + Math.random() * 1.5;
    } else {
      enemy.respawnAt = null;
    }
  }

  getNetworkState() {
    return {
      mode: this.mode,
      wave: this.wave,
      waveQueue: this.waveQueue,
      waveIntermission: this.waveIntermission,
      kills: this.kills,
      enemies: this.enemies.map((enemy) => ({
        id: enemy.netId,
        kind: enemy.kind,
        x: enemy.group.position.x,
        y: enemy.group.position.y,
        z: enemy.group.position.z,
        yaw: enemy.group.rotation.y,
        health: enemy.health,
        maxHealth: enemy.maxHealth,
        alive: enemy.alive,
        animationTime: enemy.animationTime,
        speed: enemy.speed,
      })),
    };
  }

  applyNetworkState(state) {
    if (!state || !Array.isArray(state.enemies)) return;
    this.mode = state.mode === 'zombie' ? 'zombie' : 'training';
    this.wave = Math.max(0, Math.floor(Number(state.wave) || 0));
    this.waveQueue = Math.max(0, Math.floor(Number(state.waveQueue) || 0));
    this.waveIntermission = Math.max(0, Number(state.waveIntermission) || 0);
    this.kills = Math.max(0, Math.floor(Number(state.kills) || 0));
    this.score = this.kills;

    const receivedIds = new Set();
    let highestId = 0;
    for (const remote of state.enemies) {
      const id = Number(remote?.id);
      const x = Number(remote?.x);
      const y = Number(remote?.y);
      const z = Number(remote?.z);
      if (!Number.isInteger(id) || id < 1 || ![x, y, z].every(Number.isFinite)) continue;
      const kind = remote.kind === 'zombie' ? 'zombie' : 'bot';
      const maxHealth = Math.max(1, Number(remote.maxHealth) || 100);
      let enemy = this.enemies.find((candidate) => candidate.netId === id);
      if (!enemy) {
        enemy = new Enemy(this.scene, new THREE.Vector3(x, y, z), this, kind, {
          health: maxHealth,
          speed: Math.max(0, Number(remote.speed) || 0),
        });
        enemy.netId = id;
        this.enemies.push(enemy);
      }

      const alive = remote.alive === true;
      if (alive && !enemy.alive) {
        enemy.spawnAt(new THREE.Vector3(x, y, z), {
          health: maxHealth,
          speed: Math.max(0, Number(remote.speed) || enemy.speed),
        });
      }
      enemy.alive = alive;
      enemy.group.visible = alive;
      enemy.group.position.set(x, y, z);
      enemy.group.rotation.y = Number.isFinite(Number(remote.yaw)) ? Number(remote.yaw) : 0;
      enemy.maxHealth = maxHealth;
      enemy.health = Math.max(0, Math.min(maxHealth, Number(remote.health) || 0));
      if (Number.isFinite(Number(remote.animationTime))) enemy.animationTime = Number(remote.animationTime);
      enemy.respawnAt = null;
      receivedIds.add(id);
      highestId = Math.max(highestId, id);
    }

    for (const enemy of this.enemies) {
      if (!receivedIds.has(enemy.netId)) {
        enemy.alive = false;
        enemy.group.visible = false;
      }
    }
    this.nextNetId = Math.max(this.nextNetId, highestId + 1);
  }

  spawnTracer(from, to, hit = true) {
    const end = new THREE.Vector3(to.x, to.y, to.z);
    if (!hit) {
      end.x += (Math.random() * 2 - 1) * 1.8;
      end.y += (Math.random() * 2 - 1) * 0.9;
      end.z += (Math.random() * 2 - 1) * 1.8;
    }
    const geo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(from.x, from.y + 1.2, from.z),
      end,
    ]);
    const mat = new THREE.LineBasicMaterial({ color: 0xff5533, transparent: true, opacity: 0.85 });
    const line = new THREE.Line(geo, mat);
    this.scene.add(line);
    this.tracers.push({ line, life: 0.12 });
  }

  update(dt, player) {
    this.elapsed += dt;
    if (this.networkClient) {
      for (const enemy of this.enemies) enemy.animate(dt);
    } else {
      for (const enemy of this.enemies) enemy.update(dt, player, this.colliders, this.bounds);

      if (this.mode === 'training') {
        for (const enemy of this.enemies) {
          if (!enemy.alive && enemy.respawnAt !== null && this.elapsed >= enemy.respawnAt) {
            const spawn = this.spawns[Math.floor(Math.random() * this.spawns.length)];
            enemy.spawnAt(spawn);
          }
        }
      } else if (this.mode === 'zombie') {
        if (this.waveIntermission > 0) {
          this.waveIntermission = Math.max(0, this.waveIntermission - dt);
          if (this.waveIntermission === 0) this.beginWave(this.wave + 1);
        } else if (this.waveQueue > 0 && this.aliveCount < this.maxZombiesAlive) {
          this.spawnCooldown -= dt;
          if (this.spawnCooldown <= 0) {
            this.spawnZombie(player);
            this.spawnCooldown = 0.82;
          }
        } else if (this.waveQueue === 0 && this.aliveCount === 0) {
          this.waveIntermission = 4;
        }
      }
    }

    for (let i = this.tracers.length - 1; i >= 0; i--) {
      const tracer = this.tracers[i];
      tracer.life -= dt;
      tracer.line.material.opacity = Math.max(0, tracer.life / 0.12) * 0.85;
      if (tracer.life <= 0) {
        this.scene.remove(tracer.line);
        tracer.line.geometry.dispose();
        tracer.line.material.dispose();
        this.tracers.splice(i, 1);
      }
    }
  }

  reset() {
    this.start(this.mode);
  }
}
