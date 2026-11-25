# `WaterZone` — TypeDefIndex 3407

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `FPSRigidBodyWalker` | `FPSWalkerComponent` |
| `0x28` | `Footsteps` | `FootstepsComponent` |
| `0x30` | `PlayerWeapons` | `PlayerWeaponsComponent` |
| `0x38` | `WeaponEffects` | `WeaponEffectsComponent` |
| `0x40` | `GameObject` | `playerObj` |
| `0x48` | `GameObject` | `weaponObj` |
| `0x50` | `bool` | `swimTimeState` |
| `0x58` | `AudioSource` | `audioSource` |
| `0x60` | `AudioClip` | `underwaterSound` |
| `0x68` | `AudioSource[]` | `aboveWaterAudioSources` |
| `0x70` | `Transform` | `waterPlane` |
| `0x78` | `float` | `underwaterYpos` |
| `0x80` | `Transform` | `waterPlaneTop` |
| `0x88` | `Vector3` | `waterPlaneRot` |
| `0x98` | `ParticleSystem` | `rippleEffect` |
| `0xA0` | `float` | `rippleEmitTime` |
| `0xA4` | `float` | `rippleEmitDelay` |
| `0xA8` | `ParticleSystem` | `bubblesEffect` |
| `0xB0` | `float` | `particlesYPos` |
| `0xB4` | `float` | `particleForwardPos` |
| `0xB8` | `GameObject` | `waterSplash` |
| `0xC0` | `Vector3` | `splashPos` |
| `0xCC` | `float` | `lastSplashTime` |
| `0xD0` | `ParticleSystem` | `splashTrail` |
| `0xD8` | `Vector3` | `trailPos` |
| `0xE4` | `float` | `splashTrailTime` |
| `0xE8` | `bool` | `changeSunlightColor` |
| `0xF0` | `Light` | `SunlightObj` |
| `0xF8` | `Color` | `underwaterSunightColor` |
| `0x108` | `Color` | `origSunightColor` |
| `0x118` | `bool` | `underwaterLightEnabled` |
| `0x11C` | `Color` | `underwaterLightColor` |
| `0x12C` | `bool` | `useCausticsLight` |
| `0x130` | `Light` | `causticsLight` |
| `0x138` | `int` | `index` |
| `0x13C` | `int` | `fps` |
| `0x140` | `Texture2D[]` | `frames` |
| `0x148` | `bool` | `effectsState` |
| `0x149` | `bool` | `underwaterFogEnabled` |
| `0x14C` | `FogMode` | `underwaterFogMode` |
| `0x150` | `Color` | `underwaterFogColor` |
| `0x160` | `float` | `underwaterFogDensity` |
| `0x164` | `float` | `underwaterLinearFogStart` |
| `0x168` | `float` | `underwaterLinearFogEnd` |
| `0x16C` | `bool` | `fogEnabled` |
| `0x170` | `FogMode` | `origFogMode` |
| `0x174` | `Color` | `origFogColor` |
| `0x184` | `Color` | `origLightColor` |
| `0x194` | `float` | `origFogDensity` |
| `0x198` | `float` | `origLinearFogStart` |
| `0x19C` | `float` | `origLinearFogEnd` |
| `0x1A0` | `Transform` | `myTransform` |
| `0x1A8` | `Transform` | `mainCamTransform` |

## `WaterZone.Start` — RVA `0xc99e2c`

- Lift status: **exact**; input span: 1732 bytes; span to next metadata RVA: 1732 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=234 (informational only).

```csharp
public static ulong WaterZone_Start_RVAc99e2c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13214376 = default(uint);
        uint __arm64_flags_left_13214388 = default(uint);
        uint __arm64_flags_left_13214416 = default(uint);
        uint __arm64_flags_left_13214428 = default(uint);
        uint __arm64_flags_left_13214476 = default(uint);
        uint __arm64_flags_left_13214492 = default(uint);
        uint __arm64_flags_right_13214376 = default(uint);
        uint __arm64_flags_right_13214388 = default(uint);
        uint __arm64_flags_right_13214416 = default(uint);
        uint __arm64_flags_right_13214428 = default(uint);
        uint __arm64_flags_right_13214476 = default(uint);
        uint __arm64_flags_right_13214492 = default(uint);
        ulong __arm64_pair_address_13214224 = default(ulong);
        ulong __arm64_pair_address_13214228 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x49EUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC99EF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x268UL))));
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x278UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x280UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x288UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x49EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC99EF0;
        label_0xC99EF0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x1A0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x1A0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x1A8UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x1A8UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xCD8UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x40UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x168UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x48UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x188UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x268UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x28UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFC0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5A0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x88UL))));
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x38UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x88UL))));
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xB8UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFF80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x98UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xA8UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFF90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA0UL))));
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xD0UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xEA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8D000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x4A8UL))));
        x20 = x0;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x168UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A118;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A114UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A118;
        label_0xC9A118:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x1 = x21;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CB368UL /* metadata target: Physics.IgnoreCollision */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x58UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176AAF4UL /* metadata target: AudioSource.set_loop */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        x22 = 0x1A8C000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x390UL))))), 0));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779C90UL /* metadata target: RenderSettings.get_fog */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x0 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x16CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x1779E18UL /* metadata target: RenderSettings.get_fogColor */, x0, x1, x2, x3);
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x174UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x178UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x17CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x180UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1779F1CUL /* metadata target: RenderSettings.get_fogDensity */, x0, x1, x2, x3);
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x194UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1779DB4UL /* metadata target: RenderSettings.get_fogMode */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x170UL))), unchecked((uint)(x0)));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779CF4UL /* metadata target: RenderSettings.get_fogStartDistance */, x0, x1, x2, x3);
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x198UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1779D54UL /* metadata target: RenderSettings.get_fogEndDistance */, x0, x1, x2, x3);
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x19CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1779F7CUL /* metadata target: RenderSettings.get_ambientLight */, x0, x1, x2, x3);
        x20 = x19;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xF0UL))));
        __arm64_pair_address_13214224 = unchecked((ulong)((x20) + (0x94UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13214224, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13214224) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        __arm64_pair_address_13214228 = unchecked((ulong)((x20) + (0x9CUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13214228, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13214228) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A228;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A224UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A228;
        label_0xC9A228:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A334;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3D0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x280UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x21 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A25C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A258UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A25C;
        label_0xC9A25C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1556240UL /* metadata target: Type.GetTypeFromHandle */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A280;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A280;
        label_0xC9A280:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798B54UL /* metadata target: Object.FindObjectsOfType */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x278UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x21 = x0;
        __arm64_flags_left_13214376 = unchecked((uint)(x8));
        __arm64_flags_right_13214376 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13214376) - (__arm64_flags_right_13214376))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13214376)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13214376)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13214376) - (__arm64_flags_right_13214376))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13214376)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC9A334;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC9A2B4;
        label_0xC9A2B4:
        ;
        __arm64_flags_left_13214388 = unchecked((uint)(x23));
        __arm64_flags_right_13214388 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13214388 >= __arm64_flags_right_13214388))
        {
            goto label_0xC9A4EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = unchecked((ulong)((x21) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BA6CUL /* metadata target: Light.get_type */, x0, x1, x2, x3);
        __arm64_flags_left_13214416 = unchecked((uint)(x0));
        __arm64_flags_right_13214416 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13214416) - (__arm64_flags_right_13214416))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC9A304;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        __arm64_flags_left_13214428 = unchecked((uint)(x23));
        __arm64_flags_right_13214428 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13214428 >= __arm64_flags_right_13214428))
        {
            goto label_0xC9A4EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x24);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D50UL /* metadata target: GameObject.get_activeInHierarchy */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A318;
        }
        else
        {
            goto label_0xC9A304;
        }
        label_0xC9A304:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13214476 = unchecked((uint)(x23));
        __arm64_flags_right_13214476 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13214476) - (__arm64_flags_right_13214476))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13214476)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13214476)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13214476) - (__arm64_flags_right_13214476))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13214476)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC9A2B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A314UL);
        }
        goto label_0xC9A334;
        label_0xC9A318:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        __arm64_flags_left_13214492 = unchecked((uint)(x23));
        __arm64_flags_right_13214492 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13214492 >= __arm64_flags_right_13214492))
        {
            goto label_0xC9A4EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = x20;
        RuntimeMemory.WriteU64(x20, x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC9A334;
        label_0xC9A334:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A348;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A344UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A348;
        label_0xC9A348:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A378;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BAE4UL /* metadata target: Light.get_color */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x108UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x10CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x110UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x114UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        goto label_0xC9A378;
        label_0xC9A378:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A38C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A388UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A38C;
        label_0xC9A38C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A3DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x78UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        goto label_0xC9A3DC;
        label_0xC9A3DC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x12CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A428;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A3F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A3F4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A3F8;
        label_0xC9A3F8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A428;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A428;
        label_0xC9A428:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A43C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A438UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A43C;
        label_0xC9A43C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A46C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A46C;
        label_0xC9A46C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x50UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x8) + (0x255UL)));
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WritePtr(x9, unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x259UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A4D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x13CUL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x288UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x179595CUL /* metadata target: MonoBehaviour.InvokeRepeating */);
        label_0xC9A4D4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC9A4E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC9A4EC;
        label_0xC9A4EC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WaterZone.Update` — RVA `0xc9a4f0`

- Lift status: **exact**; input span: 316 bytes; span to next metadata RVA: 316 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=41 (informational only).

```csharp
public static ulong WaterZone_Update_RVAc9a4f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13214968 = default(ulong);
        ulong __arm64_pair_address_13215256 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x70UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x40UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13214968 = unchecked((ulong)((sp) + (0x48UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13214968, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13214968) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x49FUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A528;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEA8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x49FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9A528;
        label_0xC9A528:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x30UL))), 0x0UL);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A628;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D50UL /* metadata target: GameObject.get_activeInHierarchy */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A568;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x50UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A628;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x8) + (0x255UL)));
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        RuntimeMemory.WritePtr(x9, unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x259UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x0 = RuntimeCalls.InvokeDirect(0xC9A62CUL /* metadata target: WaterZone.StopUnderwaterEffects */, x0, x1, x2, x3);
        goto label_0xC9A568;
        label_0xC9A568:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A628;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xEA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A628;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x20UL))), v0);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x8);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A628;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A628;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D940UL /* metadata target: Transform.get_up */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4F4UL))))), 0));
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1774BA0UL /* metadata target: Bounds.Contains */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A608;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC9A8D4UL /* metadata target: WaterZone.StartUnderwaterEffects */, x0, x1, x2, x3);
        goto label_0xC9A610;
        label_0xC9A608:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC9A62CUL /* metadata target: WaterZone.StopUnderwaterEffects */, x0, x1, x2, x3);
        goto label_0xC9A610;
        label_0xC9A610:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x58UL))));
        __arm64_pair_address_13215256 = unchecked((ulong)((sp) + (0x48UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13215256)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13215256) + (0x8UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x40UL))))), 0));
        return x0;
        label_0xC9A628:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WaterZone.StopUnderwaterEffects` — RVA `0xc9a62c`

- Lift status: **partial**; input span: 680 bytes; span to next metadata RVA: 680 bytes.
- Metadata signature: `private void StopUnderwaterEffects() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=80 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc9a6a0; reason: Unsupported instruction 'b.hs' at 0xc9a6a4; reason: Unknown IR expression at 0xc9a6a4; reason: Unsupported instruction 'cmp' at 0xc9a6e4; reason: Unsupported instruction 'b.lt' at 0xc9a6e8; reason: Unknown IR expression at 0xc9a6e8

```csharp
public static ulong WaterZone_StopUnderwaterEffects_RVAc9a62c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13215376 = default(uint);
        uint __arm64_flags_right_13215376 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4A5UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A660;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4A5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9A660;
        label_0xC9A660:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x148UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A8B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A7A8UL /* metadata target: AudioSource.Pause */, x0, x1, x2, x3);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A6EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A690UL);
        }
        __arm64_flags_left_13215376 = unchecked((uint)(x8));
        __arm64_flags_right_13215376 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13215376) - (__arm64_flags_right_13215376))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13215376)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13215376)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13215376) - (__arm64_flags_right_13215376))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13215376)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC9A6EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x0UL;
        x24 = unchecked((ulong)((x22) + (0x20UL)));
        goto label_0xC9A6A0;
        label_0xC9A6A0:
        ;
        RuntimeCalls.Unsupported("cmp", 0xC9A6A0UL);
        RuntimeCalls.Unsupported("b.hs", 0xC9A6A4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9A8CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (x23))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A6BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A6B8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A6BC;
        label_0xC9A6BC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A6DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A6CCUL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, x3);
        goto label_0xC9A6DC;
        label_0xC9A6DC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xC9A6E4UL);
        RuntimeCalls.Unsupported("b.lt", 0xC9A6E8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9A6A0;
        }
        else
        {
            goto label_0xC9A6EC;
        }
        label_0xC9A6EC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x16CUL))))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779CB8UL /* metadata target: RenderSettings.set_fog */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x174UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x178UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x17CUL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x180UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779E9CUL /* metadata target: RenderSettings.set_fogColor */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x194UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779F44UL /* metadata target: RenderSettings.set_fogDensity */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x170UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779DDCUL /* metadata target: RenderSettings.set_fogMode */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x198UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779D1CUL /* metadata target: RenderSettings.set_fogStartDistance */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x19CUL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779D7CUL /* metadata target: RenderSettings.set_fogEndDistance */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x184UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x188UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x18CUL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x190UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A000UL /* metadata target: RenderSettings.set_ambientLight */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A78C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A788UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A78C;
        label_0xC9A78C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A7C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE8UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A7C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A7ACUL);
        }
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x114UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x110UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x10CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x108UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BB80UL /* metadata target: Light.set_color */, x0, x1, x2, x3);
        goto label_0xC9A7C4;
        label_0xC9A7C4:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A7D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A7D4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A7D8;
        label_0xC9A7D8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A808;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A808;
        label_0xC9A808:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x12CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A854;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A824;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A820UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A824;
        label_0xC9A824:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A854;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A854;
        label_0xC9A854:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A864UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A868;
        label_0xC9A868:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A898;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A898;
        label_0xC9A898:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9A8D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A8B0UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x230UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x148UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC9A8B8;
        label_0xC9A8B8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC9A8CC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9A8D0;
        label_0xC9A8D0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `WaterZone.StartUnderwaterEffects` — RVA `0xc9a8d4`

- Lift status: **partial**; input span: 1460 bytes; span to next metadata RVA: 1460 bytes.
- Metadata signature: `private void StartUnderwaterEffects() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=161 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc9a96c; reason: Unsupported instruction 'b.hs' at 0xc9a970; reason: Unknown IR expression at 0xc9a970; reason: Unsupported instruction 'cmp' at 0xc9a9b4; reason: Unsupported instruction 'b.lt' at 0xc9a9b8; reason: Unknown IR expression at 0xc9a9b8; reason: Unsupported instruction 'frintp' at 0xc9adac; reason: Unsupported instruction 'frintm' at 0xc9adb8

```csharp
public static ulong WaterZone_StartUnderwaterEffects_RVAc9a8d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13217172 = default(double);
        double __arm64_fcvtz_source_13217220 = default(double);
        uint __arm64_flags_left_13216088 = default(uint);
        ulong __arm64_flags_left_13217180 = default(ulong);
        ulong __arm64_flags_result_13217180 = default(ulong);
        uint __arm64_flags_right_13216088 = default(uint);
        ulong __arm64_flags_right_13217180 = default(ulong);
        float __arm64_float_flags_left_13216896 = default(float);
        float __arm64_float_flags_left_13217120 = default(float);
        double __arm64_float_flags_left_13217132 = default(double);
        double __arm64_float_flags_left_13217156 = default(double);
        double __arm64_float_flags_left_13217224 = default(double);
        float __arm64_float_flags_right_13216896 = default(float);
        float __arm64_float_flags_right_13217120 = default(float);
        double __arm64_float_flags_right_13217132 = default(double);
        double __arm64_float_flags_right_13217156 = default(double);
        double __arm64_float_flags_right_13217224 = default(double);
        ulong __arm64_pair_address_13215964 = default(ulong);
        ulong __arm64_pair_address_13216040 = default(ulong);
        ulong __arm64_pair_address_13216424 = default(ulong);
        ulong __arm64_pair_address_13216984 = default(ulong);
        ulong __arm64_pair_address_13217024 = default(ulong);
        ulong __arm64_pair_address_13217036 = default(ulong);
        ulong __arm64_pair_address_13217392 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x50UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13215964 = unchecked((ulong)((sp) + (0x58UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13215964, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13215964) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x68UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4A4UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A920;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4A4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9A920;
        label_0xC9A920:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x48UL))), 0x0UL);
        __arm64_pair_address_13216040 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13216040, v0);
#else
        __WriteVector128(__arm64_pair_address_13216040, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13216040) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13216040) + (0x10UL))), v0);
#endif
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x148UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9ABB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, x3);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        __arm64_flags_left_13216088 = unchecked((uint)(x8));
        __arm64_flags_right_13216088 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13216088) - (__arm64_flags_right_13216088))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13216088)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13216088)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13216088) - (__arm64_flags_right_13216088))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13216088)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC9A9BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x24 = unchecked((ulong)((x22) + (0x20UL)));
        goto label_0xC9A96C;
        label_0xC9A96C:
        ;
        RuntimeCalls.Unsupported("cmp", 0xC9A96CUL);
        RuntimeCalls.Unsupported("b.hs", 0xC9A970UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (x23))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9A988;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A984UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9A988;
        label_0xC9A988:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9A9AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A99CUL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A7A8UL /* metadata target: AudioSource.Pause */, x0, x1, x2, x3);
        goto label_0xC9A9AC;
        label_0xC9A9AC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xC9A9B4UL);
        RuntimeCalls.Unsupported("b.lt", 0xC9A9B8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9A96C;
        }
        else
        {
            goto label_0xC9A9BC;
        }
        label_0xC9A9BC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9A9E4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x150UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x110UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x158UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x118UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x149UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779CB8UL /* metadata target: RenderSettings.set_fog */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x150UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x154UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x158UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x15CUL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779E9CUL /* metadata target: RenderSettings.set_fogColor */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x160UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779F44UL /* metadata target: RenderSettings.set_fogDensity */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x14CUL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779DDCUL /* metadata target: RenderSettings.set_fogMode */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x164UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779D1CUL /* metadata target: RenderSettings.set_fogStartDistance */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x168UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779D7CUL /* metadata target: RenderSettings.set_fogEndDistance */, x0, x1, x2, x3);
        goto label_0xC9AA50;
        label_0xC9AA50:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x118UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AA70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AA58UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x11CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x120UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x124UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x128UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A000UL /* metadata target: RenderSettings.set_ambientLight */, x0, x1, x2, x3);
        goto label_0xC9AA70;
        label_0xC9AA70:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AA84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AA80UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9AA84;
        label_0xC9AA84:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AAB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE8UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AAB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AAA4UL);
        }
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        __arm64_pair_address_13216424 = unchecked((ulong)((x19) + (0xFCUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13216424)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13216424) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xF8UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177BB80UL /* metadata target: Light.set_color */, x0, x1, x2, x3);
        goto label_0xC9AAB8;
        label_0xC9AAB8:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AACC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AAC8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9AACC;
        label_0xC9AACC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AAFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9AAFC;
        label_0xC9AAFC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x12CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AB48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AB18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AB14UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9AB18;
        label_0xC9AB18:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AB48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9AB48;
        label_0xC9AB48:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AB5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AB58UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9AB5C;
        label_0xC9AB5C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AB8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9AB8C;
        label_0xC9AB8C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x230UL))), unchecked((byte)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x148UL))), unchecked((byte)(unchecked((uint)(x9)))));
        goto label_0xC9ABB0;
        label_0xC9ABB0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9ABC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9ABC0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9ABC4;
        label_0xC9ABC4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AC30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x256UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AC30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AC08UL);
        }
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x78UL))))), 0));
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        v0 = v8;
        v1 = v9;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        goto label_0xC9AC30;
        label_0xC9AC30:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xEA8UL))));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AC60UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        x1 = 0x0UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x524UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13216896 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13216896 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13216896 <= __arm64_float_flags_right_13216896) || ((__arm64_float_flags_left_13216896 != __arm64_float_flags_left_13216896) || (__arm64_float_flags_right_13216896 != __arm64_float_flags_right_13216896))))
        {
            goto label_0xC9ACA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40500000UL)), 0)), 0));
        goto label_0xC9ACD4;
        label_0xC9ACA0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC9ACD4;
        label_0xC9ACD4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        __arm64_pair_address_13216984 = unchecked((ulong)((x19) + (0xB0UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13216984, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13216984) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x48UL))), x0);
        x8 = sp;
        x0 = unchecked((ulong)((sp) + (0x48UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
        __arm64_pair_address_13217024 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13217024);
#else
        v0 = __ReadVector128(__arm64_pair_address_13217024);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13217024) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13217024) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13217036 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13217036, v0);
#else
        __WriteVector128(__arm64_pair_address_13217036, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13217036) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13217036) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x242UL))))))));
        v8 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AD38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9AD38;
        label_0xC9AD38:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AD50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AD4CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9AD50;
        label_0xC9AD50:
        ;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = sp;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13217120 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13217120 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13217120 >= __arm64_float_flags_right_13217120))
        {
            goto label_0xC9AD80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AD68UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13217132 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13217132 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13217132 != __arm64_float_flags_right_13217132) || ((__arm64_float_flags_left_13217132 != __arm64_float_flags_left_13217132) || (__arm64_float_flags_right_13217132 != __arm64_float_flags_right_13217132))))
        {
            goto label_0xC9ADA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AD74UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC9AD94;
        label_0xC9AD80:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13217156 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13217156 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13217156 != __arm64_float_flags_right_13217156) || ((__arm64_float_flags_left_13217156 != __arm64_float_flags_left_13217156) || (__arm64_float_flags_right_13217156 != __arm64_float_flags_right_13217156))))
        {
            goto label_0xC9ADB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AD8CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC9AD94;
        label_0xC9AD94:
        ;
        __arm64_fcvtz_source_13217172 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13217172 != __arm64_fcvtz_source_13217172) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13217172 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13217172 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13217172)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13217180 = x8;
        __arm64_flags_right_13217180 = 0x1UL;
        __arm64_flags_result_13217180 = unchecked((ulong)((__arm64_flags_left_13217180) & (__arm64_flags_right_13217180)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13217180 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC9ADBC;
        label_0xC9ADA8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC9ADACUL);
        goto label_0xC9ADBC;
        label_0xC9ADB4:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC9ADB8UL);
        goto label_0xC9ADBC;
        label_0xC9ADBC:
        ;
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13217220 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13217220 != __arm64_fcvtz_source_13217220) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13217220 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13217220 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13217220)))))))));
        __arm64_float_flags_left_13217224 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13217224 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC9ADD0UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AE10UL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xB0UL))))), 0));
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v9 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x179D9B8UL /* metadata target: Transform.get_forward */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC9AE80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AE38UL);
        }
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xB4UL))))), 0));
        x0 = x20;
        x1 = 0x0UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x68UL))));
        __arm64_pair_address_13217392 = unchecked((ulong)((sp) + (0x58UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13217392)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13217392) + (0x8UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x50UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xA0UL)));
        return x0;
        label_0xC9AE80:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC9AE84;
        label_0xC9AE84:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WaterZone.NextFrame` — RVA `0xc9ae88`

- Lift status: **partial**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `private void NextFrame() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=29 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.hs' at 0xc9af20; reason: Unknown IR expression at 0xc9af20

```csharp
public static ulong WaterZone_NextFrame_RVAc9ae88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13217560 = default(uint);
        uint __arm64_flags_right_13217560 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4A0UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AEB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4A0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9AEB4;
        label_0xC9AEB4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x12CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AF44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AED8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9AED4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9AED8;
        label_0xC9AED8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AF44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AF50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17916A4UL /* metadata target: Behaviour.get_isActiveAndEnabled */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9AF44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9AF50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x138UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x11 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) / (unchecked((int)(unchecked((uint)(x10)))))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)((unchecked((uint)(x11))) * (unchecked((uint)(x10))))))))));
        __arm64_flags_left_13217560 = unchecked((uint)(x9));
        __arm64_flags_right_13217560 = unchecked((uint)(x10));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x138UL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.hs", 0xC9AF20UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9AF54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9AF50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x177BF3CUL /* metadata target: Light.set_cookie */);
        label_0xC9AF44:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC9AF50:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC9AF54;
        label_0xC9AF54:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WaterZone.OnTriggerStay` — RVA `0xc9af58`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void OnTriggerStay(Collider col) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong WaterZone_OnTriggerStay_RVAc9af58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC9AF5CUL /* metadata target: WaterZone.EnterWater */);
        return default(ulong);
    }
```

## `WaterZone.EnterWater` — RVA `0xc9af5c`

- Lift status: **partial**; input span: 1588 bytes; span to next metadata RVA: 1588 bytes.
- Metadata signature: `private void EnterWater(Collider col) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=151 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintp' at 0xc9b4e4; reason: Unsupported instruction 'frintm' at 0xc9b4f0; reason: Unsupported instruction 'csel' at 0xc9b508; reason: Unknown IR expression at 0xc9b508; reason: Unsupported instruction 'frintp' at 0xc9b52c; reason: Unsupported instruction 'frintm' at 0xc9b538; reason: Unsupported instruction 'csel' at 0xc9b550; reason: Unknown IR expression at 0xc9b550

```csharp
public static ulong WaterZone_EnterWater_RVAc9af5c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13218980 = default(double);
        double __arm64_fcvtz_source_13219020 = default(double);
        double __arm64_fcvtz_source_13219068 = default(double);
        double __arm64_fcvtz_source_13219140 = default(double);
        ulong __arm64_flags_left_13218988 = default(ulong);
        ulong __arm64_flags_left_13219028 = default(ulong);
        ulong __arm64_flags_result_13218988 = default(ulong);
        ulong __arm64_flags_result_13219028 = default(ulong);
        ulong __arm64_flags_right_13218988 = default(ulong);
        ulong __arm64_flags_right_13219028 = default(ulong);
        float __arm64_float_flags_left_13217932 = default(float);
        float __arm64_float_flags_left_13218096 = default(float);
        float __arm64_float_flags_left_13218176 = default(float);
        float __arm64_float_flags_left_13218192 = default(float);
        float __arm64_float_flags_left_13218204 = default(float);
        float __arm64_float_flags_left_13218384 = default(float);
        float __arm64_float_flags_left_13218528 = default(float);
        double __arm64_float_flags_left_13218540 = default(double);
        float __arm64_float_flags_left_13218624 = default(float);
        float __arm64_float_flags_left_13218928 = default(float);
        double __arm64_float_flags_left_13218940 = default(double);
        double __arm64_float_flags_left_13218964 = default(double);
        double __arm64_float_flags_left_13219004 = default(double);
        double __arm64_float_flags_left_13219072 = default(double);
        double __arm64_float_flags_left_13219144 = default(double);
        float __arm64_float_flags_right_13217932 = default(float);
        float __arm64_float_flags_right_13218096 = default(float);
        float __arm64_float_flags_right_13218176 = default(float);
        float __arm64_float_flags_right_13218192 = default(float);
        float __arm64_float_flags_right_13218204 = default(float);
        float __arm64_float_flags_right_13218384 = default(float);
        float __arm64_float_flags_right_13218528 = default(float);
        double __arm64_float_flags_right_13218540 = default(double);
        float __arm64_float_flags_right_13218624 = default(float);
        float __arm64_float_flags_right_13218928 = default(float);
        double __arm64_float_flags_right_13218940 = default(double);
        double __arm64_float_flags_right_13218964 = default(double);
        double __arm64_float_flags_right_13219004 = default(double);
        double __arm64_float_flags_right_13219072 = default(double);
        double __arm64_float_flags_right_13219144 = default(double);
        ulong __arm64_pair_address_13217632 = default(ulong);
        ulong __arm64_pair_address_13217636 = default(ulong);
        ulong __arm64_pair_address_13217728 = default(ulong);
        ulong __arm64_pair_address_13218368 = default(ulong);
        ulong __arm64_pair_address_13218432 = default(ulong);
        ulong __arm64_pair_address_13218444 = default(ulong);
        ulong __arm64_pair_address_13218756 = default(ulong);
        ulong __arm64_pair_address_13218776 = default(ulong);
        ulong __arm64_pair_address_13218832 = default(ulong);
        ulong __arm64_pair_address_13218844 = default(ulong);
        ulong __arm64_pair_address_13219196 = default(ulong);
        ulong __arm64_pair_address_13219200 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        __arm64_pair_address_13217632 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13217632, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13217632) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13217636 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13217636, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13217636) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x60UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x4A2UL))))))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9AFB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x4A2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9AFB8;
        label_0xC9AFB8:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x68UL))), 0x0UL);
        __arm64_pair_address_13217728 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13217728, v0);
#else
        __WriteVector128(__arm64_pair_address_13217728, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13217728) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13217728) + (0x10UL))), v0);
#endif
        if ((x20 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8D000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xEC0UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x21);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9B56C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x255UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE08UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8D000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xEA8UL))));
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x23 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x470UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13217932 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13217932 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13217932 <= __arm64_float_flags_right_13217932))
        {
            goto label_0xC9B09C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B094UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x258UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC9B148;
        label_0xC9B09C:
        ;
        x24 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x258UL))), unchecked((byte)(unchecked((uint)(x24)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x50UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B0BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x23) + (0x260UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x50UL))), unchecked((byte)(unchecked((uint)(x24)))));
        goto label_0xC9B0BC;
        label_0xC9B0BC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x23 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x324UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13218096 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218096 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13218096 <= __arm64_float_flags_right_13218096))
        {
            goto label_0xC9B140;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B138UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x257UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC9B148;
        label_0xC9B140:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x257UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9B148;
        label_0xC9B148:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x23) + (0x3B4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B174UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13218176 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218176 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13218176 <= __arm64_float_flags_right_13218176))
        {
            goto label_0xC9B300;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B188UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xC4UL))))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x256UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        __arm64_float_flags_left_13218192 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218192 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13218192 != __arm64_float_flags_right_13218192) || ((__arm64_float_flags_left_13218192 != __arm64_float_flags_left_13218192) || (__arm64_float_flags_right_13218192 != __arm64_float_flags_right_13218192))))
        {
            goto label_0xC9B328;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B198UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xC0UL))))), 0));
        __arm64_float_flags_left_13218204 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218204 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13218204 != __arm64_float_flags_right_13218204) || ((__arm64_float_flags_left_13218204 != __arm64_float_flags_left_13218204) || (__arm64_float_flags_right_13218204 != __arm64_float_flags_right_13218204))))
        {
            goto label_0xC9B328;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B1ECUL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v9 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4E4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v2 = v9;
        x1 = 0x0UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        __arm64_pair_address_13218368 = unchecked((ulong)((x19) + (0xA0UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13218368)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13218368) + (0x4UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13218384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13218384 >= __arm64_float_flags_right_13218384) || ((__arm64_float_flags_left_13218384 != __arm64_float_flags_left_13218384) || (__arm64_float_flags_right_13218384 != __arm64_float_flags_right_13218384))))
        {
            goto label_0xC9B56C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x68UL))), x0);
        x8 = sp;
        x0 = unchecked((ulong)((sp) + (0x68UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
        __arm64_pair_address_13218432 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13218432);
#else
        v0 = __ReadVector128(__arm64_pair_address_13218432);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13218432) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13218432) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13218444 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13218444, v0);
#else
        __WriteVector128(__arm64_pair_address_13218444, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13218444) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13218444) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x242UL))))))));
        v8 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B2B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9B2B8;
        label_0xC9B2B8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B2D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B2CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9B2D0;
        label_0xC9B2D0:
        ;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = sp;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13218528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13218528 >= __arm64_float_flags_right_13218528))
        {
            goto label_0xC9B4B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B2E8UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13218540 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13218540 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13218540 != __arm64_float_flags_right_13218540) || ((__arm64_float_flags_left_13218540 != __arm64_float_flags_left_13218540) || (__arm64_float_flags_right_13218540 != __arm64_float_flags_right_13218540))))
        {
            goto label_0xC9B528;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B2F4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC9B4CC;
        label_0xC9B300:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x256UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B56C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x264UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x256UL))), unchecked((byte)(unchecked((uint)(x9)))));
        goto label_0xC9B56C;
        label_0xC9B328:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xE4UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x520UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13218624 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218624 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13218624 >= __arm64_float_flags_right_13218624) || ((__arm64_float_flags_left_13218624 != __arm64_float_flags_left_13218624) || (__arm64_float_flags_right_13218624 != __arm64_float_flags_right_13218624))))
        {
            goto label_0xC9B56C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B390UL);
        }
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4E4UL))))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_13218756 = unchecked((ulong)((x19) + (0xD8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13218756, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13218756) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B3D8UL);
        }
        __arm64_pair_address_13218776 = unchecked((ulong)((x19) + (0xDCUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13218776)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13218776) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xD8UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC9B58C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x68UL))), x0);
        x8 = sp;
        x0 = unchecked((ulong)((sp) + (0x68UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
        __arm64_pair_address_13218832 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13218832);
#else
        v0 = __ReadVector128(__arm64_pair_address_13218832);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13218832) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13218832) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13218844 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13218844, v0);
#else
        __WriteVector128(__arm64_pair_address_13218844, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13218844) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13218844) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x242UL))))))));
        v8 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B448;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9B448;
        label_0xC9B448:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B460;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B45CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9B460;
        label_0xC9B460:
        ;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = sp;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13218928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13218928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13218928 >= __arm64_float_flags_right_13218928))
        {
            goto label_0xC9B490;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B478UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13218940 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13218940 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13218940 != __arm64_float_flags_right_13218940) || ((__arm64_float_flags_left_13218940 != __arm64_float_flags_left_13218940) || (__arm64_float_flags_right_13218940 != __arm64_float_flags_right_13218940))))
        {
            goto label_0xC9B4E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B484UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC9B4A4;
        label_0xC9B490:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13218964 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13218964 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13218964 != __arm64_float_flags_right_13218964) || ((__arm64_float_flags_left_13218964 != __arm64_float_flags_left_13218964) || (__arm64_float_flags_right_13218964 != __arm64_float_flags_right_13218964))))
        {
            goto label_0xC9B4EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B49CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC9B4A4;
        label_0xC9B4A4:
        ;
        __arm64_fcvtz_source_13218980 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13218980 != __arm64_fcvtz_source_13218980) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13218980 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13218980 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13218980)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13218988 = x8;
        __arm64_flags_right_13218988 = 0x1UL;
        __arm64_flags_result_13218988 = unchecked((ulong)((__arm64_flags_left_13218988) & (__arm64_flags_right_13218988)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13218988 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC9B4F4;
        label_0xC9B4B8:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13219004 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13219004 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13219004 != __arm64_float_flags_right_13219004) || ((__arm64_float_flags_left_13219004 != __arm64_float_flags_left_13219004) || (__arm64_float_flags_right_13219004 != __arm64_float_flags_right_13219004))))
        {
            goto label_0xC9B534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B4C4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC9B4CC;
        label_0xC9B4CC:
        ;
        __arm64_fcvtz_source_13219020 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13219020 != __arm64_fcvtz_source_13219020) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13219020 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13219020 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13219020)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13219028 = x8;
        __arm64_flags_right_13219028 = 0x1UL;
        __arm64_flags_result_13219028 = unchecked((ulong)((__arm64_flags_left_13219028) & (__arm64_flags_right_13219028)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13219028 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC9B53C;
        label_0xC9B4E0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC9B4E4UL);
        goto label_0xC9B4F4;
        label_0xC9B4EC:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC9B4F0UL);
        goto label_0xC9B4F4;
        label_0xC9B4F4:
        ;
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13219068 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13219068 != __arm64_fcvtz_source_13219068) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13219068 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13219068 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13219068)))))))));
        __arm64_float_flags_left_13219072 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13219072 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC9B508UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC9B56C;
        label_0xC9B528:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC9B52CUL);
        goto label_0xC9B53C;
        label_0xC9B534:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC9B538UL);
        goto label_0xC9B53C;
        label_0xC9B53C:
        ;
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13219140 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13219140 != __arm64_fcvtz_source_13219140) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13219140 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13219140 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13219140)))))))));
        __arm64_float_flags_left_13219144 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13219144 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC9B550UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xA0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC9B56C;
        label_0xC9B56C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        __arm64_pair_address_13219196 = unchecked((ulong)((sp) + (0x50UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13219196)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13219196) + (0x8UL))))), 0));
        __arm64_pair_address_13219200 = unchecked((ulong)((sp) + (0x40UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13219200)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13219200) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xA0UL)));
        return x0;
        label_0xC9B58C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `WaterZone.OnTriggerEnter` — RVA `0xc9b590`

- Lift status: **partial**; input span: 2112 bytes; span to next metadata RVA: 2112 bytes.
- Metadata signature: `private void OnTriggerEnter(Collider col) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=279 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc9ba54; reason: Unknown IR expression at 0xc9ba54; reason: Unsupported instruction 'b.ne' at 0xc9bab0; reason: Unknown IR expression at 0xc9bab0; reason: Unsupported instruction 'frintp' at 0xc9bbd0; reason: Unsupported instruction 'frintm' at 0xc9bbdc; reason: Unsupported instruction 'b.ne' at 0xc9bc50; reason: Unknown IR expression at 0xc9bc50

```csharp
public static ulong WaterZone_OnTriggerEnter_RVAc9b590(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13220768 = default(double);
        double __arm64_fcvtz_source_13220792 = default(double);
        double __arm64_fcvtz_source_13220836 = default(double);
        ulong __arm64_flags_left_13220420 = default(ulong);
        ulong __arm64_flags_left_13220428 = default(ulong);
        ulong __arm64_flags_left_13220512 = default(ulong);
        ulong __arm64_flags_left_13220520 = default(ulong);
        uint __arm64_flags_left_13220596 = default(uint);
        ulong __arm64_flags_left_13220616 = default(ulong);
        ulong __arm64_flags_left_13220800 = default(ulong);
        ulong __arm64_flags_left_13220928 = default(ulong);
        ulong __arm64_flags_left_13220936 = default(ulong);
        uint __arm64_flags_left_13220992 = default(uint);
        uint __arm64_flags_left_13221136 = default(uint);
        ulong __arm64_flags_left_13221244 = default(ulong);
        ulong __arm64_flags_left_13221252 = default(ulong);
        ulong __arm64_flags_result_13220428 = default(ulong);
        ulong __arm64_flags_result_13220520 = default(ulong);
        ulong __arm64_flags_result_13220800 = default(ulong);
        ulong __arm64_flags_result_13220936 = default(ulong);
        ulong __arm64_flags_result_13221252 = default(ulong);
        ulong __arm64_flags_right_13220420 = default(ulong);
        ulong __arm64_flags_right_13220428 = default(ulong);
        ulong __arm64_flags_right_13220512 = default(ulong);
        ulong __arm64_flags_right_13220520 = default(ulong);
        uint __arm64_flags_right_13220596 = default(uint);
        ulong __arm64_flags_right_13220616 = default(ulong);
        ulong __arm64_flags_right_13220800 = default(ulong);
        ulong __arm64_flags_right_13220928 = default(ulong);
        ulong __arm64_flags_right_13220936 = default(ulong);
        uint __arm64_flags_right_13220992 = default(uint);
        uint __arm64_flags_right_13221136 = default(uint);
        ulong __arm64_flags_right_13221244 = default(ulong);
        ulong __arm64_flags_right_13221252 = default(ulong);
        float __arm64_float_flags_left_13219836 = default(float);
        float __arm64_float_flags_left_13219868 = default(float);
        float __arm64_float_flags_left_13220748 = default(float);
        double __arm64_float_flags_left_13220756 = default(double);
        double __arm64_float_flags_left_13220780 = default(double);
        double __arm64_float_flags_left_13220840 = default(double);
        float __arm64_float_flags_right_13219836 = default(float);
        float __arm64_float_flags_right_13219868 = default(float);
        float __arm64_float_flags_right_13220748 = default(float);
        double __arm64_float_flags_right_13220756 = default(double);
        double __arm64_float_flags_right_13220780 = default(double);
        double __arm64_float_flags_right_13220840 = default(double);
        ulong __arm64_pair_address_13219220 = default(ulong);
        ulong __arm64_pair_address_13219224 = default(ulong);
        ulong __arm64_pair_address_13219228 = default(ulong);
        ulong __arm64_pair_address_13219448 = default(ulong);
        ulong __arm64_pair_address_13220256 = default(ulong);
        ulong __arm64_pair_address_13220276 = default(ulong);
        ulong __arm64_pair_address_13220672 = default(ulong);
        ulong __arm64_pair_address_13220676 = default(ulong);
        ulong __arm64_pair_address_13221040 = default(ulong);
        ulong __arm64_pair_address_13221044 = default(ulong);
        ulong __arm64_pair_address_13221048 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xE0UL)));
        __arm64_pair_address_13219220 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13219220, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13219220) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13219224 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13219224, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13219224) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13219228 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13219228, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13219228) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4A1UL))))))));
        x21 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xED0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4A1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9B670;
        label_0xC9B670:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x48UL))), 0x0UL);
        __arm64_pair_address_13219448 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13219448, v0);
#else
        __WriteVector128(__arm64_pair_address_13219448, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13219448) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13219448) + (0x10UL))), v0);
#endif
        if ((x21 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x22 = x0;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xEC0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xEA8UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x24);
        x20 = x0;
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9B6F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2A0UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B824;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x228UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9B824;
        }
        else
        {
            goto label_0xC9B6F4;
        }
        label_0xC9B6F4:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE48UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798300UL /* metadata target: Object.get_name */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE50UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BC98;
        }
        else
        {
            goto label_0xC9B7B0;
        }
        label_0xC9B7B0:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x23);
        v8 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x444UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13219836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13219836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13219836 <= __arm64_float_flags_right_13219836) || ((__arm64_float_flags_left_13219836 != __arm64_float_flags_left_13219836) || (__arm64_float_flags_right_13219836 != __arm64_float_flags_right_13219836))))
        {
            goto label_0xC9BC98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B804UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xCCUL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3A0UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13219868 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13219868 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13219868 >= __arm64_float_flags_right_13219868) || ((__arm64_float_flags_left_13219868 != __arm64_float_flags_left_13219868) || (__arm64_float_flags_right_13219868 != __arm64_float_flags_right_13219868))))
        {
            goto label_0xC9BC98;
        }
        else
        {
            goto label_0xC9B824;
        }
        label_0xC9B824:
        ;
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9B8CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC9AF5CUL /* metadata target: WaterZone.EnterWater */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x150UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B864UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9B868;
        label_0xC9B868:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9B940;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x150UL))));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x43FA0000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xC8D260UL /* metadata target: PlayAudioAtPos.PlayClipAt */, x0, x1, x2, x3);
        goto label_0xC9B940;
        label_0xC9B8CC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x150UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9B8F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B8ECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9B8F0;
        label_0xC9B8F0:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9B940;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B908UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x150UL))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x43FA0000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC8D260UL /* metadata target: PlayAudioAtPos.PlayClipAt */, x0, x1, x2, x3);
        goto label_0xC9B944;
        label_0xC9B940:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            goto label_0xC9B944;
        }
        label_0xC9B944:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x23);
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = sp;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9FCUL /* metadata target: Collider.get_bounds */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        x0 = x20;
        x1 = 0x0UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4E0UL))))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_13220256 = unchecked((ulong)((x19) + (0xC0UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13220256, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13220256) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9B9B4UL);
        }
        __arm64_pair_address_13220276 = unchecked((ulong)((x19) + (0xC4UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13220276)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13220276) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC0UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ECD4UL /* metadata target: Transform.GetEnumerator */, x0, x1, x2, x3);
        x20 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8C000UL;
        x26 = 0x1A8D000UL;
        x27 = 0x1A8E000UL;
        x21 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xED0UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xE68UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xA8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA60UL))));
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x28 = 0x1BAB000UL;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        x29 = 0x7FF0000000000000UL;
        x23 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC9BA28;
        label_0xC9BA28:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = RuntimeMemory.ReadU64(x24);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BA58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC9BA40;
        label_0xC9BA40:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13220420 = x11;
        __arm64_flags_right_13220420 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13220420) - (__arm64_flags_right_13220420))) == 0x0UL))
        {
            goto label_0xC9BA68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BA4CUL);
        }
        __arm64_flags_left_13220428 = x9;
        __arm64_flags_right_13220428 = 0x1UL;
        __arm64_flags_result_13220428 = unchecked((ulong)((__arm64_flags_left_13220428) - (__arm64_flags_right_13220428)));
        x9 = __arm64_flags_result_13220428;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC9BA54UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9BA40;
        }
        else
        {
            goto label_0xC9BA58;
        }
        label_0xC9BA58:
        ;
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BA74;
        label_0xC9BA68:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC9BA74;
        label_0xC9BA74:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BC00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = RuntimeMemory.ReadU64(x24);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BAB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC9BA9C;
        label_0xC9BA9C:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13220512 = x11;
        __arm64_flags_right_13220512 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13220512) - (__arm64_flags_right_13220512))) == 0x0UL))
        {
            goto label_0xC9BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BAA8UL);
        }
        __arm64_flags_left_13220520 = x9;
        __arm64_flags_right_13220520 = 0x1UL;
        __arm64_flags_result_13220520 = unchecked((ulong)((__arm64_flags_left_13220520) - (__arm64_flags_right_13220520)));
        x9 = __arm64_flags_result_13220520;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC9BAB0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9BA9C;
        }
        else
        {
            goto label_0xC9BAB4;
        }
        label_0xC9BAB4:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BAD4;
        label_0xC9BAC4:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC9BAD4;
        label_0xC9BAD4:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x26);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_13220596 = unchecked((uint)(x10));
        __arm64_flags_right_13220596 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_13220596 >= __arm64_flags_right_13220596))))
        {
            goto label_0xC9BCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13220616 = x8;
        __arm64_flags_right_13220616 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13220616) - (__arm64_flags_right_13220616))) == 0x0UL))))
        {
            goto label_0xC9BCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x22 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BCCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x48UL))), x0);
        x8 = sp;
        x0 = unchecked((ulong)((sp) + (0x48UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_pair_address_13220672 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13220672);
#else
        v0 = __ReadVector128(__arm64_pair_address_13220672);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13220672) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13220672) + (0x10UL))));
#endif
        __arm64_pair_address_13220676 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13220676, v0);
#else
        __WriteVector128(__arm64_pair_address_13220676, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13220676) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13220676) + (0x10UL))), v1);
#endif
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x242UL))))))));
        v8 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9BB6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x242UL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC9BB6C;
        label_0xC9BB6C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9BB7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BB78UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BB7C;
        label_0xC9BB7C:
        ;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = sp;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_float_flags_left_13220748 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13220748 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13220748 >= __arm64_float_flags_right_13220748))
        {
            goto label_0xC9BBAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BB94UL);
        }
        __arm64_float_flags_left_13220756 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13220756 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))));
        if (((__arm64_float_flags_left_13220756 != __arm64_float_flags_right_13220756) || ((__arm64_float_flags_left_13220756 != __arm64_float_flags_left_13220756) || (__arm64_float_flags_right_13220756 != __arm64_float_flags_right_13220756))))
        {
            goto label_0xC9BBCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BB9CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        __arm64_fcvtz_source_13220768 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13220768 != __arm64_fcvtz_source_13220768) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13220768 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13220768 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13220768)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))))))), 0));
        goto label_0xC9BBC0;
        label_0xC9BBAC:
        ;
        __arm64_float_flags_left_13220780 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13220780 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0))));
        if (((__arm64_float_flags_left_13220780 != __arm64_float_flags_right_13220780) || ((__arm64_float_flags_left_13220780 != __arm64_float_flags_left_13220780) || (__arm64_float_flags_right_13220780 != __arm64_float_flags_right_13220780))))
        {
            goto label_0xC9BBD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BBB4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        __arm64_fcvtz_source_13220792 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13220792 != __arm64_fcvtz_source_13220792) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13220792 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13220792 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13220792)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))))))), 0));
        goto label_0xC9BBC0;
        label_0xC9BBC0:
        ;
        __arm64_flags_left_13220800 = x8;
        __arm64_flags_right_13220800 = 0x1UL;
        __arm64_flags_result_13220800 = unchecked((ulong)((__arm64_flags_left_13220800) & (__arm64_flags_right_13220800)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13220800 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC9BBE0;
        label_0xC9BBCC:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC9BBD0UL);
        goto label_0xC9BBE0;
        label_0xC9BBD8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC9BBDCUL);
        goto label_0xC9BBE0;
        label_0xC9BBE0:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x29)))), 0));
        __arm64_fcvtz_source_13220836 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13220836 != __arm64_fcvtz_source_13220836) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13220836 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13220836 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13220836)))))))));
        __arm64_float_flags_left_13220840 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13220840 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x1 = unchecked((ulong)(((__arm64_float_flags_left_13220840 == __arm64_float_flags_right_13220840) ? unchecked((uint)(x23)) : unchecked((uint)(x8)))));
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC9BA28;
        label_0xC9BC00:
        ;
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xEC8UL))));
        x21 = 0x0UL;
        x22 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        goto label_0xC9BC10;
        label_0xC9BC10:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BC7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x23);
        x20 = x0;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BC54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC9BC3C;
        label_0xC9BC3C:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13220928 = x11;
        __arm64_flags_right_13220928 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13220928) - (__arm64_flags_right_13220928))) == 0x0UL))
        {
            goto label_0xC9BC64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BC48UL);
        }
        __arm64_flags_left_13220936 = x9;
        __arm64_flags_right_13220936 = 0x1UL;
        __arm64_flags_result_13220936 = unchecked((ulong)((__arm64_flags_left_13220936) - (__arm64_flags_right_13220936)));
        x9 = __arm64_flags_result_13220936;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC9BC50UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9BC3C;
        }
        else
        {
            goto label_0xC9BC54;
        }
        label_0xC9BC54:
        ;
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BC70;
        label_0xC9BC64:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC9BC70;
        label_0xC9BC70:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BC7C;
        label_0xC9BC7C:
        ;
        if ((x21 != 0x0UL))
        {
            goto label_0xC9BCD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BC80UL);
        }
        __arm64_flags_left_13220992 = unchecked((uint)(x22));
        __arm64_flags_right_13220992 = unchecked((uint)0xAUL);
        if ((unchecked((uint)((__arm64_flags_left_13220992) - (__arm64_flags_right_13220992))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BC8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BC88UL);
        }
        if ((unchecked((uint)(x22)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9BC98;
        }
        else
        {
            goto label_0xC9BC8C;
        }
        label_0xC9BC8C:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xCCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC9BC98;
        label_0xC9BC98:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        __arm64_pair_address_13221040 = unchecked((ulong)((sp) + (0x70UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13221040)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13221040) + (0x8UL))))), 0));
        __arm64_pair_address_13221044 = unchecked((ulong)((sp) + (0x60UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13221044)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13221044) + (0x8UL))))), 0));
        __arm64_pair_address_13221048 = unchecked((ulong)((sp) + (0x50UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13221048)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13221048) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xE0UL)));
        return x0;
        label_0xC9BCC4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BCC8;
        label_0xC9BCC8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BCCC;
        label_0xC9BCCC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BCD0;
        label_0xC9BCD0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BCD4;
        label_0xC9BCD4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BCD8;
        label_0xC9BCD8:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BD04;
        label_0xC9BD04:
        ;
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xEC8UL))));
        x22 = x0;
        __arm64_flags_left_13221136 = unchecked((uint)(x1));
        __arm64_flags_right_13221136 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13221136) - (__arm64_flags_right_13221136))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC9BD30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x21 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC9BC10;
        label_0xC9BD30:
        ;
        x21 = 0x0UL;
        goto label_0xC9BD3C;
        label_0xC9BD3C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xEC8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x19 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BDB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x10 = 0x1A8C000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xEC8UL))));
        x1 = RuntimeMemory.ReadU64(x10);
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BD90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC9BD78;
        label_0xC9BD78:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13221244 = x11;
        __arm64_flags_right_13221244 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13221244) - (__arm64_flags_right_13221244))) == 0x0UL))
        {
            goto label_0xC9BDA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9BD84UL);
        }
        __arm64_flags_left_13221252 = x9;
        __arm64_flags_right_13221252 = 0x1UL;
        __arm64_flags_result_13221252 = unchecked((ulong)((__arm64_flags_left_13221252) - (__arm64_flags_right_13221252)));
        x9 = __arm64_flags_result_13221252;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC9BD8CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC9BD78;
        }
        else
        {
            goto label_0xC9BD90;
        }
        label_0xC9BD90:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BDAC;
        label_0xC9BDA0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC9BDAC;
        label_0xC9BDAC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BDB8;
        label_0xC9BDB8:
        ;
        if ((x21 != 0x0UL))
        {
            goto label_0xC9BDC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)(x22))));
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC9BDC4;
        label_0xC9BDC4:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `WaterZone.OnTriggerExit` — RVA `0xc9bdd0`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `private void OnTriggerExit(Collider col) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong WaterZone_OnTriggerExit_RVAc9bdd0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x4A3UL))))))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9BE00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEC0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x4A3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9BE00;
        label_0xC9BE00:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC9BE5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC9BE5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xEC0UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9BE50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x50UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC9BE5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x8) + (0x255UL)));
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WritePtr(x9, unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x259UL))), unchecked((byte)(unchecked((uint)(x10)))));
        goto label_0xC9BE50;
        label_0xC9BE50:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC9BE5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WaterZone.ctor` — RVA `0xc9be60`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong WaterZone_ctor_RVAc9be60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x10 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x10) + (0xA70UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x10) + (0xA70UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)(0x3F000000UL))));
        x8 = unchecked((ulong)((x0) + (0x108UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xA4UL))), unchecked((uint)(x9)));
        x9 = unchecked((ulong)(unchecked((uint)(0x1EUL))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x10)), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0xF8UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0xF8UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x8, v0);
#else
        __WriteVector128(x8, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x14UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x14UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x13CUL))), unchecked((uint)(x9)));
        x9 = unchecked((ulong)(unchecked((uint)(0x999AUL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E19UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x160UL))), unchecked((uint)(x9)));
        x9 = unchecked((ulong)(unchecked((uint)(0x41700000UL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x168UL))), unchecked((uint)(x9)));
        x9 = unchecked((ulong)(unchecked((uint)(0x41F00000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x14CUL))), unchecked((uint)(x10)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0x150UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0x150UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x170UL))), unchecked((uint)(x10)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x6CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x6CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x7CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x7CUL))), v0);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x8CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x19CUL))), unchecked((uint)(x9)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
