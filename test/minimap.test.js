import test from 'node:test';
import assert from 'node:assert/strict';
import { Minimap, worldToMinimap } from '../src/Minimap.js';

const MAP_SIZE = 128;
const MAP_PADDING = 11;

test('arena coordinates project to consistent top-down minimap positions', () => {
  assert.deepEqual(worldToMinimap(0, 0, 30, MAP_SIZE), { x: 64, y: 64 });
  assert.deepEqual(worldToMinimap(-30, 30, 30, MAP_SIZE), {
    x: MAP_PADDING,
    y: MAP_PADDING,
  });
  assert.deepEqual(worldToMinimap(30, -30, 30, MAP_SIZE), {
    x: MAP_SIZE - MAP_PADDING,
    y: MAP_SIZE - MAP_PADDING,
  });
  assert.deepEqual(worldToMinimap(100, -100, 30, MAP_SIZE), {
    x: MAP_SIZE - MAP_PADDING,
    y: MAP_SIZE - MAP_PADDING,
  });
});

function makeCanvas(size) {
  const calls = [];
  const context = {};
  for (const method of [
    'setTransform', 'clearRect', 'beginPath', 'moveTo', 'lineTo',
    'quadraticCurveTo', 'closePath', 'fill', 'save', 'clip', 'arc',
    'stroke', 'fillRect', 'restore', 'fillText', 'translate', 'rotate',
  ]) {
    context[method] = (...args) => calls.push([method, ...args]);
  }
  const canvas = {
    width: 0,
    height: 0,
    getContext: () => context,
    getBoundingClientRect: () => ({ width: size, height: size }),
  };
  return { canvas, calls };
}

test('TDM minimap keeps opposing bots hidden and shows friendly bots', () => {
  const { canvas, calls } = makeCanvas(MAP_SIZE);
  const world = {
    bounds: 30,
    teamSpawns: {
      blue: [{ x: 0, z: 24 }],
      red: [{ x: 0, z: -24 }],
    },
    colliders: [],
  };
  const player = {
    team: 'blue',
    health: 100,
    maxHealth: 100,
    camera: { position: { x: 0, z: 24 }, rotation: { y: 0 } },
  };
  const enemies = [
    { kind: 'bot', team: 'blue', alive: true, group: { visible: true, position: { x: -3, z: 8 } } },
    { kind: 'bot', team: 'red', alive: true, group: { visible: true, position: { x: 3, z: -8 } } },
  ];
  const minimap = new Minimap(canvas, world);

  minimap.update(0, { mode: 'tdm', player, enemies });

  // Two team zones + the center landmark + two arcs for the friendly bot.
  // An extra pair would mean the opposing bot leaked onto the tactical map.
  assert.equal(calls.filter(([name]) => name === 'arc').length, 5);
});

test('minimap draws cover, pickups, team markers and local actors at a low update rate', () => {
  const { canvas, calls } = makeCanvas(MAP_SIZE);
  const world = {
    bounds: 30,
    teamSpawns: {
      blue: [{ x: 0, z: 24 }],
      red: [{ x: 0, z: -24 }],
    },
    colliders: [{ minX: -2, maxX: 2, minZ: -3, maxZ: 3 }],
  };
  const player = {
    team: 'blue',
    health: 75,
    maxHealth: 100,
    camera: {
      position: { x: 0, z: 24 },
      rotation: { y: 0 },
    },
  };
  const enemy = {
    kind: 'zombie',
    team: 'red',
    alive: true,
    group: { visible: true, position: { x: 4, z: 3 } },
  };
  const pickups = [{
    active: true,
    type: 'ammo',
    mesh: { visible: true, position: { x: -4, z: 0 } },
  }];
  const minimap = new Minimap(canvas, world);

  minimap.update(0, { mode: 'zombie', player, enemies: [enemy], pickups });
  assert.equal(canvas.width, MAP_SIZE);
  assert.ok(calls.some(([name]) => name === 'fillText'));
  assert.ok(calls.filter(([name]) => name === 'arc').length >= 5);

  const callCount = calls.length;
  minimap.update(0.02, { mode: 'zombie', player, enemies: [enemy], pickups });
  assert.equal(calls.length, callCount, 'drawing is throttled between HUD refreshes');
  minimap.update(0.09, { mode: 'zombie', player, enemies: [enemy], pickups });
  assert.ok(calls.length > callCount);
});
