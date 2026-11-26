# `WeaponEffects` — TypeDefIndex 3367

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `PlayerWeapons` | `PlayerWeaponsComponent` |
| `0x28` | `WeaponBehavior` | `WeaponBehaviorComponent` |
| `0x30` | `FPSRigidBodyWalker` | `FPSWalkerComponent` |
| `0x38` | `GameObject` | `weaponObj` |
| `0x40` | `GameObject` | `dirtImpact` |
| `0x48` | `GameObject` | `metalImpact` |
| `0x50` | `GameObject` | `woodImpact` |
| `0x58` | `GameObject` | `waterImpact` |
| `0x60` | `GameObject` | `glassImpact` |
| `0x68` | `GameObject` | `fleshImpact` |
| `0x70` | `GameObject` | `stoneImpact` |
| `0x78` | `GameObject` | `explosion` |
| `0x80` | `GameObject` | `explosionObj` |
| `0x88` | `GameObject` | `waterSplash` |
| `0x90` | `ParticleSystem` | `rippleEffect` |
| `0x98` | `ParticleSystem` | `bubblesEffect` |
| `0xA0` | `ParticleSystem` | `splashTrail` |
| `0xA8` | `int` | `impactObjID` |
| `0xB0` | `GameObject` | `impactObj` |
| `0xB8` | `ParticleSystem` | `npcTracerParticles` |
| `0xC0` | `ParticleSystem` | `playerTracerParticles` |
| `0xC8` | `ParticleSystem` | `bubbleParticles` |
| `0xD0` | `int[]` | `dirtMarksID` |
| `0xD8` | `int[]` | `metalMarksID` |
| `0xE0` | `int[]` | `woodMarksID` |
| `0xE8` | `int[]` | `glassMarksID` |
| `0xF0` | `int[]` | `stoneMarksID` |
| `0xF8` | `int[]` | `dirtMarksMeleeID` |
| `0x100` | `int[]` | `metalMarksMeleeID` |
| `0x108` | `int[]` | `woodMarksMeleeID` |
| `0x110` | `int` | `markObjID` |
| `0x118` | `AudioClip[]` | `defaultImpactSounds` |
| `0x120` | `AudioClip[]` | `metalImpactSounds` |
| `0x128` | `AudioClip[]` | `woodImpactSounds` |
| `0x130` | `AudioClip[]` | `waterImpactSounds` |
| `0x138` | `AudioClip[]` | `glassImpactSounds` |
| `0x140` | `AudioClip[]` | `fleshImpactSounds` |
| `0x148` | `AudioClip[]` | `stoneImpactSounds` |
| `0x150` | `AudioClip[]` | `defaultImpactSoundsMelee` |
| `0x158` | `AudioClip[]` | `metalImpactSoundsMelee` |
| `0x160` | `AudioClip[]` | `woodImpactSoundsMelee` |
| `0x168` | `AudioClip[]` | `fleshImpactSoundsMelee` |
| `0x170` | `AudioClip[]` | `stoneImpactSoundsMelee` |
| `0x178` | `AudioClip` | `hitSound` |
| `0x180` | `float` | `hitVolumeAmt` |
| `0x188` | `ParticleSystem` | `partSys` |
| `0x190` | `ParticleSystem` | `tracerParticles` |
| `0x198` | `ParticleSystem.Particle[]` | `activeParticles` |
| `0x1A0` | `int` | `numparticles` |
| `0x1A4` | `int` | `numParticlesAlive` |
| `0x1A8` | `bool` | `rotateParticle` |
| `0x1AC` | `float` | `randvel` |

## `WeaponEffects.Start` — RVA `0xc8ed38`

- Lift status: **exact**; input span: 324 bytes; span to next metadata RVA: 324 bytes.
- Metadata signature: `public void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=47 (informational only).

```csharp
public static ulong WeaponEffects_Start_RVAc8ed38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x448UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8ED88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x448UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC8ED88;
        label_0xC8ED88:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8EE78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x38UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8EE78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD08UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49488UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x20UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xC8EE78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8EE78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8EE78;
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
            goto label_0xC8EE78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8EE78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD10UL))));
        x20 = 0x1A8E000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x0);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x100UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x19) + (0x168UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x168UL))), x1);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC8EE78:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WeaponEffects.ImpactEffects` — RVA `0xc8ee7c`

- Lift status: **partial**; input span: 2716 bytes; span to next metadata RVA: 2716 bytes.
- Metadata signature: `public bool ImpactEffects(Collider hitcol, Vector3 hitPoint, bool NpcAttack, bool meleeAttack, Vector3 rayNormal) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=389 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xc8efbc; reason: Unknown IR expression at 0xc8efbc; reason: Unsupported instruction 'b.ne' at 0xc8f4f8; reason: Unknown IR expression at 0xc8f4f8; reason: Unsupported instruction 'b.ne' at 0xc8f554; reason: Unknown IR expression at 0xc8f554; reason: Unsupported instruction 'b.ne' at 0xc8f630; reason: Unknown IR expression at 0xc8f630

```csharp
public static uint WeaponEffects_ImpactEffects_RVAc8ee7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13168564 = default(uint);
        uint __arm64_flags_left_13168584 = default(uint);
        uint __arm64_flags_left_13168600 = default(uint);
        uint __arm64_flags_left_13168748 = default(uint);
        uint __arm64_flags_left_13168764 = default(uint);
        uint __arm64_flags_left_13168780 = default(uint);
        uint __arm64_flags_left_13168924 = default(uint);
        uint __arm64_flags_left_13168940 = default(uint);
        uint __arm64_flags_left_13169708 = default(uint);
        ulong __arm64_flags_left_13169896 = default(ulong);
        ulong __arm64_flags_left_13169904 = default(ulong);
        ulong __arm64_flags_left_13169988 = default(ulong);
        ulong __arm64_flags_left_13169996 = default(ulong);
        uint __arm64_flags_left_13170072 = default(uint);
        ulong __arm64_flags_left_13170092 = default(ulong);
        ulong __arm64_flags_left_13170208 = default(ulong);
        ulong __arm64_flags_left_13170216 = default(ulong);
        uint __arm64_flags_left_13170272 = default(uint);
        uint __arm64_flags_left_13170400 = default(uint);
        uint __arm64_flags_left_13170792 = default(uint);
        ulong __arm64_flags_left_13170884 = default(ulong);
        ulong __arm64_flags_left_13170892 = default(ulong);
        ulong __arm64_flags_result_13169904 = default(ulong);
        ulong __arm64_flags_result_13169996 = default(ulong);
        ulong __arm64_flags_result_13170216 = default(ulong);
        ulong __arm64_flags_result_13170892 = default(ulong);
        uint __arm64_flags_right_13168564 = default(uint);
        uint __arm64_flags_right_13168584 = default(uint);
        uint __arm64_flags_right_13168600 = default(uint);
        uint __arm64_flags_right_13168748 = default(uint);
        uint __arm64_flags_right_13168764 = default(uint);
        uint __arm64_flags_right_13168780 = default(uint);
        uint __arm64_flags_right_13168924 = default(uint);
        uint __arm64_flags_right_13168940 = default(uint);
        uint __arm64_flags_right_13169708 = default(uint);
        ulong __arm64_flags_right_13169896 = default(ulong);
        ulong __arm64_flags_right_13169904 = default(ulong);
        ulong __arm64_flags_right_13169988 = default(ulong);
        ulong __arm64_flags_right_13169996 = default(ulong);
        uint __arm64_flags_right_13170072 = default(uint);
        ulong __arm64_flags_right_13170092 = default(ulong);
        ulong __arm64_flags_right_13170208 = default(ulong);
        ulong __arm64_flags_right_13170216 = default(ulong);
        uint __arm64_flags_right_13170272 = default(uint);
        uint __arm64_flags_right_13170400 = default(uint);
        uint __arm64_flags_right_13170792 = default(uint);
        ulong __arm64_flags_right_13170884 = default(ulong);
        ulong __arm64_flags_right_13170892 = default(ulong);
        ulong __arm64_pair_address_13168252 = default(ulong);
        ulong __arm64_pair_address_13168256 = default(ulong);
        ulong __arm64_pair_address_13168260 = default(ulong);
        ulong __arm64_pair_address_13170376 = default(ulong);
        ulong __arm64_pair_address_13170380 = default(ulong);
        ulong __arm64_pair_address_13170388 = default(ulong);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13168252 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13168252, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13168252) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = __arm64_pair_address_13168252;
        __arm64_pair_address_13168256 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13168256, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13168256) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13168260 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13168260, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13168260) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x449UL))))))));
        v11 = v5;
        v12 = v4;
        v13 = v3;
        x22 = unchecked((ulong)(unchecked((uint)(x3))));
        x20 = unchecked((ulong)(unchecked((uint)(x2))));
        v8 = v2;
        v9 = v1;
        v10 = v0;
        x23 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8EF68;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
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
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x449UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC8EF68;
        label_0xC8EF68:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x28UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x1 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCEB858UL /* metadata target: <PrivateImplementationDetails>.ComputeStringHash */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0xADCBUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x97C0UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168564 = unchecked((uint)(x0));
        __arm64_flags_right_13168564 = unchecked((uint)(x8));
        if (((__arm64_flags_left_13168564 >= __arm64_flags_right_13168564) && (!((unchecked((uint)((__arm64_flags_left_13168564) - (__arm64_flags_right_13168564))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC8F064;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8EFBCUL)));
        }
        RuntimeCalls.Unsupported("b.eq", 0xC8EFBCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC8F23C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x3588UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x4E1UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168584 = unchecked((uint)(x0));
        __arm64_flags_right_13168584 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13168584) - (__arm64_flags_right_13168584))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F1B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xCA9AUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x6DD4UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168600 = unchecked((uint)(x0));
        __arm64_flags_right_13168600 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13168600) - (__arm64_flags_right_13168600))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0xB0UL))), x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0xF8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F760;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F048;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F044UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F048;
        label_0xC8F048:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F060UL)));
        }
        goto label_0xC8F834;
        label_0xC8F064:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xB5EDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xAB33UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168748 = unchecked((uint)(x0));
        __arm64_flags_right_13168748 = unchecked((uint)(x8));
        if (((__arm64_flags_left_13168748 >= __arm64_flags_right_13168748) && (!((unchecked((uint)((__arm64_flags_left_13168748) - (__arm64_flags_right_13168748))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC8F114;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x317CUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xA951UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168764 = unchecked((uint)(x0));
        __arm64_flags_right_13168764 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13168764) - (__arm64_flags_right_13168764))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F2B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xB5EDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xAB33UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168780 = unchecked((uint)(x0));
        __arm64_flags_right_13168780 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13168780) - (__arm64_flags_right_13168780))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0xB0UL))), x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0xF8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F7A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x168UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F0F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F0F4UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F0F8;
        label_0xC8F0F8:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x168UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F110UL)));
        }
        goto label_0xC8F834;
        label_0xC8F114:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x56B0UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xD635UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168924 = unchecked((uint)(x0));
        __arm64_flags_right_13168924 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13168924) - (__arm64_flags_right_13168924))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F33C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x3C0UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xAFB8UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13168940 = unchecked((uint)(x0));
        __arm64_flags_right_13168940 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13168940) - (__arm64_flags_right_13168940))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD0UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0xB0UL))), x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0xF8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3D4;
        }
        else
        {
            goto label_0xC8F170;
        }
        label_0xC8F170:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F19C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F198UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F19C;
        label_0xC8F19C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F1B4UL)));
        }
        goto label_0xC8F834;
        label_0xC8F1B8:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0xB0UL))), x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0xF8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F718;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x160UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F220;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F21CUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F220;
        label_0xC8F220:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x160UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F238UL)));
        }
        goto label_0xC8F834;
        label_0xC8F23C:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x22 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0xB0UL))), x1);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x88UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0xF8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F29C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F298UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F29C;
        label_0xC8F29C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F2B4UL)));
        }
        goto label_0xC8F834;
        label_0xC8F2B8:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0xB0UL))), x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0xF8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F7F0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x158UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F320;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F31CUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F320;
        label_0xC8F320:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x158UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F338UL)));
        }
        goto label_0xC8F834;
        label_0xC8F33C:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x0 = x23;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F3B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x22 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0xB0UL))), x1);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x80UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0xF8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F39C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F398UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F39C;
        label_0xC8F39C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F3B4UL)));
        }
        goto label_0xC8F834;
        label_0xC8F3B8:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0xB0UL))), x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0xF8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F170;
        }
        else
        {
            goto label_0xC8F3D4;
        }
        label_0xC8F3D4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F400;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F3FCUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F400;
        label_0xC8F400:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            goto label_0xC8F418;
        }
        label_0xC8F418:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        __arm64_flags_left_13169708 = unchecked((uint)(x0));
        __arm64_flags_right_13169708 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13169708 >= __arm64_flags_right_13169708))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x22) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = unchecked((ulong)((x19) + (0x178UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x178UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC8F448;
        label_0xC8F448:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xEC8UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ECD4UL /* metadata target: Transform.GetEnumerator */, x0, x1, x2, x3);
        x22 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F844;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x25 = 0x1A8C000UL;
        x26 = 0x1A8D000UL;
        x27 = 0x1A8E000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xED0UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xE68UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xA8UL))));
        x23 = unchecked((ulong)((x19) + (0x188UL)));
        goto label_0xC8F4CC;
        label_0xC8F4CC:
        ;
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = RuntimeMemory.ReadU64(x25);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F4FC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC8F4E4;
        label_0xC8F4E4:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13169896 = x11;
        __arm64_flags_right_13169896 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13169896) - (__arm64_flags_right_13169896))) == 0x0UL))
        {
            goto label_0xC8F50C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F4F0UL)));
        }
        __arm64_flags_left_13169904 = x9;
        __arm64_flags_right_13169904 = 0x1UL;
        __arm64_flags_result_13169904 = unchecked((ulong)((__arm64_flags_left_13169904) - (__arm64_flags_right_13169904)));
        x9 = __arm64_flags_result_13169904;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC8F4F8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC8F4E4;
        }
        else
        {
            goto label_0xC8F4FC;
        }
        label_0xC8F4FC:
        ;
        x0 = x22;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F518;
        label_0xC8F50C:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC8F518;
        label_0xC8F518:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F5E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = RuntimeMemory.ReadU64(x25);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F558;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC8F540;
        label_0xC8F540:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13169988 = x11;
        __arm64_flags_right_13169988 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13169988) - (__arm64_flags_right_13169988))) == 0x0UL))
        {
            goto label_0xC8F568;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F54CUL)));
        }
        __arm64_flags_left_13169996 = x9;
        __arm64_flags_right_13169996 = 0x1UL;
        __arm64_flags_result_13169996 = unchecked((ulong)((__arm64_flags_left_13169996) - (__arm64_flags_right_13169996)));
        x9 = __arm64_flags_result_13169996;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC8F554UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC8F540;
        }
        else
        {
            goto label_0xC8F558;
        }
        label_0xC8F558:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F578;
        label_0xC8F568:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC8F578;
        label_0xC8F578:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F83C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x26);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_13170072 = unchecked((uint)(x10));
        __arm64_flags_right_13170072 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_13170072 >= __arm64_flags_right_13170072))))
        {
            goto label_0xC8F838;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13170092 = x8;
        __arm64_flags_right_13170092 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13170092) - (__arm64_flags_right_13170092))) == 0x0UL))))
        {
            goto label_0xC8F838;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x23, x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x188UL))));
        x0 = x19;
        v0 = v13;
        v1 = v12;
        v2 = v11;
        x0 = RuntimeCalls.InvokeDirect(0xC8F918UL /* metadata target: WeaponEffects.EmitRotatedParticle */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F4CC;
        label_0xC8F5E8:
        ;
        x23 = 0x0UL;
        x25 = unchecked((ulong)(unchecked((uint)(0x1CUL))));
        goto label_0xC8F5F0;
        label_0xC8F5F0:
        ;
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F65C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x24);
        x22 = x0;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F634;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC8F61C;
        label_0xC8F61C:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13170208 = x11;
        __arm64_flags_right_13170208 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13170208) - (__arm64_flags_right_13170208))) == 0x0UL))
        {
            goto label_0xC8F644;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F628UL)));
        }
        __arm64_flags_left_13170216 = x9;
        __arm64_flags_right_13170216 = 0x1UL;
        __arm64_flags_result_13170216 = unchecked((ulong)((__arm64_flags_left_13170216) - (__arm64_flags_right_13170216)));
        x9 = __arm64_flags_result_13170216;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC8F630UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC8F61C;
        }
        else
        {
            goto label_0xC8F634;
        }
        label_0xC8F634:
        ;
        x0 = x22;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F650;
        label_0xC8F644:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC8F650;
        label_0xC8F650:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F65C;
        label_0xC8F65C:
        ;
        if ((x23 != 0x0UL))
        {
            goto label_0xC8F848;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F660UL)));
        }
        __arm64_flags_left_13170272 = unchecked((uint)(x25));
        __arm64_flags_right_13170272 = unchecked((uint)0x1CUL);
        if ((unchecked((uint)((__arm64_flags_left_13170272) - (__arm64_flags_right_13170272))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F66C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F668UL)));
        }
        if ((unchecked((uint)(x25)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F6B4;
        }
        else
        {
            goto label_0xC8F66C;
        }
        label_0xC8F66C:
        ;
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F680;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x229UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F6DC;
        }
        else
        {
            goto label_0xC8F680;
        }
        label_0xC8F680:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC8F688;
        label_0xC8F688:
        ;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x180UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x178UL))));
        x8 = unchecked((ulong)(unchecked((uint)(0x43FA0000UL))));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40400000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xC8D260UL /* metadata target: PlayAudioAtPos.PlayClipAt */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F6B4;
        label_0xC8F6B4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_13170376 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13170376)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13170376) + (0x8UL))))), 0));
        __arm64_pair_address_13170380 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13170380)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13170380) + (0x8UL))))), 0));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        __arm64_pair_address_13170388 = sp;
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13170388)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13170388) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13170388) + (0x80UL)));
        return unchecked((uint)(x0));
        label_0xC8F6DC:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x154UL))))));
        __arm64_flags_left_13170400 = unchecked((uint)(x9));
        __arm64_flags_right_13170400 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13170400) - (__arm64_flags_right_13170400))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13170400)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13170400)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13170400) - (__arm64_flags_right_13170400))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13170400)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC8F704;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x1DEUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F680;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x432000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x390UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3F4CUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        goto label_0xC8F688;
        label_0xC8F704:
        ;
        x8 = 0x432000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4F4UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E4CUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        goto label_0xC8F688;
        label_0xC8F718:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F744;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F740UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F744;
        label_0xC8F744:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F75CUL)));
        }
        goto label_0xC8F834;
        label_0xC8F760:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F78C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F788UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F78C;
        label_0xC8F78C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F7A4UL)));
        }
        goto label_0xC8F834;
        label_0xC8F7A8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F7D4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F7D0UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F7D4;
        label_0xC8F7D4:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F7ECUL)));
        }
        goto label_0xC8F834;
        label_0xC8F7F0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8F834;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F840;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F818UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F81C;
        label_0xC8F81C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8F418;
        }
        else
        {
            goto label_0xC8F834;
        }
        label_0xC8F834:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F838;
        label_0xC8F838:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F83C;
        label_0xC8F83C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F840;
        label_0xC8F840:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F844;
        label_0xC8F844:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F848;
        label_0xC8F848:
        ;
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F868;
        label_0xC8F868:
        ;
        __arm64_flags_left_13170792 = unchecked((uint)(x1));
        __arm64_flags_right_13170792 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13170792) - (__arm64_flags_right_13170792))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC8F884;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F870UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x23 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x25 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC8F5F0;
        label_0xC8F884:
        ;
        x19 = x0;
        x23 = 0x0UL;
        goto label_0xC8F894;
        label_0xC8F894:
        ;
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC8F900;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = RuntimeMemory.ReadU64(x24);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8F8D8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC8F8C0;
        label_0xC8F8C0:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13170884 = x11;
        __arm64_flags_right_13170884 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13170884) - (__arm64_flags_right_13170884))) == 0x0UL))
        {
            goto label_0xC8F8E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8F8CCUL)));
        }
        __arm64_flags_left_13170892 = x9;
        __arm64_flags_right_13170892 = 0x1UL;
        __arm64_flags_result_13170892 = unchecked((ulong)((__arm64_flags_left_13170892) - (__arm64_flags_right_13170892)));
        x9 = __arm64_flags_result_13170892;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC8F8D4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC8F8C0;
        }
        else
        {
            goto label_0xC8F8D8;
        }
        label_0xC8F8D8:
        ;
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F8F4;
        label_0xC8F8E8:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC8F8F4;
        label_0xC8F8F4:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F900;
        label_0xC8F900:
        ;
        if ((x23 != 0x0UL))
        {
            goto label_0xC8F90C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8F90C;
        label_0xC8F90C:
        ;
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `WeaponEffects.EmitRotatedParticle` — RVA `0xc8f918`

- Lift status: **partial**; input span: 828 bytes; span to next metadata RVA: 828 bytes.
- Metadata signature: `public void EmitRotatedParticle(ParticleSystem partSysToRotate, Vector3 direction) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=82 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintp' at 0xc8fa2c; reason: Unsupported instruction 'frintm' at 0xc8fa38; reason: Unsupported instruction 'csel' at 0xc8fa50; reason: Unknown IR expression at 0xc8fa50; reason: Unsupported instruction 'b.le' at 0xc8fb14; reason: Unknown IR expression at 0xc8fb14; reason: Unsupported instruction 'smaddl' at 0xc8fbec

```csharp
public static ulong WeaponEffects_EmitRotatedParticle_RVAc8f918(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13171220 = default(double);
        double __arm64_fcvtz_source_13171268 = default(double);
        ulong __arm64_flags_left_13171228 = default(ulong);
        uint __arm64_flags_left_13171684 = default(uint);
        ulong __arm64_flags_result_13171228 = default(ulong);
        ulong __arm64_flags_right_13171228 = default(ulong);
        uint __arm64_flags_right_13171684 = default(uint);
        float __arm64_float_flags_left_13171168 = default(float);
        double __arm64_float_flags_left_13171180 = default(double);
        double __arm64_float_flags_left_13171204 = default(double);
        double __arm64_float_flags_left_13171272 = default(double);
        float __arm64_float_flags_left_13171424 = default(float);
        float __arm64_float_flags_left_13171456 = default(float);
        float __arm64_float_flags_left_13171528 = default(float);
        float __arm64_float_flags_left_13171652 = default(float);
        float __arm64_float_flags_right_13171168 = default(float);
        double __arm64_float_flags_right_13171180 = default(double);
        double __arm64_float_flags_right_13171204 = default(double);
        double __arm64_float_flags_right_13171272 = default(double);
        float __arm64_float_flags_right_13171424 = default(float);
        float __arm64_float_flags_right_13171456 = default(float);
        float __arm64_float_flags_right_13171528 = default(float);
        float __arm64_float_flags_right_13171652 = default(float);
        float __arm64_fp_left_13171524 = default(float);
        float __arm64_fp_left_13171648 = default(float);
        float __arm64_fp_right_13171524 = default(float);
        float __arm64_fp_right_13171648 = default(float);
        ulong __arm64_pair_address_13170972 = default(ulong);
        ulong __arm64_pair_address_13170976 = default(ulong);
        ulong __arm64_pair_address_13170980 = default(ulong);
        ulong __arm64_pair_address_13170984 = default(ulong);
        ulong __arm64_pair_address_13171008 = default(ulong);
        ulong __arm64_pair_address_13171084 = default(ulong);
        ulong __arm64_pair_address_13171400 = default(ulong);
        ulong __arm64_pair_address_13171500 = default(ulong);
        ulong __arm64_pair_address_13171564 = default(ulong);
        ulong __arm64_pair_address_13171624 = default(ulong);
        ulong __arm64_pair_address_13171764 = default(ulong);
        ulong __arm64_pair_address_13171768 = default(ulong);
        ulong __arm64_pair_address_13171772 = default(ulong);
        ulong __arm64_pair_address_13171776 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        __arm64_pair_address_13170972 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13170972, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13170972) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13170976 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13170976, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13170976) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13170980 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13170980, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13170980) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13170984 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13170984, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13170984) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        v10 = v0;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13171008 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13171008, v0);
#else
        __WriteVector128(__arm64_pair_address_13171008, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13171008) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13171008) + (0x10UL))), v0);
#endif
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x28UL))), 0x0UL);
        if ((x1 == 0x0UL))
        {
            goto label_0xC8FC4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = x1;
        x20 = x0;
        x0 = x1;
        x1 = 0x0UL;
        v8 = v2;
        v9 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13171084 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13171084, v0);
#else
        __WriteVector128(__arm64_pair_address_13171084, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13171084) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13171084) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x242UL))))))));
        v11 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F9B8;
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
        goto label_0xC8F9B8;
        label_0xC8F9B8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8F9D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8F9CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8F9D0;
        label_0xC8F9D0:
        ;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v12;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13171168 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13171168 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13171168 >= __arm64_float_flags_right_13171168))
        {
            goto label_0xC8FA00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8F9E8UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13171180 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13171180 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13171180 != __arm64_float_flags_right_13171180) || ((__arm64_float_flags_left_13171180 != __arm64_float_flags_left_13171180) || (__arm64_float_flags_right_13171180 != __arm64_float_flags_right_13171180))))
        {
            goto label_0xC8FA28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8F9F4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC8FA14;
        label_0xC8FA00:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13171204 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13171204 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13171204 != __arm64_float_flags_right_13171204) || ((__arm64_float_flags_left_13171204 != __arm64_float_flags_left_13171204) || (__arm64_float_flags_right_13171204 != __arm64_float_flags_right_13171204))))
        {
            goto label_0xC8FA34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8FA0CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC8FA14;
        label_0xC8FA14:
        ;
        __arm64_fcvtz_source_13171220 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13171220 != __arm64_fcvtz_source_13171220) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13171220 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13171220 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13171220)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13171228 = x8;
        __arm64_flags_right_13171228 = 0x1UL;
        __arm64_flags_result_13171228 = unchecked((ulong)((__arm64_flags_left_13171228) & (__arm64_flags_right_13171228)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13171228 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC8FA3C;
        label_0xC8FA28:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC8FA2CUL);
        goto label_0xC8FA3C;
        label_0xC8FA34:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC8FA38UL);
        goto label_0xC8FA3C;
        label_0xC8FA3C:
        ;
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13171268 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13171268 != __arm64_fcvtz_source_13171268) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13171268 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13171268 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13171268)))))))));
        __arm64_float_flags_left_13171272 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13171272 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC8FA50UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1A8UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x198UL))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C99D8UL /* metadata target: ParticleSystem.GetParticles */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x1A4UL))), unchecked((uint)(x0)));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        x23 = unchecked((ulong)(unchecked((uint)(0x84UL))));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3E800000UL)), 0)), 0));
        goto label_0xC8FA98;
        label_0xC8FA98:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13171400 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13171400, v0);
#else
        __WriteVector128(__arm64_pair_address_13171400, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13171400) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13171400) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x1UL)))))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x22))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13171424 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13171424 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13171424 >= __arm64_float_flags_right_13171424) || ((__arm64_float_flags_left_13171424 != __arm64_float_flags_left_13171424) || (__arm64_float_flags_right_13171424 != __arm64_float_flags_right_13171424))))
        {
            goto label_0xC8FC14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17901F4UL /* metadata target: Random.get_value */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17C9580UL /* metadata target: ParticleSystem.get_main */, x0, x1, x2, x3);
        __arm64_float_flags_left_13171456 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13171456 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x0);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = unchecked((ulong)((sp) + (0x28UL)));
        x1 = 0x0UL;
        RuntimeCalls.Unsupported("b.le", 0xC8FB14UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC8FB58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8FB18UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0x17C9D80UL /* metadata target: ParticleSystem.MainModule.get_startSpeed */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13171500 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13171500, v0);
#else
        __WriteVector128(__arm64_pair_address_13171500, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13171500) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13171500) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x0 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17901F4UL /* metadata target: Random.get_value */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_fp_left_13171524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_13171524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_13171524 != __arm64_fp_left_13171524) ? __arm64_fp_left_13171524 : ((__arm64_fp_right_13171524 != __arm64_fp_right_13171524) ? __arm64_fp_right_13171524 : (((__arm64_fp_left_13171524 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_13171524 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_13171524), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_13171524), 0))))), 0) : ((__arm64_fp_left_13171524 <= __arm64_fp_right_13171524) ? __arm64_fp_left_13171524 : __arm64_fp_right_13171524))))), 0));
        __arm64_float_flags_left_13171528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13171528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13171528 >= __arm64_float_flags_right_13171528) || ((__arm64_float_flags_left_13171528 != __arm64_float_flags_left_13171528) || (__arm64_float_flags_right_13171528 != __arm64_float_flags_right_13171528))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC8FBD4;
        label_0xC8FB58:
        ;
        x0 = RuntimeCalls.InvokeDirect(0x17C9D80UL /* metadata target: ParticleSystem.MainModule.get_startSpeed */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13171564 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13171564, v0);
#else
        __WriteVector128(__arm64_pair_address_13171564, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13171564) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13171564) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17C9580UL /* metadata target: ParticleSystem.get_main */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x0);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = unchecked((ulong)((sp) + (0x28UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9D80UL /* metadata target: ParticleSystem.MainModule.get_startSpeed */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13171624 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13171624, v0);
#else
        __WriteVector128(__arm64_pair_address_13171624, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13171624) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13171624) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x0 = 0x0UL;
        v12 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17901F4UL /* metadata target: Random.get_value */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
        __arm64_fp_left_13171648 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_13171648 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_13171648 != __arm64_fp_left_13171648) ? __arm64_fp_left_13171648 : ((__arm64_fp_right_13171648 != __arm64_fp_right_13171648) ? __arm64_fp_right_13171648 : (((__arm64_fp_left_13171648 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_13171648 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_13171648), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_13171648), 0))))), 0) : ((__arm64_fp_left_13171648 <= __arm64_fp_right_13171648) ? __arm64_fp_left_13171648 : __arm64_fp_right_13171648))))), 0));
        __arm64_float_flags_left_13171652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13171652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13171652 >= __arm64_float_flags_right_13171652) || ((__arm64_float_flags_left_13171652 != __arm64_float_flags_left_13171652) || (__arm64_float_flags_right_13171652 != __arm64_float_flags_right_13171652))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC8FBD4;
        label_0xC8FBD4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x198UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x1ACUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8FC4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13171684 = unchecked((uint)(x22));
        __arm64_flags_right_13171684 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13171684 >= __arm64_flags_right_13171684))
        {
            goto label_0xC8FC50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8FBECUL);
        }
        RuntimeCalls.Unsupported("smaddl", 0xC8FBECUL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9414UL /* metadata target: ParticleSystem.Particle.set_velocity */, x0, x1, x2, x3);
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x1A4UL))))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) - (unchecked((uint)(0x1UL)))))));
        goto label_0xC8FA98;
        label_0xC8FC14:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x198UL))));
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x1A4UL))))));
        x0 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C98CCUL /* metadata target: ParticleSystem.SetParticles */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8FC28;
        label_0xC8FC28:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        __arm64_pair_address_13171764 = unchecked((ulong)((sp) + (0x90UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13171764)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13171764) + (0x8UL))))), 0));
        __arm64_pair_address_13171768 = unchecked((ulong)((sp) + (0x80UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13171768)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13171768) + (0x8UL))))), 0));
        __arm64_pair_address_13171772 = unchecked((ulong)((sp) + (0x70UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13171772)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13171772) + (0x8UL))))), 0));
        __arm64_pair_address_13171776 = unchecked((ulong)((sp) + (0x60UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13171776)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13171776) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xD0UL)));
        return x0;
        label_0xC8FC4C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC8FC50;
        label_0xC8FC50:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `WeaponEffects.BulletMarks` — RVA `0xc8fc54`

- Lift status: **exact**; input span: 2740 bytes; span to next metadata RVA: 2740 bytes.
- Metadata signature: `public void BulletMarks(RaycastHit hit, bool meleeAttack) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=377 (informational only).

```csharp
public static uint WeaponEffects_BulletMarks_RVAc8fc54(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13172364 = default(uint);
        uint __arm64_flags_left_13172480 = default(uint);
        uint __arm64_flags_left_13172524 = default(uint);
        uint __arm64_flags_right_13172364 = default(uint);
        uint __arm64_flags_right_13172480 = default(uint);
        uint __arm64_flags_right_13172524 = default(uint);
        float __arm64_float_flags_left_13173580 = default(float);
        float __arm64_float_flags_left_13174364 = default(float);
        float __arm64_float_flags_right_13173580 = default(float);
        float __arm64_float_flags_right_13174364 = default(float);
        ulong __arm64_pair_address_13171796 = default(ulong);
        ulong __arm64_pair_address_13171800 = default(ulong);
        ulong __arm64_pair_address_13171804 = default(ulong);
        ulong __arm64_pair_address_13171808 = default(ulong);
        ulong __arm64_pair_address_13172992 = default(ulong);
        ulong __arm64_pair_address_13172996 = default(ulong);
        ulong __arm64_pair_address_13173188 = default(ulong);
        ulong __arm64_pair_address_13173352 = default(ulong);
        ulong __arm64_pair_address_13173384 = default(ulong);
        ulong __arm64_pair_address_13173448 = default(ulong);
        ulong __arm64_pair_address_13173532 = default(ulong);
        ulong __arm64_pair_address_13173856 = default(ulong);
        ulong __arm64_pair_address_13173968 = default(ulong);
        ulong __arm64_pair_address_13173972 = default(ulong);
        ulong __arm64_pair_address_13173976 = default(ulong);
        ulong __arm64_pair_address_13173980 = default(ulong);
        ulong __arm64_pair_address_13174192 = default(ulong);
        ulong __arm64_pair_address_13174196 = default(ulong);
        ulong __arm64_pair_address_13174200 = default(ulong);
        ulong __arm64_pair_address_13174208 = default(ulong);
        ulong __arm64_pair_address_13174324 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13171796 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13171796, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13171796) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_13171796;
        __arm64_pair_address_13171800 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13171800, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13171800) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13171804 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13171804, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13171804) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13171808 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13171808, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13171808) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x44AUL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x2))));
        x19 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8FD34;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xFD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x44AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC8FD34;
        label_0xC8FD34:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x1A8E000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD0UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x22);
        x2 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FD84;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FD74UL)));
        }
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FD94;
        }
        else
        {
            goto label_0xC8FD78;
        }
        label_0xC8FD78:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF8UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8FE78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FD80UL)));
        }
        goto label_0xC90700;
        label_0xC8FD84:
        ;
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FDBC;
        }
        else
        {
            goto label_0xC8FD88;
        }
        label_0xC8FD88:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD0UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8FE78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FD90UL)));
        }
        goto label_0xC90700;
        label_0xC8FD94:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FDE4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x100UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8FE78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FDB8UL)));
        }
        goto label_0xC90700;
        label_0xC8FDBC:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FE0C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8FE78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FDE0UL)));
        }
        goto label_0xC90700;
        label_0xC8FDE4:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FE34;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x108UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8FE78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FE08UL)));
        }
        goto label_0xC90700;
        label_0xC8FE0C:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FE54;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8FE78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FE30UL)));
        }
        goto label_0xC90700;
        label_0xC8FE34:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FD78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8FE50UL)));
        }
        goto label_0xC8FE70;
        label_0xC8FE54:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904E4;
        }
        else
        {
            goto label_0xC8FE70;
        }
        label_0xC8FE70:
        ;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE8UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            goto label_0xC8FE78;
        }
        label_0xC8FE78:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        __arm64_flags_left_13172364 = unchecked((uint)(x0));
        __arm64_flags_right_13172364 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13172364 >= __arm64_flags_right_13172364))
        {
            goto label_0xC90704;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x22) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xD8UL))));
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x110UL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8FECC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8FECC;
        label_0xC8FECC:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C50UL /* metadata target: GameObject.get_layer */, x0, x1, x2, x3);
        __arm64_flags_left_13172480 = unchecked((uint)(x0));
        __arm64_flags_right_13172480 = unchecked((uint)0x9UL);
        if ((unchecked((uint)((__arm64_flags_left_13172480) - (__arm64_flags_right_13172480))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C50UL /* metadata target: GameObject.get_layer */, x0, x1, x2, x3);
        __arm64_flags_left_13172524 = unchecked((uint)(x0));
        __arm64_flags_right_13172524 = unchecked((uint)0xDUL);
        if ((unchecked((uint)((__arm64_flags_left_13172524) - (__arm64_flags_right_13172524))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFD8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F6110UL /* metadata target: String.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF0UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F6110UL /* metadata target: String.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F6110UL /* metadata target: String.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE48UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F6110UL /* metadata target: String.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEC58UL /* metadata target: RaycastHit.get_collider */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792774UL /* metadata target: GameObject.get_tag */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F6110UL /* metadata target: String.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC904BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x110UL))))));
        x0 = x19;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x22 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17CED04UL /* metadata target: RaycastHit.get_point */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17CED10UL /* metadata target: RaycastHit.get_normal */, x0, x1, x2, x3);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x2CBUL))))))));
        v11 = v0;
        v12 = v1;
        v13 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC900C8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x2CBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC900C8;
        label_0xC900C8:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD88UL))));
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x304UL))))), 0));
        x0 = x22;
        x9 = RuntimeMemory.ReadU64(x9);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_13172992 = unchecked((ulong)((x8) + (0x8UL)));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13172992)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13172992) + (0x4UL))))), 0));
        __arm64_pair_address_13172996 = x8;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13172996)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13172996) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC8D3FCUL /* metadata target: AzuObjectPool.SpawnPooledObj */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ED7CUL /* metadata target: Transform.GetChild */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x0) + (0x48UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC8E2C4UL /* metadata target: FadeOutDecals.InitializeDecal */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DCB4UL /* metadata target: Transform.set_parent */, x0, x1, x2, x3);
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x25 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x32CUL))))))));
        x23 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC901AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC901AC;
        label_0xC901AC:
        ;
        x25 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x1E8UL))));
        x0 = x19;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13173188 = unchecked((ulong)((x8) + (0x18UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13173188)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13173188) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17CED10UL /* metadata target: RaycastHit.get_normal */, x0, x1, x2, x3);
        v0 = v8;
        v1 = v9;
        v2 = v10;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178AE38UL /* metadata target: Quaternion.FromToRotation */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D774UL /* metadata target: Transform.set_rotation */, x0, x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v10 = v0;
        v8 = v1;
        v9 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17CED24UL /* metadata target: RaycastHit.get_transform */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x0;
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DCB4UL /* metadata target: Transform.set_parent */, x0, x1, x2, x3);
        x26 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x1E1UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90258;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x1E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC90258;
        label_0xC90258:
        ;
        x8 = RuntimeMemory.ReadU64(x25);
        x0 = x22;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13173352 = unchecked((ulong)((x8) + (0xCUL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13173352)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13173352) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CED24UL /* metadata target: RaycastHit.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        __arm64_pair_address_13173384 = unchecked((ulong)((sp) + (0x48UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13173384, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13173384) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D774UL /* metadata target: Transform.set_rotation */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x1E1UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC902B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x1E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC902B8;
        label_0xC902B8:
        ;
        x8 = RuntimeMemory.ReadU64(x25);
        x0 = x22;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13173448 = unchecked((ulong)((x8) + (0xCUL)));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13173448)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13173448) + (0x4UL))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x1E1UL))))))));
        v14 = v0;
        v15 = v1;
        v8 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90314;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x1E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC90314;
        label_0xC90314:
        ;
        x8 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13173532 = unchecked((ulong)((x8) + (0xCUL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13173532)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13173532) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
        x8 = 0x432000UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2ECUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13173580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13173580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13173580 >= __arm64_float_flags_right_13173580) || ((__arm64_float_flags_left_13173580 != __arm64_float_flags_left_13173580) || (__arm64_float_flags_right_13173580 != __arm64_float_flags_right_13173580))))
        {
            goto label_0xC903B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x23 = x0;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CED24UL /* metadata target: RaycastHit.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179E9FCUL /* metadata target: Transform.get_root */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x24 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC903A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC903A0;
        label_0xC903A0:
        ;
        x0 = x23;
        x1 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC905C8;
        }
        else
        {
            goto label_0xC903B4;
        }
        label_0xC903B4:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        v12 = v1;
        x0 = x22;
        goto label_0xC90408;
        label_0xC90408:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC90438;
        label_0xC90438:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */, x0, x1, x2, x3);
        x0 = x21;
        x1 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DCB4UL /* metadata target: Transform.set_parent */, x0, x1, x2, x3);
        __arm64_pair_address_13173856 = unchecked((ulong)((sp) + (0x48UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13173856)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13173856) + (0x4UL))))), 0));
        x0 = x21;
        v0 = v10;
        x1 = 0x0UL;
        v1 = v8;
        v2 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9050C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CED04UL /* metadata target: RaycastHit.get_point */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17CED10UL /* metadata target: RaycastHit.get_normal */, x0, x1, x2, x3);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x0 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFBAUL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x46UL))));
        goto label_0xC90574;
        label_0xC904BC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        __arm64_pair_address_13173968 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13173968)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13173968) + (0x8UL))))), 0));
        __arm64_pair_address_13173972 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13173972)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13173972) + (0x8UL))))), 0));
        __arm64_pair_address_13173976 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13173976)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13173976) + (0x8UL))))), 0));
        __arm64_pair_address_13173980 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13173980)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13173980) + (0x8UL))))), 0));
        return unchecked((uint)(x0));
        label_0xC904E4:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8FD88;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF0UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC8FE78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC90508UL)));
        }
        goto label_0xC90700;
        label_0xC9050C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBE800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179012CUL /* metadata target: Random.Range */, x0, x1, x2, x3);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = x21;
        v0 = v3;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CED04UL /* metadata target: RaycastHit.get_point */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x17CED10UL /* metadata target: RaycastHit.get_normal */, x0, x1, x2, x3);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x0 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFCEUL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x32UL))));
        goto label_0xC90574;
        label_0xC90574:
        ;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179016CUL /* metadata target: Random.Range */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        x0 = x21;
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        v4 = v12;
        v5 = v13;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        __arm64_pair_address_13174192 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13174192)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13174192) + (0x8UL))))), 0));
        __arm64_pair_address_13174196 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13174196)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13174196) + (0x8UL))))), 0));
        __arm64_pair_address_13174200 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13174200)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13174200) + (0x8UL))))), 0));
        x1 = 0x0UL;
        __arm64_pair_address_13174208 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13174208)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13174208) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13174208) + (0x90UL)));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0x179E490UL /* metadata target: Transform.RotateAround */)));
        label_0xC905C8:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x1E1UL))))))));
        v8 = v0;
        v14 = v1;
        v15 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9062C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x1E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9062C;
        label_0xC9062C:
        ;
        x8 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13174324 = unchecked((ulong)((x8) + (0xCUL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13174324)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13174324) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13174364 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13174364 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13174364 < __arm64_float_flags_right_13174364))
        {
            goto label_0xC90438;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        v12 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90700;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 != 0x0UL))
        {
            goto label_0xC90408;
        }
        else
        {
            goto label_0xC90700;
        }
        label_0xC90700:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC90704;
        label_0xC90704:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `WeaponEffects.BulletTracers` — RVA `0xc90708`

- Lift status: **partial**; input span: 1224 bytes; span to next metadata RVA: 1224 bytes.
- Metadata signature: `public void BulletTracers(Vector3 direction, Vector3 position, float tracerDist = 0.0, float tracerDistSwim = 0.0, bool isPlayer = true) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=132 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintp' at 0xc90a90; reason: Unsupported instruction 'frintm' at 0xc90a9c; reason: Unsupported instruction 'csel' at 0xc90ab4; reason: Unknown IR expression at 0xc90ab4; reason: Unsupported instruction 'frintp' at 0xc90acc; reason: Unsupported instruction 'frintm' at 0xc90ad8; reason: Unsupported instruction 'csel' at 0xc90af0; reason: Unknown IR expression at 0xc90af0

```csharp
public static ulong WeaponEffects_BulletTracers_RVAc90708(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13175376 = default(double);
        double __arm64_fcvtz_source_13175416 = default(double);
        double __arm64_fcvtz_source_13175464 = default(double);
        double __arm64_fcvtz_source_13175524 = default(double);
        ulong __arm64_flags_left_13175384 = default(ulong);
        ulong __arm64_flags_left_13175424 = default(ulong);
        uint __arm64_flags_left_13175656 = default(uint);
        ulong __arm64_flags_result_13175384 = default(ulong);
        ulong __arm64_flags_result_13175424 = default(ulong);
        ulong __arm64_flags_right_13175384 = default(ulong);
        ulong __arm64_flags_right_13175424 = default(ulong);
        uint __arm64_flags_right_13175656 = default(uint);
        float __arm64_float_flags_left_13175056 = default(float);
        double __arm64_float_flags_left_13175068 = default(double);
        float __arm64_float_flags_left_13175316 = default(float);
        double __arm64_float_flags_left_13175328 = default(double);
        double __arm64_float_flags_left_13175360 = default(double);
        double __arm64_float_flags_left_13175400 = default(double);
        double __arm64_float_flags_left_13175468 = default(double);
        double __arm64_float_flags_left_13175528 = default(double);
        float __arm64_float_flags_right_13175056 = default(float);
        double __arm64_float_flags_right_13175068 = default(double);
        float __arm64_float_flags_right_13175316 = default(float);
        double __arm64_float_flags_right_13175328 = default(double);
        double __arm64_float_flags_right_13175360 = default(double);
        double __arm64_float_flags_right_13175400 = default(double);
        double __arm64_float_flags_right_13175468 = default(double);
        double __arm64_float_flags_right_13175528 = default(double);
        ulong __arm64_pair_address_13174540 = default(ulong);
        ulong __arm64_pair_address_13174544 = default(ulong);
        ulong __arm64_pair_address_13174548 = default(ulong);
        ulong __arm64_pair_address_13174552 = default(ulong);
        ulong __arm64_pair_address_13174640 = default(ulong);
        ulong __arm64_pair_address_13174888 = default(ulong);
        ulong __arm64_pair_address_13174972 = default(ulong);
        ulong __arm64_pair_address_13175232 = default(ulong);
        ulong __arm64_pair_address_13175640 = default(ulong);
        ulong __arm64_pair_address_13175728 = default(ulong);
        ulong __arm64_pair_address_13175732 = default(ulong);
        ulong __arm64_pair_address_13175736 = default(ulong);
        ulong __arm64_pair_address_13175740 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        __arm64_pair_address_13174540 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13174540, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13174540) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13174544 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13174544, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13174544) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13174548 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13174548, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13174548) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13174552 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13174552, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13174552) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x44BUL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        v14 = v7;
        v15 = v6;
        v11 = v5;
        v13 = v4;
        v12 = v3;
        v8 = v2;
        v9 = v1;
        v10 = v0;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9076C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x44BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC9076C;
        label_0xC9076C:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13174640 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13174640, v0);
#else
        __WriteVector128(__arm64_pair_address_13174640, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13174640) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13174640) + (0x10UL))), v0);
#endif
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x28UL))), 0x0UL);
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90794;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0xAAUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90A34;
        }
        else
        {
            goto label_0xC90794;
        }
        label_0xC90794:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        goto label_0xC90798;
        label_0xC90798:
        ;
        x0 = unchecked((ulong)((x19) + (0x190UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x190UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x256UL))))))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC907D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC907CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC907D0;
        label_0xC907D0:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90BA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC907F4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x3E3UL))))))));
        x20 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90848;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x3E3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC90848;
        label_0xC90848:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        v3 = v10;
        v4 = v9;
        v5 = v8;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13174888 = unchecked((ulong)((x8) + (0x48UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13174888)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13174888) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x50UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x178AE38UL /* metadata target: Quaternion.FromToRotation */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D774UL /* metadata target: Transform.set_rotation */, x0, x1, x2, x3);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13174972 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13174972, v0);
#else
        __WriteVector128(__arm64_pair_address_13174972, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13174972) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13174972) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x242UL))))))));
        v8 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC908E8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC908E8;
        label_0xC908E8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90900;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC908FCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC90900;
        label_0xC90900:
        ;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13175056 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13175056 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13175056 >= __arm64_float_flags_right_13175056))
        {
            goto label_0xC90A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90918UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13175068 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13175068 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13175068 != __arm64_float_flags_right_13175068) || ((__arm64_float_flags_left_13175068 != __arm64_float_flags_left_13175068) || (__arm64_float_flags_right_13175068 != __arm64_float_flags_right_13175068))))
        {
            goto label_0xC90A8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90924UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC90A50;
        label_0xC90930:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)(unchecked((uint)(x8)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90944;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90940UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC90944;
        label_0xC90944:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90BA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90968UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13175232 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13175232, v0);
#else
        __WriteVector128(__arm64_pair_address_13175232, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13175232) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13175232) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x242UL))))))));
        v11 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC909EC;
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
        goto label_0xC909EC;
        label_0xC909EC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90A04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90A00UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC90A04;
        label_0xC90A04:
        ;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v12;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13175316 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13175316 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13175316 >= __arm64_float_flags_right_13175316))
        {
            goto label_0xC90A64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90A1CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13175328 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13175328 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13175328 != __arm64_float_flags_right_13175328) || ((__arm64_float_flags_left_13175328 != __arm64_float_flags_left_13175328) || (__arm64_float_flags_right_13175328 != __arm64_float_flags_right_13175328))))
        {
            goto label_0xC90AC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90A28UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC90A78;
        label_0xC90A34:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        goto label_0xC90798;
        label_0xC90A3C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13175360 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13175360 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13175360 != __arm64_float_flags_right_13175360) || ((__arm64_float_flags_left_13175360 != __arm64_float_flags_left_13175360) || (__arm64_float_flags_right_13175360 != __arm64_float_flags_right_13175360))))
        {
            goto label_0xC90A98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90A48UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC90A50;
        label_0xC90A50:
        ;
        __arm64_fcvtz_source_13175376 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13175376 != __arm64_fcvtz_source_13175376) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13175376 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13175376 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13175376)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13175384 = x8;
        __arm64_flags_right_13175384 = 0x1UL;
        __arm64_flags_result_13175384 = unchecked((ulong)((__arm64_flags_left_13175384) & (__arm64_flags_right_13175384)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13175384 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC90AA0;
        label_0xC90A64:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13175400 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13175400 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13175400 != __arm64_float_flags_right_13175400) || ((__arm64_float_flags_left_13175400 != __arm64_float_flags_left_13175400) || (__arm64_float_flags_right_13175400 != __arm64_float_flags_right_13175400))))
        {
            goto label_0xC90AD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90A70UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC90A78;
        label_0xC90A78:
        ;
        __arm64_fcvtz_source_13175416 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13175416 != __arm64_fcvtz_source_13175416) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13175416 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13175416 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13175416)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13175424 = x8;
        __arm64_flags_right_13175424 = 0x1UL;
        __arm64_flags_result_13175424 = unchecked((ulong)((__arm64_flags_left_13175424) & (__arm64_flags_right_13175424)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13175424 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC90ADC;
        label_0xC90A8C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC90A90UL);
        goto label_0xC90AA0;
        label_0xC90A98:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC90A9CUL);
        goto label_0xC90AA0;
        label_0xC90AA0:
        ;
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13175464 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13175464 != __arm64_fcvtz_source_13175464) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13175464 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13175464 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13175464)))))))));
        __arm64_float_flags_left_13175468 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13175468 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC90AB4UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC90BA8;
        label_0xC90AC8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC90ACCUL);
        goto label_0xC90ADC;
        label_0xC90AD4:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC90AD8UL);
        goto label_0xC90ADC;
        label_0xC90ADC:
        ;
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13175524 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13175524 != __arm64_fcvtz_source_13175524) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13175524 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13175524 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13175524)))))))));
        __arm64_float_flags_left_13175528 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13175528 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC90AF0UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x198UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C99D8UL /* metadata target: ParticleSystem.GetParticles */, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x198UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x1A4UL))), unchecked((uint)(x0)));
        if ((x21 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9580UL /* metadata target: ParticleSystem.get_main */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x0);
        x8 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = unchecked((ulong)((sp) + (0x28UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9D80UL /* metadata target: ParticleSystem.MainModule.get_startSpeed */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x8UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13175640 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13175640, v0);
#else
        __WriteVector128(__arm64_pair_address_13175640, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13175640) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13175640) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13175656 = unchecked((uint)(x8));
        __arm64_flags_right_13175656 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13175656 >= __arm64_flags_right_13175656))
        {
            goto label_0xC90BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x84UL))));
        RuntimeCalls.Unsupported("smaddl", 0xC90B74UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x20UL)))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9414UL /* metadata target: ParticleSystem.Particle.set_velocity */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC90BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x1A4UL))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x198UL))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C98CCUL /* metadata target: ParticleSystem.SetParticles */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90BA8;
        label_0xC90BA8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        __arm64_pair_address_13175728 = unchecked((ulong)((sp) + (0x90UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13175728)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13175728) + (0x8UL))))), 0));
        __arm64_pair_address_13175732 = unchecked((ulong)((sp) + (0x80UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13175732)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13175732) + (0x8UL))))), 0));
        __arm64_pair_address_13175736 = unchecked((ulong)((sp) + (0x70UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13175736)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13175736) + (0x8UL))))), 0));
        __arm64_pair_address_13175740 = unchecked((ulong)((sp) + (0x60UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13175740)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13175740) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return x0;
        label_0xC90BC8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90BCC;
        label_0xC90BCC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `WeaponEffects.ExplosionEffect` — RVA `0xc90bd0`

- Lift status: **partial**; input span: 1312 bytes; span to next metadata RVA: 1312 bytes.
- Metadata signature: `public void ExplosionEffect(Vector3 position) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=181 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc90d34; reason: Unknown IR expression at 0xc90d34; reason: Unsupported instruction 'b.ne' at 0xc90d90; reason: Unknown IR expression at 0xc90d90; reason: Unsupported instruction 'frintp' at 0xc90efc; reason: Unsupported instruction 'frintm' at 0xc90f08; reason: Unsupported instruction 'csel' at 0xc90f1c; reason: Unknown IR expression at 0xc90f1c

```csharp
public static ulong WeaponEffects_ExplosionEffect_RVAc90bd0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13176524 = default(double);
        double __arm64_fcvtz_source_13176548 = default(double);
        double __arm64_fcvtz_source_13176592 = default(double);
        ulong __arm64_flags_left_13176100 = default(ulong);
        ulong __arm64_flags_left_13176108 = default(ulong);
        ulong __arm64_flags_left_13176192 = default(ulong);
        ulong __arm64_flags_left_13176200 = default(ulong);
        uint __arm64_flags_left_13176280 = default(uint);
        ulong __arm64_flags_left_13176300 = default(ulong);
        ulong __arm64_flags_left_13176556 = default(ulong);
        ulong __arm64_flags_left_13176684 = default(ulong);
        ulong __arm64_flags_left_13176692 = default(ulong);
        uint __arm64_flags_left_13176884 = default(uint);
        ulong __arm64_flags_left_13176988 = default(ulong);
        ulong __arm64_flags_left_13176996 = default(ulong);
        ulong __arm64_flags_result_13176108 = default(ulong);
        ulong __arm64_flags_result_13176200 = default(ulong);
        ulong __arm64_flags_result_13176556 = default(ulong);
        ulong __arm64_flags_result_13176692 = default(ulong);
        ulong __arm64_flags_result_13176996 = default(ulong);
        ulong __arm64_flags_right_13176100 = default(ulong);
        ulong __arm64_flags_right_13176108 = default(ulong);
        ulong __arm64_flags_right_13176192 = default(ulong);
        ulong __arm64_flags_right_13176200 = default(ulong);
        uint __arm64_flags_right_13176280 = default(uint);
        ulong __arm64_flags_right_13176300 = default(ulong);
        ulong __arm64_flags_right_13176556 = default(ulong);
        ulong __arm64_flags_right_13176684 = default(ulong);
        ulong __arm64_flags_right_13176692 = default(ulong);
        uint __arm64_flags_right_13176884 = default(uint);
        ulong __arm64_flags_right_13176988 = default(ulong);
        ulong __arm64_flags_right_13176996 = default(ulong);
        float __arm64_float_flags_left_13176504 = default(float);
        double __arm64_float_flags_left_13176512 = default(double);
        double __arm64_float_flags_left_13176536 = default(double);
        double __arm64_float_flags_left_13176596 = default(double);
        float __arm64_float_flags_right_13176504 = default(float);
        double __arm64_float_flags_right_13176512 = default(double);
        double __arm64_float_flags_right_13176536 = default(double);
        double __arm64_float_flags_right_13176596 = default(double);
        ulong __arm64_pair_address_13175764 = default(ulong);
        ulong __arm64_pair_address_13175768 = default(ulong);
        ulong __arm64_pair_address_13175772 = default(ulong);
        ulong __arm64_pair_address_13175904 = default(ulong);
        ulong __arm64_pair_address_13176424 = default(ulong);
        ulong __arm64_pair_address_13176428 = default(ulong);
        ulong __arm64_pair_address_13176772 = default(ulong);
        ulong __arm64_pair_address_13176776 = default(ulong);
        ulong __arm64_pair_address_13176780 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        __arm64_pair_address_13175764 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13175764, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13175764) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13175768 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13175768, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13175768) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13175772 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13175772, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13175772) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
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
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x44CUL))))))));
        v8 = v2;
        v9 = v1;
        v10 = v0;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
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
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x44CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC90C58;
        label_0xC90C58:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x48UL))), 0x0UL);
        __arm64_pair_address_13175904 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13175904, v0);
#else
        __WriteVector128(__arm64_pair_address_13175904, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13175904) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13175904) + (0x10UL))), v0);
#endif
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        x19 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x80UL))), x1);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ECD4UL /* metadata target: Transform.GetEnumerator */, x0, x1, x2, x3);
        x19 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC90FEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1A8C000UL;
        x26 = 0x1A8D000UL;
        x27 = 0x1A8E000UL;
        x28 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xED0UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xE68UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xA8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA60UL))));
        x20 = unchecked((ulong)((x20) + (0x188UL)));
        x24 = 0x1BAB000UL;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        x29 = 0x7FF0000000000000UL;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC90D08;
        label_0xC90D08:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x25);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90D38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC90D20;
        label_0xC90D20:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13176100 = x11;
        __arm64_flags_right_13176100 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13176100) - (__arm64_flags_right_13176100))) == 0x0UL))
        {
            goto label_0xC90D48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90D2CUL);
        }
        __arm64_flags_left_13176108 = x9;
        __arm64_flags_right_13176108 = 0x1UL;
        __arm64_flags_result_13176108 = unchecked((ulong)((__arm64_flags_left_13176108) - (__arm64_flags_right_13176108)));
        x9 = __arm64_flags_result_13176108;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC90D34UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC90D20;
        }
        else
        {
            goto label_0xC90D38;
        }
        label_0xC90D38:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90D54;
        label_0xC90D48:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC90D54;
        label_0xC90D54:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90F30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x25);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90D94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC90D7C;
        label_0xC90D7C:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13176192 = x11;
        __arm64_flags_right_13176192 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13176192) - (__arm64_flags_right_13176192))) == 0x0UL))
        {
            goto label_0xC90DA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90D88UL);
        }
        __arm64_flags_left_13176200 = x9;
        __arm64_flags_right_13176200 = 0x1UL;
        __arm64_flags_result_13176200 = unchecked((ulong)((__arm64_flags_left_13176200) - (__arm64_flags_right_13176200)));
        x9 = __arm64_flags_result_13176200;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC90D90UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC90D7C;
        }
        else
        {
            goto label_0xC90D94;
        }
        label_0xC90D94:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90DB4;
        label_0xC90DA4:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC90DB4;
        label_0xC90DB4:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x22 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC90FE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = RuntimeMemory.ReadU64(x26);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_13176280 = unchecked((uint)(x10));
        __arm64_flags_right_13176280 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_13176280 >= __arm64_flags_right_13176280))))
        {
            goto label_0xC90FD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13176300 = x8;
        __arm64_flags_right_13176300 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13176300) - (__arm64_flags_right_13176300))) == 0x0UL))))
        {
            goto label_0xC90FD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x23 = x0;
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90E14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90E10UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90E14;
        label_0xC90E14:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90D08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x20, x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x22 = RuntimeMemory.ReadU64(x20);
        if ((x22 == 0x0UL))
        {
            goto label_0xC90FE4;
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
        __arm64_pair_address_13176424 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13176424);
#else
        v0 = __ReadVector128(__arm64_pair_address_13176424);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13176424) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13176424) + (0x10UL))));
#endif
        __arm64_pair_address_13176428 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13176428, v0);
#else
        __WriteVector128(__arm64_pair_address_13176428, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13176428) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13176428) + (0x10UL))), v1);
#endif
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x242UL))))))));
        v8 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90E98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC90E98;
        label_0xC90E98:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC90EA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90EA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90EA8;
        label_0xC90EA8:
        ;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = sp;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_float_flags_left_13176504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13176504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13176504 >= __arm64_float_flags_right_13176504))
        {
            goto label_0xC90ED8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90EC0UL);
        }
        __arm64_float_flags_left_13176512 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13176512 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0))));
        if (((__arm64_float_flags_left_13176512 != __arm64_float_flags_right_13176512) || ((__arm64_float_flags_left_13176512 != __arm64_float_flags_left_13176512) || (__arm64_float_flags_right_13176512 != __arm64_float_flags_right_13176512))))
        {
            goto label_0xC90EF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90EC8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        __arm64_fcvtz_source_13176524 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13176524 != __arm64_fcvtz_source_13176524) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13176524 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13176524 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13176524)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))))))), 0));
        goto label_0xC90EEC;
        label_0xC90ED8:
        ;
        __arm64_float_flags_left_13176536 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13176536 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0))));
        if (((__arm64_float_flags_left_13176536 != __arm64_float_flags_right_13176536) || ((__arm64_float_flags_left_13176536 != __arm64_float_flags_left_13176536) || (__arm64_float_flags_right_13176536 != __arm64_float_flags_right_13176536))))
        {
            goto label_0xC90F04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90EE0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        __arm64_fcvtz_source_13176548 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13176548 != __arm64_fcvtz_source_13176548) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13176548 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13176548 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13176548)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))))))), 0));
        goto label_0xC90EEC;
        label_0xC90EEC:
        ;
        __arm64_flags_left_13176556 = x8;
        __arm64_flags_right_13176556 = 0x1UL;
        __arm64_flags_result_13176556 = unchecked((ulong)((__arm64_flags_left_13176556) & (__arm64_flags_right_13176556)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13176556 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC90F0C;
        label_0xC90EF8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC90EFCUL);
        goto label_0xC90F0C;
        label_0xC90F04:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC90F08UL);
        goto label_0xC90F0C;
        label_0xC90F0C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x29)))), 0));
        __arm64_fcvtz_source_13176592 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13176592 != __arm64_fcvtz_source_13176592) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13176592 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13176592 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13176592)))))))));
        __arm64_float_flags_left_13176596 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13176596 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC90F1CUL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC90D08;
        label_0xC90F30:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xEC8UL))));
        x20 = 0x0UL;
        goto label_0xC90F3C;
        label_0xC90F3C:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC90FA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x22);
        x19 = x0;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC90F80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC90F68;
        label_0xC90F68:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13176684 = x11;
        __arm64_flags_right_13176684 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13176684) - (__arm64_flags_right_13176684))) == 0x0UL))
        {
            goto label_0xC90F90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC90F74UL);
        }
        __arm64_flags_left_13176692 = x9;
        __arm64_flags_right_13176692 = 0x1UL;
        __arm64_flags_result_13176692 = unchecked((ulong)((__arm64_flags_left_13176692) - (__arm64_flags_right_13176692)));
        x9 = __arm64_flags_result_13176692;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC90F7CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC90F68;
        }
        else
        {
            goto label_0xC90F80;
        }
        label_0xC90F80:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90F9C;
        label_0xC90F90:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC90F9C;
        label_0xC90F9C:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90FA8;
        label_0xC90FA8:
        ;
        if ((x20 != 0x0UL))
        {
            goto label_0xC90FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
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
        __arm64_pair_address_13176772 = unchecked((ulong)((sp) + (0x70UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13176772)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13176772) + (0x8UL))))), 0));
        __arm64_pair_address_13176776 = unchecked((ulong)((sp) + (0x60UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13176776)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13176776) + (0x8UL))))), 0));
        __arm64_pair_address_13176780 = unchecked((ulong)((sp) + (0x50UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13176780)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13176780) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xE0UL)));
        return x0;
        label_0xC90FD8:
        ;
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90FE0;
        label_0xC90FE0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90FE4;
        label_0xC90FE4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90FE8;
        label_0xC90FE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90FEC;
        label_0xC90FEC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90FF0;
        label_0xC90FF0:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC91028;
        label_0xC91028:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xEC8UL))));
        x21 = x0;
        __arm64_flags_left_13176884 = unchecked((uint)(x1));
        __arm64_flags_right_13176884 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13176884) - (__arm64_flags_right_13176884))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC91050;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC90F3C;
        label_0xC91050:
        ;
        x20 = 0x0UL;
        goto label_0xC9105C;
        label_0xC9105C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xEC8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x19 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC910D8;
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
            goto label_0xC910B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC91098;
        label_0xC91098:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13176988 = x11;
        __arm64_flags_right_13176988 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13176988) - (__arm64_flags_right_13176988))) == 0x0UL))
        {
            goto label_0xC910C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC910A4UL);
        }
        __arm64_flags_left_13176996 = x9;
        __arm64_flags_right_13176996 = 0x1UL;
        __arm64_flags_result_13176996 = unchecked((ulong)((__arm64_flags_left_13176996) - (__arm64_flags_right_13176996)));
        x9 = __arm64_flags_result_13176996;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC910ACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC91098;
        }
        else
        {
            goto label_0xC910B0;
        }
        label_0xC910B0:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC910CC;
        label_0xC910C0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC910CC;
        label_0xC910CC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC910D8;
        label_0xC910D8:
        ;
        if ((x20 != 0x0UL))
        {
            goto label_0xC910E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC910E4;
        label_0xC910E4:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `WeaponEffects.ctor` — RVA `0xc910f0`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong WeaponEffects_ctor_RVAc910f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x180UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
