# `ColorGradingModel.BasicSettings` — TypeDefIndex 3566

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `postExposure` |
| `0x4` | `float` | `temperature` |
| `0x8` | `float` | `tint` |
| `0xC` | `float` | `hueShift` |
| `0x10` | `float` | `saturation` |
| `0x14` | `float` | `contrast` |

## `ColorGradingModel.BasicSettings.get_defaultSettings` — RVA `0xcdb640`

- Lift status: **partial**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public static ColorGradingModel.BasicSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xcdb640

```csharp
public static ulong ColorGradingModel_BasicSettings_get_defaultSettings_RVAcdb640(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        RuntimeCalls.Unsupported("fmov", 0xCDB640UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x8UL))), 0x0UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        return x0;
        return default(ulong);
    }
```
