# `ColorGradingModel.TonemappingSettings` — TypeDefIndex 3565

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `ColorGradingModel.Tonemapper` | `tonemapper` |
| `0x4` | `float` | `neutralBlackIn` |
| `0x8` | `float` | `neutralWhiteIn` |
| `0xC` | `float` | `neutralBlackOut` |
| `0x10` | `float` | `neutralWhiteOut` |
| `0x14` | `float` | `neutralWhiteLevel` |
| `0x18` | `float` | `neutralWhiteClip` |

## `ColorGradingModel.TonemappingSettings.get_defaultSettings` — RVA `0xcdb61c`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public static ColorGradingModel.TonemappingSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong ColorGradingModel_TonemappingSettings_get_defaultSettings_RVAcdb61c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x433000UL;
        x10 = 0x431000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x250UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x250UL))));
#endif
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x10) + (0xC98UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(x8, unchecked((uint)(x9)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x4UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x4UL))), v0);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x14UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        return x0;
        return default(ulong);
    }
```
