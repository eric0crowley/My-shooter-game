const MINIMAP_PADDING = 11;
const UPDATE_INTERVAL_SECONDS = 0.1;

const COLORS = Object.freeze({
  background: '#0a1218',
  border: 'rgba(201, 235, 235, 0.27)',
  grid: 'rgba(193, 224, 225, 0.075)',
  cover: '#435158',
  coverEdge: 'rgba(216, 234, 230, 0.28)',
  blue: '#65c9ff',
  red: '#ff746b',
  zombie: '#e6a269',
  health: '#a9e678',
  ammo: '#ffd16a',
  player: '#f6ffff',
});

function clamp(value, minimum, maximum) {
  return Math.min(maximum, Math.max(minimum, Number(value) || 0));
}

function roundedRectPath(context, x, y, width, height, radius) {
  const r = Math.min(radius, width / 2, height / 2);
  context.beginPath();
  context.moveTo(x + r, y);
  context.lineTo(x + width - r, y);
  context.quadraticCurveTo(x + width, y, x + width, y + r);
  context.lineTo(x + width, y + height - r);
  context.quadraticCurveTo(x + width, y + height, x + width - r, y + height);
  context.lineTo(x + r, y + height);
  context.quadraticCurveTo(x, y + height, x, y + height - r);
  context.lineTo(x, y + r);
  context.quadraticCurveTo(x, y, x + r, y);
  context.closePath();
}

export function worldToMinimap(x, z, bounds, size, padding = MINIMAP_PADDING) {
  const safeBounds = Math.max(1, Number(bounds) || 1);
  const safeSize = Math.max(padding * 2 + 1, Number(size) || padding * 2 + 1);
  const span = safeSize - padding * 2;
  const worldX = clamp(x, -safeBounds, safeBounds);
  const worldZ = clamp(z, -safeBounds, safeBounds);
  return {
    x: padding + ((worldX + safeBounds) / (safeBounds * 2)) * span,
    y: padding + ((safeBounds - worldZ) / (safeBounds * 2)) * span,
  };
}

function midpoint(spawns) {
  if (!Array.isArray(spawns) || spawns.length === 0) return null;
  const total = spawns.reduce(
    (sum, spawn) => ({ x: sum.x + spawn.x, z: sum.z + spawn.z }),
    { x: 0, z: 0 }
  );
  return { x: total.x / spawns.length, z: total.z / spawns.length };
}

export class Minimap {
  constructor(canvas, world) {
    this.canvas = canvas;
    this.context = canvas?.getContext?.('2d') || null;
    this.world = world;
    this.elapsed = UPDATE_INTERVAL_SECONDS;
    this.pixelRatio = 0;
    this.cssSize = 0;
  }

  update(deltaSeconds, state) {
    if (!this.context || !this.canvas || !state?.player) return;
    this.elapsed += Math.max(0, Number(deltaSeconds) || 0);
    if (this.elapsed < UPDATE_INTERVAL_SECONDS) return;
    this.elapsed %= UPDATE_INTERVAL_SECONDS;

    const rect = this.canvas.getBoundingClientRect();
    const size = Math.floor(Math.min(rect.width, rect.height));
    if (size <= 0) return;
    const pixelRatio = Math.min(globalThis.devicePixelRatio || 1, 2);
    const backingSize = Math.round(size * pixelRatio);
    if (this.canvas.width !== backingSize || this.canvas.height !== backingSize) {
      this.canvas.width = backingSize;
      this.canvas.height = backingSize;
    }
    this.pixelRatio = pixelRatio;
    this.cssSize = size;

    const context = this.context;
    context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
    context.clearRect(0, 0, size, size);
    roundedRectPath(context, 0.5, 0.5, size - 1, size - 1, 13);
    context.fillStyle = COLORS.background;
    context.fill();
    context.save();
    roundedRectPath(context, 2, 2, size - 4, size - 4, 12);
    context.clip();

    const bounds = this.world.bounds;
    const scale = (size - MINIMAP_PADDING * 2) / (bounds * 2);
    this.drawTeamZones(context, size, bounds, scale);
    this.drawGrid(context, size, bounds);
    this.drawCover(context, size, bounds);
    this.drawLandmarks(context, size, bounds);
    this.drawPickups(context, size, bounds, state.pickups);
    this.drawActors(context, size, bounds, state);

    context.restore();
    roundedRectPath(context, 0.5, 0.5, size - 1, size - 1, 13);
    context.strokeStyle = COLORS.border;
    context.lineWidth = 1;
    context.stroke();

    context.fillStyle = 'rgba(240, 250, 250, 0.72)';
    context.font = '700 8px system-ui, sans-serif';
    context.textAlign = 'left';
    context.textBaseline = 'top';
    context.fillText('نقشه · شمال', 9, 7);
  }

  drawTeamZones(context, size, bounds, scale) {
    for (const [team, color] of [['blue', COLORS.blue], ['red', COLORS.red]]) {
      const center = midpoint(this.world.teamSpawns?.[team]);
      if (!center) continue;
      const point = worldToMinimap(center.x, center.z, bounds, size);
      context.beginPath();
      context.arc(point.x, point.y, 5.5 * scale, 0, Math.PI * 2);
      context.fillStyle = team === 'blue'
        ? 'rgba(72, 186, 255, 0.11)'
        : 'rgba(255, 108, 88, 0.11)';
      context.fill();
      context.strokeStyle = color;
      context.globalAlpha = 0.58;
      context.lineWidth = 1;
      context.stroke();
      context.globalAlpha = 1;
    }
  }

  drawGrid(context, size, bounds) {
    context.strokeStyle = COLORS.grid;
    context.lineWidth = 0.65;
    for (let coordinate = -20; coordinate <= 20; coordinate += 10) {
      const verticalStart = worldToMinimap(coordinate, bounds, bounds, size);
      const verticalEnd = worldToMinimap(coordinate, -bounds, bounds, size);
      context.beginPath();
      context.moveTo(verticalStart.x, verticalStart.y);
      context.lineTo(verticalEnd.x, verticalEnd.y);
      context.stroke();

      const horizontalStart = worldToMinimap(-bounds, coordinate, bounds, size);
      const horizontalEnd = worldToMinimap(bounds, coordinate, bounds, size);
      context.beginPath();
      context.moveTo(horizontalStart.x, horizontalStart.y);
      context.lineTo(horizontalEnd.x, horizontalEnd.y);
      context.stroke();
    }
  }

  drawCover(context, size, bounds) {
    for (const box of this.world.colliders || []) {
      const width = box.maxX - box.minX;
      const depth = box.maxZ - box.minZ;
      if (width >= bounds * 0.35 || depth >= bounds * 0.35) continue;
      const topLeft = worldToMinimap(box.minX, box.maxZ, bounds, size);
      const bottomRight = worldToMinimap(box.maxX, box.minZ, bounds, size);
      const pixelWidth = Math.max(2, bottomRight.x - topLeft.x);
      const pixelHeight = Math.max(2, bottomRight.y - topLeft.y);
      roundedRectPath(context, topLeft.x, topLeft.y, pixelWidth, pixelHeight, 2);
      context.fillStyle = COLORS.cover;
      context.fill();
      context.strokeStyle = COLORS.coverEdge;
      context.lineWidth = 0.6;
      context.stroke();
    }
  }

  drawLandmarks(context, size, bounds) {
    const center = worldToMinimap(0, 0, bounds, size);
    const scale = (size - MINIMAP_PADDING * 2) / (bounds * 2);
    context.beginPath();
    context.arc(center.x, center.y, 4.3 * scale, 0, Math.PI * 2);
    context.strokeStyle = 'rgba(105, 226, 223, 0.56)';
    context.lineWidth = 1;
    context.stroke();

    for (const [team, color] of [['blue', COLORS.blue], ['red', COLORS.red]]) {
      const point = midpoint(this.world.teamSpawns?.[team]);
      if (!point) continue;
      const marker = worldToMinimap(point.x, point.z, bounds, size);
      context.fillStyle = color;
      context.globalAlpha = 0.85;
      context.fillRect(marker.x - 2, marker.y - 2, 4, 4);
      context.globalAlpha = 1;
    }
  }

  drawPickups(context, size, bounds, pickups = []) {
    for (const pickup of pickups) {
      if (!pickup?.active || !pickup.mesh?.visible) continue;
      const point = worldToMinimap(pickup.mesh.position.x, pickup.mesh.position.z, bounds, size);
      context.fillStyle = pickup.type === 'health' ? COLORS.health : COLORS.ammo;
      context.fillRect(point.x - 1.8, point.y - 1.8, 3.6, 3.6);
    }
  }

  drawActors(context, size, bounds, state) {
    const player = state.player;
    const playerPoint = worldToMinimap(player.camera.position.x, player.camera.position.z, bounds, size);

    for (const remote of state.remotePlayers || []) {
      if (!remote || remote.alive === false) continue;
      const point = worldToMinimap(remote.x, remote.z, bounds, size);
      this.drawDot(context, point, COLORS.blue, 2.2);
    }

    for (const enemy of state.enemies || []) {
      if (!enemy?.alive || !enemy.group?.visible) continue;
      const isZombie = enemy.kind === 'zombie';
      const visibleInMode = state.mode === 'tdm'
        ? enemy.team === player.team
        : true;
      if (!visibleInMode) continue;
      const point = worldToMinimap(enemy.group.position.x, enemy.group.position.z, bounds, size);
      const color = isZombie ? COLORS.zombie : enemy.team === 'blue' ? COLORS.blue : COLORS.red;
      this.drawDot(context, point, color, isZombie ? 2.4 : 2.1);
    }

    this.drawPlayerArrow(context, playerPoint, player.camera.rotation.y, player.health, player.maxHealth);
  }

  drawDot(context, point, color, radius) {
    context.beginPath();
    context.arc(point.x, point.y, radius + 1, 0, Math.PI * 2);
    context.fillStyle = 'rgba(6, 12, 16, 0.86)';
    context.fill();
    context.beginPath();
    context.arc(point.x, point.y, radius, 0, Math.PI * 2);
    context.fillStyle = color;
    context.fill();
  }

  drawPlayerArrow(context, point, yaw, health, maxHealth) {
    const healthRatio = clamp(health / Math.max(1, maxHealth), 0, 1);
    const healthColor = healthRatio <= 0.3 ? '#ff7772' : COLORS.player;
    const angle = Math.atan2(-Math.sin(yaw), -Math.cos(yaw));
    context.save();
    context.translate(point.x, point.y);
    context.rotate(angle);
    context.beginPath();
    context.moveTo(0, -6);
    context.lineTo(4.4, 4.2);
    context.lineTo(0, 2.4);
    context.lineTo(-4.4, 4.2);
    context.closePath();
    context.fillStyle = healthColor;
    context.fill();
    context.strokeStyle = 'rgba(6, 12, 16, 0.9)';
    context.lineWidth = 1.1;
    context.stroke();
    context.restore();
  }
}
