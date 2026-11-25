# `ScreenSpaceReflectionModel.Settings` — TypeDefIndex 3594

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `ScreenSpaceReflectionModel.ReflectionSettings` | `reflection` |
| `0x20` | `ScreenSpaceReflectionModel.IntensitySettings` | `intensity` |
| `0x30` | `ScreenSpaceReflectionModel.ScreenEdgeMask` | `screenEdgeMask` |

## `ScreenSpaceReflectionModel.Settings.get_defaultSettings` — RVA `0xcdc01c`

- Lift status: **exact**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `public static ScreenSpaceReflectionModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong ScreenSpaceReflectionModel_Settings_get_defaultSettings_RVAcdc01c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xBD8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xED0UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xA58UL))))), 0));
        x9 = 0x432000UL;
        RuntimeMemory.WriteF64(x8, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xB30UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0xB30UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x8UL))), unchecked((uint)(x9)));
        x9 = unchecked((ulong)(unchecked((uint)(0xC28FUL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3CF5UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0xCUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x14UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x1CUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x8) + (0x1DUL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x1FUL))), unchecked((byte)(unchecked((uint)0x0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x30UL))), unchecked((uint)(x9)));
        return x0;
        return default(ulong);
    }
```
