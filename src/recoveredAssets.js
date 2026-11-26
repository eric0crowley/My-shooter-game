// Small, runtime-ready selections copied from the APK recovery archive into
// Vite's public directory. The source object IDs are retained for traceability.
export const RECOVERED_WEAPON_ASSETS = Object.freeze({
  rifle: Object.freeze({
    displayName: 'M4A1',
    model: '/recovered/weapons/m4a1.obj',
    texture: '/recovered/weapons/m4a1-base.png',
    targetLength: 0.76,
    rotation: Object.freeze([0, Math.PI / 2, 0]),
    position: Object.freeze([0.23, -0.23, -0.62]),
    sourceMesh: 'Mesh_sharedassets1_00000126_M4A1',
    sourceTexture: 'Texture2D_sharedassets1_00000057_M4A1_M4A1_BaseMap',
  }),
  pistol: Object.freeze({
    displayName: 'Glock 19',
    model: '/recovered/weapons/glock19.obj',
    texture: '/recovered/weapons/glock19-base.png',
    targetLength: 0.43,
    rotation: Object.freeze([0, Math.PI / 2, 0]),
    position: Object.freeze([0.22, -0.23, -0.55]),
    sourceMesh: 'Mesh_sharedassets1_00000123_Glock_19',
    sourceTexture: 'Texture2D_sharedassets1_00000053_Glock_19_Glock_19_BaseMap',
  }),
  shotgun: Object.freeze({
    displayName: 'Benelli M4',
    model: '/recovered/weapons/benelli-m4.obj',
    texture: '/recovered/weapons/benelli-m4-base.png',
    targetLength: 0.72,
    rotation: Object.freeze([0, Math.PI / 2, 0]),
    position: Object.freeze([0.24, -0.24, -0.62]),
    sourceMesh: 'Mesh_sharedassets1_00000131_Benelli_M4',
    sourceTexture: 'Texture2D_sharedassets1_00000073_Benelli_M4_Diffuse_1',
  }),
});

export const RECOVERED_ZOMBIE_ASSET = Object.freeze({
  model: '/recovered/zombies/zombie-c.obj',
  texture: '/recovered/zombies/zombie-c-albedo.png',
  targetHeight: 1.72,
  sourceMesh: 'Mesh_sharedassets3_00000044_ZombieC',
  sourceMaterial: 'Material_sharedassets3_00000007_ZombieC_MAT',
  sourceTexture: 'Texture2D_sharedassets3_00000020_ZombieC_MAT_AlbedoTransparency',
});

export const RECOVERED_AUDIO_ASSETS = Object.freeze({
  'shot:rifle': '/recovered/audio/rifle-shot.wav',
  'shot:pistol': '/recovered/audio/pistol-shot.wav',
  'shot:shotgun': '/recovered/audio/shotgun-shot.wav',
  'reload:rifle': '/recovered/audio/rifle-reload.wav',
  'reload:pistol': '/recovered/audio/pistol-reload.wav',
  'reload:shotgun': '/recovered/audio/shotgun-reload.wav',
});
