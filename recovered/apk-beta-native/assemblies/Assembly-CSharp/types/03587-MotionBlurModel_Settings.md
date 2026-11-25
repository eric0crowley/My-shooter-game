# `MotionBlurModel.Settings` — TypeDefIndex 3587

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `shutterAngle` |
| `0x4` | `int` | `sampleCount` |
| `0x8` | `float` | `frameBlending` |

## `MotionBlurModel.Settings.get_defaultSettings` — RVA `0xcdbf64`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public static MotionBlurModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong MotionBlurModel_Settings_get_defaultSettings_RVAcdbf64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = 0x43870000UL;
        x0 = unchecked((ulong)((unchecked((ulong)((x0) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0xAUL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        return x0;
        return default(ulong);
    }
```
