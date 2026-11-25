import test from 'node:test';
import assert from 'node:assert/strict';
import * as THREE from 'three';
import { Weapon } from '../src/Weapon.js';

function makeWeapon(colliders = []) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 200);
  camera.position.set(0, 1.7, 0);
  camera.lookAt(0, 1.7, -20);

  const group = new THREE.Group();
  group.position.set(0, 0, -10);
  const body = new THREE.Mesh(new THREE.BoxGeometry(1, 2, 1), new THREE.MeshBasicMaterial());
  body.position.y = 1;
  group.add(body);
  group.userData.enemy = {
    alive: true,
    health: 100,
    takeDamage(amount) { this.health -= amount; },
  };
  scene.add(group);

  const weapon = new Weapon(camera, scene, () => [group], colliders);
  scene.add(camera);
  scene.updateMatrixWorld(true);
  return { weapon, group, scene };
}

function withFixedRandom(run) {
  const original = Math.random;
  Math.random = () => 0.5;
  try { run(); } finally { Math.random = original; }
}

test('hitscan damages an enemy with a clear lane', () => {
  const { weapon, group } = makeWeapon();
  withFixedRandom(() => weapon.fire());
  assert.ok(group.userData.enemy.health < 100);
});

test('arena cover stops bullets before they reach an enemy', () => {
  const wall = { minX: -2, maxX: 2, minZ: -6, maxZ: -5 };
  const { weapon, group, scene } = makeWeapon([wall]);
  withFixedRandom(() => weapon.fire());
  assert.equal(group.userData.enemy.health, 100, 'the wall absorbs the pellet');
  assert.equal(weapon.impacts.length, 1, 'the impact is drawn on the wall');
  assert.equal(scene.children.includes(group), true);
});

test('reload only progresses while the game loop is updating', () => {
  const { weapon } = makeWeapon();
  weapon.current.ammo = 0;
  weapon.startReload();
  weapon.update(0.5);
  weapon.update(0.5);
  assert.equal(weapon.reloading, true, 'pausing freezes the reload timer');
  weapon.update(0.5);
  assert.equal(weapon.reloading, false);
  assert.equal(weapon.ammo, weapon.maxAmmo);
});

test('reset clears transient shot effects', () => {
  const { weapon } = makeWeapon();
  withFixedRandom(() => weapon.fire());
  assert.ok(weapon.impacts.length > 0 || weapon.tracers.length > 0);
  weapon.reset();
  assert.equal(weapon.impacts.length, 0);
  assert.equal(weapon.tracers.length, 0);
});
