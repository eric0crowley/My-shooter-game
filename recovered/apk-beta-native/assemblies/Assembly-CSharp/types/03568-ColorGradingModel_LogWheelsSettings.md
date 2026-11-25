# `ColorGradingModel.LogWheelsSettings` — TypeDefIndex 3568

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `Color` | `slope` |
| `0x10` | `Color` | `power` |
| `0x20` | `Color` | `offset` |

## `ColorGradingModel.LogWheelsSettings.get_defaultSettings` — RVA `0xcdb668`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public static ColorGradingModel.LogWheelsSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong ColorGradingModel_LogWheelsSettings_get_defaultSettings_RVAcdb668(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13481580 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13481580 = unchecked((ulong)((x8) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481580, v0);
#else
        __WriteVector128(__arm64_pair_address_13481580, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481580) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481580) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x8, v0);
#else
        __WriteVector128(x8, v0);
#endif
        return x0;
        return default(ulong);
    }
```
