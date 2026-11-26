# `JoystickConfig` — TypeDefIndex 5090

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x38` | `JoystickConfig.ClampMode` | `clampMode` |
| `0x3C` | `bool` | `perAxisDeadzones` |
| `0x40` | `JoystickConfig.StickMode` | `stickMode` |
| `0x44` | `DirectionState.OriginalDirResetMode` | `originalDirResetMode` |
| `0x48` | `float` | `angularMagnet` |
| `0x4C` | `JoystickConfig.DigitalDetectionMode` | `digitalDetectionMode` |
| `0x50` | `bool` | `blockX` |
| `0x51` | `bool` | `blockY` |

## `JoystickConfig.ctor` — RVA `0xc609d8`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong JoystickConfig_ctor_RVAc609d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56BB8UL /* metadata target: AnalogConfig.ctor */, x0, x1, x2, x3);
        x9 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xB38UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x38UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(unchecked((uint)(0x3F000000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x48UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x1CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `JoystickConfig.AnimateDirToAnalogVec` — RVA `0xc60a0c`

- Lift status: **partial**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public Vector2 AnimateDirToAnalogVec(Vector2 curVec, Dir targetDir) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=20 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc60a2c; reason: Unknown IR expression at 0xc60a2c

```csharp
public static ulong JoystickConfig_AnimateDirToAnalogVec_RVAc60a0c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12978720 = default(uint);
        uint __arm64_flags_left_12978744 = default(uint);
        uint __arm64_flags_right_12978720 = default(uint);
        uint __arm64_flags_right_12978744 = default(uint);
        ulong __arm64_load_address_12978848 = default(ulong);
        ulong __arm64_pair_address_12978704 = default(ulong);
        ulong __arm64_pair_address_12978708 = default(ulong);
        ulong __arm64_pair_address_12978832 = default(ulong);
        ulong __arm64_pair_address_12978836 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        __arm64_pair_address_12978704 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12978704, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12978704) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12978708 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12978708, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12978708) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x30);
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x38UL))))));
        __arm64_flags_left_12978720 = unchecked((uint)(x1));
        __arm64_flags_right_12978720 = unchecked((uint)0x0UL);
        x9 = unchecked((ulong)(unchecked((uint)(0x24UL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x28UL))));
        RuntimeCalls.Unsupported("csel", 0xC60A2CUL);
        x9 = (__Unsupported<bool>("Unknown IR expression") ? x10 : x9);
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (x9))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        __arm64_flags_left_12978744 = unchecked((uint)(x11));
        __arm64_flags_right_12978744 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12978744) - (__arm64_flags_right_12978744))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x8))));
        x2 = 0x0UL;
        v8 = v1;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xC598B4UL /* metadata target: CFUtils.DirToVector */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        v10 = v0;
        v11 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x179AD80UL /* metadata target: Time.get_unscaledTime */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4F4UL))))), 0));
        x8 = 0x432000UL;
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
        v5 = v0;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = v9;
        v1 = v8;
        v2 = v10;
        v3 = v11;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        __arm64_pair_address_12978832 = unchecked((ulong)((sp) + (0x18UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12978832)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12978832) + (0x8UL))))), 0));
        __arm64_pair_address_12978836 = unchecked((ulong)((sp) + (0x8UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12978836)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12978836) + (0x8UL))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
        x0 = 0x0UL;
        __arm64_load_address_12978848 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12978848)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12978848) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC5877CUL /* metadata target: CFUtils.SmoothTowardsVec2 */);
        return default(ulong);
    }
```

## `JoystickConfig.ClampNormalizedPos` — RVA `0xc60aa8`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public Vector2 ClampNormalizedPos(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong JoystickConfig_ClampNormalizedPos_RVAc60aa8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x38UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC60AB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xC5926CUL /* metadata target: CFUtils.ClampPerAxisInsideUnitSquare */);
        label_0xC60AB8:
        ;
        x0 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0xC51FC4UL /* metadata target: CFUtils.ClampInsideUnitCircle */);
        return default(ulong);
    }
```
