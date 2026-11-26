# `ColorGradingModel.ColorWheelsSettings` — TypeDefIndex 3571

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `ColorGradingModel.ColorWheelMode` | `mode` |
| `0x4` | `ColorGradingModel.LogWheelsSettings` | `log` |
| `0x34` | `ColorGradingModel.LinearWheelsSettings` | `linear` |

## `ColorGradingModel.ColorWheelsSettings.get_defaultSettings` — RVA `0xcdb688`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public static ColorGradingModel.ColorWheelsSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong ColorGradingModel_ColorWheelsSettings_get_defaultSettings_RVAcdb688(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WriteU32(x8, unchecked((uint)(x9)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x4UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x4UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x14UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x14UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x24UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x24UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x34UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x34UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x44UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x44UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x54UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x54UL))), v0);
#endif
        return x0;
        return default(ulong);
    }
```
