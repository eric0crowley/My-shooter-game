import * as THREE from 'three';

// Procedural training arena: geometry is kept asset-free so it can ship with
// the browser build and be bundled directly into a Capacitor APK.
export function buildWorld(scene) {
  const colliders = [];
  const navigationMeshes = [];
  const size = 60;
  const half = size / 2;
  const wallH = 6;
  const wallT = 1;

  // ---- Floor ----
  const floorMat = new THREE.MeshStandardMaterial({
    color: 0x26343b,
    roughness: 0.94,
    metalness: 0.08,
  });
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(size, size), floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  scene.add(floor);
  navigationMeshes.push(floor);

  const grid = new THREE.GridHelper(size, 30, 0x426369, 0x30434a);
  grid.position.y = 0.025;
  const gridMaterials = Array.isArray(grid.material) ? grid.material : [grid.material];
  for (const material of gridMaterials) {
    material.transparent = true;
    material.opacity = 0.38;
    material.depthWrite = false;
  }
  scene.add(grid);

  // ---- Perimeter walls and subtle interior light strips ----
  const wallMat = new THREE.MeshStandardMaterial({ color: 0x17232b, roughness: 0.88, metalness: 0.18 });
  const wallTrimMat = new THREE.MeshStandardMaterial({
    color: 0x327578,
    emissive: 0x12484b,
    emissiveIntensity: 0.8,
    roughness: 0.4,
    metalness: 0.35,
  });

  function addWall(cx, cz, w, d) {
    const wall = new THREE.Mesh(new THREE.BoxGeometry(w, wallH, d), wallMat);
    wall.position.set(cx, wallH / 2, cz);
    wall.castShadow = true;
    wall.receiveShadow = true;
    scene.add(wall);
    navigationMeshes.push(wall);
    colliders.push({ minX: cx - w / 2, maxX: cx + w / 2, minZ: cz - d / 2, maxZ: cz + d / 2 });

    // A narrow emissive stripe sits on the arena-facing wall surface.
    const horizontal = w > d;
    const strip = new THREE.Mesh(
      horizontal
        ? new THREE.BoxGeometry(w - 2, 0.055, 0.035)
        : new THREE.BoxGeometry(0.035, 0.055, d - 2),
      wallTrimMat
    );
    const innerX = cx - Math.sign(cx || 1) * (horizontal ? 0 : w / 2);
    const innerZ = cz - Math.sign(cz || 1) * (horizontal ? d / 2 : 0);
    strip.position.set(innerX, wallH - 0.85, innerZ);
    scene.add(strip);
  }

  addWall(0, -half, size, wallT);
  addWall(0, half, size, wallT);
  addWall(-half, 0, wallT, size);
  addWall(half, 0, wallT, size);

  // ---- Cover ----
  const crateMat = new THREE.MeshStandardMaterial({ color: 0x536064, roughness: 0.76, metalness: 0.22 });
  const crateTopMat = new THREE.MeshStandardMaterial({
    color: 0x75847f,
    emissive: 0x192c2c,
    emissiveIntensity: 0.36,
    roughness: 0.62,
    metalness: 0.2,
  });
  const obstacleDefs = [
    [-10, -10, 4, 4, 4], [10, 10, 4, 4, 4], [12, -8, 3, 3, 3], [-12, 8, 3, 3, 3],
    [0, 0, 6, 2, 3], [-8, 14, 3, 6, 3], [8, -14, 3, 6, 3], [18, 0, 3, 8, 3],
    [-18, 0, 3, 8, 3], [0, 18, 8, 3, 3], [0, -18, 8, 3, 3],
  ];

  for (const [x, z, w, d, h] of obstacleDefs) {
    const cover = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), crateMat);
    cover.position.set(x, h / 2, z);
    cover.castShadow = true;
    cover.receiveShadow = true;
    scene.add(cover);
    navigationMeshes.push(cover);

    const topMark = new THREE.Mesh(
      new THREE.BoxGeometry(Math.max(0.4, w * 0.58), 0.06, Math.max(0.3, d * 0.16)),
      crateTopMat
    );
    topMark.position.set(x, h + 0.035, z);
    scene.add(topMark);
    colliders.push({ minX: x - w / 2, maxX: x + w / 2, minZ: z - d / 2, maxZ: z + d / 2 });
  }

  // ---- Pickups (placed in open lanes, not inside cover) ----
  const pickups = [];
  const pickupDefs = [
    { x: -5, z: 11, type: 'health' },
    { x: 7, z: 7, type: 'ammo' },
    { x: -5, z: -5, type: 'health' },
    { x: 5, z: -8, type: 'ammo' },
    { x: 13, z: 4, type: 'health' },
    { x: -14, z: -6, type: 'ammo' },
  ];

  for (const def of pickupDefs) {
    const isHealth = def.type === 'health';
    const color = isHealth ? 0x9deb78 : 0xffc85c;
    const group = new THREE.Group();
    const core = new THREE.Mesh(
      isHealth ? new THREE.OctahedronGeometry(0.34, 0) : new THREE.BoxGeometry(0.52, 0.34, 0.42),
      new THREE.MeshStandardMaterial({
        color,
        emissive: color,
        emissiveIntensity: 0.62,
        roughness: 0.38,
        metalness: 0.18,
      })
    );
    core.castShadow = true;
    group.add(core);

    const iconMat = new THREE.MeshBasicMaterial({ color: 0x17211d });
    if (isHealth) {
      const upright = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.32, 0.055), iconMat);
      const crossbar = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.09, 0.055), iconMat);
      upright.position.z = 0.3;
      crossbar.position.z = 0.3;
      group.add(upright, crossbar);
    } else {
      for (let i = -1; i <= 1; i++) {
        const mark = new THREE.Mesh(new THREE.BoxGeometry(0.055, 0.22, 0.04), iconMat);
        mark.position.set(i * 0.13, 0, 0.22);
        group.add(mark);
      }
    }

    const baseY = 0.95;
    group.position.set(def.x, baseY, def.z);
    scene.add(group);
    pickups.push({
      mesh: group,
      type: def.type,
      baseY,
      phase: Math.random() * Math.PI * 2,
      active: true,
      respawnAt: 0,
    });
  }

  // ---- Lighting ----
  scene.add(new THREE.HemisphereLight(0xc6e1eb, 0x171d21, 0.78));
  const sun = new THREE.DirectionalLight(0xfff3dd, 1.35);
  sun.position.set(20, 40, 10);
  sun.castShadow = true;
  sun.shadow.mapSize.set(1024, 1024);
  sun.shadow.camera.left = -40;
  sun.shadow.camera.right = 40;
  sun.shadow.camera.top = 40;
  sun.shadow.camera.bottom = -40;
  scene.add(sun);

  const playerSpawn = new THREE.Vector3(0, 1.7, 24);
  const teamSpawns = {
    blue: [
      new THREE.Vector3(0, 0, 24),
      new THREE.Vector3(-20, 0, 24), new THREE.Vector3(-10, 0, 24),
      new THREE.Vector3(10, 0, 24), new THREE.Vector3(20, 0, 24),
    ],
    red: [
      new THREE.Vector3(-20, 0, -24), new THREE.Vector3(-10, 0, -24),
      new THREE.Vector3(0, 0, -24), new THREE.Vector3(10, 0, -24),
      new THREE.Vector3(20, 0, -24),
    ],
  };

  // Paint team zones and the central crossfire mark onto the floor. These
  // elements are decorative only and do not alter collision or navigation.
  const bluePaint = new THREE.MeshBasicMaterial({
    color: 0x48baff,
    transparent: true,
    opacity: 0.13,
    depthWrite: false,
  });
  const redPaint = new THREE.MeshBasicMaterial({
    color: 0xff6c58,
    transparent: true,
    opacity: 0.13,
    depthWrite: false,
  });
  for (const [spawns, material] of [[teamSpawns.blue, bluePaint], [teamSpawns.red, redPaint]]) {
    const center = spawns.reduce(
      (sum, spawn) => sum.add(spawn),
      new THREE.Vector3()
    ).multiplyScalar(1 / Math.max(1, spawns.length));
    const zone = new THREE.Mesh(new THREE.CircleGeometry(5.5, 40), material);
    zone.rotation.x = -Math.PI / 2;
    zone.position.set(center.x, 0.035, center.z);
    scene.add(zone);

    const boundary = new THREE.Mesh(
      new THREE.TorusGeometry(5.5, 0.045, 6, 64),
      material.clone()
    );
    boundary.rotation.x = Math.PI / 2;
    boundary.position.set(center.x, 0.06, center.z);
    scene.add(boundary);
  }

  const centerMark = new THREE.Mesh(
    new THREE.TorusGeometry(4.3, 0.055, 6, 72),
    new THREE.MeshBasicMaterial({
      color: 0x79e1d9,
      transparent: true,
      opacity: 0.56,
      depthWrite: false,
    })
  );
  centerMark.rotation.x = Math.PI / 2;
  centerMark.position.y = 0.055;
  scene.add(centerMark);

  return {
    colliders,
    navigationMeshes,
    bounds: half,
    pickups,
    playerSpawn,
    teamSpawns,
    enemySpawns: [
      new THREE.Vector3(-20, 0, -20), new THREE.Vector3(20, 0, -20),
      new THREE.Vector3(-22, 0, 0), new THREE.Vector3(22, 0, 0),
      new THREE.Vector3(0, 0, -24), new THREE.Vector3(-14, 0, -14),
      new THREE.Vector3(14, 0, 14),
    ],
  };
}
