# `DepthOfFieldModel.Settings` — TypeDefIndex 3576

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `float` | `focusDistance` |
| `0x4` | `float` | `aperture` |
| `0x8` | `float` | `focalLength` |
| `0xC` | `bool` | `useCameraFov` |
| `0x10` | `DepthOfFieldModel.KernelSize` | `kernelSize` |

## `DepthOfFieldModel.Settings.get_defaultSettings` — RVA `0xcdbd20`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public static DepthOfFieldModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong DepthOfFieldModel_Settings_get_defaultSettings_RVAcdbd20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xCD0UL))))), 0));
        x10 = unchecked((ulong)(unchecked((uint)(0x42480000UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0xCUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x8) + (0xDUL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0xFUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x8UL))), unchecked((uint)(x10)));
        RuntimeMemory.WriteF64(x8, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x9)));
        return x0;
        return default(ulong);
    }
```
