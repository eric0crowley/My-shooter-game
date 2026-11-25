import * as THREE from 'three';

// Multi-weapon hitscan system (rifle / pistol / shotgun).
// Patterns inspired by open-source Three.js FPS projects (mr-vance/ShooterGame,
// mohsenheydari/three-fps, weiserhei/threejs-fps — all MIT) and Source-engine
// style feel: per-weapon fire rate, magazine, reload, recoil, spread, pellets,
// plus headshot multiplier and distance damage falloff (hit registration).
const WEAPONS = [
  { id: 'rifle',   name: 'تفنگ تهاجمی', auto: true,  damage: 22, fireRate: 0.10, mag: 30, spread: 0.012, pellets: 1, range: 120, color: 0x2b2f3a, reload: 1.4 },
  { id: 'pistol',  name: 'تپانچه',       auto: false, damage: 34, fireRate: 0.22, mag: 12, spread: 0.02,  pellets: 1, range: 100, color: 0x444a55, reload: 1.1 },
  { id: 'shotgun', name: 'شات‌گان',      auto: false, damage: 11, fireRate: 0.75, mag: 6,  spread: 0.09,  pellets: 9, range: 40,  color: 0x5a3a22, reload: 1.8 },
];

export class Weapon {
  constructor(camera, scene, getEnemyMeshes) {
    this.camera = camera;
    this.scene = scene;
    this.getEnemyMeshes = getEnemyMeshes;

    this.weapons = WEAPONS.map((w) => ({ ...w, ammo: w.mag, cooldown: 0, reloading: false, reloadTimer: null }));
    this.index = 0;
    this.triggerDown = false;
    this.firedThisPress = false;
    this.onHit = null;

    this.raycaster = new THREE.Raycaster();
    this.view = new THREE.Group();
    camera.add(this.view);

    this.flash = new THREE.PointLight(0xffcc66, 0, 8);
    this.flash.position.set(0.18, -0.14, -1.05);
    camera.add(this.flash);
    this.flashTime = 0;

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
    window.clearTimeout(w.reloadTimer);
    w.reloadTimer = window.setTimeout(() => {
      w.ammo = w.mag;
      w.reloading = false;
      w.reloadTimer = null;
    }, w.reload * 1000);
  }

  refill() {
    for (const w of this.weapons) w.ammo = w.mag;
  }

  reset() {
    for (const w of this.weapons) {
      window.clearTimeout(w.reloadTimer);
      w.ammo = w.mag;
      w.cooldown = 0;
      w.reloading = false;
      w.reloadTimer = null;
    }
    this.triggerDown = false;
    this.firedThisPress = false;
    this.index = 0;
    this.buildViewModel();
  }

  update(dt) {
    const w = this.current;
    if (w.cooldown > 0) w.cooldown -= dt;

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
  }

  fire() {
    const w = this.current;
    w.ammo--;
    w.cooldown = w.fireRate;
    this.flashTime = 0.05;
    this.view.position.z = 0.06; // recoil kick

    this.camera.updateMatrixWorld();
    const origin = new THREE.Vector3();
    const dir = new THREE.Vector3();
    this.camera.getWorldPosition(origin);
    this.camera.getWorldDirection(dir);

    const up = new THREE.Vector3(0, 1, 0);
    const right = new THREE.Vector3().crossVectors(dir, up).normalize();
    const realUp = new THREE.Vector3().crossVectors(right, dir).normalize();

    const enemies = this.getEnemyMeshes().filter((m) => m.visible);
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
      if (hits.length > 0) {
        const hit = hits[0];
        // Distance damage falloff.
        let dmg = w.damage * THREE.MathUtils.clamp(1 - (hit.distance - 12) / 45, 0.5, 1);
        // Headshot multiplier (head mesh is tagged userData.part === 'head').
        if (hit.object.userData && hit.object.userData.part === 'head') dmg *= 2;
        const group = hit.object.parent;
        if (group && group.userData && group.userData.enemy) {
          group.userData.enemy.takeDamage(dmg);
          hitSomething = true;
        }
      }
    }
    if (hitSomething && this.onHit) this.onHit();
  }
}
