# APK extraction report

> This is a data/asset reconstruction from the IL2CPP APK, not recovered original C# source.

- Unity version: `2022.3.62f1`
- Referenced meshes: 181 (180 OBJ exports)
- Skin data: 26 bind-pose meshes; 25 weighted meshes include 79,390 vertex records, 902 bind poses, source-ordered vertex geometry and 104,862 triangles in `mesh-skin-data.json.gz`; 12,873 implicit fourth influences were corrected to the normalized residual for the Editor Builder
- Referenced materials: 164
- Referenced textures: 114 (114 PNG exports)
- Referenced UI/native sprites: 154 (154 PNG exports)
- Embedded fonts exported: 4/4 (3 referenced by UI Text, 374.8 KiB)
- Shared-asset UI prefabs indexed: 3 roots, 7 objects, 4 styled Images, 2 styled Texts, 1 Buttons, 2 styled Shadow/Outline effects
- Audio clips indexed: 151; audio files exported: 151 (mp3=2, wav=149; all, 16.70 MiB)
- FSB5/MPEG MP3 export strips zero alignment padding; the offline validator checks MPEG frame structure, channels, sample rate, and frame-derived duration against the manifest.
- Animation data: 177 clips; 5,064 streamed curves, 2,725 dense curves/12,422 frames, 7,706 constant values; decoded muscle clips, bindings and events are preserved in `animation-curve-data.json.gz` (inspection data, not playable Unity clips)
- Animator rig metadata: 56 AnimatorControllers (250 states, 225 transition records, 227 blend trees); 20 Avatars (1,105 skeleton nodes, 478 human mappings, 1,105 transform-name entries). Full decoded trees are preserved in compressed data manifests (not rebuilt as executable Unity assets)
- UGUI presentation data: 1200 Images, 548 Texts and 359 Shadow/Outline effects (serialized style settings)
- UI Buttons: 289 (transition/color/navigation fields restored); 551 persistent onClick calls decoded; Builder can rebind 123 AudioSource.Play and 63 GameObject.SetActive calls, while 365 custom IL2CPP handlers remain metadata-only
- Canvas metadata: 29 Canvases, 29 CanvasScalers, 27 CanvasGroups
- Renderer settings: 8376 (MeshRenderer=7526, ParticleSystemRenderer=132, SkinnedMeshRenderer=716, SpriteRenderer=2)
- Camera and light settings: 6 Cameras, 115 Lights
- UI text values recovered: 546
- UI Text Font references resolved from serialized PPtrs: 550

## Scenes

- `level0` → 00 - Splash: 12 GameObjects
- `level1` → 01 - MainMenu: 1612 GameObjects
- `level2` → 02 - GamePlay: 26373 GameObjects
- `level3` → 03 - Z-GamePlay: 28494 GameObjects

## Extraction warnings

- Mesh Mesh_sharedassets2_00000375_power_line: ValueError: UnityPy returned an empty/non-exportable mesh
