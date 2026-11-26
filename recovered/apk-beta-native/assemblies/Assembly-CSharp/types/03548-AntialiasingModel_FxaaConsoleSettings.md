# `AntialiasingModel.FxaaConsoleSettings` — TypeDefIndex 3548

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `subpixelSpreadAmount` |
| `0x4` | `float` | `edgeSharpnessAmount` |
| `0x8` | `float` | `edgeDetectionThreshold` |
| `0xC` | `float` | `minimumRequiredLuminance` |

## `AntialiasingModel.FxaaConsoleSettings.cctor` — RVA `0xcdafac`

- Lift status: **exact**; input span: 228 bytes; span to next metadata RVA: 228 bytes.
- Metadata signature: `private static void .cctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong AntialiasingModel_FxaaConsoleSettings_cctor_RVAcdafac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13479948 = default(uint);
        uint __arm64_flags_left_13479968 = default(uint);
        uint __arm64_flags_left_13479988 = default(uint);
        uint __arm64_flags_left_13480008 = default(uint);
        uint __arm64_flags_right_13479948 = default(uint);
        uint __arm64_flags_right_13479968 = default(uint);
        uint __arm64_flags_right_13479988 = default(uint);
        uint __arm64_flags_right_13480008 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x606UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x4F8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDAFE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x606UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDAFE8;
        label_0xCDAFE8:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDB08C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x1 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDB088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x870UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x870UL))));
#endif
        __arm64_flags_left_13479948 = unchecked((uint)(x8));
        __arm64_flags_right_13479948 = unchecked((uint)0x1UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x20UL))), v0);
#endif
        if ((unchecked((uint)((__arm64_flags_left_13479948) - (__arm64_flags_right_13479948))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDB088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xD40UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xD40UL))));
#endif
        __arm64_flags_left_13479968 = unchecked((uint)(x8));
        __arm64_flags_right_13479968 = unchecked((uint)0x2UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x30UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x30UL))), v0);
#endif
        if (((!((__arm64_flags_left_13479968 >= __arm64_flags_right_13479968))) || (unchecked((uint)((__arm64_flags_left_13479968) - (__arm64_flags_right_13479968))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDB088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xA20UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xA20UL))));
#endif
        __arm64_flags_left_13479988 = unchecked((uint)(x8));
        __arm64_flags_right_13479988 = unchecked((uint)0x3UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x40UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x40UL))), v0);
#endif
        if ((unchecked((uint)((__arm64_flags_left_13479988) - (__arm64_flags_right_13479988))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDB088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xA30UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xA30UL))));
#endif
        __arm64_flags_left_13480008 = unchecked((uint)(x8));
        __arm64_flags_right_13480008 = unchecked((uint)0x4UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x50UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x50UL))), v0);
#endif
        if (((!((__arm64_flags_left_13480008 >= __arm64_flags_right_13480008))) || (unchecked((uint)((__arm64_flags_left_13480008) - (__arm64_flags_right_13480008))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDB088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xF10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xF10UL))));
#endif
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x130UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x60UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x60UL))), v0);
#endif
        x9 = RuntimeMemory.ReadU64(x8);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        RuntimeMemory.WriteU64(x9, x1);
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xCDB088:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCDB08C;
        label_0xCDB08C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
