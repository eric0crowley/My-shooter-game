import test from 'node:test';
import assert from 'node:assert/strict';
import * as THREE from 'three';
import { Enemy, EnemyManager, zombieWavePlan } from '../src/EnemyManager.js';

test('first zombie wave is small enough for the starter arena', () => {
  assert.deepEqual(zombieWavePlan(1), {
    count: 7,
    maxAlive: 6,
    health: 72,
    speed: 2.55,
    damage: 12,
    attackRate: 1.15,
  });
});

test('later waves scale up but keep mobile-safe caps', () => {
  const plan = zombieWavePlan(100);
  assert.equal(plan.count, 36);
  assert.equal(plan.maxAlive, 10);
  assert.equal(plan.speed, 3.8);
  assert.equal(plan.damage, 28);
  assert.equal(plan.attackRate, 0.62);
  assert.ok(plan.health > zombieWavePlan(1).health);
});

test('invalid wave numbers are normalized to wave one', () => {
  assert.deepEqual(zombieWavePlan(0), zombieWavePlan(1));
  assert.deepEqual(zombieWavePlan(Number.NaN), zombieWavePlan(1));
});

test('training bots fire visible ranged shots and can hit at shooting distance', () => {
  const scene = new THREE.Scene();
  const shots = [];
  const manager = {
    onKill() {},
    spawnTracer: (...args) => shots.push(args),
  };
  const bot = new Enemy(scene, new THREE.Vector3(0, 0, 0), manager, 'bot');
  const player = {
    camera: { position: new THREE.Vector3(0, 1.7, 10) },
    health: 100,
    damage(amount) { this.health -= amount; },
  };
  bot.attackCooldown = 0;
  const originalRandom = Math.random;
  try {
    Math.random = () => 0.2;
    bot.update(0.016, player, [], 30);
  } finally {
    Math.random = originalRandom;
  }

  assert.equal(player.health, 92);
  assert.equal(shots.length, 1);
  assert.equal(shots[0][2], true);
  assert.equal(bot.group.position.z, 0, 'the bot holds a clear firing lane');
});

test('training bots attack the nearest active player in a LAN match', () => {
  const scene = new THREE.Scene();
  const manager = { onKill() {}, spawnTracer() {} };
  const bot = new Enemy(scene, new THREE.Vector3(0, 0, 0), manager, 'bot');
  const host = {
    camera: { position: new THREE.Vector3(0, 1.7, 30) },
    health: 100,
    damage(amount) { this.health -= amount; },
  };
  const guest = {
    camera: { position: new THREE.Vector3(5, 1.7, 10) },
    health: 100,
    damage(amount) { this.health -= amount; },
  };
  bot.attackCooldown = 0;
  const originalRandom = Math.random;
  try {
    Math.random = () => 0.2;
    bot.update(0, [host, guest], [], 30);
  } finally {
    Math.random = originalRandom;
  }
  assert.equal(host.health, 100);
  assert.equal(guest.health, 92);
});

test('network snapshots keep training bots aligned without client-side score authority', () => {
  const hostScene = new THREE.Scene();
  const clientScene = new THREE.Scene();
  const spawns = [new THREE.Vector3(-8, 0, -8), new THREE.Vector3(8, 0, -8)];
  const host = new EnemyManager(hostScene, spawns, [], 30);
  const client = new EnemyManager(clientScene, spawns, [], 30);
  host.start('training');
  client.start('training');
  host.enemies[0].group.position.set(4, 0, -2);
  host.enemies[0].health = 63;
  host.kills = 2;
  client.networkClient = true;

  client.applyNetworkState(host.getNetworkState());
  assert.equal(client.enemies.length, 6);
  assert.equal(client.enemies[0].netId, host.enemies[0].netId);
  assert.equal(client.enemies[0].group.position.x, 4);
  assert.equal(client.enemies[0].health, 63);
  assert.equal(client.kills, 2);

  client.enemies[0].takeDamage(1000);
  assert.equal(client.kills, 2, 'clients do not award or decide team kills');
  assert.equal(client.enemies[0].alive, false);
});

test('network clients can create wave enemies from host snapshots', () => {
  const hostScene = new THREE.Scene();
  const clientScene = new THREE.Scene();
  const spawns = [new THREE.Vector3(-8, 0, -8), new THREE.Vector3(8, 0, -8)];
  const host = new EnemyManager(hostScene, spawns, [], 30);
  const client = new EnemyManager(clientScene, spawns, [], 30);
  host.start('zombie');
  host.spawnZombie({ camera: { position: new THREE.Vector3(0, 1.7, 20) } });
  client.start('zombie');
  client.networkClient = true;
  client.applyNetworkState(host.getNetworkState());

  assert.equal(client.mode, 'zombie');
  assert.equal(client.wave, 1);
  assert.equal(client.enemies.length, 1);
  assert.equal(client.enemies[0].kind, 'zombie');
  assert.equal(client.enemies[0].netId, 1);
  assert.equal(client.enemies[0].alive, true);
});

test('training bots miss some shots and cannot shoot through arena cover', () => {
  const scene = new THREE.Scene();
  const shots = [];
  const manager = {
    onKill() {},
    spawnTracer: (...args) => shots.push(args),
  };
  const bot = new Enemy(scene, new THREE.Vector3(0, 0, 0), manager, 'bot');
  const player = {
    camera: { position: new THREE.Vector3(0, 1.7, 10) },
    health: 100,
    damage(amount) { this.health -= amount; },
  };
  bot.attackCooldown = 0;
  const originalRandom = Math.random;
  try {
    Math.random = () => 0.9;
    bot.update(0.016, player, [], 30);
  } finally {
    Math.random = originalRandom;
  }
  assert.equal(player.health, 100);
  assert.equal(shots.length, 1);
  assert.equal(shots[0][2], false);

  bot.attackCooldown = 0;
  const wall = { minX: -2, maxX: 2, minZ: 4, maxZ: 6 };
  bot.update(0.016, player, [wall], 30);
  assert.equal(player.health, 100);
  assert.equal(shots.length, 1);
});
