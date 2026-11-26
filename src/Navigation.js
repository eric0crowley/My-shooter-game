import { init, NavMeshQuery } from '@recast-navigation/core';
import { threeToSoloNavMesh } from '@recast-navigation/three';

// The current graybox uses a flat XZ collision model, so this navmesh is a
// deliberate first step: it routes AI around static cover without introducing
// runtime physics or a large navigation asset pipeline.
export const DEFAULT_NAVMESH_CONFIG = Object.freeze({
  cs: 0.3,
  ch: 0.2,
  walkableHeight: 9,
  walkableClimb: 2,
  walkableRadius: 2,
  walkableSlopeAngle: 45,
  maxEdgeLen: 12,
  maxSimplificationError: 1.3,
  minRegionArea: 8,
  mergeRegionArea: 20,
  maxVertsPerPoly: 6,
  detailSampleDist: 6,
  detailSampleMaxError: 1,
});

let initialization = null;

function toVector3(value) {
  const x = Number(value?.x);
  const y = Number(value?.y ?? 0);
  const z = Number(value?.z);
  if (![x, y, z].every(Number.isFinite)) return null;
  return { x, y, z };
}

/**
 * Builds one static navigation mesh from the supplied Three.js world meshes.
 * Navigation is an optional enhancement: callers can keep their existing
 * movement fallback if initialization or mesh generation fails.
 */
export async function createNavigationSystem(meshes, config = {}) {
  const sourceMeshes = [...new Set(Array.isArray(meshes) ? meshes : [])].filter(
    (mesh) => mesh?.isMesh && (mesh.geometry?.attributes?.position?.count || 0) >= 3
  );
  if (sourceMeshes.length === 0) {
    throw new Error('Cannot build navigation: no renderable world meshes were supplied.');
  }

  initialization ??= init().catch((error) => {
    initialization = null;
    throw error;
  });
  await initialization;

  const generated = threeToSoloNavMesh(sourceMeshes, {
    ...DEFAULT_NAVMESH_CONFIG,
    ...config,
  });
  if (!generated.success || !generated.navMesh) {
    throw new Error(`Could not generate navigation mesh: ${generated.error || 'unknown error'}`);
  }

  const query = new NavMeshQuery(generated.navMesh);
  let disposed = false;

  return {
    findPath(start, end) {
      if (disposed) return [];
      const from = toVector3(start);
      const to = toVector3(end);
      if (!from || !to) return [];

      const result = query.computePath(from, to, {
        halfExtents: { x: 2.5, y: 4, z: 2.5 },
        maxPathPolys: 512,
        maxStraightPathPoints: 64,
      });
      if (!result.success) return [];
      return result.path.map(({ x, y, z }) => ({ x, y, z }));
    },

    dispose() {
      if (disposed) return;
      disposed = true;
      query.destroy();
      generated.navMesh.destroy();
    },
  };
}
