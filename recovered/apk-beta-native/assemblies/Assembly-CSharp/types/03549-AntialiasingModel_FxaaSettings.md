# `AntialiasingModel.FxaaSettings` — TypeDefIndex 3549

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `AntialiasingModel.FxaaPreset` | `preset` |

## `AntialiasingModel.FxaaSettings.get_defaultSettings` — RVA `0xcdb090`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public static AntialiasingModel.FxaaSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint AntialiasingModel_FxaaSettings_get_defaultSettings_RVAcdb090(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```
