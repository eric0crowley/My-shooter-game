# `ColorGradingModel.Settings` — TypeDefIndex 3573

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `ColorGradingModel.TonemappingSettings` | `tonemapping` |
| `0x1C` | `ColorGradingModel.BasicSettings` | `basic` |
| `0x34` | `ColorGradingModel.ChannelMixerSettings` | `channelMixer` |
| `0x5C` | `ColorGradingModel.ColorWheelsSettings` | `colorWheels` |
| `0xC0` | `ColorGradingModel.CurvesSettings` | `curves` |

## `ColorGradingModel.Settings.get_defaultSettings` — RVA `0xcdb4f8`

- Lift status: **exact**; input span: 204 bytes; span to next metadata RVA: 204 bytes.
- Metadata signature: `public static ColorGradingModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong ColorGradingModel_Settings_get_defaultSettings_RVAcdb4f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13481244 = default(ulong);
        ulong __arm64_pair_address_13481248 = default(ulong);
        ulong __arm64_pair_address_13481328 = default(ulong);
        ulong __arm64_pair_address_13481332 = default(ulong);
        ulong __arm64_pair_address_13481336 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x170UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x8UL))), x19);
        x9 = 0x433000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x250UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x9) + (0x250UL))));
#endif
        x19 = x8;
        x8 = unchecked((ulong)((sp) + (0x48UL)));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x10 = 0x431000UL;
        __arm64_pair_address_13481244 = unchecked((ulong)((x8) + (0xE0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481244, v0);
#else
        __WriteVector128(__arm64_pair_address_13481244, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481244) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481244) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13481248 = unchecked((ulong)((x8) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481248, v0);
#else
        __WriteVector128(__arm64_pair_address_13481248, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481248) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481248) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v1);
#endif
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x10) + (0xC98UL))))), 0));
        x10 = 0x432000UL;
        x9 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x48UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x5CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x10) + (0x720UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x10) + (0x720UL))));
#endif
        x10 = 0x432000UL;
        x9 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x148UL))), 0x0UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x74UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x74UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x10) + (0x580UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x10) + (0x580UL))));
#endif
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x6CUL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x64UL))), 0x0UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x3CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x3CUL))), v1);
#endif
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x94UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x94UL)))) + (0x8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x54UL))), unchecked((ulong)(unchecked((uint)(x9)))));
        x20 = unchecked((ulong)((x8) + (0xC0UL)));
        __arm64_pair_address_13481328 = unchecked((ulong)((x8) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481328, v0);
#else
        __WriteVector128(__arm64_pair_address_13481328, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481328) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481328) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13481332 = unchecked((ulong)((x8) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481332, v0);
#else
        __WriteVector128(__arm64_pair_address_13481332, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481332) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481332) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13481336 = unchecked((ulong)((x8) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481336, v0);
#else
        __WriteVector128(__arm64_pair_address_13481336, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481336) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481336) + (0x10UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xA4UL))), unchecked((uint)(x10)));
        x0 = RuntimeCalls.InvokeDirect(0xCDB6B0UL /* metadata target: ColorGradingModel.CurvesSettings.get_defaultSettings */, x0, x1, x2, x3);
        x1 = sp;
        x2 = unchecked((ulong)(unchecked((uint)(0x48UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x48UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x108UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x160UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x150UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```
