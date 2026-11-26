# `VignetteModel.Settings` — TypeDefIndex 3599

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `VignetteModel.Mode` | `mode` |
| `0x4` | `Color` | `color` |
| `0x14` | `Vector2` | `center` |
| `0x1C` | `float` | `intensity` |
| `0x20` | `float` | `smoothness` |
| `0x24` | `float` | `roundness` |
| `0x28` | `Texture` | `mask` |
| `0x30` | `float` | `opacity` |
| `0x34` | `bool` | `rounded` |

## `VignetteModel.Settings.get_defaultSettings` — RVA `0xcdc294`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `public static VignetteModel.Settings get_defaultSettings() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong VignetteModel_Settings_get_defaultSettings_RVAcdc294(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13484712 = default(ulong);
        ulong __arm64_pair_address_13484780 = default(ulong);
        ulong __arm64_pair_address_13484796 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x60UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x19 = x8;
        __arm64_pair_address_13484712 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13484712, v0);
#else
        __WriteVector128(__arm64_pair_address_13484712, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13484712) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13484712) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(sp, v0);
#else
        __WriteVector128(sp, v0);
#endif
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        x8 = 0x431000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x14UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xF70UL))))), 0));
        x8 = sp;
        x20 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        x0 = unchecked((ulong)((x8) + (0x28UL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x10UL))), unchecked((uint)(x20)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x24UL))), unchecked((uint)(x20)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x1CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x30UL))), unchecked((uint)(x20)));
        RuntimeMemory.WriteU8(unchecked((ulong)((sp) + (0x34UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        __arm64_pair_address_13484780 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13484780);
#else
        v1 = __ReadVector128(__arm64_pair_address_13484780);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13484780) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13484780) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(sp);
#else
        v2 = __ReadVector128(sp);
#endif
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        __arm64_pair_address_13484796 = unchecked((ulong)((x19) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13484796, v1);
#else
        __WriteVector128(__arm64_pair_address_13484796, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13484796) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13484796) + (0x10UL))), v0);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x19, v2);
#else
        __WriteVector128(x19, v2);
#endif
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```
