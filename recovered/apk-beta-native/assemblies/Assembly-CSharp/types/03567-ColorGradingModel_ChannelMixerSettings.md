# `ColorGradingModel.ChannelMixerSettings` — TypeDefIndex 3567

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `Vector3` | `red` |
| `0xC` | `Vector3` | `green` |
| `0x18` | `Vector3` | `blue` |
| `0x24` | `int` | `currentEditingChannel` |

## `ColorGradingModel.ChannelMixerSettings.get_defaultSettings` — RVA `0xcdb650`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public static ColorGradingModel.ChannelMixerSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong ColorGradingModel_ChannelMixerSettings_get_defaultSettings_RVAcdb650(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13481568 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xD50UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xD50UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), unchecked((ulong)(unchecked((uint)(x9)))));
        __arm64_pair_address_13481568 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13481568, v0);
#else
        __WriteVector128(__arm64_pair_address_13481568, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13481568) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13481568) + (0x10UL))), v0);
#endif
        return x0;
        return default(ulong);
    }
```
