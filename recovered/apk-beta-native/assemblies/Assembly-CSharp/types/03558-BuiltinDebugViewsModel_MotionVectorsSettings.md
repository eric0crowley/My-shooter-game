# `BuiltinDebugViewsModel.MotionVectorsSettings` — TypeDefIndex 3558

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `sourceOpacity` |
| `0x4` | `float` | `motionImageOpacity` |
| `0x8` | `float` | `motionImageAmplitude` |
| `0xC` | `float` | `motionVectorsOpacity` |
| `0x10` | `int` | `motionVectorsResolution` |
| `0x14` | `float` | `motionVectorsAmplitude` |

## `BuiltinDebugViewsModel.MotionVectorsSettings.get_defaultSettings` — RVA `0xcdb328`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public static BuiltinDebugViewsModel.MotionVectorsSettings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong BuiltinDebugViewsModel_MotionVectorsSettings_get_defaultSettings_RVAcdb328(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x433000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x240UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x240UL))));
#endif
        x9 = 0x18UL;
        x9 = unchecked((ulong)((unchecked((ulong)((x9) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x4280UL) << (int)(unchecked((int)(0x30UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x10UL))), x9);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x8, v0);
#else
        __WriteVector128(x8, v0);
#endif
        return x0;
        return default(ulong);
    }
```
