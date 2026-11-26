import test from "node:test";
import assert from "node:assert/strict";
import * as THREE from "three";
import { Enemy, EnemyManager } from "../src/EnemyManager.js";
import { Player } from "../src/Player.js";

function disposeScene(scene) {
  scene.traverse((object) => {
    object.geometry?.dispose();
    if (Array.isArray(object.material))
      object.material.forEach((material) => material.dispose());
    else object.material?.dispose();
  });
}

test("offline team match creates balanced five-versus-five sides and filters friendly fire targets", () => {
  const scene = new THREE.Scene();
  const teamSpawns = {
    blue: [0, 1, 2, 3, 4].map((index) => new THREE.Vector3(index * 2, 0, 20)),
    red: [0, 1, 2, 3, 4].map((index) => new THREE.Vector3(index * 2, 0, -20)),
  };
  const manager = new EnemyManager(scene, [], [], 30, teamSpawns);
  try {
    manager.start("tdm");
    assert.equal(
      manager.enemies.length,
      9,
      "the player fills the fifth blue-team slot",
    );
    assert.equal(
      manager.enemies.filter((enemy) => enemy.team === "blue").length,
      4,
    );
    assert.equal(
      manager.enemies.filter((enemy) => enemy.team === "red").length,
      5,
    );
    assert.equal(
      manager.getMeshes("blue").length,
      5,
      "blue players can only shoot the opposing team",
    );
    assert.ok(
      manager
        .getMeshes("blue")
        .every((mesh) => mesh.userData.enemy.team === "red"),
    );
    assert.equal(manager.getMeshes("red").length, 4);
    assert.equal(
      manager.enemies.find((enemy) => enemy.team === "blue").displayName,
      "هم‌تیمی 1",
    );
    assert.equal(
      manager.enemies.find((enemy) => enemy.team === "red").displayName,
      "حریف 1",
    );
  } finally {
    disposeScene(scene);
  }
});

test("team AI selects and damages the nearest opposing bot, not a nearby ally", () => {
  const scene = new THREE.Scene();
  const manager = { onKill() {}, spawnTracer() {} };
  const bot = new Enemy(scene, new THREE.Vector3(0, 0, 0), manager, "bot", {
    team: "blue",
  });
  const ally = new Enemy(scene, new THREE.Vector3(0, 0, 2), manager, "bot", {
    team: "blue",
  });
  const opponent = new Enemy(
    scene,
    new THREE.Vector3(0, 0, 8),
    manager,
    "bot",
    { team: "red" },
  );
  bot.attackCooldown = 0;
  const originalRandom = Math.random;
  try {
    Math.random = () => 0.2;
    bot.update(0.016, [bot, ally, opponent], [], 30);
  } finally {
    Math.random = originalRandom;
    disposeScene(scene);
  }

  assert.equal(ally.health, 100, "friendly bots are not valid attack targets");
  assert.equal(
    opponent.health,
    92,
    "the nearest opponent receives the ranged hit",
  );
});

test('TDM bots choose a nearby blocked firing angle and retreat instead of shooting immediately', () => {
  const scene = new THREE.Scene();
  const wall = { minX: -2, maxX: 2, minZ: -1, maxZ: 1 };
  const teamSpawns = {
    blue: [new THREE.Vector3(0, 0, 8)],
    red: [new THREE.Vector3(0, 0, -8)],
  };
  const manager = new EnemyManager(scene, [], [wall], 20, teamSpawns);
  const player = {
    team: 'blue',
    isPlayer: true,
    alive: true,
    camera: { position: new THREE.Vector3(0, 1.7, 8) },
    health: 100,
    damage(amount) { this.health -= amount; },
  };
  let tracerCount = 0;
  try {
    manager.start('tdm');
    const redBot = manager.enemies.find((enemy) => enemy.team === 'red');
    redBot.takeDamage(8, player);
    assert.ok(redBot.coverTarget, 'a usable cover point should be selected');
    assert.ok(redBot.coverTarget.z < wall.minZ, 'the point must put the wall between bot and player');

    const startZ = redBot.group.position.z;
    manager.spawnTracer = () => { tracerCount++; };
    redBot.attackCooldown = 0;
    redBot.update(0.1, [player], [wall], manager.bounds);

    assert.ok(redBot.group.position.z > startZ, 'the bot should start moving toward cover');
    assert.equal(tracerCount, 0, 'the bot should hold fire during its retreat');
  } finally {
    disposeScene(scene);
  }
});

test("match manager passes the local player into both teams target lists", () => {
  const scene = new THREE.Scene();
  const teamSpawns = {
    blue: [new THREE.Vector3(0, 0, 20), new THREE.Vector3(-20, 0, 20)],
    red: [new THREE.Vector3(0, 0, 0)],
  };
  const manager = new EnemyManager(scene, [], [], 30, teamSpawns);
  const player = {
    team: "blue",
    alive: true,
    camera: { position: new THREE.Vector3(0, 1.7, 10) },
    health: 100,
    damage(amount) {
      this.health -= amount;
    },
  };
  try {
    manager.start("tdm");
    const redBot = manager.enemies.find((enemy) => enemy.team === "red");
    redBot.attackCooldown = 0;
    const originalRandom = Math.random;
    try {
      Math.random = () => 0.2;
      manager.update(0.016, [player]);
    } finally {
      Math.random = originalRandom;
    }
    assert.equal(
      player.health,
      92,
      "the red team can acquire and shoot the local player",
    );
  } finally {
    disposeScene(scene);
  }
});

test("team bots respawn on their own side and keep their scoreboard record", () => {
  const scene = new THREE.Scene();
  const teamSpawns = {
    blue: [new THREE.Vector3(0, 0, 20), new THREE.Vector3(-10, 0, 20)],
    red: [new THREE.Vector3(10, 0, -20)],
  };
  const manager = new EnemyManager(scene, [], [], 30, teamSpawns);
  let respawned = null;
  try {
    manager.start("tdm");
    manager.onRespawnEvent = (enemy) => {
      respawned = enemy;
    };
    for (const enemy of manager.enemies) enemy.detectRange = 0;
    const redBot = manager.enemies.find((enemy) => enemy.team === "red");
    const player = { team: "blue", isPlayer: true };
    redBot.takeDamage(1000, player);
    redBot.respawnAt = 0;
    manager.update(0.016, [player]);

    assert.equal(respawned, redBot);
    assert.equal(redBot.alive, true);
    assert.equal(redBot.team, "red");
    assert.equal(redBot.deaths, 1);
    assert.equal(redBot.displayName, "حریف 1");
    assert.equal(redBot.group.position.x, teamSpawns.red[0].x);
    assert.equal(redBot.group.position.z, teamSpawns.red[0].z);
  } finally {
    disposeScene(scene);
  }
});

test("player death reports the opponent team so the match can award the elimination", () => {
  const player = new Player(
    new THREE.PerspectiveCamera(),
    [],
    new THREE.Vector3(0, 1.7, 0),
  );
  const attacker = { team: "red" };
  let deathAttacker = null;
  player.onDeath = (source) => {
    deathAttacker = source;
  };

  player.damage(player.maxHealth, attacker);

  assert.equal(player.team, "blue");
  assert.equal(player.alive, false);
  assert.equal(player.deaths, 1);
  assert.equal(deathAttacker, attacker);
});

test("team score events identify the attacker and personal kills exclude bot-on-bot kills", () => {
  const scene = new THREE.Scene();
  const spawns = {
    blue: [new THREE.Vector3(0, 0, 20), new THREE.Vector3(-5, 0, 20)],
    red: [new THREE.Vector3(0, 0, -20)],
  };
  const manager = new EnemyManager(scene, [], [], 30, spawns);
  const events = [];
  try {
    manager.start("tdm");
    manager.onKillEvent = (enemy, attacker) => events.push({ enemy, attacker });
    const player = { team: "blue", isPlayer: true };
    const blueBot = manager.enemies.find((enemy) => enemy.team === "blue");
    const redBot = manager.enemies.find((enemy) => enemy.team === "red");

    redBot.takeDamage(1000, player);
    assert.equal(manager.kills, 1);
    assert.equal(manager.score, 1);
    assert.equal(player.kills, 1);
    assert.equal(redBot.deaths, 1);
    assert.equal(redBot.respawnAt > manager.elapsed, true);

    blueBot.takeDamage(1000, redBot);
    assert.equal(
      manager.kills,
      1,
      "a teammate kill does not inflate the human player stat",
    );
    assert.equal(redBot.kills, 1);
    assert.equal(blueBot.deaths, 1);
    assert.equal(events.length, 2);
    assert.equal(events[0].attacker, player);
    assert.equal(events[1].attacker, redBot);
  } finally {
    disposeScene(scene);
  }
});
