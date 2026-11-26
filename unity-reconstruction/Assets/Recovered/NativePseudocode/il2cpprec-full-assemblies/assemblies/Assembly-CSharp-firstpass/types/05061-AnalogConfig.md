# `AnalogConfig` — TypeDefIndex 5061

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `float` | `analogDeadZone` |
| `0x14` | `float` | `analogEndZone` |
| `0x18` | `float` | `analogRangeStartValue` |
| `0x1C` | `float` | `digitalEnterThresh` |
| `0x20` | `float` | `digitalLeaveThresh` |
| `0x24` | `float` | `digitalToAnalogPressSpeed` |
| `0x28` | `float` | `digitalToAnalogReleaseSpeed` |
| `0x2C` | `bool` | `useRamp` |
| `0x30` | `AnimationCurve` | `ramp` |

## `AnalogConfig.ctor` — RVA `0xc56bb8`

- Lift status: **exact**; input span: 432 bytes; span to next metadata RVA: 432 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=46 (informational only).

```csharp
public static ulong AnalogConfig_ctor_RVAc56bb8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12938428 = default(uint);
        uint __arm64_flags_left_12938504 = default(uint);
        uint __arm64_flags_right_12938428 = default(uint);
        uint __arm64_flags_right_12938504 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2A5UL))))))));
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
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2A5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC56BFC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        x9 = 0x431000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xCF0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xCF0UL))));
#endif
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xD08UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x3F000000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x28UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x10UL))), v0);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x20UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x0;
        x0 = unchecked((ulong)((sp) + (0xA0UL)));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB0UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x176CBFCUL /* metadata target: Keyframe.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
        }
        else
        {
            x8 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x2CUL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((x8) + (0x2CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0xCUL))), v1);
#else
            __WriteVector128(unchecked((ulong)((x8) + (0xCUL))), v1);
#endif
            x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
            if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
            {
            }
            else
            {
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xCUL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((x8) + (0xCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
                x0 = unchecked((ulong)((sp) + (0x60UL)));
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
                __arm64_flags_left_12938428 = unchecked((uint)(x8));
                __arm64_flags_right_12938428 = unchecked((uint)0x1UL);
                if (((!((__arm64_flags_left_12938428 >= __arm64_flags_right_12938428))) || (unchecked((uint)((__arm64_flags_left_12938428) - (__arm64_flags_right_12938428))) == unchecked((uint)0x0UL))))
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
                    RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#else
                    __WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
#else
                    __WriteVector128(unchecked((ulong)((x20) + (0x3CUL))), v1);
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
                    __arm64_flags_left_12938504 = unchecked((uint)(x8));
                    __arm64_flags_right_12938504 = unchecked((uint)0x2UL);
                    if (((!((__arm64_flags_left_12938504 >= __arm64_flags_right_12938504))) || (unchecked((uint)((__arm64_flags_left_12938504) - (__arm64_flags_right_12938504))) == unchecked((uint)0x0UL))))
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
                        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x64UL))), v0);
#else
                        __WriteVector128(unchecked((ulong)((x20) + (0x64UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x58UL))), v1);
#else
                        __WriteVector128(unchecked((ulong)((x20) + (0x58UL))), v1);
#endif
                        x0 = RuntimeMemory.ReadU64(x8);
                        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
                        x1 = x20;
                        x2 = 0x0UL;
                        x21 = x0;
                        x0 = RuntimeCalls.InvokeDirect(0x176D1ACUL /* metadata target: AnimationCurve.ctor */, x0, x1, x2, x3);
                        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x21);
                        x0 = x19;
                        x1 = x21;
                        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
                        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
                        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
                        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
                        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
                        return x0;
                    }
                }
            }
            label_0xC56D60:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        }
        label_0xC56D64:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AnalogConfig.GetAnalogVal` — RVA `0xc574f8`

- Lift status: **exact**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public float GetAnalogVal(float rawVal) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong AnalogConfig_GetAnalogVal_RVAc574f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12940560 = default(float);
        float __arm64_float_flags_left_12940572 = default(float);
        float __arm64_float_flags_left_12940620 = default(float);
        float __arm64_float_flags_left_12940676 = default(float);
        float __arm64_float_flags_right_12940560 = default(float);
        float __arm64_float_flags_right_12940572 = default(float);
        float __arm64_float_flags_right_12940620 = default(float);
        float __arm64_float_flags_right_12940676 = default(float);
        float __arm64_fp_left_12940636 = default(float);
        float __arm64_fp_left_12940672 = default(float);
        float __arm64_fp_right_12940636 = default(float);
        float __arm64_fp_right_12940672 = default(float);
        ulong __arm64_load_address_12940716 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x10UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        v8 = v0;
        __arm64_float_flags_left_12940560 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12940560 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12940560 <= __arm64_float_flags_right_12940560))
        {
            goto label_0xC575A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC57518UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x14UL))))), 0));
        __arm64_float_flags_left_12940572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12940572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12940572 >= __arm64_float_flags_right_12940572))
        {
            goto label_0xC57564;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x2CUL))))))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC57578;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC57578;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176CDA8UL /* metadata target: AnimationCurve.Evaluate */, x0, x1, x2, x3);
        __arm64_float_flags_left_12940620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12940620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((__arm64_float_flags_left_12940620 < __arm64_float_flags_right_12940620))
        {
            goto label_0xC5759C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC57558UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_fp_left_12940636 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12940636 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12940636 != __arm64_fp_left_12940636) ? __arm64_fp_left_12940636 : ((__arm64_fp_right_12940636 != __arm64_fp_right_12940636) ? __arm64_fp_right_12940636 : (((__arm64_fp_left_12940636 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12940636 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12940636), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12940636), 0))))), 0) : ((__arm64_fp_left_12940636 <= __arm64_fp_right_12940636) ? __arm64_fp_left_12940636 : __arm64_fp_right_12940636))))), 0));
        goto label_0xC5759C;
        label_0xC57564:
        ;
        goto label_0xC575A8;
        label_0xC57578:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x18UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_fp_left_12940672 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12940672 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12940672 != __arm64_fp_left_12940672) ? __arm64_fp_left_12940672 : ((__arm64_fp_right_12940672 != __arm64_fp_right_12940672) ? __arm64_fp_right_12940672 : (((__arm64_fp_left_12940672 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12940672 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12940672), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12940672), 0))))), 0) : ((__arm64_fp_left_12940672 <= __arm64_fp_right_12940672) ? __arm64_fp_left_12940672 : __arm64_fp_right_12940672))))), 0));
        __arm64_float_flags_left_12940676 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12940676 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12940676 >= __arm64_float_flags_right_12940676) || ((__arm64_float_flags_left_12940676 != __arm64_float_flags_left_12940676) || (__arm64_float_flags_right_12940676 != __arm64_float_flags_right_12940676))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC5759C;
        label_0xC5759C:
        ;
        goto label_0xC575A8;
        label_0xC575A8:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_12940716 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12940716)), 0));
        return x0;
        return default(ulong);
    }
```

## `AnalogConfig.GetSignedDigitalVal` — RVA `0xc5acc4`

- Lift status: **partial**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public int GetSignedDigitalVal(float rawVal, int prevDigiVal) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=4 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc5acfc; reason: Unknown IR expression at 0xc5acfc; reason: Unsupported instruction 'csel' at 0xc5acd8; reason: Unknown IR expression at 0xc5acd8

```csharp
public static uint AnalogConfig_GetSignedDigitalVal_RVAc5acc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12954828 = default(uint);
        uint __arm64_flags_left_12954864 = default(uint);
        uint __arm64_flags_right_12954828 = default(uint);
        uint __arm64_flags_right_12954864 = default(uint);
        float __arm64_float_flags_left_12954820 = default(float);
        float __arm64_float_flags_left_12954852 = default(float);
        float __arm64_float_flags_left_12954884 = default(float);
        float __arm64_float_flags_right_12954820 = default(float);
        float __arm64_float_flags_right_12954852 = default(float);
        float __arm64_float_flags_right_12954884 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_float_flags_left_12954820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12954820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12954820 >= __arm64_float_flags_right_12954820))
        {
            label_0xC5ACF0:
            ;
            __arm64_flags_left_12954864 = unchecked((uint)(x1));
            __arm64_flags_right_12954864 = unchecked((uint)0x1UL);
            x8 = unchecked((ulong)(unchecked((uint)(0x1CUL))));
            x9 = unchecked((ulong)(unchecked((uint)(0x20UL))));
            RuntimeCalls.Unsupported("csel", 0xC5ACFCUL);
            x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (x8))))), 0));
            __arm64_float_flags_left_12954884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12954884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            x0 = unchecked((ulong)(((__arm64_float_flags_left_12954884 < __arm64_float_flags_right_12954884) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        else
        {
            __arm64_flags_left_12954828 = unchecked((uint)(x1));
            __arm64_flags_right_12954828 = unchecked((uint)0x1UL);
            x8 = unchecked((ulong)(unchecked((uint)(0x1CUL))));
            x9 = unchecked((ulong)(unchecked((uint)(0x20UL))));
            RuntimeCalls.Unsupported("csel", 0xC5ACD8UL);
            x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (x8))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)))), 0));
            __arm64_float_flags_left_12954852 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12954852 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            x0 = unchecked((ulong)(((__arm64_float_flags_left_12954852 > __arm64_float_flags_right_12954852) ? unchecked((uint)0xFFFFFFFFUL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `AnalogConfig.GetDigitalVal` — RVA `0xc5ad10`

- Lift status: **partial**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool GetDigitalVal(float rawVal, bool prevDigiVal) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=2 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc5ad1c; reason: Unknown IR expression at 0xc5ad1c

```csharp
public static uint AnalogConfig_GetDigitalVal_RVAc5ad10(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12954896 = default(uint);
        uint __arm64_flags_result_12954896 = default(uint);
        uint __arm64_flags_right_12954896 = default(uint);
        float __arm64_float_flags_left_12954916 = default(float);
        float __arm64_float_flags_right_12954916 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12954896 = unchecked((uint)(x1));
        __arm64_flags_right_12954896 = unchecked((uint)0x1UL);
        __arm64_flags_result_12954896 = unchecked((uint)((__arm64_flags_left_12954896) & (__arm64_flags_right_12954896)));
        x8 = unchecked((ulong)(unchecked((uint)(0x1CUL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        RuntimeCalls.Unsupported("csel", 0xC5AD1CUL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (x8))))), 0));
        __arm64_float_flags_left_12954916 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12954916 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x0 = unchecked((ulong)(((__arm64_float_flags_left_12954916 < __arm64_float_flags_right_12954916) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `AnalogConfig.AnimateDigitalToAnalog` — RVA `0xc5ad30`

- Lift status: **partial**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public float AnimateDigitalToAnalog(float curVal, float targetVal, bool pressed) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=8 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc5ad48; reason: Unknown IR expression at 0xc5ad48; reason: Unsupported instruction 'fabd' at 0xc5ad64

```csharp
public static ulong AnalogConfig_AnimateDigitalToAnalog_RVAc5ad30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12954940 = default(uint);
        uint __arm64_flags_result_12954940 = default(uint);
        uint __arm64_flags_right_12954940 = default(uint);
        float __arm64_float_flags_left_12954984 = default(float);
        float __arm64_float_flags_left_12955004 = default(float);
        float __arm64_float_flags_left_12955016 = default(float);
        float __arm64_float_flags_left_12955040 = default(float);
        float __arm64_float_flags_right_12954984 = default(float);
        float __arm64_float_flags_right_12955004 = default(float);
        float __arm64_float_flags_right_12955016 = default(float);
        float __arm64_float_flags_right_12955040 = default(float);
        float __arm64_fp_left_12955032 = default(float);
        float __arm64_fp_left_12955036 = default(float);
        float __arm64_fp_right_12955032 = default(float);
        float __arm64_fp_right_12955036 = default(float);
        ulong __arm64_load_address_12955076 = default(ulong);
        ulong __arm64_pair_address_12954932 = default(ulong);
        ulong __arm64_pair_address_12955072 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        __arm64_pair_address_12954932 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12954932, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12954932) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        __arm64_flags_left_12954940 = unchecked((uint)(x1));
        __arm64_flags_right_12954940 = unchecked((uint)0x1UL);
        __arm64_flags_result_12954940 = unchecked((uint)((__arm64_flags_left_12954940) & (__arm64_flags_right_12954940)));
        x8 = unchecked((ulong)(unchecked((uint)(0x28UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x24UL))));
        RuntimeCalls.Unsupported("csel", 0xC5AD48UL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x8);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (x8))))), 0));
        v8 = v1;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        RuntimeCalls.Unsupported("fabd", 0xC5AD64UL);
        __arm64_float_flags_left_12954984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12954984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12954984 <= __arm64_float_flags_right_12954984))
        {
        }
        else
        {
            x8 = 0x432000UL;
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4F4UL))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            __arm64_float_flags_left_12955004 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12955004 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            if ((__arm64_float_flags_left_12955004 < __arm64_float_flags_right_12955004))
            {
            }
            else
            {
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                __arm64_float_flags_left_12955016 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12955016 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F400000UL)), 0)), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12955016 > __arm64_float_flags_right_12955016) || ((__arm64_float_flags_left_12955016 != __arm64_float_flags_left_12955016) || (__arm64_float_flags_right_12955016 != __arm64_float_flags_right_12955016))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
                __arm64_fp_left_12955032 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
                __arm64_fp_right_12955032 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12955032 != __arm64_fp_left_12955032) ? __arm64_fp_left_12955032 : ((__arm64_fp_right_12955032 != __arm64_fp_right_12955032) ? __arm64_fp_right_12955032 : (((__arm64_fp_left_12955032 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12955032 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12955032), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12955032), 0))))), 0) : ((__arm64_fp_left_12955032 <= __arm64_fp_right_12955032) ? __arm64_fp_left_12955032 : __arm64_fp_right_12955032))))), 0));
                __arm64_fp_left_12955036 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                __arm64_fp_right_12955036 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12955036 != __arm64_fp_left_12955036) ? __arm64_fp_left_12955036 : ((__arm64_fp_right_12955036 != __arm64_fp_right_12955036) ? __arm64_fp_right_12955036 : (((__arm64_fp_left_12955036 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12955036 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12955036), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12955036), 0))))), 0) : ((__arm64_fp_left_12955036 <= __arm64_fp_right_12955036) ? __arm64_fp_left_12955036 : __arm64_fp_right_12955036))))), 0));
                __arm64_float_flags_left_12955040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12955040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12955040 >= __arm64_float_flags_right_12955040) || ((__arm64_float_flags_left_12955040 != __arm64_float_flags_left_12955040) || (__arm64_float_flags_right_12955040 != __arm64_float_flags_right_12955040))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
            }
        }
        label_0xC5ADB8:
        ;
        v0 = v8;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_12955072 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12955072)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12955072) + (0x8UL))))), 0));
        __arm64_load_address_12955076 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12955076)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12955076) + (0x20UL)));
        return x0;
        return default(ulong);
    }
```
