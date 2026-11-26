# `InputRig.Touch` — TypeDefIndex 4986

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `TouchPhase` | `phase` |
| `0x4` | `float` | `deltaTime` |
| `0x8` | `int` | `fingerId` |
| `0xC` | `int` | `tapCount` |
| `0x10` | `Vector2` | `position` |
| `0x18` | `Vector2` | `rawPosition` |
| `0x20` | `Vector2` | `deltaPosition` |
| `0x28` | `float` | `altitudeAngle` |
| `0x2C` | `float` | `azimuthAngle` |
| `0x30` | `float` | `maximumPossiblePressure` |
| `0x34` | `float` | `pressure` |
| `0x38` | `float` | `radius` |
| `0x3C` | `float` | `radiusVariance` |
| `0x40` | `TouchType` | `type` |

## `InputRig.Touch.cctor` — RVA `0xc3e9d8`

- Lift status: **exact**; input span: 152 bytes; span to next metadata RVA: 152 bytes.
- Metadata signature: `private static void .cctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=24 (informational only).

```csharp
public static ulong InputRig_Touch_cctor_RVAc3e9d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12839476 = default(ulong);
        ulong __arm64_pair_address_12839480 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x19 = 0x1A8C000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1E6UL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x478UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x488UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3EA1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x488UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x478UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1E6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC3EA1C;
        label_0xC3EA1C:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x9 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x40UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_12839476 = unchecked((ulong)((x8) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12839476, v0);
#else
        __WriteVector128(__arm64_pair_address_12839476, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12839476) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12839476) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12839480 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12839480, v0);
#else
        __WriteVector128(__arm64_pair_address_12839480, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12839480) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12839480) + (0x10UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU32(x8, unchecked((uint)(x9)));
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x48UL))), x0);
        x0 = x8;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `InputRig.Touch.ctor` — RVA `0xc3ea70`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `public void .ctor(Touch t) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong InputRig_Touch_ctor_RVAc3ea70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12839636 = default(ulong);
        ulong __arm64_pair_address_12839652 = default(ulong);
        ulong __arm64_pair_address_12839676 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = x1;
        x19 = x0;
        x0 = x1;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F60UL /* metadata target: Touch.get_phase */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(x19, unchecked((uint)(x0)));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F50UL /* metadata target: Touch.get_deltaTime */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17C6F18UL /* metadata target: Touch.get_fingerId */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x8UL))), unchecked((uint)(x0)));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F58UL /* metadata target: Touch.get_tapCount */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xCUL))), unchecked((uint)(x0)));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F20UL /* metadata target: Touch.get_position */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12839636 = unchecked((ulong)((x19) + (0x10UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12839636, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12839636) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17C6F30UL /* metadata target: Touch.get_rawPosition */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12839652 = unchecked((ulong)((x19) + (0x18UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12839652, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12839652) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17C6F40UL /* metadata target: Touch.get_deltaPosition */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        x9 = 0x431000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x760UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((x8) + (0x760UL))));
#endif
        v3 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xB80UL))))), 0));
        __arm64_pair_address_12839676 = unchecked((ulong)((x19) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12839676, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12839676) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x40UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x28UL))), v2);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v3.GetUInt64(0)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `InputRig.Touch.TranslateUnityTouches` — RVA `0xc3eb18`

- Lift status: **partial**; input span: 460 bytes; span to next metadata RVA: 460 bytes.
- Metadata signature: `public static InputRig.Touch[] TranslateUnityTouches(Touch[] tarr) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=68 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ge' at 0xc3ec64; reason: Unknown IR expression at 0xc3ec64

```csharp
public static ulong InputRig_Touch_TranslateUnityTouches_RVAc3eb18(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12839860 = default(uint);
        ulong __arm64_flags_left_12840028 = default(ulong);
        ulong __arm64_flags_left_12840044 = default(ulong);
        ulong __arm64_flags_left_12840120 = default(ulong);
        uint __arm64_flags_right_12839860 = default(uint);
        ulong __arm64_flags_right_12840028 = default(ulong);
        ulong __arm64_flags_right_12840044 = default(ulong);
        ulong __arm64_flags_right_12840120 = default(ulong);
        ulong __arm64_pair_address_12840084 = default(ulong);
        ulong __arm64_pair_address_12840088 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x120UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E7UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3EB5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x488UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x478UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC3EB5C;
        label_0xC3EB5C:
        ;
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x478UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC3EBC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC3EBC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3EB84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC3EB7CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xC3EB84;
        label_0xC3EB84:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC3EBF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3EBAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC3EB98UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC3ECE0;
        }
        else
        {
            goto label_0xC3EBAC;
        }
        label_0xC3EBAC:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12839860 = unchecked((uint)(x1));
        __arm64_flags_right_12839860 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_12839860) - (__arm64_flags_right_12839860))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC3EBFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC3EBBCUL);
        }
        goto label_0xC3EC38;
        label_0xC3EBC0:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3EBD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC3EBCCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xC3EBD4;
        label_0xC3EBD4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        goto label_0xC3EBDC;
        label_0xC3EBDC:
        ;
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x120UL)));
        return x0;
        label_0xC3EBF8:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        goto label_0xC3EBFC;
        label_0xC3EBFC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x488UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3EC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        goto label_0xC3EC28;
        label_0xC3EC28:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x50UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC3EC38;
        label_0xC3EC38:
        ;
        x22 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xC3EC40;
        label_0xC3EC40:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x24 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0x18UL))))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3EC58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC3EC50UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xC3EC58;
        label_0xC3EC58:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        __arm64_flags_left_12840028 = x22;
        __arm64_flags_right_12840028 = x24;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        RuntimeCalls.Unsupported("b.ge", 0xC3EC64UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC3EBDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        __arm64_flags_left_12840044 = x22;
        __arm64_flags_right_12840044 = x8;
        if ((__arm64_flags_left_12840044 >= __arm64_flags_right_12840044))
        {
            goto label_0xC3ECDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)((x19) + (unchecked((ulong)(unchecked((uint)(x23)))))));
        x0 = unchecked((ulong)((sp) + (0x48UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x44UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = unchecked((ulong)((sp) + (0x90UL)));
        x1 = unchecked((ulong)((sp) + (0x48UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xD0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_12840084 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12840084, v0);
#else
        __WriteVector128(__arm64_pair_address_12840084, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12840084) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12840084) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12840088 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12840088, v0);
#else
        __WriteVector128(__arm64_pair_address_12840088, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12840088) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12840088) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xC3EA70UL /* metadata target: InputRig.Touch.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC3ECE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = sp;
        x1 = unchecked((ulong)((sp) + (0x90UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x44UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_12840120 = x22;
        __arm64_flags_right_12840120 = x8;
        if ((__arm64_flags_left_12840120 >= __arm64_flags_right_12840120))
        {
            goto label_0xC3ECDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)(x23)))))));
        x1 = sp;
        x2 = unchecked((ulong)(unchecked((uint)(0x44UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x22 = unchecked((ulong)((x22) + (0x1UL)));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x44UL)))))));
        goto label_0xC3EC40;
        label_0xC3ECDC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC3ECE0;
        label_0xC3ECE0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```
