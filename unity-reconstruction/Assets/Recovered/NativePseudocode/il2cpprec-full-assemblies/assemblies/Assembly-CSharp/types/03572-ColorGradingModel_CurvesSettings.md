# `ColorGradingModel.CurvesSettings` — TypeDefIndex 3572

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `ColorGradingCurve` | `master` |
| `0x8` | `ColorGradingCurve` | `red` |
| `0x10` | `ColorGradingCurve` | `green` |
| `0x18` | `ColorGradingCurve` | `blue` |
| `0x20` | `ColorGradingCurve` | `hueVShue` |
| `0x28` | `ColorGradingCurve` | `hueVSsat` |
| `0x30` | `ColorGradingCurve` | `satVSsat` |
| `0x38` | `ColorGradingCurve` | `lumVSsat` |
| `0x40` | `int` | `e_CurrentEditingCurve` |
| `0x44` | `bool` | `e_CurveY` |
| `0x45` | `bool` | `e_CurveR` |
| `0x46` | `bool` | `e_CurveG` |
| `0x47` | `bool` | `e_CurveB` |

## `ColorGradingModel.CurvesSettings.get_defaultSettings` — RVA `0xcdb6b0`

- Lift status: **exact**; input span: 1564 bytes; span to next metadata RVA: 1564 bytes.
- Metadata signature: `public static ColorGradingModel.CurvesSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=208 (informational only).

```csharp
public static ulong ColorGradingModel_CurvesSettings_get_defaultSettings_RVAcdb6b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13481920 = default(uint);
        uint __arm64_flags_left_13482204 = default(uint);
        uint __arm64_flags_left_13482472 = default(uint);
        uint __arm64_flags_left_13482740 = default(uint);
        uint __arm64_flags_right_13481920 = default(uint);
        uint __arm64_flags_right_13482204 = default(uint);
        uint __arm64_flags_right_13482472 = default(uint);
        uint __arm64_flags_right_13482740 = default(uint);
        ulong __arm64_pair_address_13481756 = default(ulong);
        ulong __arm64_pair_address_13481760 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x250UL)));
        x20 = 0x1BAB000UL;
        x24 = 0x1A8C000UL;
        x19 = x8;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x60FUL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xE80UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDB70C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x500UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x60FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDB70C;
        label_0xCDB70C:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x240UL))), 0x0UL);
        __arm64_pair_address_13481756 = unchecked((ulong)((sp) + (0x220UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481756, v0);
#else
        __WriteVector128(__arm64_pair_address_13481756, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481756) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481756) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13481760 = unchecked((ulong)((sp) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481760, v0);
#else
        __WriteVector128(__arm64_pair_address_13481760, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481760) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481760) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x0;
        x0 = unchecked((ulong)((sp) + (0x1E0UL)));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x1E0UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x1E0UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1F8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1F0UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDBCC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x1E0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x1E0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x6CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x21) + (0x6CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x1C0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x1C0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x21) + (0x4CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x21) + (0x4CUL))), v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDB774UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x4CUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x21) + (0x4CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x1C0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x1C0UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#endif
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x1A0UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x1A0UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1B8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1B0UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x2CUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x21) + (0x2CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x1A0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x1A0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x21) + (0xCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x21) + (0xCUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x180UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x180UL))), v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13481920 = unchecked((uint)(x8));
        __arm64_flags_right_13481920 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13481920 >= __arm64_flags_right_13481920))) || (unchecked((uint)((__arm64_flags_left_13481920) - (__arm64_flags_right_13481920))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDB7C8UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0xCUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x21) + (0xCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x180UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x180UL))));
#endif
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE88UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#endif
        x22 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(x23);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x500UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1ACUL /* metadata target: AnimationCurve.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x21;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((sp) + (0x200UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x200UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = x0;
        x0 = unchecked((ulong)((sp) + (0x160UL)));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x178UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x170UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDBCC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x160UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x160UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0xECUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x25) + (0xECUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x140UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x140UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0xCCUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0xCCUL))), v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDB890UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0xCCUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x25) + (0xCCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x140UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x140UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#endif
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x138UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x130UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0xACUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x25) + (0xACUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x120UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x120UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x8CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x8CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x100UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x100UL))), v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13482204 = unchecked((uint)(x8));
        __arm64_flags_right_13482204 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13482204 >= __arm64_flags_right_13482204))) || (unchecked((uint)((__arm64_flags_left_13482204) - (__arm64_flags_right_13482204))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDB8E4UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0x8CUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x25) + (0x8CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x100UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x100UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#endif
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1ACUL /* metadata target: AnimationCurve.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x21;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)((sp) + (0x200UL)));
        x0 = unchecked((ulong)((x8) | (0x8UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x208UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = x0;
        x0 = unchecked((ulong)((sp) + (0xE0UL)));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xF8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xF0UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDBCC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDB984UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xE0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0xE0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0x6CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x25) + (0x6CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xC0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0xC0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x4CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x4CUL))), v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDB99CUL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0x4CUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x25) + (0x4CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xC0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0xC0UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#endif
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB0UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0x2CUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x25) + (0x2CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0xCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0xCUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13482472 = unchecked((uint)(x8));
        __arm64_flags_right_13482472 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13482472 >= __arm64_flags_right_13482472))) || (unchecked((uint)((__arm64_flags_left_13482472) - (__arm64_flags_right_13482472))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDB9F0UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x25) + (0xCUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x25) + (0xCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#endif
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1ACUL /* metadata target: AnimationCurve.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x21;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)((sp) + (0x200UL)));
        x0 = unchecked((ulong)((x8) + (0x10UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x210UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = x0;
        x0 = unchecked((ulong)((sp) + (0x60UL)));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x78UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x70UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDBCC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDBA90UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x40UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x40UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDBAA8UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x4CUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x4CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x40UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x40UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#endif
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x38UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x30UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CC0CUL /* metadata target: Keyframe.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x2CUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x2CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x20UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x20UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0xCUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(sp, v1);
#else
        __WriteVector128(sp, v1);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13482740 = unchecked((uint)(x8));
        __arm64_flags_right_13482740 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13482740 >= __arm64_flags_right_13482740))) || (unchecked((uint)((__arm64_flags_left_13482740) - (__arm64_flags_right_13482740))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDBCC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDBAFCUL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xCUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0xCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(sp);
#else
        v1 = __ReadVector128(sp);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#endif
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1ACUL /* metadata target: AnimationCurve.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x21;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x24 = unchecked((ulong)((sp) + (0x200UL)));
        x0 = unchecked((ulong)((x24) + (0x18UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x218UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1FCUL /* metadata target: AnimationCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = x20;
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x24) + (0x20UL)));
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x220UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1FCUL /* metadata target: AnimationCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = x20;
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x24) + (0x28UL)));
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x228UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1FCUL /* metadata target: AnimationCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x24) + (0x30UL)));
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x230UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1FCUL /* metadata target: AnimationCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCDE908UL /* metadata target: ColorGradingCurve.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((x24) + (0x38UL)));
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x238UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x100000000UL;
        x1 = unchecked((ulong)((sp) + (0x200UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x48UL))));
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x240UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        sp = unchecked((ulong)((sp) + (0x250UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCDBCC4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCDBCC8;
        label_0xCDBCC8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```
