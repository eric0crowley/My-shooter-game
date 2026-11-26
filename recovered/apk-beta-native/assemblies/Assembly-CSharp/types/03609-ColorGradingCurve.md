# `ColorGradingCurve` — TypeDefIndex 3609

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `AnimationCurve` | `curve` |
| `0x18` | `bool` | `m_Loop` |
| `0x1C` | `float` | `m_ZeroValue` |
| `0x20` | `float` | `m_Range` |
| `0x28` | `AnimationCurve` | `m_InternalLoopingCurve` |

## `ColorGradingCurve.ctor` — RVA `0xcde908`

- Lift status: **exact**; input span: 180 bytes; span to next metadata RVA: 180 bytes.
- Metadata signature: `public void .ctor(AnimationCurve curve, float zeroValue, bool loop, Vector2 bounds) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong ColorGradingCurve_ctor_RVAcde908(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_13494708 = default(ulong);
        ulong __arm64_pair_address_13494540 = default(ulong);
        ulong __arm64_pair_address_13494704 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        __arm64_pair_address_13494540 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13494540, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13494540) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = x1;
        x1 = 0x0UL;
        v8 = v2;
        v9 = v1;
        v10 = v0;
        x19 = x0;
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x10UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x21) + (0xCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x8UL))), unchecked((byte)(unchecked((uint)(x22)))));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCDE978:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xCDE990:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_13494704 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13494704)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13494704) + (0x8UL))))), 0));
        __arm64_load_address_13494708 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13494708)), 0));
        return x0;
        return default(ulong);
    }
```

## `ColorGradingCurve.Cache` — RVA `0xcde9bc`

- Lift status: **exact**; input span: 484 bytes; span to next metadata RVA: 484 bytes.
- Metadata signature: `public void Cache() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong ColorGradingCurve_Cache_RVAcde9bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13494816 = default(uint);
        uint __arm64_flags_right_13494816 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xF0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x623UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDE9F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x623UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDE9F0;
        label_0xCDE9F0:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xB0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x98UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x90UL))), 0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x18UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDEB88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176D0E0UL /* metadata target: AnimationCurve.get_length */, x0, x1, x2, x3);
        __arm64_flags_left_13494816 = unchecked((uint)(x0));
        __arm64_flags_right_13494816 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13494816) - (__arm64_flags_right_13494816))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13494816)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13494816)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13494816) - (__arm64_flags_right_13494816))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13494816)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCDEB88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        if ((x8 != 0x0UL))
        {
            goto label_0xCDEA64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE88UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x176D1FCUL /* metadata target: AnimationCurve.ctor */, x0, x1, x2, x3);
        x0 = x20;
        x1 = x22;
        RuntimeMemory.WriteU64(x20, x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCDEA64;
        label_0xCDEA64:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x1UL)))))));
        x2 = 0x0UL;
        x22 = unchecked((ulong)((sp) + (0x80UL)));
        x0 = RuntimeCalls.InvokeDirect(0x176CFD8UL /* metadata target: AnimationCurve.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#endif
        x0 = unchecked((ulong)((sp) + (0xA0UL)));
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xA0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0xA0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x22) + (0x2CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x22) + (0x2CUL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176CC20UL /* metadata target: Keyframe.get_time */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x20UL))))), 0));
        x0 = unchecked((ulong)((sp) + (0xA0UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176CC28UL /* metadata target: Keyframe.set_time */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176CFD8UL /* metadata target: AnimationCurve.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x80UL)));
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x22) + (0xCUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x22) + (0xCUL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176CC20UL /* metadata target: Keyframe.get_time */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x20UL))))), 0));
        x0 = unchecked((ulong)((sp) + (0x80UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176CC28UL /* metadata target: Keyframe.set_time */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176CDF4UL /* metadata target: AnimationCurve.get_keys */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCDEB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176CE6CUL /* metadata target: AnimationCurve.set_keys */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0xA0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x22) + (0x2CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x22) + (0x2CUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x60UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x60UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6CUL))), v1);
#endif
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDEB38UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x6CUL))));
#endif
        x1 = unchecked((ulong)((sp) + (0x40UL)));
        x2 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x40UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x40UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4CUL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176CEF4UL /* metadata target: AnimationCurve.AddKey */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x22) + (0xCUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x22) + (0xCUL))));
#endif
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
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDEB6CUL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x20UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x20UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x2CUL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x2CUL))));
#endif
        x1 = sp;
        x2 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(sp, v0);
#else
        __WriteVector128(sp, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xCUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0xCUL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176CEF4UL /* metadata target: AnimationCurve.AddKey */, x0, x1, x2, x3);
        goto label_0xCDEB88;
        label_0xCDEB88:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        return x0;
        label_0xCDEB9C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `ColorGradingCurve.Evaluate` — RVA `0xcdeba0`

- Lift status: **exact**; input span: 124 bytes; span to next metadata RVA: 124 bytes.
- Metadata signature: `public float Evaluate(float t) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong ColorGradingCurve_Evaluate_RVAcdeba0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13495260 = default(uint);
        uint __arm64_flags_right_13495260 = default(uint);
        ulong __arm64_load_address_13495288 = default(ulong);
        ulong __arm64_load_address_13495304 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEC18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x176D0E0UL /* metadata target: AnimationCurve.get_length */, x0, x1, x2, x3);
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDEC00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x18UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDEBE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEC18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176D0E0UL /* metadata target: AnimationCurve.get_length */, x0, x1, x2, x3);
        __arm64_flags_left_13495260 = unchecked((uint)(x0));
        __arm64_flags_right_13495260 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13495260) - (__arm64_flags_right_13495260))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCDEC10;
        }
        else
        {
            goto label_0xCDEBE4;
        }
        label_0xCDEBE4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDEC18;
        }
        else
        {
            goto label_0xCDEBEC;
        }
        label_0xCDEBEC:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = v8;
        x1 = 0x0UL;
        __arm64_load_address_13495288 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13495288)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13495288) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0x176CDA8UL /* metadata target: AnimationCurve.Evaluate */);
        label_0xCDEC00:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x1CUL))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_13495304 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13495304)), 0));
        return x0;
        label_0xCDEC10:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xCDEBEC;
        }
        else
        {
            goto label_0xCDEC18;
        }
        label_0xCDEC18:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
