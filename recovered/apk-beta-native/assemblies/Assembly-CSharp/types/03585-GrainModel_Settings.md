# `GrainModel.Settings` — TypeDefIndex 3585

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `bool` | `colored` |
| `0x4` | `float` | `intensity` |
| `0x8` | `float` | `size` |
| `0xC` | `float` | `luminanceContribution` |

## `GrainModel.Settings.get_defaultSettings` — RVA `0xcdbf08`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public static GrainModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GrainModel_Settings_get_defaultSettings_RVAcdbf08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = 0x1UL;
        x0 = unchecked((ulong)((unchecked((ulong)((x0) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x3F00UL) << (int)(unchecked((int)(0x30UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        return x0;
        return default(ulong);
    }
```
