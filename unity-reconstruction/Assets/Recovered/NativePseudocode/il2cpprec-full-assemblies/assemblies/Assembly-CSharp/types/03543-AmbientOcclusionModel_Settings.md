# `AmbientOcclusionModel.Settings` — TypeDefIndex 3543

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `intensity` |
| `0x4` | `float` | `radius` |
| `0x8` | `AmbientOcclusionModel.SampleCount` | `sampleCount` |
| `0xC` | `bool` | `downsampling` |
| `0xD` | `bool` | `forceForwardCompatibility` |
| `0xE` | `bool` | `ambientOnly` |
| `0xF` | `bool` | `highPrecision` |

## `AmbientOcclusionModel.Settings.get_defaultSettings` — RVA `0xcdadf0`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public static AmbientOcclusionModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong AmbientOcclusionModel_Settings_get_defaultSettings_RVAcdadf0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = 0x3F800000UL;
        x0 = unchecked((ulong)((unchecked((ulong)((x0) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x999AUL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x0 = unchecked((ulong)((unchecked((ulong)((x0) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x3E99UL) << (int)(unchecked((int)(0x30UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        return x0;
        return default(ulong);
    }
```
