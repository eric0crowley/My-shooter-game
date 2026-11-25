import * as THREE from 'three';
import { PointerLockControls } from 'three/examples/jsm/controls/PointerLockControls.js';

import { buildWorld } from './World.js';
import { Player } from './Player.js';
import { Weapon } from './Weapon.js';
import { EnemyManager } from './EnemyManager.js';
import { HUD } from './HUD.js';
import { LanTransport, DEFAULT_PORT } from './LanTransport.js';
import { NetworkPlayers } from './NetworkPlayers.js';
import { SoundEffects } from './SoundEffects.js';

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
const lanTransport = new LanTransport();
const networkPlayers = new NetworkPlayers(scene);
const soundEffects = new SoundEffects();
const remotePlayerStates = new Map();
const lanPeers = new Map();
let activeMode = 'training';
let lanRole = null;
let localLanId = 'host';
let localPlayerName = 'میزبان';
let localSpawnSlot = 0;
let lanMatchStarted = false;
let lanSendTimer = 0;
let selectedLanMode = 'zombie';
const numberFa = new Intl.NumberFormat('fa-IR', { useGrouping: false, maximumFractionDigits: 0 });

function updateHud() {
  hud.update(player, weapon, {
    mode: activeMode,
    kills: enemyMgr.kills,
    wave: enemyMgr.wave,
    remainingCount: enemyMgr.remainingCount,
    waveIntermission: enemyMgr.waveIntermission,
    online: lanRole !== null,
    playerCount: lanRole === 'host' ? lanPeers.size + 1 : remotePlayerStates.size,
  });
}

updateHud();
weapon.onHit = () => {
  hud.showHit();
  soundEffects.hit();
};
weapon.onShot = (id) => soundEffects.shot(id);
weapon.onReload = () => soundEffects.reload();
enemyMgr.onKillEvent = () => soundEffects.tone(680, 0.09, 'triangle', 0.06, 920);
enemyMgr.onWaveStart = (wave) => soundEffects.waveStart(wave);
weapon.onEnemyHit = (enemy, amount) => {
  if (lanRole === 'client' && Number.isInteger(enemy.netId)) {
    void lanTransport.send({ type: 'damage', enemyId: enemy.netId, amount }).catch(() => {});
  }
};
player.onDamage = () => {
  hud.showDamage();
  soundEffects.damage();
  if (isTouchDevice && navigator.vibrate) navigator.vibrate([22, 26, 22]);
};
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
const lanScreen = document.getElementById('lan-screen');
const lanStatus = document.getElementById('lan-status');
const lanHostSetup = document.getElementById('lan-host-setup');
const lanJoinSetup = document.getElementById('lan-join-setup');
const lanAddressValue = document.getElementById('lan-address-value');
const lanHostInput = document.getElementById('lan-host-input');
const lanPlayerList = document.getElementById('lan-player-list');
const lanStartMatchButton = document.getElementById('lan-start-match-btn');

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

function setLanStatus(message, isError = false) {
  lanStatus.textContent = message;
  lanStatus.classList.toggle('error', isError);
}

function toAsciiDigits(value) {
  return String(value).replace(/[۰-۹]/g, (digit) => String('۰۱۲۳۴۵۶۷۸۹'.indexOf(digit)));
}

function renderLanPlayers() {
  lanPlayerList.replaceChildren();
  const hostEntry = document.createElement('div');
  hostEntry.className = 'lan-player-entry';
  hostEntry.textContent = 'میزبان · این گوشی';
  lanPlayerList.append(hostEntry);
  for (const peer of lanPeers.values()) {
    const entry = document.createElement('div');
    entry.className = 'lan-player-entry';
    entry.textContent = peer.joined ? `${peer.name} · آماده` : 'گوشی متصل شد؛ در حال ورود…';
    lanPlayerList.append(entry);
  }
  lanStartMatchButton.disabled = ![...lanPeers.values()].some((peer) => peer.joined);
}

function openLanLobby(role) {
  lanRole = role;
  localLanId = role === 'host' ? 'host' : `guest-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 7)}`;
  localPlayerName = role === 'host' ? 'میزبان' : 'مهمان';
  localSpawnSlot = 0;
  lanMatchStarted = false;
  lanPeers.clear();
  remotePlayerStates.clear();
  networkPlayers.clear();
  startScreen.style.display = 'none';
  lanScreen.style.display = 'flex';
  lanHostSetup.hidden = role !== 'host';
  lanJoinSetup.hidden = role !== 'client';
  lanAddressValue.textContent = 'در حال آماده‌سازی…';
  renderLanPlayers();
  if (!lanTransport.available) {
    setLanStatus('شبکهٔ محلی در پیش‌نمایش وب فعال نیست؛ برای این قابلیت باید APK را روی اندروید نصب کنی.', true);
    return;
  }
  setLanStatus(role === 'host' ? 'در حال شروع میزبان شبکهٔ محلی…' : 'IP میزبان را وارد کن؛ هر دو گوشی باید روی یک وای‌فای باشند.');
}

async function startLanHost() {
  void soundEffects.unlock().catch(() => {});
  openLanLobby('host');
  if (!lanTransport.available) return;
  try {
    await lanListenersReady;
    const result = await lanTransport.startHost(DEFAULT_PORT);
    lanAddressValue.textContent = `${result.address}:${result.port}`;
    setLanStatus(result.address === '127.0.0.1'
      ? 'میزبان روشن شد، اما IP وای‌فای شناسایی نشد. به وای‌فای وصل شو و دوباره امتحان کن.'
      : 'میزبان آماده است؛ گوشی دیگر باید همین نشانی را وارد کند.');
  } catch (error) {
    setLanStatus(error?.message || 'شروع میزبان شبکهٔ محلی ناموفق بود.', true);
  }
}

function openLanJoin() {
  void soundEffects.unlock().catch(() => {});
  openLanLobby('client');
  if (lanTransport.available) lanHostInput.focus();
}

async function connectToLanHost() {
  void soundEffects.unlock().catch(() => {});
  if (!lanTransport.available) {
    setLanStatus('اتصال LAN فقط از داخل APK اندروید ممکن است.', true);
    return;
  }
  const host = toAsciiDigits(lanHostInput.value).trim();
  if (!host) {
    setLanStatus('IP نمایان‌شده روی گوشی میزبان را وارد کن.', true);
    lanHostInput.focus();
    return;
  }
  const button = document.getElementById('lan-connect-btn');
  button.disabled = true;
  setLanStatus('در حال اتصال به میزبان…');
  try {
    await lanListenersReady;
    await lanTransport.connect(host, DEFAULT_PORT);
    localPlayerName = 'مهمان';
    await lanTransport.send({ type: 'join', playerId: localLanId, name: localPlayerName });
    setLanStatus('وصل شدی؛ منتظر شروع بازی از سوی میزبان بمان.');
  } catch (error) {
    if (lanTransport.role === 'client') {
      try { await lanTransport.close('client'); } catch {}
    }
    setLanStatus(error?.message || 'اتصال انجام نشد؛ IP و وای‌فای هر دو گوشی را بررسی کن.', true);
  } finally {
    button.disabled = false;
  }
}

function makePlayerState(id, name, state) {
  const x = Number(state?.x);
  const y = Number(state?.y);
  const z = Number(state?.z);
  const yaw = Number(state?.yaw);
  const pitch = Number(state?.pitch);
  if (![x, y, z, yaw, pitch].every(Number.isFinite)) return null;
  return {
    id,
    name: String(name || 'بازیکن').slice(0, 20),
    x: THREE.MathUtils.clamp(x, -world.bounds + 0.5, world.bounds - 0.5),
    y: THREE.MathUtils.clamp(y, 1.7, 5),
    z: THREE.MathUtils.clamp(z, -world.bounds + 0.5, world.bounds - 0.5),
    yaw,
    pitch: THREE.MathUtils.clamp(pitch, -Math.PI / 2, Math.PI / 2),
    health: THREE.MathUtils.clamp(Number(state.health) || 0, 0, player.maxHealth),
    weapon: String(state.weapon || '').slice(0, 24),
    alive: state.alive !== false,
  };
}

function getLocalPlayerState() {
  return {
    id: localLanId,
    name: localPlayerName,
    x: player.camera.position.x,
    y: player.camera.position.y,
    z: player.camera.position.z,
    yaw: player.camera.rotation.y,
    pitch: player.camera.rotation.x,
    health: player.health,
    weapon: weapon.current.id,
    alive: player.alive,
  };
}

function getLanPlayersSnapshot() {
  return [getLocalPlayerState(), ...remotePlayerStates.values()].slice(0, 5);
}

function getEnemyTargets() {
  if (lanRole !== 'host' || !lanMatchStarted) return [player];
  const targets = [player];
  for (const [peerId, state] of remotePlayerStates) {
    if (!state.alive) continue;
    targets.push({
      alive: true,
      camera: { position: new THREE.Vector3(state.x, state.y, state.z) },
      damage(amount) {
        const current = remotePlayerStates.get(peerId);
        if (!current?.alive || !lanPeers.get(peerId)?.joined) return;
        current.health = Math.max(0, current.health - amount);
        current.alive = current.health > 0;
        void lanTransport.sendTo(peerId, { type: 'playerDamage', amount }).catch(() => {});
      },
    });
  }
  return targets;
}

async function closeLanSession(notifyPeers = true) {
  const role = lanRole;
  if (!role) return;
  lanRole = null;
  lanMatchStarted = false;
  if (notifyPeers && lanTransport.available) {
    try { await lanTransport.send({ type: role === 'host' ? 'roomClosed' : 'leave' }); } catch {}
  }
  try { await lanTransport.close(role); } catch {}
  lanPeers.clear();
  remotePlayerStates.clear();
  networkPlayers.clear();
}

async function leaveLanLobby() {
  await closeLanSession();
  lanScreen.style.display = 'none';
  startScreen.style.display = 'flex';
}

function startLanMatch(mode) {
  const role = lanRole;
  if (!role) return;
  activeMode = mode === 'zombie' ? 'zombie' : 'training';
  lanMatchStarted = true;
  resetGame(activeMode);
  enemyMgr.networkClient = role === 'client';
  if (role === 'client') {
    const angle = localSpawnSlot * (Math.PI * 2 / 5);
    const spawn = world.playerSpawn.clone();
    spawn.x += Math.sin(angle) * 3;
    spawn.z -= Math.cos(angle) * 3;
    player.reset(spawn);
  }
  lanScreen.style.display = 'none';
  if (isTouchDevice) enterGame();
  else controls.lock();
  updateHud();
}

async function startHostedMatch() {
  if (lanRole !== 'host' || ![...lanPeers.values()].some((peer) => peer.joined)) {
    setLanStatus('برای شروع، دست‌کم یک گوشی مهمان باید وصل شود.', true);
    return;
  }
  try {
    await lanTransport.send({ type: 'start', mode: selectedLanMode });
    startLanMatch(selectedLanMode);
  } catch (error) {
    setLanStatus(error?.message || 'شروع بازی شبکه‌ای ناموفق بود.', true);
  }
}

function removeLanPeer(peerId) {
  lanPeers.delete(peerId);
  remotePlayerStates.delete(peerId);
  renderLanPlayers();
  updateHud();
}

async function handleHostMessage(peerId, message) {
  if (!peerId || !message || typeof message.type !== 'string') return;
  const peer = lanPeers.get(peerId);
  if (message.type === 'join') {
    const joinedPeer = peer || { id: peerId, joined: false, name: 'مهمان' };
    joinedPeer.joined = true;
    joinedPeer.name = String(message.name || 'مهمان').slice(0, 20);
    joinedPeer.playerId = typeof message.playerId === 'string' ? message.playerId.slice(0, 60) : peerId;
    joinedPeer.spawnSlot = Math.min(4, Math.max(1, [...lanPeers.keys()].indexOf(peerId) + 1));
    lanPeers.set(peerId, joinedPeer);
    renderLanPlayers();
    try {
      await lanTransport.sendTo(peerId, {
        type: 'welcome',
        name: localPlayerName,
        spawnSlot: joinedPeer.spawnSlot,
      });
      if (lanMatchStarted) {
        await lanTransport.sendTo(peerId, { type: 'start', mode: activeMode });
        await lanTransport.sendTo(peerId, {
          type: 'state',
          game: enemyMgr.getNetworkState(),
          players: getLanPlayersSnapshot(),
        });
      }
    } catch (error) {
      setLanStatus(error?.message || 'ارسال اطلاعات اتاق به مهمان ناموفق بود.', true);
    }
    return;
  }

  if (message.type === 'player' && peer?.joined && message.state) {
    const playerId = peer.playerId || peerId;
    const state = makePlayerState(playerId, peer.name, message.state);
    if (state) {
      const previous = remotePlayerStates.get(peerId);
      state.health = previous?.health ?? player.maxHealth;
      state.alive = previous?.alive ?? true;
      remotePlayerStates.set(peerId, state);
    }
    return;
  }

  if (message.type === 'damage' && lanMatchStarted) {
    const id = Number(message.enemyId);
    const amount = Number(message.amount);
    if (!Number.isInteger(id) || !Number.isFinite(amount) || amount <= 0 || amount > 75) return;
    const enemy = enemyMgr.enemies.find((candidate) => candidate.netId === id);
    if (enemy?.alive) enemy.takeDamage(amount);
    return;
  }

  if (message.type === 'heal' && lanMatchStarted && peer?.joined) {
    const amount = Number(message.amount);
    const remotePlayer = remotePlayerStates.get(peerId);
    if (!remotePlayer?.alive || !Number.isFinite(amount) || amount <= 0 || amount > 30) return;
    remotePlayer.health = Math.min(player.maxHealth, remotePlayer.health + amount);
    return;
  }

  if (message.type === 'leave') removeLanPeer(peerId);
}

function handleClientMessage(message) {
  if (!message || typeof message.type !== 'string') return;
  if (message.type === 'welcome') {
    localSpawnSlot = THREE.MathUtils.clamp(Math.floor(Number(message.spawnSlot) || 1), 1, 4);
    setLanStatus(`${String(message.name || 'میزبان').slice(0, 20)} را پیدا کردی؛ منتظر شروع بازی بمان.`);
  } else if (message.type === 'playerDamage' && lanMatchStarted) {
    const amount = Number(message.amount);
    if (Number.isFinite(amount) && amount > 0 && amount <= 32) {
      player.damage(amount);
      updateHud();
    }
  } else if (message.type === 'start') {
    startLanMatch(message.mode);
  } else if (message.type === 'state' && lanMatchStarted) {
    if (message.game) enemyMgr.applyNetworkState(message.game);
    remotePlayerStates.clear();
    if (Array.isArray(message.players)) {
      for (const remote of message.players.slice(0, 5)) {
        const state = makePlayerState(remote.id, remote.name, remote);
        if (state) remotePlayerStates.set(state.id, state);
      }
    }
    updateHud();
  } else if (message.type === 'end') {
    if (running && !gameOver) endGame();
  } else if (message.type === 'roomClosed') {
    void handleLanDisconnected('میزبان بازی را بست.');
  }
}

async function handleLanDisconnected(message = 'ارتباط شبکهٔ محلی قطع شد.') {
  const role = lanRole;
  if (!role) return;
  lanRole = null;
  lanMatchStarted = false;
  running = false;
  gameOver = true;
  clearInput();
  document.body.classList.remove('playing');
  pauseScreen.style.display = 'none';
  overScreen.style.display = 'none';
  lanScreen.style.display = 'none';
  startScreen.style.display = 'flex';
  networkPlayers.clear();
  remotePlayerStates.clear();
  lanPeers.clear();
  try { await lanTransport.close(role); } catch {}
  showError(message);
  window.setTimeout(() => { errorEl.style.display = 'none'; }, 5000);
}

async function handleLanMessage(event) {
  const message = event?.message;
  if (lanRole === 'host') await handleHostMessage(event.peerId, message);
  else if (lanRole === 'client') handleClientMessage(message);
}

const lanListenersReady = Promise.all([
  lanTransport.listen('peerConnected', (event) => {
    if (lanRole !== 'host') return;
    lanPeers.set(event.peerId, { id: event.peerId, name: 'مهمان', joined: false });
    renderLanPlayers();
    setLanStatus('یک گوشی وصل شد؛ در حال تکمیل ورود بازیکن…');
  }),
  lanTransport.listen('peerDisconnected', (event) => {
    if (lanRole === 'host') removeLanPeer(event.peerId);
  }),
  lanTransport.listen('message', (event) => {
    void handleLanMessage(event).catch((error) => setLanStatus(error?.message || 'دریافت پیام ناموفق بود.', true));
  }),
  lanTransport.listen('disconnected', () => {
    if (lanRole === 'client') void handleLanDisconnected();
  }),
  lanTransport.listen('error', (event) => {
    setLanStatus(event?.message || 'خطای شبکهٔ محلی رخ داد.', true);
  }),
]);

document.getElementById('lan-host-btn').addEventListener('click', startLanHost);
document.getElementById('lan-join-btn').addEventListener('click', openLanJoin);
document.getElementById('lan-connect-btn').addEventListener('click', connectToLanHost);
document.getElementById('lan-start-match-btn').addEventListener('click', startHostedMatch);
document.getElementById('lan-back-btn').addEventListener('click', leaveLanLobby);
document.getElementById('lan-copy-address').addEventListener('click', async () => {
  const address = lanAddressValue.textContent;
  try {
    await navigator.clipboard.writeText(address);
    setLanStatus('نشانی کپی شد؛ آن را در گوشی مهمان وارد کن.');
  } catch {
    setLanStatus('نشانی را با نگه‌داشتن انگشت روی متن انتخاب و کپی کن.');
  }
});
for (const button of document.querySelectorAll('[data-lan-mode]')) {
  button.addEventListener('click', () => {
    selectedLanMode = button.dataset.lanMode === 'training' ? 'training' : 'zombie';
    for (const choice of document.querySelectorAll('[data-lan-mode]')) {
      choice.classList.toggle('selected', choice === button);
    }
  });
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
        const restored = Math.min(30, player.maxHealth - player.health);
        player.health += restored;
        if (lanRole === 'client' && restored > 0) {
          void lanTransport.send({ type: 'heal', amount: restored }).catch(() => {});
        }
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
  void soundEffects.unlock().catch(() => {});
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
  void soundEffects.unlock().catch(() => {});
  if (isTouchDevice) enterGame();
  else controls.lock();
});
document.getElementById('pause-btn').addEventListener('click', pauseGame);
document.getElementById('pause-menu-btn').addEventListener('click', returnToMenu);
document.getElementById('game-over-menu-btn').addEventListener('click', returnToMenu);
document.getElementById('restart-btn').addEventListener('click', () => {
  if (lanRole === 'client') {
    returnToMenu();
    return;
  }
  if (lanRole === 'host' && lanMatchStarted) {
    void (async () => {
      try {
        await lanTransport.send({ type: 'start', mode: activeMode });
        startLanMatch(activeMode);
      } catch (error) {
        showError(error?.message || 'شروع دوبارهٔ بازی شبکه‌ای ناموفق بود.');
      }
    })();
    return;
  }
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
  if (lanRole) void closeLanSession();
  clearInput();
  document.body.classList.remove('playing');
  if (controls.isLocked) controls.unlock();
  lanScreen.style.display = 'none';
  pauseScreen.style.display = 'none';
  overScreen.style.display = 'none';
  startScreen.style.display = 'flex';
}

function endGame() {
  soundEffects.death();
  if (lanRole === 'host' && lanMatchStarted) {
    void lanTransport.send({ type: 'end' }).catch(() => {});
  }
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
    enemyMgr.update(dt, getEnemyTargets());
    updatePickups(dt);
    updateHud();

    if (lanRole && lanMatchStarted) {
      lanSendTimer += dt;
      if (lanSendTimer >= 0.1) {
        lanSendTimer %= 0.1;
        if (lanRole === 'host') {
          void lanTransport.send({
            type: 'state',
            game: enemyMgr.getNetworkState(),
            players: getLanPlayersSnapshot(),
          }).catch(() => {});
        } else {
          void lanTransport.send({
            type: 'player',
            playerId: localLanId,
            name: localPlayerName,
            state: getLocalPlayerState(),
          }).catch(() => {});
        }
      }
    }
  }
  if (lanRole && lanMatchStarted) {
    networkPlayers.update([...remotePlayerStates.values()], lanRole === 'host' ? 'host' : localLanId, dt);
  }
  renderer.render(scene, camera);
}
animate();
