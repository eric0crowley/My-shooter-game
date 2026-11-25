# `bl_CurveControlledBob` — TypeDefIndex 3613

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `float` | `HorizontalBobRange` |
| `0x14` | `float` | `VerticalBobRange` |
| `0x18` | `AnimationCurve` | `Bobcurve` |
| `0x20` | `float` | `VerticaltoHorizontalRatio` |
| `0x24` | `float` | `m_CyclePositionX` |
| `0x28` | `float` | `m_CyclePositionY` |
| `0x2C` | `float` | `m_BobBaseInterval` |
| `0x30` | `Vector3` | `m_OriginalCameraPosition` |
| `0x3C` | `float` | `m_Time` |

## `bl_CurveControlledBob.Setup` — RVA `0xcdfb40`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `public void Setup(Camera camera, float bobBaseInterval) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong bl_CurveControlledBob_Setup_RVAcdfb40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13499264 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x60UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x38UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x30UL))), 0x0UL);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x1 == 0x0UL))
        {
        }
        else
        {
            x19 = x0;
            x0 = x1;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x179CB18UL /* metadata target: Transform.get_localPosition */, x0, x1, x2, x3);
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
                __arm64_pair_address_13499264 = unchecked((ulong)((x19) + (0x30UL)));
                RuntimeMemory.WriteF32(__arm64_pair_address_13499264, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13499264) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                if ((x20 == 0x0UL))
                {
                }
                else
                {
                    x0 = x20;
                    x1 = 0x0UL;
                    x0 = RuntimeCalls.InvokeDirect(0x176D0E0UL /* metadata target: AnimationCurve.get_length */, x0, x1, x2, x3);
                    x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
                    x0 = x20;
                    x2 = 0x0UL;
                    x0 = RuntimeCalls.InvokeDirect(0x176CFD8UL /* metadata target: AnimationCurve.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                    v0 = RuntimeMemory.ReadVector128(sp);
#else
                    v0 = __ReadVector128(sp);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xCUL))));
#else
                    v1 = __ReadVector128(unchecked((ulong)((sp) + (0xCUL))));
#endif
                    x0 = unchecked((ulong)((sp) + (0x20UL)));
                    x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x20UL))), v0);
#else
                    __WriteVector128(unchecked((ulong)((sp) + (0x20UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x2CUL))), v1);
#else
                    __WriteVector128(unchecked((ulong)((sp) + (0x2CUL))), v1);
#endif
                    x0 = RuntimeCalls.InvokeDirect(0x176CC20UL /* metadata target: Keyframe.get_time */, x0, x1, x2, x3);
                    RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x3CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                    x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                    x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
                    x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
                    return x0;
                }
            }
        }
        label_0xCDFBDC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_CurveControlledBob.DoHeadBob` — RVA `0xcdfbe0`

- Lift status: **exact**; input span: 260 bytes; span to next metadata RVA: 260 bytes.
- Metadata signature: `public Vector3 DoHeadBob(float speed) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong bl_CurveControlledBob_DoHeadBob_RVAcdfbe0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13499528 = default(float);
        float __arm64_float_flags_left_13499548 = default(float);
        float __arm64_float_flags_right_13499528 = default(float);
        float __arm64_float_flags_right_13499548 = default(float);
        ulong __arm64_pair_address_13499364 = default(ulong);
        ulong __arm64_pair_address_13499368 = default(ulong);
        ulong __arm64_pair_address_13499372 = default(ulong);
        ulong __arm64_pair_address_13499376 = default(ulong);
        ulong __arm64_pair_address_13499472 = default(ulong);
        ulong __arm64_pair_address_13499504 = default(ulong);
        ulong __arm64_pair_address_13499584 = default(ulong);
        ulong __arm64_pair_address_13499588 = default(ulong);
        ulong __arm64_pair_address_13499592 = default(ulong);
        ulong __arm64_pair_address_13499596 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x60UL)));
        __arm64_pair_address_13499364 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13499364, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13499364) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13499368 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13499368, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13499368) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13499372 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13499372, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13499372) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13499376 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13499376, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13499376) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
        }
        else
        {
            v9 = v0;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x30UL))))), 0));
            x1 = 0x0UL;
            RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0xCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x24UL))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x176CDA8UL /* metadata target: AnimationCurve.Evaluate */, x0, x1, x2, x3);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                v8 = v0;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x28UL))))), 0));
                v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x34UL))))), 0));
                v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x10UL))))), 0));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x176CDA8UL /* metadata target: AnimationCurve.Evaluate */, x0, x1, x2, x3);
                v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x14UL))))), 0));
                v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x24UL))))), 0));
                x0 = 0x0UL;
                v10 = v0;
                x0 = RuntimeCalls.InvokeDirect(0x1789B60UL /* metadata target: Time.get_deltaTime */, x0, x1, x2, x3);
                __arm64_pair_address_13499472 = unchecked((ulong)((x19) + (0x28UL)));
                v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13499472)), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13499472) + (0x4UL))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
                x0 = 0x0UL;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                x0 = RuntimeCalls.InvokeDirect(0x1789B60UL /* metadata target: Time.get_deltaTime */, x0, x1, x2, x3);
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x2CUL))))), 0));
                __arm64_pair_address_13499504 = unchecked((ulong)((x19) + (0x20UL)));
                v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13499504)), 0));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13499504) + (0x4UL))))), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x3CUL))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                __arm64_float_flags_left_13499528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                __arm64_float_flags_right_13499528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x28UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
                if (((__arm64_float_flags_left_13499528 <= __arm64_float_flags_right_13499528) || ((__arm64_float_flags_left_13499528 != __arm64_float_flags_left_13499528) || (__arm64_float_flags_right_13499528 != __arm64_float_flags_right_13499528))))
                {
                }
                else
                {
                    v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
                }
                label_0xCDFC9C:
                ;
                __arm64_float_flags_left_13499548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                __arm64_float_flags_right_13499548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                if (((__arm64_float_flags_left_13499548 <= __arm64_float_flags_right_13499548) || ((__arm64_float_flags_left_13499548 != __arm64_float_flags_left_13499548) || (__arm64_float_flags_right_13499548 != __arm64_float_flags_right_13499548))))
                {
                }
                else
                {
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x28UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                }
                label_0xCDFCAC:
                ;
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
                __arm64_pair_address_13499584 = unchecked((ulong)((sp) + (0x40UL)));
                v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13499584)), 0));
                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13499584) + (0x8UL))))), 0));
                __arm64_pair_address_13499588 = unchecked((ulong)((sp) + (0x30UL)));
                v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13499588)), 0));
                v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13499588) + (0x8UL))))), 0));
                __arm64_pair_address_13499592 = unchecked((ulong)((sp) + (0x20UL)));
                v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13499592)), 0));
                v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13499592) + (0x8UL))))), 0));
                __arm64_pair_address_13499596 = unchecked((ulong)((sp) + (0x10UL)));
                v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13499596)), 0));
                v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13499596) + (0x8UL))))), 0));
                return x0;
            }
        }
        label_0xCDFCE0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_CurveControlledBob.ctor` — RVA `0xcdfce4`

- Lift status: **exact**; input span: 584 bytes; span to next metadata RVA: 584 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=57 (informational only).

```csharp
public static ulong bl_CurveControlledBob_ctor_RVAcdfce4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13499856 = default(uint);
        uint __arm64_flags_left_13499932 = default(uint);
        uint __arm64_flags_left_13500008 = default(uint);
        uint __arm64_flags_left_13500084 = default(uint);
        uint __arm64_flags_right_13499856 = default(uint);
        uint __arm64_flags_right_13499932 = default(uint);
        uint __arm64_flags_right_13500008 = default(uint);
        uint __arm64_flags_right_13500084 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x170UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x140UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x631UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE80UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE88UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE80UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x631UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCDFD2C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xF5C3UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3EA8UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x0;
        x0 = unchecked((ulong)((sp) + (0x120UL)));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x138UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x130UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CBFCUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
        }
        else
        {
            x21 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x120UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((sp) + (0x120UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0xACUL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((x21) + (0xACUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x100UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((sp) + (0x100UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((x21) + (0x8CUL))), v1);
#else
            __WriteVector128(unchecked((ulong)((x21) + (0x8CUL))), v1);
#endif
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
            if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
            {
            }
            else
            {
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x8CUL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((x21) + (0x8CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x100UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x100UL))));
#endif
                x0 = unchecked((ulong)((sp) + (0xE0UL)));
                x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#else
                __WriteVector128(unchecked((ulong)((x20) + (0x2CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v1);
#endif
                RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), 0x0UL);
                RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), 0x0UL);
                RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xF8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
                RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xF0UL))), 0x0UL);
                x0 = RuntimeCalls.InvokeDirect(0x176CBFCUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x6CUL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((x21) + (0x6CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xE0UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0xE0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((x21) + (0x4CUL))), v0);
#else
                __WriteVector128(unchecked((ulong)((x21) + (0x4CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xC0UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0xC0UL))), v1);
#endif
                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
                __arm64_flags_left_13499856 = unchecked((uint)(x8));
                __arm64_flags_right_13499856 = unchecked((uint)0x1UL);
                if (((!((__arm64_flags_left_13499856 >= __arm64_flags_right_13499856))) || (unchecked((uint)((__arm64_flags_left_13499856) - (__arm64_flags_right_13499856))) == unchecked((uint)0x0UL))))
                {
                }
                else
                {
#if IL2CPPREC_RUNTIME_VECTOR128
                    v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x4CUL))));
#else
                    v0 = __ReadVector128(unchecked((ulong)((x21) + (0x4CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xC0UL))));
#else
                    v1 = __ReadVector128(unchecked((ulong)((sp) + (0xC0UL))));
#endif
                    x0 = unchecked((ulong)((sp) + (0xA0UL)));
                    x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#else
                    __WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#else
                    __WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#endif
                    RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), 0x0UL);
                    RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), 0x0UL);
                    RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
                    RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB0UL))), 0x0UL);
                    x0 = RuntimeCalls.InvokeDirect(0x176CBFCUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                    v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x2CUL))));
#else
                    v0 = __ReadVector128(unchecked((ulong)((x21) + (0x2CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#else
                    v1 = __ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((x21) + (0xCUL))), v0);
#else
                    __WriteVector128(unchecked((ulong)((x21) + (0xCUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v1);
#else
                    __WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v1);
#endif
                    x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
                    __arm64_flags_left_13499932 = unchecked((uint)(x8));
                    __arm64_flags_right_13499932 = unchecked((uint)0x2UL);
                    if (((!((__arm64_flags_left_13499932 >= __arm64_flags_right_13499932))) || (unchecked((uint)((__arm64_flags_left_13499932) - (__arm64_flags_right_13499932))) == unchecked((uint)0x0UL))))
                    {
                    }
                    else
                    {
#if IL2CPPREC_RUNTIME_VECTOR128
                        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0xCUL))));
#else
                        v0 = __ReadVector128(unchecked((ulong)((x21) + (0xCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
                        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
                        x0 = unchecked((ulong)((sp) + (0x60UL)));
                        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x64UL))), v0);
#else
                        __WriteVector128(unchecked((ulong)((x20) + (0x64UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x58UL))), v1);
#else
                        __WriteVector128(unchecked((ulong)((x20) + (0x58UL))), v1);
#endif
                        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), 0x0UL);
                        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), 0x0UL);
                        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x78UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
                        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x70UL))), 0x0UL);
                        x0 = RuntimeCalls.InvokeDirect(0x176CBFCUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#else
                        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#else
                        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v0);
#else
                        __WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x40UL))), v1);
#else
                        __WriteVector128(unchecked((ulong)((sp) + (0x40UL))), v1);
#endif
                        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
                        __arm64_flags_left_13500008 = unchecked((uint)(x8));
                        __arm64_flags_right_13500008 = unchecked((uint)0x3UL);
                        if (((!((__arm64_flags_left_13500008 >= __arm64_flags_right_13500008))) || (unchecked((uint)((__arm64_flags_left_13500008) - (__arm64_flags_right_13500008))) == unchecked((uint)0x0UL))))
                        {
                        }
                        else
                        {
#if IL2CPPREC_RUNTIME_VECTOR128
                            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x4CUL))));
#else
                            v0 = __ReadVector128(unchecked((ulong)((sp) + (0x4CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x40UL))));
#else
                            v1 = __ReadVector128(unchecked((ulong)((sp) + (0x40UL))));
#endif
                            x0 = unchecked((ulong)((sp) + (0x20UL)));
                            x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                            RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x80UL))), v0);
#else
                            __WriteVector128(unchecked((ulong)((x20) + (0x80UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                            RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x74UL))), v1);
#else
                            __WriteVector128(unchecked((ulong)((x20) + (0x74UL))), v1);
#endif
                            RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), 0x0UL);
                            RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), 0x0UL);
                            RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x38UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
                            RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x30UL))), 0x0UL);
                            x0 = RuntimeCalls.InvokeDirect(0x176CBFCUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x2CUL))));
#else
                            v0 = __ReadVector128(unchecked((ulong)((sp) + (0x2CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x20UL))));
#else
                            v1 = __ReadVector128(unchecked((ulong)((sp) + (0x20UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                            RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xCUL))), v0);
#else
                            __WriteVector128(unchecked((ulong)((sp) + (0xCUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                            RuntimeMemory.WriteVector128(sp, v1);
#else
                            __WriteVector128(sp, v1);
#endif
                            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
                            __arm64_flags_left_13500084 = unchecked((uint)(x8));
                            __arm64_flags_right_13500084 = unchecked((uint)0x4UL);
                            if (((!((__arm64_flags_left_13500084 >= __arm64_flags_right_13500084))) || (unchecked((uint)((__arm64_flags_left_13500084) - (__arm64_flags_right_13500084))) == unchecked((uint)0x0UL))))
                            {
                            }
                            else
                            {
#if IL2CPPREC_RUNTIME_VECTOR128
                                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xCUL))));
#else
                                v0 = __ReadVector128(unchecked((ulong)((sp) + (0xCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                v1 = RuntimeMemory.ReadVector128(sp);
#else
                                v1 = __ReadVector128(sp);
#endif
                                x8 = 0x1A8C000UL;
                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE88UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
                                RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x9CUL))), v0);
#else
                                __WriteVector128(unchecked((ulong)((x20) + (0x9CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x90UL))), v1);
#else
                                __WriteVector128(unchecked((ulong)((x20) + (0x90UL))), v1);
#endif
                                x0 = RuntimeMemory.ReadU64(x8);
                                x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
                                x1 = x20;
                                x2 = 0x0UL;
                                x21 = x0;
                                x0 = RuntimeCalls.InvokeDirect(0x176D1ACUL /* metadata target: AnimationCurve.ctor */, x0, x1, x2, x3);
                                x0 = x19;
                                RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x21);
                                x1 = x21;
                                x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
                                x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
                                x0 = x19;
                                x1 = 0x0UL;
                                RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x20UL))), unchecked((uint)(x8)));
                                x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
                                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x160UL))));
                                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x160UL)))) + (0x8UL))));
                                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x150UL))));
                                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))));
                                x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x140UL))));
                                return x0;
                            }
                        }
                    }
                }
            }
            label_0xCDFF24:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        }
        label_0xCDFF28:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
