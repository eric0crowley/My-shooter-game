import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync, statSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';
import { findEnemyFromObject } from '../src/Weapon.js';
import {
  RECOVERED_AUDIO_ASSETS,
  RECOVERED_WEAPON_ASSETS,
  RECOVERED_ZOMBIE_ASSET,
} from '../src/recoveredAssets.js';

const projectRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');

function assertPublicAsset(url) {
  assert.match(url, /^\/recovered\//, 'runtime URL should resolve from Vite public/');
  const file = resolve(projectRoot, 'public', `.${url}`);
  assert.ok(existsSync(file), `missing recovered asset: ${url}`);
  assert.ok(statSync(file).size > 0, `recovered asset is empty: ${url}`);
}

test('weapon ray hits find an enemy through recovered model group nesting', () => {
  const enemy = { takeDamage() {} };
  const enemyRoot = { userData: { enemy }, parent: null };
  const importedObjRoot = { userData: {}, parent: enemyRoot };
  const importedMesh = { userData: { part: 'body' }, parent: importedObjRoot };
  assert.equal(findEnemyFromObject(importedMesh), enemy);
  assert.equal(findEnemyFromObject({ userData: {}, parent: null }), null);
});

for (const [weaponId, asset] of Object.entries(RECOVERED_WEAPON_ASSETS)) {
  test(`${weaponId} recovered weapon model and texture are packaged`, () => {
    assert.ok(asset.sourceMesh, 'mesh provenance ID is recorded');
    assert.ok(asset.sourceTexture, 'texture provenance ID is recorded');
    assert.ok(asset.targetLength > 0, 'view-model target size is positive');
    assertPublicAsset(asset.model);
    assertPublicAsset(asset.texture);

    const modelPath = resolve(projectRoot, 'public', `.${asset.model}`);
    const object = new OBJLoader().parse(readFileSync(modelPath, 'utf8'));
    let meshCount = 0;
    let vertexCount = 0;
    object.traverse((child) => {
      if (!child.isMesh) return;
      meshCount++;
      vertexCount += child.geometry.getAttribute('position')?.count || 0;
    });
    assert.ok(meshCount > 0, 'OBJ contains at least one mesh');
    assert.ok(vertexCount > 0, 'OBJ contains renderable vertices');

    const texturePath = resolve(projectRoot, 'public', `.${asset.texture}`);
    assert.equal(readFileSync(texturePath).subarray(0, 8).toString('hex'), '89504e470d0a1a0a', 'texture is a PNG');
  });
}

test('original ZombieC mesh and albedo are packaged and parse as a renderable OBJ', () => {
  assert.ok(RECOVERED_ZOMBIE_ASSET.sourceMesh);
  assert.ok(RECOVERED_ZOMBIE_ASSET.sourceMaterial);
  assert.ok(RECOVERED_ZOMBIE_ASSET.sourceTexture);
  assert.ok(RECOVERED_ZOMBIE_ASSET.targetHeight > 0);
  assertPublicAsset(RECOVERED_ZOMBIE_ASSET.model);
  assertPublicAsset(RECOVERED_ZOMBIE_ASSET.texture);

  const modelPath = resolve(projectRoot, 'public', `.${RECOVERED_ZOMBIE_ASSET.model}`);
  const object = new OBJLoader().parse(readFileSync(modelPath, 'utf8'));
  let meshCount = 0;
  let vertexCount = 0;
  object.traverse((child) => {
    if (!child.isMesh) return;
    meshCount++;
    vertexCount += child.geometry.getAttribute('position')?.count || 0;
  });
  assert.ok(meshCount > 0);
  assert.ok(vertexCount > 0);

  const texturePath = resolve(projectRoot, 'public', `.${RECOVERED_ZOMBIE_ASSET.texture}`);
  assert.equal(readFileSync(texturePath).subarray(0, 8).toString('hex'), '89504e470d0a1a0a');
});

test('all mapped original gunfire and reload clips are packaged', () => {
  assert.deepEqual(Object.keys(RECOVERED_AUDIO_ASSETS).sort(), [
    'reload:pistol', 'reload:rifle', 'reload:shotgun',
    'shot:pistol', 'shot:rifle', 'shot:shotgun',
  ]);
  for (const url of Object.values(RECOVERED_AUDIO_ASSETS)) {
    assertPublicAsset(url);
    const audioPath = resolve(projectRoot, 'public', `.${url}`);
    const header = readFileSync(audioPath).subarray(0, 12).toString('ascii');
    assert.equal(header.slice(0, 4), 'RIFF', `${url} should be a WAV file`);
    assert.equal(header.slice(8, 12), 'WAVE', `${url} should contain a WAVE stream`);
  }
});
