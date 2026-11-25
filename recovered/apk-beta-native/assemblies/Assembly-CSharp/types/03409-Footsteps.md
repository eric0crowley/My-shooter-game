# `Footsteps` — TypeDefIndex 3409

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `FPSRigidBodyWalker` | `FPSWalkerComponent` |
| `0x28` | `FPSPlayer` | `FPSPlayerComponent` |
| `0x30` | `InputControl` | `InputComponent` |
| `0x38` | `GameObject` | `playerObj` |
| `0x40` | `string` | `materialType` |
| `0x48` | `float` | `volumeAmt` |
| `0x50` | `AudioClip` | `footStepClip` |
| `0x58` | `int` | `terrainIndex` |
| `0x5C` | `bool` | `onTerrain` |
| `0x60` | `int` | `dirtTerrainIndex1` |
| `0x64` | `int` | `dirtTerrainIndex2` |
| `0x68` | `int` | `dirtTerrainIndex3` |
| `0x6C` | `float` | `dirtStepVol` |
| `0x70` | `AudioClip[]` | `dirtSteps` |
| `0x78` | `int` | `stoneTerrainIndex1` |
| `0x7C` | `int` | `stoneTerrainIndex2` |
| `0x80` | `int` | `stoneTerrainIndex3` |
| `0x84` | `float` | `stoneStepVol` |
| `0x88` | `AudioClip[]` | `stoneSteps` |
| `0x90` | `int` | `grassTerrainIndex1` |
| `0x94` | `int` | `grassTerrainIndex2` |
| `0x98` | `int` | `grassTerrainIndex3` |
| `0x9C` | `float` | `grassStepVol` |
| `0xA0` | `AudioClip[]` | `grassSteps` |
| `0xA8` | `int` | `gravelTerrainIndex1` |
| `0xAC` | `int` | `gravelTerrainIndex2` |
| `0xB0` | `int` | `gravelTerrainIndex3` |
| `0xB4` | `float` | `gravelStepVol` |
| `0xB8` | `AudioClip[]` | `gravelSteps` |
| `0xC0` | `int` | `sandTerrainIndex1` |
| `0xC4` | `int` | `sandTerrainIndex2` |
| `0xC8` | `int` | `sandTerrainIndex3` |
| `0xCC` | `float` | `sandStepVol` |
| `0xD0` | `AudioClip[]` | `sandSteps` |
| `0xD8` | `float` | `defaultStepVol` |
| `0xE0` | `AudioClip[]` | `defaultSteps` |
| `0xE8` | `float` | `woodStepVol` |
| `0xF0` | `AudioClip[]` | `woodSteps` |
| `0xF8` | `float` | `metalStepVol` |
| `0x100` | `AudioClip[]` | `metalSteps` |
| `0x108` | `float` | `waterSoundVol` |
| `0x110` | `AudioClip[]` | `waterSounds` |
| `0x118` | `float` | `climbSoundVol` |
| `0x120` | `AudioClip[]` | `climbSounds` |
| `0x128` | `float` | `proneStepVol` |
| `0x130` | `AudioClip[]` | `proneSteps` |
| `0x138` | `AudioClip` | `dirtLand` |
| `0x140` | `AudioClip` | `metalLand` |
| `0x148` | `AudioClip` | `woodLand` |
| `0x150` | `AudioClip` | `waterLand` |
| `0x158` | `AudioClip` | `stoneLand` |
| `0x160` | `float` | `foliageRustleVol` |
| `0x168` | `AudioClip[]` | `foliageRustles` |
| `0x170` | `AudioSource` | `aSource` |
| `0x178` | `Terrain` | `terrain` |
| `0x180` | `TerrainData` | `terrainData` |
| `0x188` | `Vector3` | `terrainPos` |

## `Footsteps.Start` — RVA `0xc9c3e8`

- Lift status: **exact**; input span: 552 bytes; span to next metadata RVA: 552 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=78 (informational only).

```csharp
public static ulong Footsteps_Start_RVAc9c3e8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4A8UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9C450;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4A8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9C450;
        label_0xC9C450:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x38UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD10UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x20UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5A0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x28UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x30UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x20 = unchecked((ulong)((x19) + (0x170UL)));
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x170UL))), x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C548UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176AAA8UL /* metadata target: AudioSource.set_spatialBlend */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176AB7CUL /* metadata target: AudioSource.set_playOnAwake */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17D6EACUL /* metadata target: Terrain.get_activeTerrain */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9C590;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9C590;
        label_0xC9C590:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C600;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17D6EACUL /* metadata target: Terrain.get_activeTerrain */, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x178UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x178UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x178UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17D6CF4UL /* metadata target: Terrain.get_terrainData */, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x180UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x180UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x178UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9C60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x188UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x18CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x190UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        goto label_0xC9C600;
        label_0xC9C600:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC9C60C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `Footsteps.FootstepSfx` — RVA `0xc9c610`

- Lift status: **partial**; input span: 1872 bytes; span to next metadata RVA: 1872 bytes.
- Metadata signature: `public void FootstepSfx() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=234 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xc9ca40; reason: Unknown IR expression at 0xc9ca40

```csharp
public static ulong Footsteps_FootstepSfx_RVAc9c610(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13223676 = default(uint);
        uint __arm64_flags_left_13223832 = default(uint);
        uint __arm64_flags_left_13223912 = default(uint);
        uint __arm64_flags_left_13223972 = default(uint);
        uint __arm64_flags_left_13224136 = default(uint);
        uint __arm64_flags_left_13224148 = default(uint);
        uint __arm64_flags_left_13224160 = default(uint);
        uint __arm64_flags_left_13224172 = default(uint);
        uint __arm64_flags_left_13224184 = default(uint);
        uint __arm64_flags_left_13224196 = default(uint);
        uint __arm64_flags_left_13224208 = default(uint);
        uint __arm64_flags_left_13224220 = default(uint);
        uint __arm64_flags_left_13224232 = default(uint);
        uint __arm64_flags_left_13224244 = default(uint);
        uint __arm64_flags_left_13224256 = default(uint);
        uint __arm64_flags_left_13224268 = default(uint);
        uint __arm64_flags_left_13224280 = default(uint);
        uint __arm64_flags_left_13224292 = default(uint);
        uint __arm64_flags_left_13224304 = default(uint);
        uint __arm64_flags_left_13224340 = default(uint);
        uint __arm64_flags_left_13224356 = default(uint);
        uint __arm64_flags_left_13224372 = default(uint);
        uint __arm64_flags_left_13224388 = default(uint);
        uint __arm64_flags_left_13224456 = default(uint);
        uint __arm64_flags_left_13224504 = default(uint);
        uint __arm64_flags_left_13224524 = default(uint);
        uint __arm64_flags_left_13224592 = default(uint);
        uint __arm64_flags_left_13224640 = default(uint);
        uint __arm64_flags_left_13224656 = default(uint);
        uint __arm64_flags_left_13224724 = default(uint);
        uint __arm64_flags_left_13224824 = default(uint);
        uint __arm64_flags_left_13224924 = default(uint);
        uint __arm64_flags_left_13225024 = default(uint);
        uint __arm64_flags_left_13225124 = default(uint);
        uint __arm64_flags_left_13225196 = default(uint);
        uint __arm64_flags_right_13223676 = default(uint);
        uint __arm64_flags_right_13223832 = default(uint);
        uint __arm64_flags_right_13223912 = default(uint);
        uint __arm64_flags_right_13223972 = default(uint);
        uint __arm64_flags_right_13224136 = default(uint);
        uint __arm64_flags_right_13224148 = default(uint);
        uint __arm64_flags_right_13224160 = default(uint);
        uint __arm64_flags_right_13224172 = default(uint);
        uint __arm64_flags_right_13224184 = default(uint);
        uint __arm64_flags_right_13224196 = default(uint);
        uint __arm64_flags_right_13224208 = default(uint);
        uint __arm64_flags_right_13224220 = default(uint);
        uint __arm64_flags_right_13224232 = default(uint);
        uint __arm64_flags_right_13224244 = default(uint);
        uint __arm64_flags_right_13224256 = default(uint);
        uint __arm64_flags_right_13224268 = default(uint);
        uint __arm64_flags_right_13224280 = default(uint);
        uint __arm64_flags_right_13224292 = default(uint);
        uint __arm64_flags_right_13224304 = default(uint);
        uint __arm64_flags_right_13224340 = default(uint);
        uint __arm64_flags_right_13224356 = default(uint);
        uint __arm64_flags_right_13224372 = default(uint);
        uint __arm64_flags_right_13224388 = default(uint);
        uint __arm64_flags_right_13224456 = default(uint);
        uint __arm64_flags_right_13224504 = default(uint);
        uint __arm64_flags_right_13224524 = default(uint);
        uint __arm64_flags_right_13224592 = default(uint);
        uint __arm64_flags_right_13224640 = default(uint);
        uint __arm64_flags_right_13224656 = default(uint);
        uint __arm64_flags_right_13224724 = default(uint);
        uint __arm64_flags_right_13224824 = default(uint);
        uint __arm64_flags_right_13224924 = default(uint);
        uint __arm64_flags_right_13225024 = default(uint);
        uint __arm64_flags_right_13225124 = default(uint);
        uint __arm64_flags_right_13225196 = default(uint);
        float __arm64_float_flags_left_13223588 = default(float);
        float __arm64_float_flags_left_13223608 = default(float);
        float __arm64_float_flags_left_13223620 = default(float);
        float __arm64_float_flags_left_13224024 = default(float);
        float __arm64_float_flags_right_13223588 = default(float);
        float __arm64_float_flags_right_13223608 = default(float);
        float __arm64_float_flags_right_13223620 = default(float);
        float __arm64_float_flags_right_13224024 = default(float);
        ulong __arm64_load_address_13223776 = default(ulong);
        ulong __arm64_load_address_13225300 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4A9UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9C694;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4A9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9C694;
        label_0xC9C694:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C69CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_13223588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13223588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13223588 <= __arm64_float_flags_right_13223588) || ((__arm64_float_flags_left_13223588 != __arm64_float_flags_left_13223588) || (__arm64_float_flags_right_13223588 != __arm64_float_flags_right_13223588))))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C6B4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0xDCUL))))), 0));
        __arm64_float_flags_left_13223608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13223608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13223608 != __arm64_float_flags_right_13223608) || ((__arm64_float_flags_left_13223608 != __arm64_float_flags_left_13223608) || (__arm64_float_flags_right_13223608 != __arm64_float_flags_right_13223608))))
        {
            goto label_0xC9C6CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C6C0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0xE0UL))))), 0));
        __arm64_float_flags_left_13223620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13223620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13223620 == __arm64_float_flags_right_13223620))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            goto label_0xC9C6CC;
        }
        label_0xC9C6CC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2DCUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C768;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13223676 = unchecked((uint)(x0));
        __arm64_flags_right_13223676 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13223676 >= __arm64_flags_right_13223676))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xD8UL))))), 0));
        goto label_0xC9C720;
        label_0xC9C720:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x120UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            goto label_0xC9C72C;
        }
        label_0xC9C72C:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C740UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x48UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x1 = 0x0UL;
        __arm64_load_address_13223776 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13223776)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13223776) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */);
        label_0xC9C768:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x295UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C7C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x296UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13223832 = unchecked((uint)(x0));
        __arm64_flags_right_13223832 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13223832 >= __arm64_flags_right_13223832))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xC8UL))))), 0));
        goto label_0xC9C720;
        label_0xC9C7C0:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x255UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C838;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13223912 = unchecked((uint)(x0));
        __arm64_flags_right_13223912 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13223912 >= __arm64_flags_right_13223912))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFD0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C810UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x108UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x256UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_flags_left_13223972 = unchecked((uint)(x8));
        __arm64_flags_right_13223972 = unchecked((uint)0x0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_13223972) - (__arm64_flags_right_13223972))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x48UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x0 != 0x0UL))
        {
            goto label_0xC9C72C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C834UL);
        }
        goto label_0xC9CD48;
        label_0xC9C838:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x228UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C840UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2ACUL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x550UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13224024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13224024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13224024 >= __arm64_float_flags_right_13224024) || ((__arm64_float_flags_left_13224024 != __arm64_float_flags_left_13224024) || (__arm64_float_flags_right_13224024 != __arm64_float_flags_right_13224024))))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x5CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C97C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17D6EACUL /* metadata target: Terrain.get_activeTerrain */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9C890;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9C890;
        label_0xC9C890:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC9CD60UL /* metadata target: Footsteps.GetTerrainTextureIndex */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x60UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x58UL))), unchecked((uint)(x0)));
        __arm64_flags_left_13224136 = unchecked((uint)(x0));
        __arm64_flags_right_13224136 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224136) - (__arm64_flags_right_13224136))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CC84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x64UL))))));
        __arm64_flags_left_13224148 = unchecked((uint)(x0));
        __arm64_flags_right_13224148 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224148) - (__arm64_flags_right_13224148))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CC84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x68UL))))));
        __arm64_flags_left_13224160 = unchecked((uint)(x0));
        __arm64_flags_right_13224160 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224160) - (__arm64_flags_right_13224160))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CC84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x78UL))))));
        __arm64_flags_left_13224172 = unchecked((uint)(x0));
        __arm64_flags_right_13224172 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224172) - (__arm64_flags_right_13224172))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CA70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x7CUL))))));
        __arm64_flags_left_13224184 = unchecked((uint)(x0));
        __arm64_flags_right_13224184 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224184) - (__arm64_flags_right_13224184))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CA70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x80UL))))));
        __arm64_flags_left_13224196 = unchecked((uint)(x0));
        __arm64_flags_right_13224196 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224196) - (__arm64_flags_right_13224196))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CA70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x90UL))))));
        __arm64_flags_left_13224208 = unchecked((uint)(x0));
        __arm64_flags_right_13224208 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224208) - (__arm64_flags_right_13224208))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C9E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x94UL))))));
        __arm64_flags_left_13224220 = unchecked((uint)(x0));
        __arm64_flags_right_13224220 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224220) - (__arm64_flags_right_13224220))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C9E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x98UL))))));
        __arm64_flags_left_13224232 = unchecked((uint)(x0));
        __arm64_flags_right_13224232 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224232) - (__arm64_flags_right_13224232))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9C9E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xA8UL))))));
        __arm64_flags_left_13224244 = unchecked((uint)(x0));
        __arm64_flags_right_13224244 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224244) - (__arm64_flags_right_13224244))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CAF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xACUL))))));
        __arm64_flags_left_13224256 = unchecked((uint)(x0));
        __arm64_flags_right_13224256 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224256) - (__arm64_flags_right_13224256))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CAF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xB0UL))))));
        __arm64_flags_left_13224268 = unchecked((uint)(x0));
        __arm64_flags_right_13224268 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224268) - (__arm64_flags_right_13224268))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CAF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xC0UL))))));
        __arm64_flags_left_13224280 = unchecked((uint)(x0));
        __arm64_flags_right_13224280 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224280) - (__arm64_flags_right_13224280))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CBBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xC4UL))))));
        __arm64_flags_left_13224292 = unchecked((uint)(x0));
        __arm64_flags_right_13224292 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224292) - (__arm64_flags_right_13224292))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CBBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xC8UL))))));
        __arm64_flags_left_13224304 = unchecked((uint)(x0));
        __arm64_flags_right_13224304 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224304) - (__arm64_flags_right_13224304))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CBBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9C978UL);
        }
        goto label_0xC9CCCC;
        label_0xC9C97C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x1 = 0x0UL;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCEB858UL /* metadata target: <PrivateImplementationDetails>.ComputeStringHash */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1E1DUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x582BUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224340 = unchecked((uint)(x0));
        __arm64_flags_right_13224340 = unchecked((uint)(x8));
        if (((__arm64_flags_left_13224340 >= __arm64_flags_right_13224340) && (!((unchecked((uint)((__arm64_flags_left_13224340) - (__arm64_flags_right_13224340))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC9CA30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x3588UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x4E1UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224356 = unchecked((uint)(x0));
        __arm64_flags_right_13224356 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224356) - (__arm64_flags_right_13224356))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CB3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xCD83UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E40UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224372 = unchecked((uint)(x0));
        __arm64_flags_right_13224372 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224372) - (__arm64_flags_right_13224372))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CBA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1E1DUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x582BUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224388 = unchecked((uint)(x0));
        __arm64_flags_right_13224388 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13224388) - (__arm64_flags_right_13224388))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            goto label_0xC9C9E8;
        }
        label_0xC9C9E8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13224456 = unchecked((uint)(x0));
        __arm64_flags_right_13224456 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13224456 >= __arm64_flags_right_13224456))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x4CUL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CA30:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x317CUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xA951UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224504 = unchecked((uint)(x0));
        __arm64_flags_right_13224504 = unchecked((uint)(x8));
        if (((__arm64_flags_left_13224504 >= __arm64_flags_right_13224504) && (!((unchecked((uint)((__arm64_flags_left_13224504) - (__arm64_flags_right_13224504))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC9CAB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9CA40UL);
        }
        RuntimeCalls.Unsupported("b.eq", 0xC9CA40UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9CC04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xCA9AUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x6DD4UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224524 = unchecked((uint)(x0));
        __arm64_flags_right_13224524 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13224524) - (__arm64_flags_right_13224524))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            goto label_0xC9CA70;
        }
        label_0xC9CA70:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13224592 = unchecked((uint)(x0));
        __arm64_flags_right_13224592 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13224592 >= __arm64_flags_right_13224592))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x34UL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CAB8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x3C0UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xAFB8UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224640 = unchecked((uint)(x0));
        __arm64_flags_right_13224640 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13224640) - (__arm64_flags_right_13224640))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CC68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x6F1AUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xF8F2UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13224656 = unchecked((uint)(x0));
        __arm64_flags_right_13224656 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13224656) - (__arm64_flags_right_13224656))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            goto label_0xC9CAF4;
        }
        label_0xC9CAF4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13224724 = unchecked((uint)(x0));
        __arm64_flags_right_13224724 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13224724 >= __arm64_flags_right_13224724))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x64UL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CB3C:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13224824 = unchecked((uint)(x0));
        __arm64_flags_right_13224824 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13224824 >= __arm64_flags_right_13224824))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x98UL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CBA0:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            goto label_0xC9CBBC;
        }
        label_0xC9CBBC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13224924 = unchecked((uint)(x0));
        __arm64_flags_right_13224924 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13224924 >= __arm64_flags_right_13224924))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x7CUL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CC04:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13225024 = unchecked((uint)(x0));
        __arm64_flags_right_13225024 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13225024 >= __arm64_flags_right_13225024))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xA8UL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CC68:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD0UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CCCC;
        }
        else
        {
            goto label_0xC9CC84;
        }
        label_0xC9CC84:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13225124 = unchecked((uint)(x0));
        __arm64_flags_right_13225124 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13225124 >= __arm64_flags_right_13225124))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x1CUL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CCCC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9CD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC9CD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13225196 = unchecked((uint)(x0));
        __arm64_flags_right_13225196 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13225196 >= __arm64_flags_right_13225196))
        {
            goto label_0xC9CD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x50UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x88UL))))), 0));
        goto label_0xC9CD10;
        label_0xC9CD10:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC9CD14;
        label_0xC9CD14:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9CD30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9CD2CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9CD30;
        label_0xC9CD30:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CD4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC9C72C;
        }
        else
        {
            goto label_0xC9CD48;
        }
        label_0xC9CD48:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC9CD4C;
        label_0xC9CD4C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_13225300 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13225300)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13225300) + (0x20UL)));
        return x0;
        label_0xC9CD5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `Footsteps.GetTerrainTextureIndex` — RVA `0xc9cd60`

- Lift status: **partial**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `private int GetTerrainTextureIndex(Vector3 WorldPos) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=10 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fcsel' at 0xc9cdac; reason: Unknown IR expression at 0xc9cdac

```csharp
public static uint Footsteps_GetTerrainTextureIndex_RVAc9cd60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_13225336 = default(ulong);
        ulong __arm64_flags_left_13225364 = default(ulong);
        ulong __arm64_flags_left_13225392 = default(ulong);
        ulong __arm64_flags_right_13225336 = default(ulong);
        ulong __arm64_flags_right_13225364 = default(ulong);
        ulong __arm64_flags_right_13225392 = default(ulong);
        float __arm64_float_flags_left_13225376 = default(float);
        float __arm64_float_flags_right_13225376 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC9CDD0UL /* metadata target: Footsteps.GetTexturesAtPoint */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CDCC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x8 = x0;
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x20UL)))))))));
        __arm64_flags_left_13225336 = x10;
        __arm64_flags_right_13225336 = 0x1UL;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_13225336) - (__arm64_flags_right_13225336))))) < unchecked((long)0x0UL)) != (((unchecked((long)(__arm64_flags_left_13225336)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_13225336)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_13225336) - (__arm64_flags_right_13225336))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_13225336)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC9CDBC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x10 = 0x0UL;
        x11 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x9))))));
        x8 = unchecked((ulong)((x8) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC9CD94;
        label_0xC9CD94:
        ;
        __arm64_flags_left_13225364 = x9;
        __arm64_flags_right_13225364 = x10;
        if ((unchecked((ulong)((__arm64_flags_left_13225364) - (__arm64_flags_right_13225364))) == 0x0UL))
        {
            goto label_0xC9CDC8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC9CD9CUL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x2UL)))))))))), 0));
        __arm64_float_flags_left_13225376 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13225376 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x0 = unchecked((ulong)(((__arm64_float_flags_left_13225376 > __arm64_float_flags_right_13225376) ? unchecked((uint)(x10)) : unchecked((uint)(x0)))));
        x10 = unchecked((ulong)((x10) + (0x1UL)));
        RuntimeCalls.Unsupported("fcsel", 0xC9CDACUL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_flags_left_13225392 = x11;
        __arm64_flags_right_13225392 = x10;
        if ((!((unchecked((ulong)((__arm64_flags_left_13225392) - (__arm64_flags_right_13225392))) == 0x0UL))))
        {
            goto label_0xC9CD94;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC9CDB8UL)));
        }
        goto label_0xC9CDC0;
        label_0xC9CDBC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC9CDC0;
        label_0xC9CDC0:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC9CDC8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC9CDCC;
        label_0xC9CDCC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `Footsteps.GetTexturesAtPoint` — RVA `0xc9cdd0`

- Lift status: **partial**; input span: 420 bytes; span to next metadata RVA: 420 bytes.
- Metadata signature: `private float[] GetTexturesAtPoint(Vector3 WorldPos) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=49 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc9ce5c; reason: Unknown IR expression at 0xc9ce5c; reason: Unsupported instruction 'csel' at 0xc9ceb0; reason: Unknown IR expression at 0xc9ceb0

```csharp
public static ulong Footsteps_GetTexturesAtPoint_RVAc9cdd0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fcvtz_source_13225552 = default(float);
        float __arm64_fcvtz_source_13225636 = default(float);
        ulong __arm64_flags_left_13225732 = default(ulong);
        ulong __arm64_flags_left_13225780 = default(ulong);
        ulong __arm64_flags_left_13225788 = default(ulong);
        ulong __arm64_flags_left_13225808 = default(ulong);
        ulong __arm64_flags_right_13225732 = default(ulong);
        ulong __arm64_flags_right_13225780 = default(ulong);
        ulong __arm64_flags_right_13225788 = default(ulong);
        ulong __arm64_flags_right_13225808 = default(ulong);
        float __arm64_float_flags_left_13225556 = default(float);
        float __arm64_float_flags_left_13225640 = default(float);
        float __arm64_float_flags_right_13225556 = default(float);
        float __arm64_float_flags_right_13225640 = default(float);
        ulong __arm64_pair_address_13225424 = default(ulong);
        ulong __arm64_pair_address_13225428 = default(ulong);
        ulong __arm64_pair_address_13225824 = default(ulong);
        ulong __arm64_pair_address_13225828 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x14 = default(ulong);
        ulong x15 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13225424 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13225424, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13225424) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_13225424;
        __arm64_pair_address_13225428 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13225428, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13225428) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4AAUL))))))));
        v8 = v2;
        v9 = v0;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9CE0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2C0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4AAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9CE0C;
        label_0xC9CE0C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CF70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9CE14UL);
        }
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x188UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17D7494UL /* metadata target: TerrainData.get_size */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CF70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v10 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17D7CDCUL /* metadata target: TerrainData.get_alphamapWidth */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_fcvtz_source_13225552 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13225552 != __arm64_fcvtz_source_13225552) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13225552 >= global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x4F000000UL)), 0)) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13225552 < global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xCF000000UL)), 0)) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13225552)))))))));
        __arm64_float_flags_left_13225556 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13225556 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC9CE5CUL);
        x20 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CF70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9CE64UL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x190UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17D7494UL /* metadata target: TerrainData.get_size */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CF70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v9 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17D7D18UL /* metadata target: TerrainData.get_alphamapHeight */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9CF70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9CE8CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_fcvtz_source_13225636 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13225636 != __arm64_fcvtz_source_13225636) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13225636 >= global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x4F000000UL)), 0)) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13225636 < global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xCF000000UL)), 0)) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13225636)))))))));
        __arm64_float_flags_left_13225640 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13225640 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        x10 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC9CEB0UL);
        x2 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x10)) : unchecked((uint)(x9)))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x4 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x8;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17D7AF8UL /* metadata target: TerrainData.GetAlphamaps */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CF70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x2C0UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x156B7F4UL /* metadata target: Array.GetUpperBound */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(0x1UL)))))));
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9CF70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x20UL)))))))));
        __arm64_flags_left_13225732 = x9;
        __arm64_flags_right_13225732 = 0x1UL;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_13225732) - (__arm64_flags_right_13225732))))) < unchecked((long)0x0UL)) != (((unchecked((long)(__arm64_flags_left_13225732)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_13225732)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_13225732) - (__arm64_flags_right_13225732))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_13225732)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC9CF58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x9 = 0x0UL;
        x12 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x8))))));
        x13 = unchecked((ulong)((x19) + (0x20UL)));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x14 = unchecked((ulong)((x0) + (0x20UL)));
        goto label_0xC9CF24;
        label_0xC9CF24:
        ;
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CF6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x15 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x10UL))))));
        if ((unchecked((uint)(x15)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9CF6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x15 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x20UL))))));
        __arm64_flags_left_13225780 = x9;
        __arm64_flags_right_13225780 = x15;
        if ((__arm64_flags_left_13225780 >= __arm64_flags_right_13225780))
        {
            goto label_0xC9CF6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9CF3CUL);
        }
        __arm64_flags_left_13225788 = x9;
        __arm64_flags_right_13225788 = x8;
        if ((__arm64_flags_left_13225788 >= __arm64_flags_right_13225788))
        {
            goto label_0xC9CF6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9CF44UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x13) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x2UL)))))))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x14) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x2UL)))))))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x9 = unchecked((ulong)((x9) + (0x1UL)));
        __arm64_flags_left_13225808 = x12;
        __arm64_flags_right_13225808 = x9;
        if ((!((unchecked((ulong)((__arm64_flags_left_13225808) - (__arm64_flags_right_13225808))) == 0x0UL))))
        {
            goto label_0xC9CF24;
        }
        else
        {
            goto label_0xC9CF58;
        }
        label_0xC9CF58:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_13225824 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13225824)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13225824) + (0x8UL))))), 0));
        __arm64_pair_address_13225828 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13225828)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13225828) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13225828) + (0x40UL)));
        return x0;
        label_0xC9CF6C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC9CF70;
        label_0xC9CF70:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `Footsteps.ctor` — RVA `0xc9cf74`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong Footsteps_ctor_RVAc9cf74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL) | RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x48UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x64UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x6CUL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x7CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x84UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x94UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x9CUL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0xACUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xB4UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0xC4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xCCUL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xD8UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xE8UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xF8UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x108UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x118UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x128UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x160UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
