import test from 'node:test';
import assert from 'node:assert/strict';
import * as THREE from 'three';
import { createNavigationSystem } from '../src/Navigation.js';
import { buildWorld } from '../src/World.js';
import { Enemy } from '../src/EnemyManager.js';

test('Recast navigation routes an AI agent around static cover', async () => {
  const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(20, 20),
    new THREE.MeshBasicMaterial()
  );
  floor.rotation.x = -Math.PI / 2;

  const cover = new THREE.Mesh(
    new THREE.BoxGeometry(4, 3, 4),
    new THREE.MeshBasicMaterial()
  );
  cover.position.set(0, 1.5, 0);

  let navigation;
  try {
    navigation = await createNavigationSystem([floor, cover]);
    const path = navigation.findPath(
      new THREE.Vector3(-8, 0, 0),
      new THREE.Vector3(8, 1.7, 0)
    );

    assert.ok(path.length >= 3, 'the route should contain a detour around the cover');
    assert.ok(
      path.some((point) => Math.abs(point.x) < 3 && Math.abs(point.z) > 2),
      'at least one waypoint should pass around, rather than through, the obstacle'
    );
    assert.deepEqual(navigation.findPath({ x: Number.NaN, z: 0 }, { x: 1, z: 1 }), []);
  } finally {
    navigation?.dispose();
    floor.geometry.dispose();
    floor.material.dispose();
    cover.geometry.dispose();
    cover.material.dispose();
  }
});

test('starter arena navmesh connects spawn lanes around the authored cover', async () => {
  const scene = new THREE.Scene();
  const world = buildWorld(scene);
  let navigation;
  try {
    navigation = await createNavigationSystem(world.navigationMeshes);
    const path = navigation.findPath(
      world.playerSpawn,
      new THREE.Vector3(0, 1.7, -20)
    );
    assert.ok(path.length >= 3, 'the route should include turns around arena cover');
    for (const point of path) {
      assert.ok(Math.abs(point.x) <= world.bounds + 1);
      assert.ok(Math.abs(point.z) <= world.bounds + 1);
    }
  } finally {
    navigation?.dispose();
    scene.traverse((object) => {
      object.geometry?.dispose();
      if (Array.isArray(object.material)) object.material.forEach((material) => material.dispose());
      else object.material?.dispose();
    });
  }
});

test('bots follow a navigation waypoint instead of steering directly through cover', () => {
  const scene = new THREE.Scene();
  const waypoint = { x: 0, y: 0, z: 5 };
  const manager = {
    navigation: {
      findPath: () => [
        { x: 0, y: 0, z: 0 },
        waypoint,
        { x: 10, y: 0, z: 0 },
      ],
    },
    onKill() {},
  };
  const bot = new Enemy(scene, new THREE.Vector3(0, 0, 0), manager, 'bot');
  bot.moveToward(new THREE.Vector3(10, 0, 0), 0.1, [], 30, 10);
  assert.ok(bot.group.position.z > 0, 'the bot should head toward the route waypoint first');
});

test('navigation generation rejects empty or non-renderable source lists', async () => {
  await assert.rejects(
    createNavigationSystem([]),
    /no renderable world meshes/
  );
  await assert.rejects(
    createNavigationSystem([new THREE.Object3D()]),
    /no renderable world meshes/
  );
});
