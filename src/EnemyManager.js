import * as THREE from 'three';
import { clamp, resolveCircleBoxes, segmentIntersectsBox } from './collision.js';

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
    scene.add(this.group);
    this.spawnAt(spawn, stats);
  }

  makeModel() {
    const isZombie = this.kind === 'zombie';
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
    this.group.add(body, head);
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
      this.group.add(leftArm, rightArm, leftEye, rightEye);
      this.leftArm = leftArm;
      this.rightArm = rightArm;
    }
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

  update(dt, player, colliders, bounds) {
    if (!this.alive) return;
    this.animationTime += dt;
    if (this.kind === 'zombie' && this.leftArm) {
      this.leftArm.rotation.z = -0.75 + Math.sin(this.animationTime * 5.2) * 0.14;
      this.rightArm.rotation.z = 0.75 + Math.sin(this.animationTime * 5.2 + 1.2) * 0.14;
      this.group.position.y = Math.sin(this.animationTime * 5.2) * 0.025;
    }

    const target = player.camera.position;
    const from = this.group.position;
    const dx = target.x - from.x;
    const dz = target.z - from.z;
    const distance = Math.hypot(dx, dz);
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
      if (hit) player.damage(this.damage);
      return;
    }

    this.moveToward(target, dt, colliders, bounds, distance);
    const updatedDistance = Math.hypot(target.x - from.x, target.z - from.z);
    if (updatedDistance > this.attackRange || this.attackCooldown > 0 || !canSeeTarget) return;

    this.attackCooldown = this.attackRate;
    player.damage(this.damage);
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
    this.waveIntermission = 0;
    this.spawnCooldown = 0;

    if (this.mode === 'training') {
      for (let i = 0; i < 6; i++) {
        const spawn = this.spawns[i % this.spawns.length];
        this.enemies.push(new Enemy(this.scene, spawn, this, 'bot'));
      }
      return;
    }

    this.beginWave(1);
  }

  beginWave(wave) {
    const plan = zombieWavePlan(wave);
    this.wave = wave;
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
    const spawn = this.chooseSpawn(player.camera.position);
    let zombie = this.enemies.find((enemy) => enemy.kind === 'zombie' && !enemy.alive);
    if (!zombie) {
      zombie = new Enemy(this.scene, spawn, this, 'zombie', plan);
      this.enemies.push(zombie);
    } else {
      zombie.spawnAt(spawn, plan);
    }
    this.waveQueue--;
  }

  onKill(enemy) {
    this.score++;
    this.kills++;
    if (this.mode === 'training') {
      enemy.respawnAt = this.elapsed + 1.5 + Math.random() * 1.5;
    } else {
      enemy.respawnAt = null;
    }
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
