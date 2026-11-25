import * as THREE from 'three';
import { rayBoxEntryDistance } from './collision.js';

// Multi-weapon hitscan system (rifle / pistol / shotgun).
// Patterns inspired by open-source Three.js FPS projects (mr-vance/ShooterGame,
// mohsenheydari/three-fps, weiserhei/threejs-fps — all MIT) and Source-engine
// style feel: per-weapon fire rate, magazine, reload, recoil, spread, pellets,
// plus headshot multiplier and distance damage falloff (hit registration).
// Shots are also stopped by arena cover before they reach an enemy.
const WEAPONS = [
  { id: 'rifle',   name: 'تفنگ تهاجمی', auto: true,  damage: 22, fireRate: 0.10, mag: 30, spread: 0.012, pellets: 1, range: 120, color: 0x2b2f3a, reload: 1.4 },
  { id: 'pistol',  name: 'تپانچه',       auto: false, damage: 34, fireRate: 0.22, mag: 12, spread: 0.02,  pellets: 1, range: 100, color: 0x444a55, reload: 1.1 },
  { id: 'shotgun', name: 'شات‌گان',      auto: false, damage: 11, fireRate: 0.75, mag: 6,  spread: 0.09,  pellets: 9, range: 40,  color: 0x5a3a22, reload: 1.8 },
];

const IMPACT_ENEMY = 0xffad65;
const IMPACT_WALL = 0xb8d6d2;

export class Weapon {
  constructor(camera, scene, getEnemyMeshes, colliders = []) {
    this.camera = camera;
    this.scene = scene;
    this.getEnemyMeshes = getEnemyMeshes;
    this.colliders = colliders;

    this.weapons = WEAPONS.map((w) => ({
      ...w,
      ammo: w.mag,
      cooldown: 0,
      reloading: false,
      reloadRemaining: 0,
    }));
    this.index = 0;
    this.triggerDown = false;
    this.firedThisPress = false;
    this.onHit = null;
    this.onEnemyHit = null;
    this.onShot = null;
    this.onReload = null;

    this.raycaster = new THREE.Raycaster();
    this.view = new THREE.Group();
    camera.add(this.view);

    this.flash = new THREE.PointLight(0xffcc66, 0, 8);
    this.flash.position.set(0.18, -0.14, -1.05);
    camera.add(this.flash);
    this.flashTime = 0;

    this.impactGeometry = new THREE.IcosahedronGeometry(0.09, 0);
    this.impacts = [];
    this.tracers = [];

    this.buildViewModel();
  }

  get current() { return this.weapons[this.index]; }
  get ammo() { return this.current.ammo; }
  get maxAmmo() { return this.current.mag; }
  get reloading() { return this.current.reloading; }
  get name() { return this.current.name; }

  buildViewModel() {
    while (this.view.children.length) this.view.remove(this.view.children[0]);
    const w = this.current;
    const mat = new THREE.MeshStandardMaterial({ color: w.color, roughness: 0.6, metalness: 0.3 });
    const body = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.12, 0.5), mat);
    body.position.set(0.18, -0.18, -0.5);
    const barrel = new THREE.Mesh(new THREE.BoxGeometry(0.05, 0.05, 0.45), mat);
    barrel.position.set(0.18, -0.14, -0.82);
    this.view.add(body, barrel);
    this.view.position.set(0, 0, 0);
  }

  setTrigger(down) {
    this.triggerDown = down;
    if (!down) this.firedThisPress = false;
  }

  switchTo(i) {
    if (i < 0 || i >= this.weapons.length || i === this.index) return;
    this.index = i;
    this.buildViewModel();
  }
  switchNext() { this.switchTo((this.index + 1) % this.weapons.length); }
  switchPrev() { this.switchTo((this.index - 1 + this.weapons.length) % this.weapons.length); }

  startReload() {
    const w = this.current;
    if (w.reloading || w.ammo === w.mag) return;
    w.reloading = true;
    w.reloadRemaining = w.reload;
    if (this.onReload) this.onReload(w.id);
  }

  refill() {
    for (const w of this.weapons) {
      w.ammo = w.mag;
      w.reloading = false;
      w.reloadRemaining = 0;
    }
  }

  clearEffects() {
    for (const impact of this.impacts) {
      this.scene.remove(impact.mesh);
      impact.mesh.material.dispose();
    }
    this.impacts.length = 0;
    for (const tracer of this.tracers) {
      this.scene.remove(tracer.line);
      tracer.line.geometry.dispose();
      tracer.line.material.dispose();
    }
    this.tracers.length = 0;
  }

  reset() {
    for (const w of this.weapons) {
      w.ammo = w.mag;
      w.cooldown = 0;
      w.reloading = false;
      w.reloadRemaining = 0;
    }
    this.triggerDown = false;
    this.firedThisPress = false;
    this.index = 0;
    this.flashTime = 0;
    this.flash.intensity = 0;
    this.clearEffects();
    this.buildViewModel();
  }

  spawnImpact(point, color) {
    const material = new THREE.MeshBasicMaterial({
      color,
      transparent: true,
      opacity: 0.95,
      depthWrite: false,
    });
    const mesh = new THREE.Mesh(this.impactGeometry, material);
    mesh.position.copy(point);
    this.scene.add(mesh);
    this.impacts.push({ mesh, life: 0.18, maxLife: 0.18 });
  }

  spawnTracer(from, to) {
    const geometry = new THREE.BufferGeometry().setFromPoints([from, to]);
    const material = new THREE.LineBasicMaterial({
      color: 0xffe2a8,
      transparent: true,
      opacity: 0.55,
      depthWrite: false,
    });
    const line = new THREE.Line(geometry, material);
    this.scene.add(line);
    this.tracers.push({ line, life: 0.07, maxLife: 0.07 });
  }

  updateEffects(dt) {
    for (let i = this.impacts.length - 1; i >= 0; i--) {
      const effect = this.impacts[i];
      effect.life -= dt;
      const ratio = Math.max(0, effect.life / effect.maxLife);
      effect.mesh.material.opacity = ratio * 0.95;
      effect.mesh.scale.setScalar(0.7 + (1 - ratio) * 1.5);
      if (effect.life <= 0) {
        this.scene.remove(effect.mesh);
        effect.mesh.material.dispose();
        this.impacts.splice(i, 1);
      }
    }

    for (let i = this.tracers.length - 1; i >= 0; i--) {
      const effect = this.tracers[i];
      effect.life -= dt;
      effect.line.material.opacity = Math.max(0, effect.life / effect.maxLife) * 0.55;
      if (effect.life <= 0) {
        this.scene.remove(effect.line);
        effect.line.geometry.dispose();
        effect.line.material.dispose();
        this.tracers.splice(i, 1);
      }
    }
  }

  update(dt) {
    for (const weapon of this.weapons) {
      if (weapon.cooldown > 0) weapon.cooldown -= dt;
      if (weapon.reloading) {
        weapon.reloadRemaining -= dt;
        if (weapon.reloadRemaining <= 0) {
          weapon.ammo = weapon.mag;
          weapon.reloading = false;
          weapon.reloadRemaining = 0;
        }
      }
    }

    const w = this.current;
    if (this.triggerDown) {
      const wantFire = w.auto ? true : !this.firedThisPress;
      if (wantFire && w.cooldown <= 0 && !w.reloading && w.ammo > 0) {
        this.fire();
        this.firedThisPress = true;
      }
      if (w.ammo <= 0 && !w.reloading) this.startReload();
    }

    // Recoil recovery + muzzle flash fade.
    this.view.position.z += (0 - this.view.position.z) * Math.min(1, dt * 12);
    if (this.flashTime > 0) {
      this.flashTime -= dt;
      this.flash.intensity = 4;
    } else {
      this.flash.intensity = 0;
    }
    this.updateEffects(dt);
  }

  wallDistance(origin, direction, maxDistance) {
    let nearest = Infinity;
    for (const box of this.colliders) {
      const distance = rayBoxEntryDistance(origin.x, origin.z, direction.x, direction.z, box);
      if (distance < nearest) nearest = distance;
    }
    return Math.min(nearest, maxDistance);
  }

  fire() {
    const w = this.current;
    w.ammo--;
    w.cooldown = w.fireRate;
    this.flashTime = 0.05;
    this.view.position.z = 0.06; // recoil kick
    if (this.onShot) this.onShot(w.id);

    this.camera.updateMatrixWorld();
    const origin = new THREE.Vector3();
    const dir = new THREE.Vector3();
    this.camera.getWorldPosition(origin);
    this.camera.getWorldDirection(dir);

    const up = new THREE.Vector3(0, 1, 0);
    const right = new THREE.Vector3().crossVectors(dir, up).normalize();
    const realUp = new THREE.Vector3().crossVectors(right, dir).normalize();
    const muzzle = origin.clone()
      .addScaledVector(right, 0.16)
      .addScaledVector(realUp, -0.12)
      .addScaledVector(dir, 0.45);

    const enemies = this.getEnemyMeshes().filter((mesh) => mesh.visible);
    let hitSomething = false;

    for (let p = 0; p < w.pellets; p++) {
      const d = dir.clone();
      if (w.spread > 0) {
        d.addScaledVector(right, (Math.random() * 2 - 1) * w.spread);
        d.addScaledVector(realUp, (Math.random() * 2 - 1) * w.spread);
        d.normalize();
      }
      this.raycaster.set(origin, d);
      this.raycaster.far = w.range;
      const hits = this.raycaster.intersectObjects(enemies, true);

      let enemyHit = null;
      let targetDistance = w.range;
      let targetPoint = origin.clone().addScaledVector(d, w.range);
      if (hits.length > 0) {
        targetDistance = hits[0].distance;
        targetPoint = hits[0].point.clone();
        const group = hits[0].object.parent;
        if (group?.userData?.enemy) enemyHit = group.userData.enemy;
      }

      // Cover wins: a wall in front of the enemy absorbs the pellet.
      const wallAt = this.wallDistance(origin, d, w.range);
      if (wallAt < targetDistance) {
        const wallPoint = origin.clone().addScaledVector(d, wallAt);
        this.spawnImpact(wallPoint, IMPACT_WALL);
        this.spawnTracer(muzzle, wallPoint);
        hitSomething = true;
        continue;
      }

      if (!enemyHit) continue;
      let damage = w.damage * THREE.MathUtils.clamp(1 - (targetDistance - 12) / 45, 0.5, 1);
      if (hits[0].object.userData?.part === 'head') damage *= 2;
      enemyHit.takeDamage(damage);
      if (this.onEnemyHit) this.onEnemyHit(enemyHit, damage, hits[0].point);
      this.spawnImpact(targetPoint, IMPACT_ENEMY);
      this.spawnTracer(muzzle, targetPoint);
      hitSomething = true;
    }

    if (hitSomething && this.onHit) this.onHit();
  }
}
