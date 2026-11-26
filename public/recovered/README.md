# Runtime APK assets used by the Three.js prototype

This folder contains a small, directly loadable selection copied from the recovery data under `unity-reconstruction/Assets/Recovered/`.

- `weapons/`: OBJ meshes and PNG base maps for an M4A1, Glock 19, and Benelli M4, used as the three first-person weapon models.
- `zombies/`: the static OBJ export and albedo map for the original ZombieC character. OBJ has no skin weights, so it receives only a lightweight procedural sway.
- `audio/`: the APK's rifle, pistol, and shotgun firing/reload clips.
- `src/recoveredAssets.js` records the original Unity asset IDs and the browser paths.

The selected assets are loaded at runtime by Three.js/Vite; no Unity Editor is needed for this path. They are recovered game assets, not reconstructed source code. The rest of the extracted assets and method pseudocode remain in `unity-reconstruction/Assets/Recovered/`.
