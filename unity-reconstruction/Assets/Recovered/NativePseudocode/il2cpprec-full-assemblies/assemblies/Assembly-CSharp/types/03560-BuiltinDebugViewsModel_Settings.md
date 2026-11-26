# `BuiltinDebugViewsModel.Settings` — TypeDefIndex 3560

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `BuiltinDebugViewsModel.Mode` | `mode` |
| `0x4` | `BuiltinDebugViewsModel.DepthSettings` | `depth` |
| `0x8` | `BuiltinDebugViewsModel.MotionVectorsSettings` | `motionVectors` |

## `BuiltinDebugViewsModel.Settings.get_defaultSettings` — RVA `0xcdb2cc`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public static BuiltinDebugViewsModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong BuiltinDebugViewsModel_Settings_get_defaultSettings_RVAcdb2cc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xC70UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xC70UL))));
#endif
        x9 = 0x3F800000UL;
        x9 = unchecked((ulong)((unchecked((ulong)((x9) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x18UL) << (int)(unchecked((int)(0x20UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x10 = unchecked((ulong)(unchecked((uint)(0x42800000UL))));
        RuntimeMemory.WritePtr(x8, unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x14UL))), x9);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x4UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x4UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x1CUL))), unchecked((uint)(x10)));
        return x0;
        return default(ulong);
    }
```
