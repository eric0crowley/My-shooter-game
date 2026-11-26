# `PressureLevelBinding.RangeConfig` — TypeDefIndex 5131

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `float` | `min` |
| `0x14` | `float` | `max` |
| `0x18` | `KeyCode` | `keyTarget` |
| `0x20` | `string` | `axisTarget` |
| `0x28` | `bool` | `positiveAxisSide` |
| `0x2C` | `int` | `cachedAxisId` |

## `PressureLevelBinding.RangeConfig.ctor` — RVA `0xc68804`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong PressureLevelBinding_RangeConfig_ctor_RVAc68804(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x320UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x230UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC68838;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x320UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC68838;
        label_0xC68838:
        ;
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xA58UL))))), 0));
        x0 = x19;
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x1 = RuntimeMemory.ReadU64(x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x28UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```

## `PressureLevelBinding.RangeConfig.Update` — RVA `0xc68b78`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public void Update(InputRig rig, float val) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong PressureLevelBinding_RangeConfig_Update_RVAc68b78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13011948 = default(uint);
        uint __arm64_flags_right_13011948 = default(uint);
        float __arm64_float_flags_left_13011844 = default(float);
        float __arm64_float_flags_left_13011860 = default(float);
        float __arm64_float_flags_right_13011844 = default(float);
        float __arm64_float_flags_right_13011860 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x10UL))))), 0));
        __arm64_float_flags_left_13011844 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13011844 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13011844 > __arm64_float_flags_right_13011844))
        {
            goto label_0xC68BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68B8CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x14UL))))), 0));
        x20 = x0;
        __arm64_float_flags_left_13011860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13011860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13011860 < __arm64_float_flags_right_13011860))
        {
            goto label_0xC68BC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = x1;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x1)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC68BB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC68BA8UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC68C00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC68BB8;
        label_0xC68BB8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6920UL /* metadata target: String.IsNullOrEmpty */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC68BD4;
        }
        else
        {
            goto label_0xC68BC8;
        }
        label_0xC68BC8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC68BD4:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC68C00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x28UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        x2 = unchecked((ulong)((x20) + (0x2CUL)));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_flags_left_13011948 = unchecked((uint)(x8));
        __arm64_flags_right_13011948 = unchecked((uint)0x0UL);
        x3 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13011948) - (__arm64_flags_right_13011948))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x4 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC3DC78UL /* metadata target: InputRig.SetAxisDigital */);
        label_0xC68C00:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```
