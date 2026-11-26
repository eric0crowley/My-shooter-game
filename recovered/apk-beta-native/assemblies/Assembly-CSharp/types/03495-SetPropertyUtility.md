# `SetPropertyUtility` — TypeDefIndex 3495

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `SetPropertyUtility.SetColor` — RVA `0xccc5bc`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public static bool SetColor(ref Color currentValue, Color newValue) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static uint SetPropertyUtility_SetColor_RVAccc5bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13419968 = default(float);
        float __arm64_float_flags_left_13419980 = default(float);
        float __arm64_float_flags_left_13419992 = default(float);
        float __arm64_float_flags_left_13420004 = default(float);
        float __arm64_float_flags_right_13419968 = default(float);
        float __arm64_float_flags_right_13419980 = default(float);
        float __arm64_float_flags_right_13419992 = default(float);
        float __arm64_float_flags_right_13420004 = default(float);
        ulong __arm64_pair_address_13420020 = default(ulong);
        ulong __arm64_pair_address_13420024 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x0)), 0));
        __arm64_float_flags_left_13419968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13419968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13419968 != __arm64_float_flags_right_13419968) || ((__arm64_float_flags_left_13419968 != __arm64_float_flags_left_13419968) || (__arm64_float_flags_right_13419968 != __arm64_float_flags_right_13419968))))
        {
        }
        else
        {
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x4UL))))), 0));
            __arm64_float_flags_left_13419980 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
            __arm64_float_flags_right_13419980 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_13419980 != __arm64_float_flags_right_13419980) || ((__arm64_float_flags_left_13419980 != __arm64_float_flags_left_13419980) || (__arm64_float_flags_right_13419980 != __arm64_float_flags_right_13419980))))
            {
            }
            else
            {
                v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x8UL))))), 0));
                __arm64_float_flags_left_13419992 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
                __arm64_float_flags_right_13419992 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                if (((__arm64_float_flags_left_13419992 != __arm64_float_flags_right_13419992) || ((__arm64_float_flags_left_13419992 != __arm64_float_flags_left_13419992) || (__arm64_float_flags_right_13419992 != __arm64_float_flags_right_13419992))))
                {
                }
                else
                {
                    v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xCUL))))), 0));
                    __arm64_float_flags_left_13420004 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
                    __arm64_float_flags_right_13420004 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
                    if (((__arm64_float_flags_left_13420004 != __arm64_float_flags_right_13420004) || ((__arm64_float_flags_left_13420004 != __arm64_float_flags_left_13420004) || (__arm64_float_flags_right_13420004 != __arm64_float_flags_right_13420004))))
                    {
                    }
                    else
                    {
                        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
                        return unchecked((uint)(x0));
                    }
                }
            }
        }
        label_0xCCC5F4:
        ;
        __arm64_pair_address_13420020 = x0;
        RuntimeMemory.WriteF32(__arm64_pair_address_13420020, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13420020) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        __arm64_pair_address_13420024 = unchecked((ulong)((x0) + (0x8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13420024, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13420024) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```
