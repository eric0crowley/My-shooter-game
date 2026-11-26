# `EyeAdaptationModel.Settings` — TypeDefIndex 3581

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `lowPercent` |
| `0x4` | `float` | `highPercent` |
| `0x8` | `float` | `minLuminance` |
| `0xC` | `float` | `maxLuminance` |
| `0x10` | `float` | `keyValue` |
| `0x14` | `bool` | `dynamicKeyValue` |
| `0x18` | `EyeAdaptationModel.EyeAdaptationType` | `adaptationType` |
| `0x1C` | `float` | `speedUp` |
| `0x20` | `float` | `speedDown` |
| `0x24` | `int` | `logMin` |
| `0x28` | `int` | `logMax` |

## `EyeAdaptationModel.Settings.get_defaultSettings` — RVA `0xcdbe20`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `public static EyeAdaptationModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong EyeAdaptationModel_Settings_get_defaultSettings_RVAcdbe20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xF20UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xF20UL))));
#endif
        x9 = 0x431000UL;
        RuntimeMemory.WriteU16(unchecked((ulong)((x8) + (0x15UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x17UL))), unchecked((byte)(unchecked((uint)0x0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x8, v0);
#else
        __WriteVector128(x8, v0);
#endif
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xB50UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x3E800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x9)));
        x9 = 0x432000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x1CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0x98UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x18UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x14UL))), unchecked((byte)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x24UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        return x0;
        return default(ulong);
    }
```
