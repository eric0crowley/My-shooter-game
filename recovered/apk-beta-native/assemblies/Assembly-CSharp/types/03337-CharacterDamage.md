# `CharacterDamage` — TypeDefIndex 3337

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `bl_MiniMapItem` | `minimapitem` |
| `0x28` | `UnityEvent` | `onDie` |
| `0x30` | `AI` | `AIComponent` |
| `0x38` | `RemoveBody` | `RemoveBodyComponent` |
| `0x40` | `float` | `hitPoints` |
| `0x44` | `float` | `initialHitPoints` |
| `0x48` | `float` | `attackForce` |
| `0x50` | `GameObject` | `gunItem` |
| `0x58` | `Transform` | `gunObj` |
| `0x60` | `GameObject` | `gunInst` |
| `0x68` | `Vector3` | `gunItemRotation` |
| `0x78` | `Rigidbody[]` | `bodies` |
| `0x80` | `bool` | `ragdollActive` |
| `0x81` | `bool` | `ragdollState` |
| `0x88` | `Transform` | `deadReplacement` |
| `0x90` | `Transform` | `dead` |
| `0x98` | `AudioClip` | `dieSound` |
| `0xA0` | `bool` | `notParent` |
| `0xA1` | `bool` | `removeBody` |
| `0xA4` | `float` | `bodyStayTime` |
| `0xA8` | `float` | `gunStayTime` |
| `0xAC` | `float` | `sloMoDeathChance` |
| `0xB0` | `bool` | `sloMoBackstab` |
| `0xB4` | `float` | `sloMoDeathTime` |
| `0xB8` | `float` | `sloMoBackstabTime` |
| `0xBC` | `Vector3` | `attackerPos2` |
| `0xC8` | `Vector3` | `attackDir2` |
| `0xD8` | `Transform` | `myTransform` |
| `0xE0` | `bool` | `explosionCheck` |
| `0xE4` | `LayerMask` | `raymask` |
| `0xE8` | `Image` | `HealthBar` |
| `0xF0` | `GameObject` | `ShowMe` |

## `CharacterDamage.OnEnable` — RVA `0xc8248c`

- Lift status: **exact**; input span: 368 bytes; span to next metadata RVA: 368 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=56 (informational only).

```csharp
public static ulong CharacterDamage_OnEnable_RVAc8248c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x406UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xDE0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC824E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x406UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC824E8;
        label_0xC824E8:
        ;
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xD8UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x38UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x69UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82570;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x22 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8254C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82548UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8254C;
        label_0xC8254C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82570;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC825F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC82570;
        label_0xC82570:
        ;
        x21 = x19;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x30UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82588;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82584UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC82588;
        label_0xC82588:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC825C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC825F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDE8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x21, x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC825C0;
        label_0xC825C0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x40UL))))), 0));
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDF0UL))));
        x0 = x19;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x44UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE32400UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x78UL))), x0);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC825F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `CharacterDamage.Start` — RVA `0xc825fc`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=24 (informational only).

```csharp
public static ulong CharacterDamage_Start_RVAc825fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x21 = 0x1A8D000UL;
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x407UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xDF8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE00UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82648;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x407UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC82648;
        label_0xC82648:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x19);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x1);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `CharacterDamage.Update` — RVA `0xc8268c`

- Lift status: **partial**; input span: 1420 bytes; span to next metadata RVA: 1420 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=195 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc82778; reason: Unsupported instruction 'b.hs' at 0xc8277c; reason: Unknown IR expression at 0xc8277c; reason: Unsupported instruction 'cmp' at 0xc827ec; reason: Unsupported instruction 'b.lt' at 0xc827f0; reason: Unknown IR expression at 0xc827f0; reason: Unsupported instruction 'cmp' at 0xc82954; reason: Unsupported instruction 'b.hs' at 0xc82958

```csharp
public static ulong CharacterDamage_Update_RVAc8268c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13117204 = default(uint);
        uint __arm64_flags_left_13117276 = default(uint);
        uint __arm64_flags_left_13117440 = default(uint);
        uint __arm64_flags_left_13117452 = default(uint);
        uint __arm64_flags_left_13117492 = default(uint);
        uint __arm64_flags_left_13117744 = default(uint);
        uint __arm64_flags_left_13118212 = default(uint);
        uint __arm64_flags_left_13118248 = default(uint);
        uint __arm64_flags_right_13117204 = default(uint);
        uint __arm64_flags_right_13117276 = default(uint);
        uint __arm64_flags_right_13117440 = default(uint);
        uint __arm64_flags_right_13117452 = default(uint);
        uint __arm64_flags_right_13117492 = default(uint);
        uint __arm64_flags_right_13117744 = default(uint);
        uint __arm64_flags_right_13118212 = default(uint);
        uint __arm64_flags_right_13118248 = default(uint);
        float __arm64_float_flags_left_13118044 = default(float);
        float __arm64_float_flags_right_13118044 = default(float);
        ulong __arm64_load_address_13118472 = default(ulong);
        ulong __arm64_pair_address_13117072 = default(ulong);
        ulong __arm64_pair_address_13117076 = default(ulong);
        ulong __arm64_pair_address_13117080 = default(ulong);
        ulong __arm64_pair_address_13117888 = default(ulong);
        ulong __arm64_pair_address_13118460 = default(ulong);
        ulong __arm64_pair_address_13118464 = default(ulong);
        ulong __arm64_pair_address_13118468 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF70UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF70UL)));
        __arm64_pair_address_13117072 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13117072, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13117072) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13117076 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13117076, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13117076) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13117080 = unchecked((ulong)((sp) + (0x28UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13117080, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13117080) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x38UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x408UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82708;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x9C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x408UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC82708;
        label_0xC82708:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13117204 = unchecked((uint)(x8));
        __arm64_flags_right_13117204 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117204) - (__arm64_flags_right_13117204))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13117204)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13117204)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117204) - (__arm64_flags_right_13117204))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13117204)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC82BE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x80UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x81UL))))))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82AF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82728UL);
        }
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82BE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        __arm64_flags_left_13117276 = unchecked((uint)(x8));
        __arm64_flags_right_13117276 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117276) - (__arm64_flags_right_13117276))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13117276)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13117276)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117276) - (__arm64_flags_right_13117276))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13117276)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC827F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1A8D000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x4A8UL))));
        x23 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x24 = unchecked((ulong)((x22) + (0x20UL)));
        goto label_0xC82778;
        label_0xC82778:
        ;
        RuntimeCalls.Unsupported("cmp", 0xC82778UL);
        RuntimeCalls.Unsupported("b.hs", 0xC8277CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC82C14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (x23))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D50UL /* metadata target: GameObject.get_activeInHierarchy */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC827E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x25);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x238UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC827D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC827CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC827D0;
        label_0xC827D0:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x1 = x21;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CB368UL /* metadata target: Physics.IgnoreCollision */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC827E4;
        label_0xC827E4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xC827ECUL);
        RuntimeCalls.Unsupported("b.lt", 0xC827F0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC82778;
        }
        else
        {
            goto label_0xC827F4;
        }
        label_0xC827F4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13117440 = unchecked((uint)(x8));
        __arm64_flags_right_13117440 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117440) - (__arm64_flags_right_13117440))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13117440)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13117440)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117440) - (__arm64_flags_right_13117440))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13117440)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC8283C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC8280C;
        label_0xC8280C:
        ;
        __arm64_flags_left_13117452 = unchecked((uint)(x21));
        __arm64_flags_right_13117452 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13117452 >= __arm64_flags_right_13117452))
        {
            goto label_0xC82C14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF2D0UL /* metadata target: Rigidbody.set_isKinematic */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13117492 = unchecked((uint)(x21));
        __arm64_flags_right_13117492 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117492) - (__arm64_flags_right_13117492))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13117492)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13117492)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117492) - (__arm64_flags_right_13117492))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13117492)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC8280C;
        }
        else
        {
            goto label_0xC8283C;
        }
        label_0xC8283C:
        ;
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82858;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82854UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC82858;
        label_0xC82858:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82AF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v14 = v3;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC828D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC828D4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC828D8;
        label_0xC828D8:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x9C8UL))));
        x0 = x20;
        v0 = v8;
        v1 = v9;
        x1 = RuntimeMemory.ReadU64(x8);
        v2 = v10;
        v3 = v11;
        v4 = v12;
        v5 = v13;
        v6 = v14;
        x0 = RuntimeCalls.InvokeDirect(0xD2A1ACUL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x60UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFD0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        if ((x24 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x18UL))));
        __arm64_flags_left_13117744 = unchecked((uint)(x8));
        __arm64_flags_right_13117744 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117744) - (__arm64_flags_right_13117744))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13117744)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13117744)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13117744) - (__arm64_flags_right_13117744))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13117744)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC829AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = 0x1A8D000UL;
        x28 = 0x1A8D000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xE08UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0x4A8UL))));
        x25 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x26 = unchecked((ulong)((x24) + (0x20UL)));
        goto label_0xC82954;
        label_0xC82954:
        ;
        RuntimeCalls.Unsupported("cmp", 0xC82954UL);
        RuntimeCalls.Unsupported("b.hs", 0xC82958UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC82C14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (x25))));
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82988;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC82988;
        label_0xC82988:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x1 = x22;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CB368UL /* metadata target: Physics.IgnoreCollision */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x24) + (0x18UL))))));
        x25 = unchecked((ulong)((x25) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xC829A4UL);
        RuntimeCalls.Unsupported("b.lt", 0xC829A8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC82954;
        }
        else
        {
            goto label_0xC829AC;
        }
        label_0xC829AC:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC829C0UL);
        }
        __arm64_pair_address_13117888 = unchecked((ulong)((x19) + (0x6CUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13117888)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13117888) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x68UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179E310UL /* metadata target: Transform.Rotate */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D9B8UL /* metadata target: Transform.get_forward */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3C8UL))))), 0));
        x1 = 0x0UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xA8UL))))), 0));
        __arm64_float_flags_left_13118044 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13118044 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13118044 <= __arm64_float_flags_right_13118044) || ((__arm64_float_flags_left_13118044 != __arm64_float_flags_left_13118044) || (__arm64_float_flags_right_13118044 != __arm64_float_flags_right_13118044))))
        {
            goto label_0xC82AF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE10UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82A94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC82A94;
        label_0xC82A94:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82AF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x20 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82AD0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xA8UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC94694UL /* metadata target: WeaponPickup.DestroyWeapon */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        goto label_0xC82AF0;
        label_0xC82AF0:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x81UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC82BE4;
        label_0xC82AF8:
        ;
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82BE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x0UL;
        x22 = unchecked((ulong)((x20) + (0x20UL)));
        goto label_0xC82B04;
        label_0xC82B04:
        ;
        __arm64_flags_left_13118212 = unchecked((uint)(x21));
        __arm64_flags_right_13118212 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13118212 >= __arm64_flags_right_13118212))
        {
            goto label_0xC82C14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (x21))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF2D0UL /* metadata target: Rigidbody.set_isKinematic */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        __arm64_flags_left_13118248 = unchecked((uint)(x21));
        __arm64_flags_right_13118248 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13118248) - (__arm64_flags_right_13118248))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13118248)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13118248)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13118248) - (__arm64_flags_right_13118248))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13118248)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC82B04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82B68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82B64UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC82B68;
        label_0xC82B68:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82BDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC82C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82BAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82BA8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC82BAC;
        label_0xC82BAC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82BDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82BD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82BCCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC82BD0;
        label_0xC82BD0:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798A20UL /* metadata target: Object.Destroy */, x0, x1, x2, x3);
        goto label_0xC82BDC;
        label_0xC82BDC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x81UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC82BE4;
        label_0xC82BE4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        __arm64_pair_address_13118460 = unchecked((ulong)((sp) + (0x28UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13118460)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13118460) + (0x8UL))))), 0));
        __arm64_pair_address_13118464 = unchecked((ulong)((sp) + (0x18UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13118464)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13118464) + (0x8UL))))), 0));
        __arm64_pair_address_13118468 = unchecked((ulong)((sp) + (0x8UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13118468)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13118468) + (0x8UL))))), 0));
        __arm64_load_address_13118472 = sp;
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13118472)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13118472) + (0x90UL)));
        return x0;
        label_0xC82C10:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC82C14;
        label_0xC82C14:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `CharacterDamage.ApplyDamage` — RVA `0xc82c18`

- Lift status: **partial**; input span: 1672 bytes; span to next metadata RVA: 1672 bytes.
- Metadata signature: `public void ApplyDamage(float damage, Vector3 attackDir, Vector3 attackerPos, Transform attacker, bool isPlayer, bool isExplosion, Rigidbody hitBody, float bodyForce = 0.0) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=209 (informational only).
- Lift diagnostics: reason: Unsupported packed operation '+' at 0x0

```csharp
public static ulong CharacterDamage_ApplyDamage_RVAc82c18(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13118940 = default(uint);
        uint __arm64_flags_left_13119380 = default(uint);
        uint __arm64_flags_left_13119584 = default(uint);
        uint __arm64_flags_left_13119640 = default(uint);
        uint __arm64_flags_left_13119776 = default(uint);
        uint __arm64_flags_left_13120016 = default(uint);
        uint __arm64_flags_right_13118940 = default(uint);
        uint __arm64_flags_right_13119380 = default(uint);
        uint __arm64_flags_right_13119584 = default(uint);
        uint __arm64_flags_right_13119640 = default(uint);
        uint __arm64_flags_right_13119776 = default(uint);
        uint __arm64_flags_right_13120016 = default(uint);
        float __arm64_float_flags_left_13118656 = default(float);
        float __arm64_float_flags_left_13118704 = default(float);
        float __arm64_float_flags_left_13119040 = default(float);
        float __arm64_float_flags_left_13119084 = default(float);
        float __arm64_float_flags_left_13119312 = default(float);
        float __arm64_float_flags_left_13119352 = default(float);
        float __arm64_float_flags_left_13119504 = default(float);
        float __arm64_float_flags_left_13119936 = default(float);
        float __arm64_float_flags_right_13118656 = default(float);
        float __arm64_float_flags_right_13118704 = default(float);
        float __arm64_float_flags_right_13119040 = default(float);
        float __arm64_float_flags_right_13119084 = default(float);
        float __arm64_float_flags_right_13119312 = default(float);
        float __arm64_float_flags_right_13119352 = default(float);
        float __arm64_float_flags_right_13119504 = default(float);
        float __arm64_float_flags_right_13119936 = default(float);
        ulong __arm64_pair_address_13118488 = default(ulong);
        ulong __arm64_pair_address_13118492 = default(ulong);
        ulong __arm64_pair_address_13118496 = default(ulong);
        ulong __arm64_pair_address_13118500 = default(ulong);
        ulong __arm64_pair_address_13119196 = default(ulong);
        ulong __arm64_pair_address_13119200 = default(ulong);
        ulong __arm64_pair_address_13119204 = default(ulong);
        ulong __arm64_pair_address_13120048 = default(ulong);
        ulong __arm64_pair_address_13120052 = default(ulong);
        ulong __arm64_pair_address_13120056 = default(ulong);
        ulong __arm64_pair_address_13120060 = default(ulong);
        ulong __arm64_pair_address_13120088 = default(ulong);
        ulong __arm64_pair_address_13120092 = default(ulong);
        ulong __arm64_pair_address_13120096 = default(ulong);
        ulong __arm64_pair_address_13120100 = default(ulong);
        ulong __arm64_pair_address_13120136 = default(ulong);
        ulong __arm64_pair_address_13120140 = default(ulong);
        ulong __arm64_pair_address_13120144 = default(ulong);
        ulong __arm64_pair_address_13120148 = default(ulong);
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
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13118488 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13118488, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13118488) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_13118488;
        __arm64_pair_address_13118492 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13118492, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13118492) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13118496 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13118496, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13118496) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13118500 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13118500, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13118500) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x24 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x409UL))))))));
        v8 = v7;
        x19 = x4;
        x22 = unchecked((ulong)(unchecked((uint)(x3))));
        x21 = unchecked((ulong)(unchecked((uint)(x2))));
        x23 = x1;
        v9 = v6;
        v10 = v5;
        v12 = v4;
        v13 = v3;
        v14 = v2;
        v11 = v1;
        v15 = v0;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82CBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x409UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC82CBC;
        label_0xC82CBC:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        __arm64_float_flags_left_13118656 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13118656 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13118656 <= __arm64_float_flags_right_13118656))
        {
            goto label_0xC83220;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x296UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x114UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82CE0UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x44UL))))), 0));
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x440UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13118704 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13118704 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13118704 >= __arm64_float_flags_right_13118704) || ((__arm64_float_flags_left_13118704 != __arm64_float_flags_left_13118704) || (__arm64_float_flags_right_13118704 != __arm64_float_flags_right_13118704))))
        {
            goto label_0xC82E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82D10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82D0CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC82D10;
        label_0xC82D10:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82D20UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82D24UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82DB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x23 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0xF4UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x1 = x0;
        x0 = unchecked((ulong)((x23) + (0x238UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0x238UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x23 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x238UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CFDF0UL /* metadata target: CapsuleCollider.get_height */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3E800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x23) + (0x27CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82D8CUL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x88UL))), 0x0UL);
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x6DUL))), unchecked((byte)(unchecked((uint)(x23)))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82DA8UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x296UL))), unchecked((byte)(unchecked((uint)(x23)))));
        goto label_0xC82E38;
        label_0xC82DB0:
        ;
        if ((unchecked((uint)(x23)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = 0x1A8D000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xDE8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xF0UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xF0UL))))));
        __arm64_flags_left_13118940 = unchecked((uint)(x9));
        __arm64_flags_right_13118940 = unchecked((uint)(x10));
        if ((unchecked((uint)((__arm64_flags_left_13118940) - (__arm64_flags_right_13118940))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x8) + (0x238UL)));
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x238UL))), unchecked((ulong)(unchecked((uint)(x23)))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x25);
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x24 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82E08UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x24) + (0x88UL))), x0);
        x1 = x0;
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x88UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82E28UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x22CUL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x296UL))), unchecked((byte)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x27CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC82E38;
        label_0xC82E38:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13119040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13119040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13119040 <= __arm64_float_flags_right_13119040) || ((__arm64_float_flags_left_13119040 != __arm64_float_flags_left_13119040) || (__arm64_float_flags_right_13119040 != __arm64_float_flags_right_13119040))))
        {
            goto label_0xC82EC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x279UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82ECC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x98UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82E68UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x204UL))))), 0));
        __arm64_float_flags_left_13119084 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13119084 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13119084 > __arm64_float_flags_right_13119084))
        {
            goto label_0xC82E7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x229UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82ECC;
        }
        else
        {
            goto label_0xC82E7C;
        }
        label_0xC82E7C:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC2000000UL))));
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xB0UL))))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x40UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82ED0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        if ((x23 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82EA0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xB8UL))))), 0));
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC9FE34UL /* metadata target: FPSPlayer.ActivateBulletTime */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x23;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        goto label_0xC82ED0;
        label_0xC82EC4:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x40UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC82ED0;
        label_0xC82ECC:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x40UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        goto label_0xC82ED0;
        label_0xC82ED0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)(0x1UL)))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        x0 = 0x0UL;
        __arm64_pair_address_13119196 = unchecked((ulong)((x20) + (0xCCUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13119196, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13119196) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0));
        __arm64_pair_address_13119200 = unchecked((ulong)((x20) + (0xBCUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13119200, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13119200) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        __arm64_pair_address_13119204 = unchecked((ulong)((x20) + (0xC4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13119204, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13119204) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xE0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82EF4UL);
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((x22) + (0xF8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC82F14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82F10UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC82F14;
        label_0xC82F14:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC82F74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82F30UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1820C64UL /* metadata target: Image.set_fillAmount */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_13119312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13119312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13119312 >= __arm64_float_flags_right_13119312) || ((__arm64_float_flags_left_13119312 != __arm64_float_flags_left_13119312) || (__arm64_float_flags_right_13119312 != __arm64_float_flags_right_13119312))))
        {
            goto label_0xC82F78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE18UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(x8, unchecked((uint)(x9)));
        goto label_0xC82F78;
        label_0xC82F74:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        goto label_0xC82F78;
        label_0xC82F78:
        ;
        __arm64_float_flags_left_13119352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13119352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13119352 > __arm64_float_flags_right_13119352) || ((__arm64_float_flags_left_13119352 != __arm64_float_flags_left_13119352) || (__arm64_float_flags_right_13119352 != __arm64_float_flags_right_13119352))))
        {
            goto label_0xC83220;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE28UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13119380 = unchecked((uint)(x0));
        __arm64_flags_right_13119380 = unchecked((uint)0x20UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13119380) - (__arm64_flags_right_13119380))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC8308C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE18UL))));
        x8 = RuntimeMemory.ReadU64(x22);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCC0D38UL /* metadata target: GameController.SniperEnemySpawnFun */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC82FCCUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x1A8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40A00000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x1A8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A29C8UL /* metadata target: UnityEvent.Invoke */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A768UL /* metadata target: AudioSource.Stop */, x0, x1, x2, x3);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xACUL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17901F4UL /* metadata target: Random.get_value */, x0, x1, x2, x3);
        __arm64_float_flags_left_13119504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13119504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13119504 < __arm64_float_flags_right_13119504) || ((__arm64_float_flags_left_13119504 != __arm64_float_flags_left_13119504) || (__arm64_float_flags_right_13119504 != __arm64_float_flags_right_13119504))))
        {
            goto label_0xC83054;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83018UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83054;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83034UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xB4UL))))), 0));
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC9FE34UL /* metadata target: FPSPlayer.ActivateBulletTime */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        goto label_0xC83054;
        label_0xC83054:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13119584 = unchecked((uint)(x8));
        __arm64_flags_right_13119584 = unchecked((uint)0x1UL);
        if (((unchecked((uint)((__arm64_flags_left_13119584) - (__arm64_flags_right_13119584))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13119584) - (__arm64_flags_right_13119584))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13119584)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13119584)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13119584) - (__arm64_flags_right_13119584))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13119584)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC83084;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x80UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8308C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC83B84UL /* metadata target: CharacterDamage.RagDollDie */, x0, x1, x2, x3);
        goto label_0xC8308C;
        label_0xC83084:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC832A0UL /* metadata target: CharacterDamage.Die */, x0, x1, x2, x3);
        goto label_0xC8308C;
        label_0xC8308C:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13119640 = unchecked((uint)(x0));
        __arm64_flags_right_13119640 = unchecked((uint)0x1FUL);
        if ((!((unchecked((uint)((__arm64_flags_left_13119640) - (__arm64_flags_right_13119640))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC83138;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE20UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        x23 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE18UL))));
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCC1308UL /* metadata target: GameController.EnemyKill */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCC0C84UL /* metadata target: GameController.EnemySpawnFun */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x9 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xC0UL))))), 0));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x10UL))))), 0));
        v0 = __UnsupportedPackedBinary("+", v0, v1);
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        __arm64_flags_left_13119776 = unchecked((uint)(x0));
        __arm64_flags_right_13119776 = unchecked((uint)(x1));
        if (((!((unchecked((uint)((__arm64_flags_left_13119776) - (__arm64_flags_right_13119776))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13119776) - (__arm64_flags_right_13119776))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13119776)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13119776)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13119776) - (__arm64_flags_right_13119776))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13119776)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC8318C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178F9E4UL /* metadata target: PlayerPrefs.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC8318C;
        label_0xC83138:
        ;
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE18UL))));
        x8 = RuntimeMemory.ReadU64(x22);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCC0F24UL /* metadata target: GameController.Enemydown */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCC1308UL /* metadata target: GameController.EnemyKill */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xC0UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x10UL))))), 0));
        v0 = __UnsupportedPackedBinary("+", v0, v1);
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        goto label_0xC8318C;
        label_0xC8318C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A29C8UL /* metadata target: UnityEvent.Invoke */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1D8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A768UL /* metadata target: AudioSource.Stop */, x0, x1, x2, x3);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xACUL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17901F4UL /* metadata target: Random.get_value */, x0, x1, x2, x3);
        __arm64_float_flags_left_13119936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13119936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13119936 < __arm64_float_flags_right_13119936) || ((__arm64_float_flags_left_13119936 != __arm64_float_flags_left_13119936) || (__arm64_float_flags_right_13119936 != __arm64_float_flags_right_13119936))))
        {
            goto label_0xC83204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC831C8UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC831E4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xB4UL))))), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC9FE34UL /* metadata target: FPSPlayer.ActivateBulletTime */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        goto label_0xC83204;
        label_0xC83204:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8329C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13120016 = unchecked((uint)(x8));
        __arm64_flags_right_13120016 = unchecked((uint)0x1UL);
        if (((unchecked((uint)((__arm64_flags_left_13120016) - (__arm64_flags_right_13120016))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13120016) - (__arm64_flags_right_13120016))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13120016)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13120016)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13120016) - (__arm64_flags_right_13120016))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13120016)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC83244;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x80UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8326C;
        }
        else
        {
            goto label_0xC83220;
        }
        label_0xC83220:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_13120048 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120048)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120048) + (0x8UL))))), 0));
        __arm64_pair_address_13120052 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120052)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120052) + (0x8UL))))), 0));
        __arm64_pair_address_13120056 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120056)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120056) + (0x8UL))))), 0));
        __arm64_pair_address_13120060 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120060)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120060) + (0x8UL))))), 0));
        return x0;
        label_0xC83244:
        ;
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_13120088 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120088)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120088) + (0x8UL))))), 0));
        __arm64_pair_address_13120092 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120092)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120092) + (0x8UL))))), 0));
        __arm64_pair_address_13120096 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120096)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120096) + (0x8UL))))), 0));
        __arm64_pair_address_13120100 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120100)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120100) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13120100) + (0x80UL)));
        return RuntimeCalls.InvokeDirect(0xC832A0UL /* metadata target: CharacterDamage.Die */);
        label_0xC8326C:
        ;
        x0 = x20;
        x1 = x19;
        v0 = v8;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_13120136 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120136)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120136) + (0x8UL))))), 0));
        __arm64_pair_address_13120140 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120140)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120140) + (0x8UL))))), 0));
        __arm64_pair_address_13120144 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120144)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120144) + (0x8UL))))), 0));
        __arm64_pair_address_13120148 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13120148)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13120148) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13120148) + (0x80UL)));
        return RuntimeCalls.InvokeDirect(0xC83B84UL /* metadata target: CharacterDamage.RagDollDie */);
        label_0xC8329C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `CharacterDamage.Die` — RVA `0xc832a0`

- Lift status: **partial**; input span: 2276 bytes; span to next metadata RVA: 2276 bytes.
- Metadata signature: `private void Die() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=290 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc83674; reason: Unsupported instruction 'b.hs' at 0xc83678; reason: Unknown IR expression at 0xc83678; reason: Unsupported instruction 'cmp' at 0xc836c0; reason: Unsupported instruction 'b.lt' at 0xc836c4; reason: Unknown IR expression at 0xc836c4; reason: Unsupported instruction 'fmov' at 0xc837d8; reason: Unsupported instruction 'fmov' at 0xc837e8

```csharp
public static ulong CharacterDamage_Die_RVAc832a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13120688 = default(uint);
        uint __arm64_flags_left_13120712 = default(uint);
        uint __arm64_flags_left_13120840 = default(uint);
        uint __arm64_flags_left_13121112 = default(uint);
        uint __arm64_flags_left_13121444 = default(uint);
        uint __arm64_flags_left_13121560 = default(uint);
        ulong __arm64_flags_left_13121580 = default(ulong);
        uint __arm64_flags_right_13120688 = default(uint);
        uint __arm64_flags_right_13120712 = default(uint);
        uint __arm64_flags_right_13120840 = default(uint);
        uint __arm64_flags_right_13121112 = default(uint);
        uint __arm64_flags_right_13121444 = default(uint);
        uint __arm64_flags_right_13121560 = default(uint);
        ulong __arm64_flags_right_13121580 = default(ulong);
        float __arm64_float_flags_left_13121400 = default(float);
        float __arm64_float_flags_left_13121756 = default(float);
        float __arm64_float_flags_left_13121948 = default(float);
        float __arm64_float_flags_right_13121400 = default(float);
        float __arm64_float_flags_right_13121756 = default(float);
        float __arm64_float_flags_right_13121948 = default(float);
        ulong __arm64_pair_address_13120164 = default(ulong);
        ulong __arm64_pair_address_13120168 = default(ulong);
        ulong __arm64_pair_address_13120172 = default(ulong);
        ulong __arm64_pair_address_13120176 = default(ulong);
        ulong __arm64_pair_address_13120368 = default(ulong);
        ulong __arm64_pair_address_13121228 = default(ulong);
        ulong __arm64_pair_address_13121232 = default(ulong);
        ulong __arm64_pair_address_13121236 = default(ulong);
        ulong __arm64_pair_address_13121684 = default(ulong);
        ulong __arm64_pair_address_13121692 = default(ulong);
        ulong __arm64_pair_address_13121712 = default(ulong);
        ulong __arm64_pair_address_13121720 = default(ulong);
        ulong __arm64_pair_address_13121896 = default(ulong);
        ulong __arm64_pair_address_13122148 = default(ulong);
        ulong __arm64_pair_address_13122396 = default(ulong);
        ulong __arm64_pair_address_13122400 = default(ulong);
        ulong __arm64_pair_address_13122404 = default(ulong);
        ulong __arm64_pair_address_13122408 = default(ulong);
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
        ulong x10 = default(ulong);
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
        sp = unchecked((ulong)((sp) - (0x110UL)));
        __arm64_pair_address_13120164 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13120164, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13120164) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13120168 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13120168, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13120168) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13120172 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13120172, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13120172) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13120176 = unchecked((ulong)((sp) + (0xA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13120176, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13120176) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x27 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x40CUL))))))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83364;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x40CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC83364;
        label_0xC83364:
        ;
        x0 = RuntimeMemory.ReadU64(x27);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5CUL))), v0);
#endif
        __arm64_pair_address_13120368 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13120368, v0);
#else
        __WriteVector128(__arm64_pair_address_13120368, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13120368) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13120368) + (0x10UL))), v0);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83384;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83380UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83384;
        label_0xC83384:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC833D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x43FA0000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC8D260UL /* metadata target: PlayAudioAtPos.PlayClipAt */, x0, x1, x2, x3);
        goto label_0xC833D4;
        label_0xC833D4:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC833E4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC83E2CUL /* metadata target: NPCRegistry.UnregisterNPC */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x20UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83430;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x27);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x78UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8340C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83408UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC8340C;
        label_0xC8340C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83430;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8342CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC83F28UL /* metadata target: NPCSpawner.UnregisterSpawnedNPC */, x0, x1, x2, x3);
        goto label_0xC83430;
        label_0xC83430:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1753EC0UL /* metadata target: NavMeshAgent.set_isStopped */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1796124UL /* metadata target: MonoBehaviour.StopAllCoroutines */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83470;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8346CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83470;
        label_0xC83470:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83B44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE30UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49EC4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x20 = x0;
        __arm64_flags_left_13120688 = unchecked((uint)(x8));
        __arm64_flags_right_13120688 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13120688) - (__arm64_flags_right_13120688))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13120688)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13120688)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13120688) - (__arm64_flags_right_13120688))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13120688)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC83550;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE48UL))));
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x24 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC834C8;
        label_0xC834C8:
        ;
        __arm64_flags_left_13120712 = unchecked((uint)(x22));
        __arm64_flags_right_13120712 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13120712 >= __arm64_flags_right_13120712))
        {
            goto label_0xC83B78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DCB4UL /* metadata target: Transform.set_parent */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF2D0UL /* metadata target: Rigidbody.set_isKinematic */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF9B8UL /* metadata target: Collider.set_isTrigger */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x23);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D8CUL /* metadata target: GameObject.set_tag */, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x31UL))), unchecked((byte)(unchecked((uint)(x24)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13120840 = unchecked((uint)(x22));
        __arm64_flags_right_13120840 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13120840) - (__arm64_flags_right_13120840))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13120840)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13120840)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13120840) - (__arm64_flags_right_13120840))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13120840)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC834C8;
        }
        else
        {
            goto label_0xC83550;
        }
        label_0xC83550:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v14 = v3;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC835B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC835ACUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC835B0;
        label_0xC835B0:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE38UL))));
        x0 = x20;
        v0 = v8;
        v1 = v9;
        x1 = RuntimeMemory.ReadU64(x8);
        v2 = v10;
        v3 = v11;
        v4 = v12;
        v5 = v13;
        v6 = v14;
        x0 = RuntimeCalls.InvokeDirect(0xD2A1ACUL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x90UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDE0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x28 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x28) + (0x38UL))), x0);
        x1 = x0;
        x0 = x28;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC8414CUL /* metadata target: CharacterDamage.CopyTransformsRecurse */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD00UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE32400UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x22 = x0;
        __arm64_flags_left_13121112 = unchecked((uint)(x8));
        __arm64_flags_right_13121112 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13121112) - (__arm64_flags_right_13121112))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13121112)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13121112)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13121112) - (__arm64_flags_right_13121112))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13121112)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC836C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = 0x1A8D000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x4A8UL))));
        x20 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x25 = unchecked((ulong)((x22) + (0x20UL)));
        goto label_0xC83674;
        label_0xC83674:
        ;
        RuntimeCalls.Unsupported("cmp", 0xC83674UL);
        RuntimeCalls.Unsupported("b.hs", 0xC83678UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC83B78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x26);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (x20))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x238UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC836A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC836A0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC836A4;
        label_0xC836A4:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x23;
        x1 = x24;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CB368UL /* metadata target: Physics.IgnoreCollision */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xC836C0UL);
        RuntimeCalls.Unsupported("b.lt", 0xC836C4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC83674;
        }
        else
        {
            goto label_0xC836C8;
        }
        label_0xC836C8:
        ;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xE4UL))))));
        __arm64_pair_address_13121228 = unchecked((ulong)((x19) + (0xBCUL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13121228)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13121228) + (0x4UL))))), 0));
        __arm64_pair_address_13121232 = unchecked((ulong)((x19) + (0xC4UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13121232)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13121232) + (0x4UL))))), 0));
        __arm64_pair_address_13121236 = unchecked((ulong)((x19) + (0xCCUL)));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13121236)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13121236) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179515CUL /* metadata target: LayerMask.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x4A8UL))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83700;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC83700;
        label_0xC83700:
        ;
        x8 = 0x432000UL;
        x9 = 0x432000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4F4UL))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x2FCUL))))), 0));
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v4 = v11;
        v5 = v12;
        v6 = v13;
        x1 = unchecked((ulong)(unchecked((uint)(x22))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CCACCUL /* metadata target: Physics.SphereCast */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x28);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEE00UL /* metadata target: RaycastHit.get_rigidbody */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x27);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83764;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83764;
        label_0xC83764:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83774UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC8UL))))), 0));
        __arm64_float_flags_left_13121400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13121400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13121400 != __arm64_float_flags_right_13121400) || ((__arm64_float_flags_left_13121400 != __arm64_float_flags_left_13121400) || (__arm64_float_flags_right_13121400 != __arm64_float_flags_right_13121400))))
        {
            goto label_0xC83A54;
        }
        else
        {
            goto label_0xC83780;
        }
        label_0xC83780:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDF0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE32400UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x21 = x0;
        __arm64_flags_left_13121444 = unchecked((uint)(x8));
        __arm64_flags_right_13121444 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13121444) - (__arm64_flags_right_13121444))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13121444)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13121444)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13121444) - (__arm64_flags_right_13121444))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13121444)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC83A88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x9 = 0x432000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1E8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA60UL))));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x41CUL))))), 0));
        x26 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x27 = unchecked((ulong)((x21) + (0x20UL)));
        x29 = 0x1BAB000UL;
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("fmov", 0xC837D8UL);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0200000UL)), 0)), 0));
        x20 = 0x1BAB000UL;
        x28 = 0x1BAB000UL;
        RuntimeCalls.Unsupported("fmov", 0xC837E8UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x18UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        goto label_0xC837F0;
        label_0xC837F0:
        ;
        RuntimeCalls.Unsupported("cmp", 0xC837F0UL);
        RuntimeCalls.Unsupported("b.hs", 0xC837F4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC83B78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (x26))));
        if ((x24 == 0x0UL))
        {
            goto label_0xC838F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(x24);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xE40UL))));
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x1 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_13121560 = unchecked((uint)(x10));
        __arm64_flags_right_13121560 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_13121560 >= __arm64_flags_right_13121560))))
        {
            goto label_0xC83B7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13121580 = x8;
        __arm64_flags_right_13121580 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13121580) - (__arm64_flags_right_13121580))) == 0x0UL))))
        {
            goto label_0xC83B7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC838FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
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
            goto label_0xC83A08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xBCUL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2C8UL))))))));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC4UL))))), 0));
        v8 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC838A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
        __arm64_pair_address_13121684 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13121684, v1);
#else
        __WriteVector128(__arm64_pair_address_13121684, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13121684) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13121684) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        __arm64_pair_address_13121692 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13121692);
#else
        v1 = __ReadVector128(__arm64_pair_address_13121692);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13121692) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13121692) + (0x10UL))));
#endif
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2C8UL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC838A4;
        label_0xC838A4:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC838BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC838B0UL);
        }
        __arm64_pair_address_13121712 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13121712, v1);
#else
        __WriteVector128(__arm64_pair_address_13121712, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13121712) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13121712) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        __arm64_pair_address_13121720 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13121720);
#else
        v1 = __ReadVector128(__arm64_pair_address_13121720);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13121720) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13121720) + (0x10UL))));
#endif
        goto label_0xC838BC;
        label_0xC838BC:
        ;
        v0 = v1;
        RuntimeCalls.Unsupported("fsub", 0xC838C0UL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC838C8UL);
        RuntimeCalls.Unsupported("faddp", 0xC838CCUL);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13121756 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13121756 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13121756 <= __arm64_float_flags_right_13121756) || ((__arm64_float_flags_left_13121756 != __arm64_float_flags_left_13121756) || (__arm64_float_flags_right_13121756 != __arm64_float_flags_right_13121756))))
        {
            goto label_0xC83A1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC838E4UL);
        }
        v3 = (RuntimeVector128.Zero.WithUInt32(0, v2.GetUInt32(0)) | RuntimeVector128.Zero.WithUInt32(0, v2.GetUInt32(0)).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fdiv", 0xC838E8UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC83A40;
        label_0xC838F4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE0UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83B74;
        }
        else
        {
            goto label_0xC838FC;
        }
        label_0xC838FC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xBCUL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x29) + (0x32CUL))))))));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC4UL))))), 0));
        v8 = v2;
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x20UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x29) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC83934;
        label_0xC83934:
        ;
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2C8UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x18UL))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2C8UL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC83958;
        label_0xC83958:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83964UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83968;
        label_0xC83968:
        ;
        __arm64_pair_address_13121896 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13121896);
#else
        v3 = __ReadVector128(__arm64_pair_address_13121896);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13121896) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13121896) + (0x10UL))));
#endif
        RuntimeCalls.Unsupported("fmul", 0xC8396CUL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fadd", 0xC83974UL);
        v2 = v3;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC83980UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC83988UL);
        RuntimeCalls.Unsupported("faddp", 0xC8398CUL);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_13121948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13121948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13121948 <= __arm64_float_flags_right_13121948) || ((__arm64_float_flags_left_13121948 != __arm64_float_flags_left_13121948) || (__arm64_float_flags_right_13121948 != __arm64_float_flags_right_13121948))))
        {
            goto label_0xC839B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC839A4UL);
        }
        v3 = (RuntimeVector128.Zero.WithUInt32(0, v2.GetUInt32(0)) | RuntimeVector128.Zero.WithUInt32(0, v2.GetUInt32(0)).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fdiv", 0xC839A8UL);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC839D8;
        label_0xC839B4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x2C9UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC839C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC839C8;
        label_0xC839C8:
        ;
        x8 = RuntimeMemory.ReadU64(x22);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
        goto label_0xC839D8;
        label_0xC839D8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40900000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40F00000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179012CUL /* metadata target: Random.Range */, x0, x1, x2, x3);
        if ((x24 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC839ECUL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC839F0UL);
        goto label_0xC839F4;
        label_0xC839F4:
        ;
        RuntimeCalls.Unsupported("mov", 0xC839F4UL);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF5B8UL /* metadata target: Rigidbody.AddForce */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83A08;
        label_0xC83A08:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x26 = unchecked((ulong)((x26) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xC83A10UL);
        RuntimeCalls.Unsupported("b.lt", 0xC83A14UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC837F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83A18UL);
        }
        goto label_0xC83A88;
        label_0xC83A1C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x2C9UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83A30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC83A30;
        label_0xC83A30:
        ;
        x8 = RuntimeMemory.ReadU64(x22);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
        goto label_0xC83A40;
        label_0xC83A40:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x18UL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC83A44UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41200000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC839F4;
        label_0xC83A54:
        ;
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CEE00UL /* metadata target: RaycastHit.get_rigidbody */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83A64UL);
        }
        __arm64_pair_address_13122148 = unchecked((ulong)((x19) + (0xCCUL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13122148)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13122148) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC8UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41200000UL)), 0)), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF5B8UL /* metadata target: Rigidbody.AddForce */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83A88;
        label_0xC83A88:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83AA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83AA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83AA8;
        label_0xC83AA8:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83AF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA1UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83AE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83ADCUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xA4UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC83AF4;
        label_0xC83AE8:
        ;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83AF4;
        label_0xC83AF4:
        ;
        x20 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA0UL))))))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        if ((unchecked((uint)(x20)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83B1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83B10UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83B74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        goto label_0xC83B1C;
        label_0xC83B1C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83B38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83B38;
        label_0xC83B38:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798A20UL /* metadata target: Object.Destroy */, x0, x1, x2, x3);
        goto label_0xC83B44;
        label_0xC83B44:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        __arm64_pair_address_13122396 = unchecked((ulong)((sp) + (0xA0UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13122396)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13122396) + (0x8UL))))), 0));
        __arm64_pair_address_13122400 = unchecked((ulong)((sp) + (0x90UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13122400)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13122400) + (0x8UL))))), 0));
        __arm64_pair_address_13122404 = unchecked((ulong)((sp) + (0x80UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13122404)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13122404) + (0x8UL))))), 0));
        __arm64_pair_address_13122408 = unchecked((ulong)((sp) + (0x70UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13122408)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13122408) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x110UL)));
        return x0;
        label_0xC83B74:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC83B78;
        label_0xC83B78:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC83B7C;
        label_0xC83B7C:
        ;
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `CharacterDamage.RagDollDie` — RVA `0xc83b84`

- Lift status: **exact**; input span: 680 bytes; span to next metadata RVA: 680 bytes.
- Metadata signature: `private void RagDollDie(Rigidbody hitBody, float bodyForce) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=94 (informational only).

```csharp
public static ulong CharacterDamage_RagDollDie_RVAc83b84(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x40AUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83BC0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x40AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC83BC0;
        label_0xC83BC0:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83BD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83BD0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83BD4;
        label_0xC83BD4:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83BFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83BFC;
        label_0xC83BFC:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83C10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83C0CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83C10;
        label_0xC83C10:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x43FA0000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC8D260UL /* metadata target: PlayAudioAtPos.PlayClipAt */, x0, x1, x2, x3);
        goto label_0xC83C60;
        label_0xC83C60:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83C70UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC83E2CUL /* metadata target: NPCRegistry.UnregisterNPC */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x20UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83CBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x78UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83C98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83C94UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83C98;
        label_0xC83C98:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83CBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83CB8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC83F28UL /* metadata target: NPCSpawner.UnregisterSpawnedNPC */, x0, x1, x2, x3);
        goto label_0xC83CBC;
        label_0xC83CBC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x80UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83D04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83D00UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83D04;
        label_0xC83D04:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83D38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17799D0UL /* metadata target: Renderer.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC83D38;
        label_0xC83D38:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1796124UL /* metadata target: MonoBehaviour.StopAllCoroutines */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC8409CUL /* metadata target: CharacterDamage.ApplyForce */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC83DC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83DC0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC83DC4;
        label_0xC83DC4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83E00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA1UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC83E10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC83E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC83DF8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xA4UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC83E00;
        label_0xC83E00:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC83E10:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */);
        label_0xC83E28:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `CharacterDamage.ApplyForce` — RVA `0xc8409c`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public IEnumerator ApplyForce(Rigidbody body, float force) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong CharacterDamage_ApplyForce_RVAc8409c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x40BUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE60UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE60UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x40BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC840D8:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x21;
        RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `CharacterDamage.CopyTransformsRecurse` — RVA `0xc8414c`

- Lift status: **partial**; input span: 896 bytes; span to next metadata RVA: 896 bytes.
- Metadata signature: `private static void CopyTransformsRecurse(Transform src, Transform dst) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=136 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc84244; reason: Unknown IR expression at 0xc84244; reason: Unsupported instruction 'b.ne' at 0xc842a0; reason: Unknown IR expression at 0xc842a0; reason: Unsupported instruction 'b.ne' at 0xc84398; reason: Unknown IR expression at 0xc84398; reason: Unsupported instruction 'b.ne' at 0xc84488; reason: Unknown IR expression at 0xc84488

```csharp
public static ulong CharacterDamage_CopyTransformsRecurse_RVAc8414c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_13124148 = default(ulong);
        ulong __arm64_flags_left_13124156 = default(ulong);
        ulong __arm64_flags_left_13124240 = default(ulong);
        ulong __arm64_flags_left_13124248 = default(ulong);
        uint __arm64_flags_left_13124328 = default(uint);
        ulong __arm64_flags_left_13124348 = default(ulong);
        ulong __arm64_flags_left_13124488 = default(ulong);
        ulong __arm64_flags_left_13124496 = default(ulong);
        uint __arm64_flags_left_13124640 = default(uint);
        ulong __arm64_flags_left_13124728 = default(ulong);
        ulong __arm64_flags_left_13124736 = default(ulong);
        ulong __arm64_flags_result_13124156 = default(ulong);
        ulong __arm64_flags_result_13124248 = default(ulong);
        ulong __arm64_flags_result_13124496 = default(ulong);
        ulong __arm64_flags_result_13124736 = default(ulong);
        ulong __arm64_flags_right_13124148 = default(ulong);
        ulong __arm64_flags_right_13124156 = default(ulong);
        ulong __arm64_flags_right_13124240 = default(ulong);
        ulong __arm64_flags_right_13124248 = default(ulong);
        uint __arm64_flags_right_13124328 = default(uint);
        ulong __arm64_flags_right_13124348 = default(ulong);
        ulong __arm64_flags_right_13124488 = default(ulong);
        ulong __arm64_flags_right_13124496 = default(ulong);
        uint __arm64_flags_right_13124640 = default(uint);
        ulong __arm64_flags_right_13124728 = default(ulong);
        ulong __arm64_flags_right_13124736 = default(ulong);
        ulong sp = default(ulong);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x40EUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC841AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x40EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC841AC;
        label_0xC841AC:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC843EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xC843EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xEC8UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D774UL /* metadata target: Transform.set_rotation */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ECD4UL /* metadata target: Transform.GetEnumerator */, x0, x1, x2, x3);
        x19 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC843F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8C000UL;
        x25 = 0x1A8D000UL;
        x26 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xED0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xE68UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xD8UL))));
        goto label_0xC84218;
        label_0xC84218:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x24);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC84248;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC84230;
        label_0xC84230:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13124148 = x11;
        __arm64_flags_right_13124148 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13124148) - (__arm64_flags_right_13124148))) == 0x0UL))
        {
            goto label_0xC84258;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC8423CUL);
        }
        __arm64_flags_left_13124156 = x9;
        __arm64_flags_right_13124156 = 0x1UL;
        __arm64_flags_result_13124156 = unchecked((ulong)((__arm64_flags_left_13124156) - (__arm64_flags_right_13124156)));
        x9 = __arm64_flags_result_13124156;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC84244UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC84230;
        }
        else
        {
            goto label_0xC84248;
        }
        label_0xC84248:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC84264;
        label_0xC84258:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC84264;
        label_0xC84264:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC84354;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x24);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC842A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC8428C;
        label_0xC8428C:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13124240 = x11;
        __arm64_flags_right_13124240 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13124240) - (__arm64_flags_right_13124240))) == 0x0UL))
        {
            goto label_0xC842B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC84298UL);
        }
        __arm64_flags_left_13124248 = x9;
        __arm64_flags_right_13124248 = 0x1UL;
        __arm64_flags_result_13124248 = unchecked((ulong)((__arm64_flags_left_13124248) - (__arm64_flags_right_13124248)));
        x9 = __arm64_flags_result_13124248;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC842A0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC8428C;
        }
        else
        {
            goto label_0xC842A4;
        }
        label_0xC842A4:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC842C4;
        label_0xC842B4:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC842C4;
        label_0xC842C4:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x21 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC843E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = RuntimeMemory.ReadU64(x25);
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x130UL))))))));
        __arm64_flags_left_13124328 = unchecked((uint)(x10));
        __arm64_flags_right_13124328 = unchecked((uint)(x9));
        if ((!((__arm64_flags_left_13124328 >= __arm64_flags_right_13124328))))
        {
            goto label_0xC843E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13124348 = x8;
        __arm64_flags_right_13124348 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_13124348) - (__arm64_flags_right_13124348))) == 0x0UL))))
        {
            goto label_0xC843E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798300UL /* metadata target: Object.get_name */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179EBFCUL /* metadata target: Transform.Find */, x0, x1, x2, x3);
        x22 = x0;
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC84334;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC84330UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC84334;
        label_0xC84334:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC84218;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC8414CUL /* metadata target: CharacterDamage.CopyTransformsRecurse */, x0, x1, x2, x3);
        goto label_0xC84218;
        label_0xC84354:
        ;
        x20 = 0x0UL;
        goto label_0xC84358;
        label_0xC84358:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC843C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x23);
        x19 = x0;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8439C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC84384;
        label_0xC84384:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13124488 = x11;
        __arm64_flags_right_13124488 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13124488) - (__arm64_flags_right_13124488))) == 0x0UL))
        {
            goto label_0xC843AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC84390UL);
        }
        __arm64_flags_left_13124496 = x9;
        __arm64_flags_right_13124496 = 0x1UL;
        __arm64_flags_result_13124496 = unchecked((ulong)((__arm64_flags_left_13124496) - (__arm64_flags_right_13124496)));
        x9 = __arm64_flags_result_13124496;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC84398UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC84384;
        }
        else
        {
            goto label_0xC8439C;
        }
        label_0xC8439C:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC843B8;
        label_0xC843AC:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC843B8;
        label_0xC843B8:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC843C4;
        label_0xC843C4:
        ;
        if ((x20 != 0x0UL))
        {
            goto label_0xC843F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC843E0:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC843E8;
        label_0xC843E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC843EC;
        label_0xC843EC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC843F0;
        label_0xC843F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC843F4;
        label_0xC843F4:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC84420;
        label_0xC84420:
        ;
        __arm64_flags_left_13124640 = unchecked((uint)(x1));
        __arm64_flags_right_13124640 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13124640) - (__arm64_flags_right_13124640))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC84438;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC84428UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC84358;
        label_0xC84438:
        ;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x0);
        x20 = 0x0UL;
        goto label_0xC84448;
        label_0xC84448:
        ;
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x19 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC844B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8448C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC84474;
        label_0xC84474:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_13124728 = x11;
        __arm64_flags_right_13124728 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_13124728) - (__arm64_flags_right_13124728))) == 0x0UL))
        {
            goto label_0xC8449C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC84480UL);
        }
        __arm64_flags_left_13124736 = x9;
        __arm64_flags_right_13124736 = 0x1UL;
        __arm64_flags_result_13124736 = unchecked((ulong)((__arm64_flags_left_13124736) - (__arm64_flags_right_13124736)));
        x9 = __arm64_flags_result_13124736;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC84488UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC84474;
        }
        else
        {
            goto label_0xC8448C;
        }
        label_0xC8448C:
        ;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC844A8;
        label_0xC8449C:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC844A8;
        label_0xC844A8:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC844B4;
        label_0xC844B4:
        ;
        if ((x20 != 0x0UL))
        {
            goto label_0xC844C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC844C0;
        label_0xC844C0:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `CharacterDamage.GunPopupfunc` — RVA `0xc844cc`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private IEnumerator GunPopupfunc() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong CharacterDamage_GunPopupfunc_RVAc844cc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x40DUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE70UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE70UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x40DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC844FC:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `CharacterDamage.ctor` — RVA `0xc8454c`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong CharacterDamage_ctor_RVAc8454c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x40UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(unchecked((uint)(0x40300000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x48UL))), unchecked((uint)(x8)));
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xDE0UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x70UL))), unchecked((uint)(x8)));
        x8 = 0x431000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x68UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xCC0UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xB0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x6666UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3F66UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0xA4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))).ShiftLeftLogical(unchecked((int)0x20UL)));
        x19 = x0;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0xB4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2000UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795160UL /* metadata target: LayerMask.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xE4UL))), unchecked((uint)(x0)));
        x0 = x19;
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
