import * as THREE from 'three';
import { PointerLockControls } from 'three/examples/jsm/controls/PointerLockControls.js';

import { buildWorld } from './World.js';
import { Player } from './Player.js';
import { Weapon } from './Weapon.js';
import { EnemyManager } from './EnemyManager.js';
import { HUD } from './HUD.js';

const errorEl = document.getElementById('error');
function showError(message) {
  errorEl.style.display = 'block';
  errorEl.textContent = message;
}

window.addEventListener('error', (event) => {
  showError(`Error: ${event.message || event.error || 'Unknown error'}`);
});
window.addEventListener('unhandledrejection', (event) => {
  const reason = event.reason;
  showError(`Promise Error: ${(reason && reason.message) || reason || 'Unknown error'}`);
});

const coarsePointer = window.matchMedia?.('(pointer: coarse)').matches ?? false;
const isTouchDevice = navigator.maxTouchPoints > 0 || coarsePointer;
document.body.classList.toggle('touch-device', isTouchDevice);

// ---------- Renderer / scene / camera ----------
const canvas = document.getElementById('game');
let renderer;
try {
  renderer = new THREE.WebGLRenderer({
    canvas,
    antialias: !isTouchDevice,
    powerPreference: 'high-performance',
  });
} catch (error) {
  showError('مرورگر از WebGL پشتیبانی نمی‌کند. لطفاً با مرورگر به‌روزتری بازی را باز کن.');
  throw error;
}
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, isTouchDevice ? 1.5 : 2));
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.05;
renderer.shadowMap.enabled = !isTouchDevice;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x101820);
scene.fog = new THREE.Fog(0x101820, 24, 76);

const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  200
);
camera.rotation.order = 'YXZ';

// ---------- World + actors ----------
const world = buildWorld(scene);
const controls = new PointerLockControls(camera, document.body);
scene.add(camera);

const player = new Player(camera, world.colliders, world.playerSpawn);
const weapon = new Weapon(camera, scene, () => enemyMgr.getMeshes());
const enemyMgr = new EnemyManager(
  scene,
  world.enemySpawns,
  world.colliders,
  world.bounds
);
const hud = new HUD();
let activeMode = 'training';
const numberFa = new Intl.NumberFormat('fa-IR', { useGrouping: false, maximumFractionDigits: 0 });

function updateHud() {
  hud.update(player, weapon, {
    mode: activeMode,
    kills: enemyMgr.kills,
    wave: enemyMgr.wave,
    remainingCount: enemyMgr.remainingCount,
    waveIntermission: enemyMgr.waveIntermission,
  });
}

updateHud();
weapon.onHit = () => hud.showHit();
player.onDamage = () => hud.showDamage();
player.onDeath = () => endGame();

// ---------- State and input ----------
const input = {
  forward: false,
  back: false,
  left: false,
  right: false,
  jump: false,
  moveX: 0,
  moveY: 0,
};
const keyMap = {
  KeyW: 'forward',
  KeyS: 'back',
  KeyA: 'left',
  KeyD: 'right',
  Space: 'jump',
  ArrowUp: 'forward',
  ArrowDown: 'back',
  ArrowLeft: 'left',
  ArrowRight: 'right',
};

let running = false;
let gameOver = false;
let lookPointerId = null;
let previousLookPoint = null;
let movePointerId = null;

const startScreen = document.getElementById('start-screen');
const pauseScreen = document.getElementById('pause-screen');
const overScreen = document.getElementById('game-over');
const finalScore = document.getElementById('final-score');
const finalLabel = document.getElementById('final-label');
const finalWaveRow = document.getElementById('final-wave-row');
const finalWave = document.getElementById('final-wave');
const pauseCopy = document.getElementById('pause-copy');
const movePad = document.getElementById('move-pad');
const moveKnob = document.getElementById('move-knob');

function clearInput() {
  input.forward = false;
  input.back = false;
  input.left = false;
  input.right = false;
  input.jump = false;
  input.moveX = 0;
  input.moveY = 0;
  movePointerId = null;
  weapon.setTrigger(false);
  moveKnob.style.transform = 'translate(0, 0)';
  lookPointerId = null;
  previousLookPoint = null;
}

document.addEventListener('keydown', (event) => {
  if (event.code === 'Escape' && isTouchDevice && running) {
    pauseGame();
    return;
  }

  const action = keyMap[event.code];
  if (action && running) {
    input[action] = true;
    if (event.code === 'Space' || event.code.startsWith('Arrow')) event.preventDefault();
  }
  if (!running) return;

  if (event.code === 'KeyR') weapon.startReload();
  if (event.code === 'Digit1') weapon.switchTo(0);
  if (event.code === 'Digit2') weapon.switchTo(1);
  if (event.code === 'Digit3') weapon.switchTo(2);
  if (event.code === 'KeyQ') weapon.switchNext();
});

document.addEventListener('keyup', (event) => {
  const action = keyMap[event.code];
  if (action) input[action] = false;
});

document.addEventListener('mousedown', (event) => {
  if (running && event.button === 0 && !event.target.closest('button')) {
    weapon.setTrigger(true);
  }
});
document.addEventListener('mouseup', (event) => {
  if (event.button === 0) weapon.setTrigger(false);
});

document.addEventListener('wheel', (event) => {
  if (!running) return;
  event.preventDefault();
  if (event.deltaY > 0) weapon.switchNext();
  else if (event.deltaY < 0) weapon.switchPrev();
}, { passive: false });

// Left virtual joystick: the strength of the drag also controls movement speed.
function updateMoveStick(event) {
  const rect = movePad.getBoundingClientRect();
  const centerX = rect.left + rect.width / 2;
  const centerY = rect.top + rect.height / 2;
  const maxDistance = rect.width * 0.31;
  let dx = event.clientX - centerX;
  let dy = event.clientY - centerY;
  const distance = Math.hypot(dx, dy);
  if (distance > maxDistance) {
    const scale = maxDistance / distance;
    dx *= scale;
    dy *= scale;
  }
  moveKnob.style.transform = `translate(${dx}px, ${dy}px)`;
  input.moveX = THREE.MathUtils.clamp(dx / maxDistance, -1, 1);
  input.moveY = THREE.MathUtils.clamp(-dy / maxDistance, -1, 1);
}

movePad.addEventListener('pointerdown', (event) => {
  if (!running || !isTouchDevice) return;
  event.preventDefault();
  movePointerId = event.pointerId;
  movePad.setPointerCapture(event.pointerId);
  updateMoveStick(event);
});
movePad.addEventListener('pointermove', (event) => {
  if (event.pointerId === movePointerId) {
    event.preventDefault();
    updateMoveStick(event);
  }
});
function releaseMoveStick(event) {
  if (event.pointerId !== movePointerId) return;
  movePointerId = null;
  input.moveX = 0;
  input.moveY = 0;
  moveKnob.style.transform = 'translate(0, 0)';
}
movePad.addEventListener('pointerup', releaseMoveStick);
movePad.addEventListener('pointercancel', releaseMoveStick);
movePad.addEventListener('lostpointercapture', releaseMoveStick);

// Dragging on the open right side of a touch screen turns the camera.
canvas.addEventListener('pointerdown', (event) => {
  if (!isTouchDevice || event.pointerType === 'mouse' || !running) return;
  if (event.clientX < window.innerWidth * 0.4) return;
  event.preventDefault();
  lookPointerId = event.pointerId;
  previousLookPoint = { x: event.clientX, y: event.clientY };
  canvas.setPointerCapture(event.pointerId);
});
canvas.addEventListener('pointermove', (event) => {
  if (event.pointerId !== lookPointerId || !previousLookPoint) return;
  const dx = event.clientX - previousLookPoint.x;
  const dy = event.clientY - previousLookPoint.y;
  previousLookPoint = { x: event.clientX, y: event.clientY };
  const sensitivity = window.innerWidth < 600 ? 0.0042 : 0.0036;
  camera.rotation.y -= dx * sensitivity;
  camera.rotation.x = THREE.MathUtils.clamp(
    camera.rotation.x - dy * sensitivity,
    -Math.PI / 2 + 0.035,
    Math.PI / 2 - 0.035
  );
});
function releaseLook(event) {
  if (event.pointerId !== lookPointerId) return;
  lookPointerId = null;
  previousLookPoint = null;
}
canvas.addEventListener('pointerup', releaseLook);
canvas.addEventListener('pointercancel', releaseLook);
canvas.addEventListener('lostpointercapture', releaseLook);

function bindHoldButton(button, onPress, onRelease) {
  let pointerId = null;
  button.addEventListener('pointerdown', (event) => {
    if (!running) return;
    event.preventDefault();
    pointerId = event.pointerId;
    button.setPointerCapture(event.pointerId);
    onPress();
  });
  const finish = (event) => {
    if (event.pointerId !== pointerId) return;
    pointerId = null;
    onRelease();
  };
  button.addEventListener('pointerup', finish);
  button.addEventListener('pointercancel', finish);
  button.addEventListener('lostpointercapture', finish);
}

bindHoldButton(
  document.getElementById('touch-fire'),
  () => weapon.setTrigger(true),
  () => weapon.setTrigger(false)
);
bindHoldButton(
  document.getElementById('touch-jump'),
  () => { input.jump = true; },
  () => { input.jump = false; }
);
document.getElementById('touch-reload').addEventListener('click', () => {
  if (running) weapon.startReload();
});
document.getElementById('touch-switch').addEventListener('click', () => {
  if (running) weapon.switchNext();
});

// ---------- Pickups ----------
function updatePickups(dt) {
  const now = performance.now();
  for (const pickup of world.pickups) {
    if (!pickup.active) {
      if (now > pickup.respawnAt) {
        pickup.active = true;
        pickup.mesh.visible = true;
      }
      continue;
    }

    pickup.mesh.rotation.y += dt * 2;
    pickup.mesh.position.y = pickup.baseY + Math.sin(now / 400 + pickup.phase) * 0.2;
    const dx = player.camera.position.x - pickup.mesh.position.x;
    const dz = player.camera.position.z - pickup.mesh.position.z;
    if (Math.hypot(dx, dz) < 1.3) {
      if (pickup.type === 'health') {
        player.health = Math.min(player.maxHealth, player.health + 30);
      } else {
        weapon.refill();
      }
      pickup.active = false;
      pickup.mesh.visible = false;
      pickup.respawnAt = now + 12000;
    }
  }
}

// ---------- Start / pause / restart flow ----------
function enterGame() {
  startScreen.style.display = 'none';
  pauseScreen.style.display = 'none';
  overScreen.style.display = 'none';
  running = true;
  gameOver = false;
  document.body.classList.add('playing');
  pauseCopy.textContent = isTouchDevice
    ? 'برای ادامه، دکمهٔ ادامه را بزن.'
    : 'برای ادامه، دکمه را بزن یا روی صفحه کلیک کن.';
}

function startGame(mode = 'training') {
  activeMode = mode === 'zombie' ? 'zombie' : 'training';
  resetGame(activeMode);
  if (isTouchDevice) {
    enterGame();
    return;
  }
  controls.lock();
}

controls.addEventListener('lock', enterGame);
controls.addEventListener('unlock', () => {
  clearInput();
  if (!gameOver) {
    running = false;
    document.body.classList.remove('playing');
    pauseScreen.style.display = 'flex';
  }
});

document.getElementById('start-training-btn').addEventListener('click', () => startGame('training'));
document.getElementById('start-zombie-btn').addEventListener('click', () => startGame('zombie'));
document.getElementById('resume-btn').addEventListener('click', () => {
  if (isTouchDevice) enterGame();
  else controls.lock();
});
document.getElementById('pause-btn').addEventListener('click', pauseGame);
document.getElementById('pause-menu-btn').addEventListener('click', returnToMenu);
document.getElementById('game-over-menu-btn').addEventListener('click', returnToMenu);
document.getElementById('restart-btn').addEventListener('click', () => {
  resetGame();
  if (isTouchDevice) enterGame();
  else {
    overScreen.style.display = 'none';
    controls.lock();
  }
});

function pauseGame() {
  if (!running || gameOver) return;
  if (isTouchDevice) {
    clearInput();
    running = false;
    document.body.classList.remove('playing');
    pauseScreen.style.display = 'flex';
  } else {
    controls.unlock();
  }
}

function resetGame(mode = activeMode) {
  clearInput();
  activeMode = mode === 'zombie' ? 'zombie' : 'training';
  document.body.classList.toggle('zombie-mode', activeMode === 'zombie');
  player.reset(world.playerSpawn);
  weapon.reset();
  enemyMgr.start(activeMode);
  for (const pickup of world.pickups) {
    pickup.active = true;
    pickup.mesh.visible = true;
    pickup.mesh.position.y = pickup.baseY;
    pickup.respawnAt = 0;
  }
  updateHud();
  gameOver = false;
  overScreen.style.display = 'none';
}

function returnToMenu() {
  gameOver = true;
  running = false;
  clearInput();
  document.body.classList.remove('playing');
  if (controls.isLocked) controls.unlock();
  pauseScreen.style.display = 'none';
  overScreen.style.display = 'none';
  startScreen.style.display = 'flex';
}

function endGame() {
  gameOver = true;
  running = false;
  clearInput();
  document.body.classList.remove('playing');
  finalScore.textContent = numberFa.format(enemyMgr.kills);
  finalLabel.textContent = activeMode === 'zombie' ? 'زامبی ازبین‌رفته' : 'حذف';
  finalWaveRow.style.display = activeMode === 'zombie' ? 'block' : 'none';
  finalWave.textContent = numberFa.format(enemyMgr.wave);
  overScreen.style.display = 'flex';
  if (controls.isLocked) controls.unlock();
}

// Stop held inputs if the browser backgrounds the game.
document.addEventListener('visibilitychange', () => {
  if (document.hidden && running) pauseGame();
});

// ---------- Resize + render ----------
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

const clock = new THREE.Clock();
function animate() {
  requestAnimationFrame(animate);
  const dt = Math.min(clock.getDelta(), 0.05);
  if (running && !gameOver) {
    player.update(dt, input, world.bounds);
    weapon.update(dt);
    enemyMgr.update(dt, player);
    updatePickups(dt);
    updateHud();
  }
  renderer.render(scene, camera);
}
animate();
