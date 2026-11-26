// Small 2D (XZ plane) collision helpers used by both the player and the bots.
// We treat every actor as a circle and every wall/obstacle as an axis-aligned
// box, which keeps the math cheap and robust enough for a learning project.

export function clamp(v, min, max) {
  return Math.max(min, Math.min(max, v));
}

// Push a circle (center px,pz | radius r) out of every box it overlaps.
// boxes: Array<{ minX, maxX, minZ, maxZ }>
// Returns the corrected [px, pz].
export function resolveCircleBoxes(px, pz, r, boxes) {
  for (const b of boxes) {
    const cx = clamp(px, b.minX, b.maxX);
    const cz = clamp(pz, b.minZ, b.maxZ);
    const dx = px - cx;
    const dz = pz - cz;
    const d2 = dx * dx + dz * dz;

    if (d2 > 1e-7) {
      // Outside (or on an edge of) the box: push along the shortest exit.
      if (d2 < r * r) {
        const d = Math.sqrt(d2);
        const push = r - d;
        px += (dx / d) * push;
        pz += (dz / d) * push;
      }
    } else {
      // Center is strictly inside the box: eject through the nearest face.
      const left = px - b.minX;
      const right = b.maxX - px;
      const top = pz - b.minZ;
      const bottom = b.maxZ - pz;
      const m = Math.min(left, right, top, bottom);
      if (m === left) px = b.minX - r;
      else if (m === right) px = b.maxX + r;
      else if (m === top) pz = b.minZ - r;
      else pz = b.maxZ + r;
    }
  }
  return [px, pz];
}

// Liang–Barsky segment vs AABB test (in XZ) for simple line-of-sight checks.
export function segmentIntersectsBox(x0, z0, x1, z1, b) {
  let t0 = 0;
  let t1 = 1;
  const dx = x1 - x0;
  const dz = z1 - z0;
  const p = [-dx, dx, -dz, dz];
  const q = [x0 - b.minX, b.maxX - x0, z0 - b.minZ, b.maxZ - z0];

  for (let i = 0; i < 4; i++) {
    if (p[i] === 0) {
      if (q[i] < 0) return false; // parallel and outside this slab
    } else {
      const t = q[i] / p[i];
      if (p[i] < 0) {
        if (t > t1) return false;
        if (t > t0) t0 = t;
      } else {
        if (t < t0) return false;
        if (t < t1) t1 = t;
      }
    }
  }
  return true;
}
