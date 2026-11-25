# `BreakableObject` — TypeDefIndex 3388

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `float` | `hitPoints` |
| `0x28` | `ParticleSystem` | `breakParticles` |
| `0x30` | `bool` | `broken` |
| `0x38` | `Transform` | `myTransform` |

## `BreakableObject.Start` — RVA `0xc95684`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong BreakableObject_Start_RVAc95684(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x479UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC956B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x479UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC956B0;
        label_0xC956B0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x38UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC95700;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x0);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC95700:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BreakableObject.DetectBroken` — RVA `0xc95704`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `private IEnumerator DetectBroken() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong BreakableObject_DetectBroken_RVAc95704(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x47AUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x188UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x188UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x47AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC95738:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x20;
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `BreakableObject.ApplyDamage` — RVA `0xc95798`

- Lift status: **partial**; input span: 744 bytes; span to next metadata RVA: 744 bytes.
- Metadata signature: `public void ApplyDamage(float damage) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=91 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintp' at 0xc95920; reason: Unsupported instruction 'frintm' at 0xc9592c; reason: Unsupported instruction 'csel' at 0xc95944; reason: Unknown IR expression at 0xc95944

```csharp
public static ulong BreakableObject_ApplyDamage_RVAc95798(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13195528 = default(double);
        double __arm64_fcvtz_source_13195576 = default(double);
        ulong __arm64_flags_left_13195536 = default(ulong);
        ulong __arm64_flags_result_13195536 = default(ulong);
        ulong __arm64_flags_right_13195536 = default(ulong);
        float __arm64_float_flags_left_13195276 = default(float);
        float __arm64_float_flags_left_13195476 = default(float);
        double __arm64_float_flags_left_13195488 = default(double);
        double __arm64_float_flags_left_13195512 = default(double);
        double __arm64_float_flags_left_13195580 = default(double);
        float __arm64_float_flags_right_13195276 = default(float);
        float __arm64_float_flags_right_13195476 = default(float);
        double __arm64_float_flags_right_13195488 = default(double);
        double __arm64_float_flags_right_13195512 = default(double);
        double __arm64_float_flags_right_13195580 = default(double);
        ulong __arm64_pair_address_13195164 = default(ulong);
        ulong __arm64_pair_address_13195264 = default(ulong);
        ulong __arm64_pair_address_13195380 = default(ulong);
        ulong __arm64_pair_address_13195392 = default(ulong);
        ulong __arm64_pair_address_13195888 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x80UL)));
        __arm64_pair_address_13195164 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13195164, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13195164) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x47BUL))))))));
        v8 = v0;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC957F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x248UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x190UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x198UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x47BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC957F8;
        label_0xC957F8:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x58UL))), 0x0UL);
        __arm64_pair_address_13195264 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13195264, v0);
#else
        __WriteVector128(__arm64_pair_address_13195264, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13195264) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13195264) + (0x10UL))), v0);
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x20UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13195276 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13195276 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if (((__arm64_float_flags_left_13195276 > __arm64_float_flags_right_13195276) || ((__arm64_float_flags_left_13195276 != __arm64_float_flags_left_13195276) || (__arm64_float_flags_right_13195276 != __arm64_float_flags_right_13195276))))
        {
            goto label_0xC95A64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x30UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC95A64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9583C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC95838UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9583C;
        label_0xC9583C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC95954;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC95A7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9CB4UL /* metadata target: ParticleSystem.get_emission */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x58UL))), x0);
        x8 = sp;
        x0 = unchecked((ulong)((sp) + (0x58UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9F50UL /* metadata target: ParticleSystem.EmissionModule.get_rateOverTime */, x0, x1, x2, x3);
        __arm64_pair_address_13195380 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13195380);
#else
        v0 = __ReadVector128(__arm64_pair_address_13195380);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13195380) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13195380) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x20UL)));
        x1 = 0x0UL;
        __arm64_pair_address_13195392 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13195392, v0);
#else
        __WriteVector128(__arm64_pair_address_13195392, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13195392) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13195392) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17CA508UL /* metadata target: ParticleSystem.MinMaxCurve.get_constant */, x0, x1, x2, x3);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x242UL))))))));
        v8 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC958AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC958AC;
        label_0xC958AC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC958C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC958C0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC958C4;
        label_0xC958C4:
        ;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        x0 = sp;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13195476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13195476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13195476 >= __arm64_float_flags_right_13195476))
        {
            goto label_0xC958F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC958DCUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13195488 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13195488 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13195488 != __arm64_float_flags_right_13195488) || ((__arm64_float_flags_left_13195488 != __arm64_float_flags_left_13195488) || (__arm64_float_flags_right_13195488 != __arm64_float_flags_right_13195488))))
        {
            goto label_0xC9591C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC958E8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC95908;
        label_0xC958F4:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13195512 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13195512 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13195512 != __arm64_float_flags_right_13195512) || ((__arm64_float_flags_left_13195512 != __arm64_float_flags_left_13195512) || (__arm64_float_flags_right_13195512 != __arm64_float_flags_right_13195512))))
        {
            goto label_0xC95928;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC95900UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC95908;
        label_0xC95908:
        ;
        __arm64_fcvtz_source_13195528 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13195528 != __arm64_fcvtz_source_13195528) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13195528 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13195528 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13195528)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13195536 = x8;
        __arm64_flags_right_13195536 = 0x1UL;
        __arm64_flags_result_13195536 = unchecked((ulong)((__arm64_flags_left_13195536) & (__arm64_flags_right_13195536)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13195536 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC95930;
        label_0xC9591C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC95920UL);
        goto label_0xC95930;
        label_0xC95928:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC9592CUL);
        goto label_0xC95930;
        label_0xC95930:
        ;
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13195576 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13195576 != __arm64_fcvtz_source_13195576) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13195576 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13195576 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13195576)))))))));
        __arm64_float_flags_left_13195580 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13195580 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC95944UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C9B7CUL /* metadata target: ParticleSystem.Emit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC95954;
        label_0xC95954:
        ;
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x248UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC95980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC95980;
        label_0xC95980:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC959F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AE58UL /* metadata target: Time.get_timeScale */, x0, x1, x2, x3);
        x0 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x179AE58UL /* metadata target: Time.get_timeScale */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = v0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x400UL))))), 0));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179012CUL /* metadata target: Random.Range */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC95A7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A500UL /* metadata target: AudioSource.set_pitch */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC95A7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, x3);
        goto label_0xC959F4;
        label_0xC959F4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC95A7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC95A7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17799D0UL /* metadata target: Renderer.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC95A7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x190UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC95A7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17CF938UL /* metadata target: Collider.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x30UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0xC95704UL /* metadata target: BreakableObject.DetectBroken */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        goto label_0xC95A64;
        label_0xC95A64:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        __arm64_pair_address_13195888 = unchecked((ulong)((sp) + (0x40UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13195888)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13195888) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x80UL)));
        return x0;
        label_0xC95A7C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BreakableObject.ctor` — RVA `0xc95a80`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong BreakableObject_ctor_RVAc95a80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x43160000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x20UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
