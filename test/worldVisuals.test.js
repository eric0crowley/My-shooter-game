import test from 'node:test';
import assert from 'node:assert/strict';
import * as THREE from 'three';
import { buildWorld } from '../src/World.js';

test('industrial arena landmarks and team spawn cues are present without changing navigation geometry', () => {
  const scene = new THREE.Scene();
  const world = buildWorld(scene);
  try {
    const landmarks = scene.getObjectByName('arena-landmarks');
    assert.ok(landmarks);
    assert.ok(scene.getObjectByName('blue-team-banner'));
    assert.ok(scene.getObjectByName('red-team-banner'));
    assert.ok(scene.getObjectByName('far-gate-emblem'));
    assert.equal(world.navigationMeshes.length, 16, 'decorative beams and banners stay out of the navmesh');
    assert.equal(world.colliders.length, 15, 'team markings do not change the tested collision layout');
    assert.ok(landmarks.children.length > 20, 'the frame, spawn markers and route markings dress the arena');
  } finally {
    scene.traverse((object) => {
      object.geometry?.dispose();
      if (Array.isArray(object.material)) object.material.forEach((material) => material.dispose());
      else object.material?.dispose();
    });
  }
});
