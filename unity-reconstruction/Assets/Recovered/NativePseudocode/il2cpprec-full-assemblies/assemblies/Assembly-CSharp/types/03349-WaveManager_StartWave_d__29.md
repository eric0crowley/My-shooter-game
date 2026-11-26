# `WaveManager.<StartWave>d__29` — TypeDefIndex 3349

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `WaveManager` | `<>4__this` |

## `WaveManager.<StartWave>d__29.ctor` — RVA `0xc87d9c`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong WaveManager_StartWave_d__29_ctor_RVAc87d9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x10UL))), unchecked((uint)(x19)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `WaveManager.<StartWave>d__29.Dispose` — RVA `0xc880bc`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong WaveManager_StartWave_d__29_Dispose_RVAc880bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `WaveManager.<StartWave>d__29.MoveNext` — RVA `0xc880c0`

- Lift status: **partial**; input span: 1620 bytes; span to next metadata RVA: 1620 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=187 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ge' at 0xc88324; reason: Unknown IR expression at 0xc88324; reason: Unsupported instruction 'b.gt' at 0xc8836c; reason: Unknown IR expression at 0xc8836c

```csharp
public static uint WaveManager_StartWave_d__29_MoveNext_RVAc880c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13140248 = default(uint);
        uint __arm64_flags_left_13140324 = default(uint);
        uint __arm64_flags_left_13140720 = default(uint);
        uint __arm64_flags_left_13140824 = default(uint);
        ulong __arm64_flags_left_13141060 = default(ulong);
        uint __arm64_flags_left_13141100 = default(uint);
        ulong __arm64_flags_left_13141132 = default(ulong);
        uint __arm64_flags_left_13141200 = default(uint);
        ulong __arm64_flags_left_13141232 = default(ulong);
        uint __arm64_flags_left_13141296 = default(uint);
        ulong __arm64_flags_left_13141328 = default(ulong);
        uint __arm64_flags_left_13141392 = default(uint);
        ulong __arm64_flags_left_13141424 = default(ulong);
        uint __arm64_flags_right_13140248 = default(uint);
        uint __arm64_flags_right_13140324 = default(uint);
        uint __arm64_flags_right_13140720 = default(uint);
        uint __arm64_flags_right_13140824 = default(uint);
        ulong __arm64_flags_right_13141060 = default(ulong);
        uint __arm64_flags_right_13141100 = default(uint);
        ulong __arm64_flags_right_13141132 = default(ulong);
        uint __arm64_flags_right_13141200 = default(uint);
        ulong __arm64_flags_right_13141232 = default(ulong);
        uint __arm64_flags_right_13141296 = default(uint);
        ulong __arm64_flags_right_13141328 = default(ulong);
        uint __arm64_flags_right_13141392 = default(uint);
        ulong __arm64_flags_right_13141424 = default(ulong);
        double __arm64_float_flags_left_13140452 = default(double);
        float __arm64_float_flags_left_13140636 = default(float);
        float __arm64_float_flags_left_13141680 = default(float);
        double __arm64_float_flags_right_13140452 = default(double);
        float __arm64_float_flags_right_13140636 = default(float);
        float __arm64_float_flags_right_13141680 = default(float);
        ulong __arm64_load_address_13141764 = default(ulong);
        ulong __arm64_pair_address_13140372 = default(ulong);
        ulong __arm64_pair_address_13140404 = default(ulong);
        ulong __arm64_pair_address_13140580 = default(ulong);
        ulong __arm64_pair_address_13140584 = default(ulong);
        ulong __arm64_pair_address_13140612 = default(ulong);
        ulong __arm64_pair_address_13140616 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x42EUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC88110;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x42EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC88110;
        label_0xC88110:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        __arm64_flags_left_13140248 = unchecked((uint)(x8));
        __arm64_flags_right_13140248 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13140248) - (__arm64_flags_right_13140248))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC88174;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88120UL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8831C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x20 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88130UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x38UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x40UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88140UL)));
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x88UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8814CUL)));
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((x9) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x20) + (0x44UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x20) + (0x44UL)))) + (0x8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x4CUL))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x11) + (0x18UL))))));
        __arm64_flags_left_13140324 = unchecked((uint)(x10));
        __arm64_flags_right_13140324 = unchecked((uint)(x11));
        if (((unchecked((uint)((__arm64_flags_left_13140324) - (__arm64_flags_right_13140324))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13140324) - (__arm64_flags_right_13140324))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13140324)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13140324)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13140324) - (__arm64_flags_right_13140324))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13140324)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC88324;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC88338;
        label_0xC88174:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x20 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            goto label_0xC88180;
        }
        label_0xC88180:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x181BDD4UL /* metadata target: Graphic.get_rectTransform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88194UL)));
        }
        __arm64_pair_address_13140372 = unchecked((ulong)((x20) + (0xC0UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13140372)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13140372) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C820UL /* metadata target: RectTransform.set_anchoredPosition */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x181BDD4UL /* metadata target: Graphic.get_rectTransform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC881B4UL)));
        }
        __arm64_pair_address_13140404 = unchecked((ulong)((x20) + (0xC8UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13140404)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13140404) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C820UL /* metadata target: RectTransform.set_anchoredPosition */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x20) + (0xC0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x20) + (0xC0UL))));
#endif
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x3CUL))))), 0));
        x0 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0xD0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0xD0UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x4008000000000000UL))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_float_flags_left_13140452 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        __arm64_float_flags_right_13140452 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        if (((__arm64_float_flags_left_13140452 >= __arm64_float_flags_right_13140452) || ((__arm64_float_flags_left_13140452 != __arm64_float_flags_left_13140452) || (__arm64_float_flags_right_13140452 != __arm64_float_flags_right_13140452))))
        {
            goto label_0xC88230;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC881F4UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x39UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x88UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88200UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x39UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1789B60UL /* metadata target: Time.get_deltaTime */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x40UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88220UL)));
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x88UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8822CUL)));
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC88230;
        label_0xC88230:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        __arm64_pair_address_13140580 = unchecked((ulong)((x20) + (0x98UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13140580)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13140580) + (0x4UL))))), 0));
        __arm64_pair_address_13140584 = unchecked((ulong)((x20) + (0x90UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13140584)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13140584) + (0x4UL))))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        __arm64_pair_address_13140612 = unchecked((ulong)((x20) + (0xA8UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13140612)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13140612) + (0x4UL))))), 0));
        __arm64_pair_address_13140616 = unchecked((ulong)((x20) + (0xA0UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13140616)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13140616) + (0x4UL))))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        __arm64_float_flags_left_13140636 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13140636 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13140636 > __arm64_float_flags_right_13140636) || ((__arm64_float_flags_left_13140636 != __arm64_float_flags_left_13140636) || (__arm64_float_flags_right_13140636 != __arm64_float_flags_right_13140636))))
        {
            goto label_0xC886AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC882C0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC882BCUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC882C0;
        label_0xC882C0:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC886A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x68UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC886A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF68UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC882EC;
        label_0xC882EC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_13140720 = unchecked((uint)(x21));
        __arm64_flags_right_13140720 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13140720) - (__arm64_flags_right_13140720))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13140720)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13140720)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13140720) - (__arm64_flags_right_13140720))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13140720)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC88670;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88308UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x78UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC882EC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88318UL)));
        }
        goto label_0xC8870C;
        label_0xC8831C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC886F4;
        label_0xC88324:
        ;
        RuntimeCalls.Unsupported("b.ge", 0xC88324UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC88330;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        goto label_0xC88338;
        label_0xC88330:
        ;
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x6AUL))), unchecked((byte)(unchecked((uint)(x10)))));
        goto label_0xC88338;
        label_0xC88338:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x70UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x4CUL))), unchecked((uint)(x10)));
        if ((x11 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88344UL)));
        }
        RuntimeMemory.WriteU32(unchecked((ulong)((x11) + (0x20UL))), unchecked((uint)(x10)));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88350UL)));
        }
        RuntimeMemory.WriteU32(unchecked((ulong)((x11) + (0x20UL))), unchecked((uint)(x10)));
        x11 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        __arm64_flags_left_13140824 = unchecked((uint)(x10));
        __arm64_flags_right_13140824 = unchecked((uint)0x1UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x9CUL))), unchecked((uint)(x11)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0xACUL))), unchecked((uint)(x11)));
        RuntimeMemory.WriteU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x38UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x38UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.gt", 0xC8836CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC88378;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x6AUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC88428;
        }
        else
        {
            goto label_0xC88378;
        }
        label_0xC88378:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x3CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x39UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x88UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8839CUL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x39UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x58UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC883BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC883B8UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC883BC;
        label_0xC883BC:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC8841C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x69UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC8841C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x58UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A66CUL /* metadata target: AudioSource.PlayOneShot */, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC883F4UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC9FE34UL /* metadata target: FPSPlayer.ActivateBulletTime */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x69UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC8841C;
        label_0xC8841C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x6AUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC88428;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88424UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x6AUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC88428;
        label_0xC88428:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x1A8D000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF68UL))));
        x21 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC88440;
        label_0xC88440:
        ;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        __arm64_flags_left_13141060 = x21;
        __arm64_flags_right_13141060 = x8;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_13141060) - (__arm64_flags_right_13141060))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_13141060)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_13141060)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_13141060) - (__arm64_flags_right_13141060))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_13141060)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC88180;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x4CUL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13141100 = unchecked((uint)(x9));
        __arm64_flags_right_13141100 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13141100 >= __arm64_flags_right_13141100))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13141132 = x21;
        __arm64_flags_right_13141132 = x9;
        if ((__arm64_flags_left_13141132 >= __arm64_flags_right_13141132))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88494UL)));
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x4CUL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13141200 = unchecked((uint)(x9));
        __arm64_flags_right_13141200 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13141200 >= __arm64_flags_right_13141200))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13141232 = x21;
        __arm64_flags_right_13141232 = x9;
        if ((__arm64_flags_left_13141232 >= __arm64_flags_right_13141232))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC884F8UL)));
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x2UL))))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x70UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x4CUL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13141296 = unchecked((uint)(x9));
        __arm64_flags_right_13141296 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13141296 >= __arm64_flags_right_13141296))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13141328 = x21;
        __arm64_flags_right_13141328 = x9;
        if ((__arm64_flags_left_13141328 >= __arm64_flags_right_13141328))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88558UL)));
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x2UL))))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x6CUL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x4CUL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13141392 = unchecked((uint)(x9));
        __arm64_flags_right_13141392 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13141392 >= __arm64_flags_right_13141392))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13141424 = x21;
        __arm64_flags_right_13141424 = x9;
        if ((__arm64_flags_left_13141424 >= __arm64_flags_right_13141424))
        {
            goto label_0xC88710;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC885B8UL)));
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x2UL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x30UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x44UL))))));
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x70UL))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(x24)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x44UL))), unchecked((uint)(x8)));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88608UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x78UL))), unchecked((byte)(unchecked((uint)(x23)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88624UL)));
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x74UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88640UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x69UL))), unchecked((byte)(unchecked((uint)(x23)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8865CUL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x68UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x0 != 0x0UL))
        {
            goto label_0xC88440;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC8866CUL)));
        }
        goto label_0xC8870C;
        label_0xC88670:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x38UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x88UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC88688UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x38UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x60UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x20) + (0x68UL))), unchecked((ushort)(unchecked((uint)(x8)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC8870C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A66CUL /* metadata target: AudioSource.PlayOneShot */, x0, x1, x2, x3);
        goto label_0xC886A8;
        label_0xC886A8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x40UL))))), 0));
        goto label_0xC886AC;
        label_0xC886AC:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0300000UL)), 0)), 0));
        __arm64_float_flags_left_13141680 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13141680 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13141680 <= __arm64_float_flags_right_13141680))
        {
            goto label_0xC886D4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC886B8UL)));
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x18UL))), 0x0UL);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x0)));
        goto label_0xC886F4;
        label_0xC886D4:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC87DC4UL /* metadata target: WaveManager.FadeWarmupText */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x68UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC886F4;
        label_0xC886F4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_13141764 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13141764)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13141764) + (0x40UL)));
        return unchecked((uint)(x0));
        label_0xC8870C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC88710;
        label_0xC88710:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `WaveManager.<StartWave>d__29.get_Current` — RVA `0xc88714`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong WaveManager_StartWave_d__29_get_Current_RVAc88714(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `WaveManager.<StartWave>d__29.Reset` — RVA `0xc8871c`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong WaveManager_StartWave_d__29_Reset_RVAc8871c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1549CD0UL /* metadata target: NotSupportedException.ctor */, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `WaveManager.<StartWave>d__29.get_Current` — RVA `0xc88754`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong WaveManager_StartWave_d__29_get_Current_RVAc88754(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
