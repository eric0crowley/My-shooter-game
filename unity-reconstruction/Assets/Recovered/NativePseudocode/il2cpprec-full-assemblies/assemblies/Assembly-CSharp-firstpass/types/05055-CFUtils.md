# `CFUtils` — TypeDefIndex 5055

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `CFUtils.get_realDeltaTime` — RVA `0xc4e208`

- Lift status: **exact**; input span: 60 bytes; span to next metadata RVA: 60 bytes.
- Metadata signature: `public static float get_realDeltaTime() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong CFUtils_get_realDeltaTime_RVAc4e208(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12902932 = default(uint);
        uint __arm64_flags_right_12902932 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AF08UL /* metadata target: Time.get_captureFramerate */, x0, x1, x2, x3);
        __arm64_flags_left_12902932 = unchecked((uint)(x0));
        __arm64_flags_right_12902932 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12902932) - (__arm64_flags_right_12902932))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12902932)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12902932)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12902932) - (__arm64_flags_right_12902932))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12902932)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4E238;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AF08UL /* metadata target: Time.get_captureFramerate */, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4E238:
        ;
        x0 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x179ADA8UL /* metadata target: Time.get_unscaledDeltaTime */);
        return default(ulong);
    }
```

## `CFUtils.TransformRectAsBounds` — RVA `0xc51858`

- Lift status: **exact**; input span: 836 bytes; span to next metadata RVA: 836 bytes.
- Metadata signature: `public static Bounds TransformRectAsBounds(Rect r, Matrix4x4 tr, bool round) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong CFUtils_TransformRectAsBounds_RVAc51858(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12917008 = default(float);
        float __arm64_float_flags_left_12917024 = default(float);
        float __arm64_float_flags_left_12917036 = default(float);
        float __arm64_float_flags_left_12917100 = default(float);
        float __arm64_float_flags_left_12917120 = default(float);
        float __arm64_float_flags_left_12917132 = default(float);
        float __arm64_float_flags_left_12917144 = default(float);
        float __arm64_float_flags_left_12917152 = default(float);
        float __arm64_float_flags_left_12917160 = default(float);
        float __arm64_float_flags_left_12917168 = default(float);
        float __arm64_float_flags_left_12917176 = default(float);
        float __arm64_float_flags_left_12917188 = default(float);
        float __arm64_float_flags_left_12917200 = default(float);
        float __arm64_float_flags_left_12917216 = default(float);
        float __arm64_float_flags_left_12917228 = default(float);
        float __arm64_float_flags_left_12917240 = default(float);
        float __arm64_float_flags_left_12917248 = default(float);
        float __arm64_float_flags_left_12917256 = default(float);
        float __arm64_float_flags_left_12917264 = default(float);
        float __arm64_float_flags_left_12917272 = default(float);
        float __arm64_float_flags_left_12917284 = default(float);
        float __arm64_float_flags_left_12917296 = default(float);
        float __arm64_float_flags_left_12917312 = default(float);
        float __arm64_float_flags_left_12917324 = default(float);
        float __arm64_float_flags_left_12917336 = default(float);
        float __arm64_float_flags_left_12917344 = default(float);
        float __arm64_float_flags_left_12917352 = default(float);
        float __arm64_float_flags_left_12917360 = default(float);
        float __arm64_float_flags_left_12917368 = default(float);
        float __arm64_float_flags_left_12917376 = default(float);
        float __arm64_float_flags_left_12917416 = default(float);
        float __arm64_float_flags_left_12917436 = default(float);
        float __arm64_float_flags_left_12917452 = default(float);
        float __arm64_float_flags_left_12917468 = default(float);
        float __arm64_float_flags_left_12917484 = default(float);
        float __arm64_float_flags_left_12917496 = default(float);
        float __arm64_float_flags_left_12917508 = default(float);
        float __arm64_float_flags_left_12917516 = default(float);
        float __arm64_float_flags_left_12917524 = default(float);
        float __arm64_float_flags_left_12917532 = default(float);
        float __arm64_float_flags_left_12917540 = default(float);
        float __arm64_float_flags_left_12917548 = default(float);
        float __arm64_float_flags_right_12917008 = default(float);
        float __arm64_float_flags_right_12917024 = default(float);
        float __arm64_float_flags_right_12917036 = default(float);
        float __arm64_float_flags_right_12917100 = default(float);
        float __arm64_float_flags_right_12917120 = default(float);
        float __arm64_float_flags_right_12917132 = default(float);
        float __arm64_float_flags_right_12917144 = default(float);
        float __arm64_float_flags_right_12917152 = default(float);
        float __arm64_float_flags_right_12917160 = default(float);
        float __arm64_float_flags_right_12917168 = default(float);
        float __arm64_float_flags_right_12917176 = default(float);
        float __arm64_float_flags_right_12917188 = default(float);
        float __arm64_float_flags_right_12917200 = default(float);
        float __arm64_float_flags_right_12917216 = default(float);
        float __arm64_float_flags_right_12917228 = default(float);
        float __arm64_float_flags_right_12917240 = default(float);
        float __arm64_float_flags_right_12917248 = default(float);
        float __arm64_float_flags_right_12917256 = default(float);
        float __arm64_float_flags_right_12917264 = default(float);
        float __arm64_float_flags_right_12917272 = default(float);
        float __arm64_float_flags_right_12917284 = default(float);
        float __arm64_float_flags_right_12917296 = default(float);
        float __arm64_float_flags_right_12917312 = default(float);
        float __arm64_float_flags_right_12917324 = default(float);
        float __arm64_float_flags_right_12917336 = default(float);
        float __arm64_float_flags_right_12917344 = default(float);
        float __arm64_float_flags_right_12917352 = default(float);
        float __arm64_float_flags_right_12917360 = default(float);
        float __arm64_float_flags_right_12917368 = default(float);
        float __arm64_float_flags_right_12917376 = default(float);
        float __arm64_float_flags_right_12917416 = default(float);
        float __arm64_float_flags_right_12917436 = default(float);
        float __arm64_float_flags_right_12917452 = default(float);
        float __arm64_float_flags_right_12917468 = default(float);
        float __arm64_float_flags_right_12917484 = default(float);
        float __arm64_float_flags_right_12917496 = default(float);
        float __arm64_float_flags_right_12917508 = default(float);
        float __arm64_float_flags_right_12917516 = default(float);
        float __arm64_float_flags_right_12917524 = default(float);
        float __arm64_float_flags_right_12917532 = default(float);
        float __arm64_float_flags_right_12917540 = default(float);
        float __arm64_float_flags_right_12917548 = default(float);
        ulong __arm64_pair_address_12916824 = default(ulong);
        ulong __arm64_pair_address_12916828 = default(ulong);
        ulong __arm64_pair_address_12916832 = default(ulong);
        ulong __arm64_pair_address_12916836 = default(ulong);
        ulong __arm64_pair_address_12917620 = default(ulong);
        ulong __arm64_pair_address_12917624 = default(ulong);
        ulong __arm64_pair_address_12917628 = default(ulong);
        ulong __arm64_pair_address_12917640 = default(ulong);
        ulong __arm64_pair_address_12917644 = default(ulong);
        ulong __arm64_pair_address_12917648 = default(ulong);
        ulong __arm64_pair_address_12917652 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v15 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v18 = default(RuntimeVector128);
        RuntimeVector128 v19 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v20 = default(RuntimeVector128);
        RuntimeVector128 v21 = default(RuntimeVector128);
        RuntimeVector128 v22 = default(RuntimeVector128);
        RuntimeVector128 v23 = default(RuntimeVector128);
        RuntimeVector128 v24 = default(RuntimeVector128);
        RuntimeVector128 v25 = default(RuntimeVector128);
        RuntimeVector128 v26 = default(RuntimeVector128);
        RuntimeVector128 v27 = default(RuntimeVector128);
        RuntimeVector128 v28 = default(RuntimeVector128);
        RuntimeVector128 v29 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12916824 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916824, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916824) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_12916824;
        __arm64_pair_address_12916828 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916828, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916828) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12916832 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916832, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916832) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12916836 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916836, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916836) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = 0x0UL;
        x21 = x0;
        x19 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        v8 = v0;
        v9 = v1;
        v10 = v2;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1787244UL /* metadata target: Matrix4x4.MultiplyVector */, x0, x1, x2, x3);
        v11 = v0;
        v12 = v1;
        v13 = v2;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1787244UL /* metadata target: Matrix4x4.MultiplyVector */, x0, x1, x2, x3);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC51A8C:
            ;
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)))), 0));
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)))), 0));
            __arm64_float_flags_left_12917416 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917416 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)))), 0));
            v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917416 < __arm64_float_flags_right_12917416) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917416 > __arm64_float_flags_right_12917416) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917436 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917436 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
            v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917436 < __arm64_float_flags_right_12917436) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917436 > __arm64_float_flags_right_12917436) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917452 < __arm64_float_flags_right_12917452) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917452 > __arm64_float_flags_right_12917452) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917468 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917468 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
            v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)))), 0));
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917468 < __arm64_float_flags_right_12917468) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))), 0));
            v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917468 > __arm64_float_flags_right_12917468) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917484 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917484 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
            v21 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917484 < __arm64_float_flags_right_12917484) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))), 0));
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917484 > __arm64_float_flags_right_12917484) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917496 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917496 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917496 < __arm64_float_flags_right_12917496) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917496 > __arm64_float_flags_right_12917496) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917508 < __arm64_float_flags_right_12917508) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917516 < __arm64_float_flags_right_12917516) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917524 < __arm64_float_flags_right_12917524) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917532 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917532 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917532 > __arm64_float_flags_right_12917532) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917540 > __arm64_float_flags_right_12917540) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917548 > __arm64_float_flags_right_12917548) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))), 0));
        }
        else
        {
            x8 = 0x432000UL;
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)))), 0));
            v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2F0UL))))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)))), 0));
            __arm64_float_flags_left_12917008 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917008 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
            v21 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917008 < __arm64_float_flags_right_12917008) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917008 > __arm64_float_flags_right_12917008) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
            v22 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917024 < __arm64_float_flags_right_12917024) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917024 > __arm64_float_flags_right_12917024) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917036 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917036 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            v23 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917036 < __arm64_float_flags_right_12917036) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917036 > __arm64_float_flags_right_12917036) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
            v26 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))))), 0));
            v25 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))))), 0));
            v28 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v26.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v24 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))))), 0));
            v27 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v25.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v26.GetUInt64(0)))), 0))))), 0));
            v26 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0)))), 0));
            v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v25.GetUInt64(0)))), 0))))), 0));
            v25 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0)))), 0));
            __arm64_float_flags_left_12917100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v26.GetUInt64(0)))), 0);
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0))))), 0));
            v24 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0)))), 0));
            v29 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917100 < __arm64_float_flags_right_12917100) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v26.GetUInt64(0)))), 0))), 0));
            v26 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917100 > __arm64_float_flags_right_12917100) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v26.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917120 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917120 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v25.GetUInt64(0)))), 0);
            v28 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917120 < __arm64_float_flags_right_12917120) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v25.GetUInt64(0)))), 0))), 0));
            v25 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917120 > __arm64_float_flags_right_12917120) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v25.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917132 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917132 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0);
            v27 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917132 < __arm64_float_flags_right_12917132) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0))), 0));
            v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917132 > __arm64_float_flags_right_12917132) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917144 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917144 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0);
            v21 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917144 < __arm64_float_flags_right_12917144) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v22.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0);
            v22 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917152 < __arm64_float_flags_right_12917152) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v22.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v23.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v29.GetUInt64(0)))), 0);
            v23 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917160 < __arm64_float_flags_right_12917160) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v23.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v29.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917168 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917168 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0);
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917168 > __arm64_float_flags_right_12917168) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917176 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917176 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v25.GetUInt64(0)))), 0);
            v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917176 > __arm64_float_flags_right_12917176) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v25.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917188 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917188 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v26.GetUInt64(0)))), 0);
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)))), 0));
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917188 > __arm64_float_flags_right_12917188) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v26.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917200 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917200 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
            v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)))), 0));
            v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917200 < __arm64_float_flags_right_12917200) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917200 > __arm64_float_flags_right_12917200) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
            v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917216 < __arm64_float_flags_right_12917216) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917216 > __arm64_float_flags_right_12917216) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917228 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917228 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0);
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917228 < __arm64_float_flags_right_12917228) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917228 > __arm64_float_flags_right_12917228) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917240 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917240 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
            v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917240 < __arm64_float_flags_right_12917240) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917248 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v22.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917248 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917248 < __arm64_float_flags_right_12917248) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v22.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v23.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0);
            v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917256 < __arm64_float_flags_right_12917256) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v23.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917264 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917264 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917264 > __arm64_float_flags_right_12917264) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917272 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917272 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
            v28 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917272 > __arm64_float_flags_right_12917272) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917284 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917284 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
            v27 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917284 > __arm64_float_flags_right_12917284) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917296 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917296 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0);
            v24 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917296 < __arm64_float_flags_right_12917296) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917296 > __arm64_float_flags_right_12917296) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v28.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0);
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917312 < __arm64_float_flags_right_12917312) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0))), 0));
            v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917312 > __arm64_float_flags_right_12917312) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v27.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917324 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917324 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917324 < __arm64_float_flags_right_12917324) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917324 > __arm64_float_flags_right_12917324) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917336 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917336 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917336 < __arm64_float_flags_right_12917336) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917344 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917344 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917344 < __arm64_float_flags_right_12917344) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917352 < __arm64_float_flags_right_12917352) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917360 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917360 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917360 > __arm64_float_flags_right_12917360) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917368 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917368 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0);
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917368 > __arm64_float_flags_right_12917368) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12917376 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12917376 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12917376 > __arm64_float_flags_right_12917376) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))), 0));
        }
        label_0xC51B34:
        ;
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12917620 = x19;
        RuntimeMemory.WriteF32(__arm64_pair_address_12917620, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12917620) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0));
        __arm64_pair_address_12917624 = unchecked((ulong)((x19) + (0x8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12917624, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12917624) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        __arm64_pair_address_12917628 = unchecked((ulong)((x19) + (0x10UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12917628, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12917628) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_12917640 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12917640)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12917640) + (0x8UL))))), 0));
        __arm64_pair_address_12917644 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12917644)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12917644) + (0x8UL))))), 0));
        __arm64_pair_address_12917648 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12917648)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12917648) + (0x8UL))))), 0));
        __arm64_pair_address_12917652 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12917652)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12917652) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ClampInsideUnitCircle` — RVA `0xc51fc4`

- Lift status: **exact**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `public static Vector2 ClampInsideUnitCircle(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=24 (informational only).

```csharp
public static ulong CFUtils_ClampInsideUnitCircle_RVAc51fc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12918760 = default(float);
        float __arm64_float_flags_left_12918836 = default(float);
        float __arm64_float_flags_right_12918760 = default(float);
        float __arm64_float_flags_right_12918836 = default(float);
        ulong __arm64_load_address_12918924 = default(ulong);
        ulong __arm64_pair_address_12918728 = default(ulong);
        ulong __arm64_pair_address_12918904 = default(ulong);
        ulong __arm64_pair_address_12918920 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        __arm64_pair_address_12918728 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12918728, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12918728) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        v8 = v1;
        v9 = v0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12918760 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918760 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12918760 < __arm64_float_flags_right_12918760))
        {
        }
        else
        {
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x243UL))))))));
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
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC52010:
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
            label_0xC52028:
            ;
            x8 = 0x432000UL;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))))), 0));
            __arm64_float_flags_left_12918836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12918836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_12918836 <= __arm64_float_flags_right_12918836) || ((__arm64_float_flags_left_12918836 != __arm64_float_flags_left_12918836) || (__arm64_float_flags_right_12918836 != __arm64_float_flags_right_12918836))))
            {
                label_0xC52048:
                ;
                x19 = 0x1BAB000UL;
                x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
                if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = 0x1A8C000UL;
                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                    // Likely IL2CPP class initialization helper (guarded call).
                    x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                    x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
                }
                label_0xC52068:
                ;
                x8 = 0x1A8C000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
                x8 = RuntimeMemory.ReadU64(x8);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                __arm64_pair_address_12918904 = x8;
                v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12918904)), 0));
                v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12918904) + (0x4UL))))), 0));
            }
            else
            {
                v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            }
        }
        label_0xC5207C:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12918920 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918920)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918920) + (0x8UL))))), 0));
        __arm64_load_address_12918924 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12918924)), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ClampInsideUnitSquare` — RVA `0xc52094`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public static Vector2 ClampInsideUnitSquare(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong CFUtils_ClampInsideUnitSquare_RVAc52094(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12918936 = default(float);
        float __arm64_float_flags_left_12918948 = default(float);
        float __arm64_float_flags_left_12918972 = default(float);
        float __arm64_float_flags_left_12918984 = default(float);
        float __arm64_float_flags_left_12919000 = default(float);
        float __arm64_float_flags_right_12918936 = default(float);
        float __arm64_float_flags_right_12918948 = default(float);
        float __arm64_float_flags_right_12918972 = default(float);
        float __arm64_float_flags_right_12918984 = default(float);
        float __arm64_float_flags_right_12919000 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12918936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12918936 > __arm64_float_flags_right_12918936))
        {
            goto label_0xC520AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC520A0UL);
        }
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        __arm64_float_flags_left_12918948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12918948 >= __arm64_float_flags_right_12918948) || ((__arm64_float_flags_left_12918948 != __arm64_float_flags_left_12918948) || (__arm64_float_flags_right_12918948 != __arm64_float_flags_right_12918948))))
        {
            goto label_0xC520B8;
        }
        else
        {
            goto label_0xC520AC;
        }
        label_0xC520AC:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        goto label_0xC520B8;
        label_0xC520B8:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12918972 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918972 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12918972 > __arm64_float_flags_right_12918972))
        {
            goto label_0xC520D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC520C4UL);
        }
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        __arm64_float_flags_left_12918984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12918984 >= __arm64_float_flags_right_12918984) || ((__arm64_float_flags_left_12918984 != __arm64_float_flags_left_12918984) || (__arm64_float_flags_right_12918984 != __arm64_float_flags_right_12918984))))
        {
            goto label_0xC520E0;
        }
        else
        {
            goto label_0xC520D0;
        }
        label_0xC520D0:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12919000 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12919000 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12919000 < __arm64_float_flags_right_12919000) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        goto label_0xC520E0;
        label_0xC520E0:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ChangeMatrixTranl` — RVA `0xc52424`

- Lift status: **exact**; input span: 60 bytes; span to next metadata RVA: 60 bytes.
- Metadata signature: `public static Matrix4x4 ChangeMatrixTranl(Matrix4x4 m, Vector3 newTransl) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong CFUtils_ChangeMatrixTranl_RVAc52424(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12919876 = default(ulong);
        ulong __arm64_pair_address_12919880 = default(ulong);
        ulong __arm64_pair_address_12919884 = default(ulong);
        ulong __arm64_pair_address_12919888 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x3CUL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x2 = 0x0UL;
        x19 = x0;
        x20 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x178708CUL /* metadata target: Matrix4x4.SetColumn */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_12919876 = unchecked((ulong)((x19) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919876);
#else
        v1 = __ReadVector128(__arm64_pair_address_12919876);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919876) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919876) + (0x10UL))));
#endif
        __arm64_pair_address_12919880 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919880);
#else
        v3 = __ReadVector128(__arm64_pair_address_12919880);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919880) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919880) + (0x10UL))));
#endif
        __arm64_pair_address_12919884 = unchecked((ulong)((x20) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919884, v1);
#else
        __WriteVector128(__arm64_pair_address_12919884, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919884) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919884) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12919888 = x20;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919888, v3);
#else
        __WriteVector128(__arm64_pair_address_12919888, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919888) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919888) + (0x10UL))), v2);
#endif
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `CFUtils.TransformRect` — RVA `0xc52460`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public static Rect TransformRect(Rect r, Matrix4x4 tr, bool round) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong CFUtils_TransformRect_RVAc52460(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12919912 = default(ulong);
        ulong __arm64_pair_address_12919916 = default(ulong);
        ulong __arm64_pair_address_12919932 = default(ulong);
        ulong __arm64_pair_address_12919936 = default(ulong);
        ulong __arm64_pair_address_12919944 = default(ulong);
        ulong __arm64_pair_address_12919948 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x70UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x60UL))), x30);
        __arm64_pair_address_12919912 = unchecked((ulong)((x0) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v5 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919912);
#else
        v5 = __ReadVector128(__arm64_pair_address_12919912);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919912) + (0x10UL))));
#else
        v4 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919912) + (0x10UL))));
#endif
        __arm64_pair_address_12919916 = x0;
#if IL2CPPREC_RUNTIME_VECTOR128
        v7 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919916);
#else
        v7 = __ReadVector128(__arm64_pair_address_12919916);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v6 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919916) + (0x10UL))));
#else
        v6 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919916) + (0x10UL))));
#endif
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x0 = sp;
        __arm64_pair_address_12919932 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919932, v5);
#else
        __WriteVector128(__arm64_pair_address_12919932, v5);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919932) + (0x10UL))), v4);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919932) + (0x10UL))), v4);
#endif
        __arm64_pair_address_12919936 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919936, v7);
#else
        __WriteVector128(__arm64_pair_address_12919936, v7);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919936) + (0x10UL))), v6);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919936) + (0x10UL))), v6);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xC51858UL /* metadata target: CFUtils.TransformRectAsBounds */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_12919944 = unchecked((ulong)((sp) + (0x48UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12919944)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12919944) + (0x4UL))))), 0));
        __arm64_pair_address_12919948 = unchecked((ulong)((sp) + (0x54UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12919948)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12919948) + (0x4UL))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ClampRectInside` — RVA `0xc524ac`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public static Vector2 ClampRectInside(Rect rect, bool rectIsRound, Rect limiterRect, bool limiterIsRound) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong CFUtils_ClampRectInside_RVAc524ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC524B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC524B0UL);
        }
        return RuntimeCalls.InvokeDirect(0xC58F50UL /* metadata target: CFUtils.ClampEllipseInsideEllipse */);
        label_0xC524B4:
        ;
        return RuntimeCalls.InvokeDirect(0xC59144UL /* metadata target: CFUtils.ClampRectInsideRect */);
        return default(ulong);
    }
```

## `CFUtils.ClampInsideRect` — RVA `0xc52ca4`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `public static Vector2 ClampInsideRect(Vector2 v, Rect r) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong CFUtils_ClampInsideRect_RVAc52ca4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12922024 = default(float);
        float __arm64_float_flags_left_12922032 = default(float);
        float __arm64_float_flags_left_12922040 = default(float);
        float __arm64_float_flags_left_12922052 = default(float);
        float __arm64_float_flags_left_12922088 = default(float);
        float __arm64_float_flags_left_12922104 = default(float);
        float __arm64_float_flags_left_12922124 = default(float);
        float __arm64_float_flags_left_12922136 = default(float);
        float __arm64_float_flags_left_12922152 = default(float);
        float __arm64_float_flags_right_12922024 = default(float);
        float __arm64_float_flags_right_12922032 = default(float);
        float __arm64_float_flags_right_12922040 = default(float);
        float __arm64_float_flags_right_12922052 = default(float);
        float __arm64_float_flags_right_12922088 = default(float);
        float __arm64_float_flags_right_12922104 = default(float);
        float __arm64_float_flags_right_12922124 = default(float);
        float __arm64_float_flags_right_12922136 = default(float);
        float __arm64_float_flags_right_12922152 = default(float);
        float __arm64_fp_left_12922100 = default(float);
        float __arm64_fp_right_12922100 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12922024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12922024 >= __arm64_float_flags_right_12922024) || ((__arm64_float_flags_left_12922024 != __arm64_float_flags_left_12922024) || (__arm64_float_flags_right_12922024 != __arm64_float_flags_right_12922024))))
        {
            goto label_0xC52CD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52CB0UL);
        }
        __arm64_float_flags_left_12922032 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922032 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12922032 < __arm64_float_flags_right_12922032) || ((__arm64_float_flags_left_12922032 != __arm64_float_flags_left_12922032) || (__arm64_float_flags_right_12922032 != __arm64_float_flags_right_12922032))))
        {
            goto label_0xC52CD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52CB8UL);
        }
        __arm64_float_flags_left_12922040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12922040 < __arm64_float_flags_right_12922040) || ((__arm64_float_flags_left_12922040 != __arm64_float_flags_left_12922040) || (__arm64_float_flags_right_12922040 != __arm64_float_flags_right_12922040))))
        {
            goto label_0xC52CD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52CC0UL);
        }
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12922052 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922052 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12922052 >= __arm64_float_flags_right_12922052) || ((__arm64_float_flags_left_12922052 != __arm64_float_flags_left_12922052) || (__arm64_float_flags_right_12922052 != __arm64_float_flags_right_12922052))))
        {
            goto label_0xC52CD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52CCCUL);
        }
        return x0;
        label_0xC52CD0:
        ;
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12922088 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922088 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        if ((__arm64_float_flags_left_12922088 > __arm64_float_flags_right_12922088))
        {
            goto label_0xC52D04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52CF4UL);
        }
        __arm64_fp_left_12922100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_fp_right_12922100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(unchecked((float)((__arm64_fp_left_12922100) * (__arm64_fp_right_12922100)))))), 0));
        __arm64_float_flags_left_12922104 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922104 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        if (((__arm64_float_flags_left_12922104 >= __arm64_float_flags_right_12922104) || ((__arm64_float_flags_left_12922104 != __arm64_float_flags_left_12922104) || (__arm64_float_flags_right_12922104 != __arm64_float_flags_right_12922104))))
        {
            goto label_0xC52D0C;
        }
        else
        {
            goto label_0xC52D04;
        }
        label_0xC52D04:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        goto label_0xC52D0C;
        label_0xC52D0C:
        ;
        __arm64_float_flags_left_12922124 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922124 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12922124 > __arm64_float_flags_right_12922124))
        {
            goto label_0xC52D20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52D14UL);
        }
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)))), 0));
        __arm64_float_flags_left_12922136 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922136 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12922136 >= __arm64_float_flags_right_12922136) || ((__arm64_float_flags_left_12922136 != __arm64_float_flags_left_12922136) || (__arm64_float_flags_right_12922136 != __arm64_float_flags_right_12922136))))
        {
            goto label_0xC52D30;
        }
        else
        {
            goto label_0xC52D20;
        }
        label_0xC52D20:
        ;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12922152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12922152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12922152 < __arm64_float_flags_right_12922152) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        goto label_0xC52D30;
        label_0xC52D30:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmartDeltaAngle` — RVA `0xc57458`

- Lift status: **partial**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `public static float SmartDeltaAngle(float startAngle, float curAngle, float lastDelta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintm' at 0xc57474

```csharp
public static ulong CFUtils_SmartDeltaAngle_RVAc57458(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12940428 = default(float);
        float __arm64_float_flags_left_12940444 = default(float);
        float __arm64_float_flags_right_12940428 = default(float);
        float __arm64_float_flags_right_12940444 = default(float);
        float __arm64_fp_left_12940424 = default(float);
        float __arm64_fp_right_12940424 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC57474UL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        __arm64_fp_left_12940424 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12940424 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12940424 != __arm64_fp_left_12940424) ? __arm64_fp_left_12940424 : ((__arm64_fp_right_12940424 != __arm64_fp_right_12940424) ? __arm64_fp_right_12940424 : (((__arm64_fp_left_12940424 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12940424 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12940424), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12940424), 0))))), 0) : ((__arm64_fp_left_12940424 <= __arm64_fp_right_12940424) ? __arm64_fp_left_12940424 : __arm64_fp_right_12940424))))), 0));
        __arm64_float_flags_left_12940428 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12940428 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12940428 >= __arm64_float_flags_right_12940428) || ((__arm64_float_flags_left_12940428 != __arm64_float_flags_left_12940428) || (__arm64_float_flags_right_12940428 != __arm64_float_flags_right_12940428))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12940444 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12940444 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12940444 > __arm64_float_flags_right_12940444) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.MoveTowards` — RVA `0xc574ac`

- Lift status: **partial**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public static float MoveTowards(float a, float b, float secondsPerUnit, float deltaTime, float epsilon) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fabd' at 0xc574c4

```csharp
public static ulong CFUtils_MoveTowards_RVAc574ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12940460 = default(float);
        float __arm64_float_flags_left_12940476 = default(float);
        float __arm64_float_flags_left_12940488 = default(float);
        float __arm64_float_flags_left_12940508 = default(float);
        float __arm64_float_flags_left_12940520 = default(float);
        float __arm64_float_flags_right_12940460 = default(float);
        float __arm64_float_flags_right_12940476 = default(float);
        float __arm64_float_flags_right_12940488 = default(float);
        float __arm64_float_flags_right_12940508 = default(float);
        float __arm64_float_flags_right_12940520 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        __arm64_float_flags_left_12940460 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12940460 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12940460 <= __arm64_float_flags_right_12940460))
        {
        }
        else
        {
            x8 = 0x432000UL;
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
            __arm64_float_flags_left_12940476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12940476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
            if ((__arm64_float_flags_left_12940476 < __arm64_float_flags_right_12940476))
            {
            }
            else
            {
                RuntimeCalls.Unsupported("fabd", 0xC574C4UL);
                __arm64_float_flags_left_12940488 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12940488 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
                if ((__arm64_float_flags_left_12940488 <= __arm64_float_flags_right_12940488))
                {
                }
                else
                {
                    v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                    v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)))), 0));
                    __arm64_float_flags_left_12940508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
                    __arm64_float_flags_right_12940508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
                    v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12940508 >= __arm64_float_flags_right_12940508) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                    __arm64_float_flags_left_12940520 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
                    __arm64_float_flags_right_12940520 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12940520 > __arm64_float_flags_right_12940520) || ((__arm64_float_flags_left_12940520 != __arm64_float_flags_left_12940520) || (__arm64_float_flags_right_12940520 != __arm64_float_flags_right_12940520))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
                }
            }
        }
        label_0xC574F0:
        ;
        v0 = v1;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.get_realDeltaTimeClamped` — RVA `0xc5834c`

- Lift status: **partial**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public static float get_realDeltaTimeClamped() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fminnm' at 0xc58358

```csharp
public static ulong CFUtils_get_realDeltaTimeClamped_RVAc5834c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        RuntimeCalls.Unsupported("fminnm", 0xC58358UL);
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `CFUtils.get_editorStopped` — RVA `0xc58364`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public static bool get_editorStopped() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint CFUtils_get_editorStopped_RVAc58364(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `CFUtils.get_forcedMobileModeEnabled` — RVA `0xc5836c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public static bool get_forcedMobileModeEnabled() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint CFUtils_get_forcedMobileModeEnabled_RVAc5836c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `CFUtils.LogPrefixFull` — RVA `0xc58374`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public static string LogPrefixFull() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong CFUtils_LogPrefixFull_RVAc58374(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x19 = 0x1A8C000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x297UL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x890UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xEB8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEB8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x890UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x297UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC583BC:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AEB8UL /* metadata target: Time.get_frameCount */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x0)));
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x2 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x3 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.LogPrefix` — RVA `0xc583fc`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public static string LogPrefix() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong CFUtils_LogPrefix_RVAc583fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x19 = 0x1A8C000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x298UL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x890UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xEB8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEB8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x890UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x298UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC58444:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AEB8UL /* metadata target: Time.get_frameCount */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x0)));
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x2 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x3 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ApplyDeltaInput` — RVA `0xc58484`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public static float ApplyDeltaInput(float accum, float delta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong CFUtils_ApplyDeltaInput_RVAc58484(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12944516 = default(float);
        float __arm64_float_flags_left_12944524 = default(float);
        float __arm64_float_flags_left_12944544 = default(float);
        float __arm64_float_flags_left_12944552 = default(float);
        float __arm64_float_flags_right_12944516 = default(float);
        float __arm64_float_flags_right_12944524 = default(float);
        float __arm64_float_flags_right_12944544 = default(float);
        float __arm64_float_flags_right_12944552 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_float_flags_left_12944516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12944516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12944516 < __arm64_float_flags_right_12944516) || ((__arm64_float_flags_left_12944516 != __arm64_float_flags_left_12944516) || (__arm64_float_flags_right_12944516 != __arm64_float_flags_right_12944516))))
        {
        }
        else
        {
            __arm64_float_flags_left_12944524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12944524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
            if (((__arm64_float_flags_left_12944524 < __arm64_float_flags_right_12944524) || ((__arm64_float_flags_left_12944524 != __arm64_float_flags_left_12944524) || (__arm64_float_flags_right_12944524 != __arm64_float_flags_right_12944524))))
            {
            }
            else
            {
                return x0;
            }
        }
        label_0xC584A0:
        ;
        __arm64_float_flags_left_12944544 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12944544 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12944544 >= __arm64_float_flags_right_12944544) || ((__arm64_float_flags_left_12944544 != __arm64_float_flags_left_12944544) || (__arm64_float_flags_right_12944544 != __arm64_float_flags_right_12944544))))
        {
        }
        else
        {
            __arm64_float_flags_left_12944552 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12944552 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
            if (((__arm64_float_flags_left_12944552 >= __arm64_float_flags_right_12944552) || ((__arm64_float_flags_left_12944552 != __arm64_float_flags_left_12944552) || (__arm64_float_flags_right_12944552 != __arm64_float_flags_right_12944552))))
            {
            }
            else
            {
                return x0;
            }
        }
        label_0xC584BC:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ApplyDeltaInputInt` — RVA `0xc584c4`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public static int ApplyDeltaInputInt(int accum, int delta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static uint CFUtils_ApplyDeltaInputInt_RVAc584c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12944588 = default(uint);
        uint __arm64_flags_left_12944600 = default(uint);
        uint __arm64_flags_left_12944616 = default(uint);
        uint __arm64_flags_result_12944600 = default(uint);
        uint __arm64_flags_right_12944588 = default(uint);
        uint __arm64_flags_right_12944600 = default(uint);
        uint __arm64_flags_right_12944616 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) | (unchecked((uint)(x0)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            label_0xC584D8:
            ;
            __arm64_flags_left_12944600 = unchecked((uint)(x1));
            __arm64_flags_right_12944600 = unchecked((uint)(x0));
            __arm64_flags_result_12944600 = unchecked((uint)((__arm64_flags_left_12944600) & (__arm64_flags_right_12944600)));
            if (((unchecked((int)(__arm64_flags_result_12944600)) < unchecked((int)0x0UL)) != false))
            {
                label_0xC584E8:
                ;
                __arm64_flags_left_12944616 = unchecked((uint)(x0));
                __arm64_flags_right_12944616 = unchecked((uint)(x1));
                x0 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944616) - (__arm64_flags_right_12944616))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12944616)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12944616)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944616) - (__arm64_flags_right_12944616))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12944616)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x0)) : unchecked((uint)(x1)))));
                return unchecked((uint)(x0));
            }
            else
            {
                x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) + (unchecked((uint)(x0)))))));
                return unchecked((uint)(x0));
            }
        }
        else
        {
            __arm64_flags_left_12944588 = unchecked((uint)(x0));
            __arm64_flags_right_12944588 = unchecked((uint)(x1));
            x0 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_12944588) - (__arm64_flags_right_12944588))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944588) - (__arm64_flags_right_12944588))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12944588)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12944588)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944588) - (__arm64_flags_right_12944588))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12944588)) < unchecked((int)0x0UL)))))) ? unchecked((uint)(x0)) : unchecked((uint)(x1)))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `CFUtils.ApplyPositveDeltaInput` — RVA `0xc584f4`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public static float ApplyPositveDeltaInput(float positiveAccum, float delta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong CFUtils_ApplyPositveDeltaInput_RVAc584f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ApplyNegativeDeltaInput` — RVA `0xc58508`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public static float ApplyNegativeDeltaInput(float negativeAccum, float delta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong CFUtils_ApplyNegativeDeltaInput_RVAc58508(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ApplySignedDeltaInput` — RVA `0xc5851c`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public static void ApplySignedDeltaInput(float v, ref float plusAccum, ref float minusAccum) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong CFUtils_ApplySignedDeltaInput_RVAc5851c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12944668 = default(float);
        float __arm64_float_flags_left_12944680 = default(float);
        float __arm64_float_flags_left_12944700 = default(float);
        float __arm64_float_flags_right_12944668 = default(float);
        float __arm64_float_flags_right_12944680 = default(float);
        float __arm64_float_flags_right_12944700 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_float_flags_left_12944668 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12944668 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12944668 >= __arm64_float_flags_right_12944668))
        {
            label_0xC58538:
            ;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x0)), 0));
            __arm64_float_flags_left_12944700 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12944700 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_12944700 >= __arm64_float_flags_right_12944700) || ((__arm64_float_flags_left_12944700 != __arm64_float_flags_left_12944700) || (__arm64_float_flags_right_12944700 != __arm64_float_flags_right_12944700))))
            {
            }
            else
            {
                RuntimeMemory.WriteF32(x0, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                return x0;
            }
        }
        else
        {
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x1)), 0));
            __arm64_float_flags_left_12944680 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12944680 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_12944680 <= __arm64_float_flags_right_12944680) || ((__arm64_float_flags_left_12944680 != __arm64_float_flags_left_12944680) || (__arm64_float_flags_right_12944680 != __arm64_float_flags_right_12944680))))
            {
            }
            else
            {
                RuntimeMemory.WriteF32(x1, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            }
        }
        label_0xC58534:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ApplySignedDeltaInputInt` — RVA `0xc5854c`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public static void ApplySignedDeltaInputInt(int v, ref int plusAccum, ref int minusAccum) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong CFUtils_ApplySignedDeltaInputInt_RVAc5854c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12944724 = default(uint);
        uint __arm64_flags_left_12944744 = default(uint);
        uint __arm64_flags_right_12944724 = default(uint);
        uint __arm64_flags_right_12944744 = default(uint);
        ulong x8 = default(ulong);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            label_0xC58564:
            ;
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x2)));
            __arm64_flags_left_12944744 = unchecked((uint)(x8));
            __arm64_flags_right_12944744 = unchecked((uint)(x0));
            if (((unchecked((uint)((__arm64_flags_left_12944744) - (__arm64_flags_right_12944744))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944744) - (__arm64_flags_right_12944744))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12944744)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12944744)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944744) - (__arm64_flags_right_12944744))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12944744)) < unchecked((int)0x0UL)))))))
            {
            }
            else
            {
                RuntimeMemory.WriteU32(x2, unchecked((uint)(x0)));
            }
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x1)));
            __arm64_flags_left_12944724 = unchecked((uint)(x8));
            __arm64_flags_right_12944724 = unchecked((uint)(x0));
            if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944724) - (__arm64_flags_right_12944724))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12944724)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12944724)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12944724) - (__arm64_flags_right_12944724))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12944724)) < unchecked((int)0x0UL))))))
            {
            }
            else
            {
                RuntimeMemory.WriteU32(x1, unchecked((uint)(x0)));
                return x0;
            }
        }
        label_0xC58574:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.GetScrollValue` — RVA `0xc58578`

- Lift status: **partial**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public static int GetScrollValue(float drag, int prevScroll, float thresh, float magnet) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintm' at 0xc585d8; reason: Unsupported instruction 'fcvtms' at 0xc585e4

```csharp
public static uint CFUtils_GetScrollValue_RVAc58578(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12944836 = default(float);
        float __arm64_float_flags_left_12944872 = default(float);
        float __arm64_float_flags_left_12944880 = default(float);
        float __arm64_float_flags_right_12944836 = default(float);
        float __arm64_float_flags_right_12944872 = default(float);
        float __arm64_float_flags_right_12944880 = default(float);
        ulong __arm64_pair_address_12944760 = default(ulong);
        ulong __arm64_pair_address_12944888 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12944760 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12944760, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12944760) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12944760;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2CCUL))))))));
        v8 = v1;
        v9 = v0;
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
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x2CCUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC585A8:
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
        label_0xC585C0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)))), 0));
        __arm64_float_flags_left_12944836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12944836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12944836 < __arm64_float_flags_right_12944836) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC585D8UL);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("fcvtms", 0xC585E4UL);
        __arm64_float_flags_left_12944872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12944872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(((__arm64_float_flags_left_12944872 == __arm64_float_flags_right_12944872) ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
        __arm64_float_flags_left_12944880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12944880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x0 = unchecked((ulong)(((__arm64_float_flags_left_12944880 < __arm64_float_flags_right_12944880) ? unchecked((uint)((-(unchecked((uint)(x8)))))) : unchecked((uint)(x8)))));
        __arm64_pair_address_12944888 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12944888)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12944888) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12944888) + (0x20UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `CFUtils.GetLerpFactor` — RVA `0xc58600`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `private static float GetLerpFactor(float smoothingTime, float deltaTime, float maxLerpFactor) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong CFUtils_GetLerpFactor_RVAc58600(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmoothTowards` — RVA `0xc5861c`

- Lift status: **partial**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public static float SmoothTowards(float a, float b, float smoothingTime, float deltaTime, float epsilon, float maxLeftFactor = 0.75) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fabd' at 0xc5862c

```csharp
public static ulong CFUtils_SmoothTowards_RVAc5861c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12944932 = default(float);
        float __arm64_float_flags_left_12944944 = default(float);
        float __arm64_float_flags_left_12944956 = default(float);
        float __arm64_float_flags_left_12944968 = default(float);
        float __arm64_float_flags_left_12944980 = default(float);
        float __arm64_float_flags_right_12944932 = default(float);
        float __arm64_float_flags_right_12944944 = default(float);
        float __arm64_float_flags_right_12944956 = default(float);
        float __arm64_float_flags_right_12944968 = default(float);
        float __arm64_float_flags_right_12944980 = default(float);
        float __arm64_fp_left_12944976 = default(float);
        float __arm64_fp_right_12944976 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12944932 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12944932 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12944932 < __arm64_float_flags_right_12944932))
        {
        }
        else
        {
            RuntimeCalls.Unsupported("fabd", 0xC5862CUL);
            __arm64_float_flags_left_12944944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12944944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
            if ((__arm64_float_flags_left_12944944 <= __arm64_float_flags_right_12944944))
            {
            }
            else
            {
                v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                __arm64_float_flags_left_12944956 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12944956 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12944956 > __arm64_float_flags_right_12944956) || ((__arm64_float_flags_left_12944956 != __arm64_float_flags_left_12944956) || (__arm64_float_flags_right_12944956 != __arm64_float_flags_right_12944956))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
                __arm64_float_flags_left_12944968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12944968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12944968 > __arm64_float_flags_right_12944968) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
                __arm64_fp_left_12944976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
                __arm64_fp_right_12944976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12944976 != __arm64_fp_left_12944976) ? __arm64_fp_left_12944976 : ((__arm64_fp_right_12944976 != __arm64_fp_right_12944976) ? __arm64_fp_right_12944976 : (((__arm64_fp_left_12944976 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12944976 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12944976), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12944976), 0))))), 0) : ((__arm64_fp_left_12944976 <= __arm64_fp_right_12944976) ? __arm64_fp_left_12944976 : __arm64_fp_right_12944976))))), 0));
                __arm64_float_flags_left_12944980 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12944980 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12944980 >= __arm64_float_flags_right_12944980) || ((__arm64_float_flags_left_12944980 != __arm64_float_flags_left_12944980) || (__arm64_float_flags_right_12944980 != __arm64_float_flags_right_12944980))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            }
        }
        label_0xC5866C:
        ;
        v0 = v1;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmoothTowardsAngle` — RVA `0xc58674`

- Lift status: **partial**; input span: 264 bytes; span to next metadata RVA: 264 bytes.
- Metadata signature: `public static float SmoothTowardsAngle(float a, float b, float smoothingTime, float deltaTime, float epsilon, float maxLeftFactor = 0.75) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=8 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintm' at 0xc5868c; reason: Unsupported instruction 'fcsel' at 0xc586b0; reason: Unknown IR expression at 0xc586b0; reason: Unsupported instruction 'fcsel' at 0xc586e8; reason: Unknown IR expression at 0xc586e8; reason: Unsupported instruction 'fcsel' at 0xc586fc; reason: Unknown IR expression at 0xc586fc; reason: Unsupported instruction 'frintm' at 0xc58708

```csharp
public static ulong CFUtils_SmoothTowardsAngle_RVAc58674(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12945060 = default(float);
        float __arm64_float_flags_left_12945084 = default(float);
        float __arm64_float_flags_left_12945092 = default(float);
        float __arm64_float_flags_left_12945104 = default(float);
        float __arm64_float_flags_left_12945116 = default(float);
        float __arm64_float_flags_left_12945140 = default(float);
        float __arm64_float_flags_left_12945184 = default(float);
        float __arm64_float_flags_left_12945204 = default(float);
        float __arm64_float_flags_left_12945216 = default(float);
        float __arm64_float_flags_left_12945228 = default(float);
        float __arm64_float_flags_left_12945244 = default(float);
        float __arm64_float_flags_left_12945260 = default(float);
        float __arm64_float_flags_right_12945060 = default(float);
        float __arm64_float_flags_right_12945084 = default(float);
        float __arm64_float_flags_right_12945092 = default(float);
        float __arm64_float_flags_right_12945104 = default(float);
        float __arm64_float_flags_right_12945116 = default(float);
        float __arm64_float_flags_right_12945140 = default(float);
        float __arm64_float_flags_right_12945184 = default(float);
        float __arm64_float_flags_right_12945204 = default(float);
        float __arm64_float_flags_right_12945216 = default(float);
        float __arm64_float_flags_right_12945228 = default(float);
        float __arm64_float_flags_right_12945244 = default(float);
        float __arm64_float_flags_right_12945260 = default(float);
        float __arm64_fp_left_12945056 = default(float);
        float __arm64_fp_left_12945180 = default(float);
        float __arm64_fp_left_12945212 = default(float);
        float __arm64_fp_right_12945056 = default(float);
        float __arm64_fp_right_12945180 = default(float);
        float __arm64_fp_right_12945212 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC5868CUL);
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_fp_left_12945056 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_fp_right_12945056 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12945056 != __arm64_fp_left_12945056) ? __arm64_fp_left_12945056 : ((__arm64_fp_right_12945056 != __arm64_fp_right_12945056) ? __arm64_fp_right_12945056 : (((__arm64_fp_left_12945056 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12945056 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12945056), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12945056), 0))))), 0) : ((__arm64_fp_left_12945056 <= __arm64_fp_right_12945056) ? __arm64_fp_left_12945056 : __arm64_fp_right_12945056))))), 0));
        __arm64_float_flags_left_12945060 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945060 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x8 = 0x432000UL;
        RuntimeCalls.Unsupported("fcsel", 0xC586B0UL);
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945084 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945084 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12945084 > __arm64_float_flags_right_12945084) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12945092 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945092 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945092 < __arm64_float_flags_right_12945092))
        {
            goto label_0xC58774;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC586CCUL);
        }
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12945104 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945104 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945104 <= __arm64_float_flags_right_12945104))
        {
            goto label_0xC58774;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC586D8UL);
        }
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945116 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945116 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        RuntimeCalls.Unsupported("fcsel", 0xC586E8UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12945140 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945140 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
        RuntimeCalls.Unsupported("fcsel", 0xC586FCUL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC58708UL);
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        __arm64_fp_left_12945180 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_fp_right_12945180 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12945180 != __arm64_fp_left_12945180) ? __arm64_fp_left_12945180 : ((__arm64_fp_right_12945180 != __arm64_fp_right_12945180) ? __arm64_fp_right_12945180 : (((__arm64_fp_left_12945180 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12945180 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12945180), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12945180), 0))))), 0) : ((__arm64_fp_left_12945180 <= __arm64_fp_right_12945180) ? __arm64_fp_left_12945180 : __arm64_fp_right_12945180))))), 0));
        __arm64_float_flags_left_12945184 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945184 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945184 >= __arm64_float_flags_right_12945184) || ((__arm64_float_flags_left_12945184 != __arm64_float_flags_left_12945184) || (__arm64_float_flags_right_12945184 != __arm64_float_flags_right_12945184))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
        RuntimeCalls.Unsupported("fabd", 0xC5872CUL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945204 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945204 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12945204 > __arm64_float_flags_right_12945204) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        __arm64_fp_left_12945212 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_fp_right_12945212 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(unchecked((float)((__arm64_fp_left_12945212) * (__arm64_fp_right_12945212)))))), 0));
        __arm64_float_flags_left_12945216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        if (((__arm64_float_flags_left_12945216 <= __arm64_float_flags_right_12945216) || ((__arm64_float_flags_left_12945216 != __arm64_float_flags_left_12945216) || (__arm64_float_flags_right_12945216 != __arm64_float_flags_right_12945216))))
        {
            goto label_0xC58754;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5874CUL);
        }
        __arm64_float_flags_left_12945228 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945228 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945228 < __arm64_float_flags_right_12945228))
        {
            goto label_0xC58774;
        }
        else
        {
            goto label_0xC58754;
        }
        label_0xC58754:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945244 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945244 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        RuntimeCalls.Unsupported("fabd", 0xC58760UL);
        RuntimeCalls.Unsupported("fcsel", 0xC58764UL);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945260 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945260 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945260 > __arm64_float_flags_right_12945260) || ((__arm64_float_flags_left_12945260 != __arm64_float_flags_left_12945260) || (__arm64_float_flags_right_12945260 != __arm64_float_flags_right_12945260))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        goto label_0xC58774;
        label_0xC58774:
        ;
        v0 = v1;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmoothTowardsVec2` — RVA `0xc5877c`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `public static Vector2 SmoothTowardsVec2(Vector2 a, Vector2 b, float smoothingTime, float deltaTime, float sqrEpsilon, float maxLeftFactor = 0.75) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong CFUtils_SmoothTowardsVec2_RVAc5877c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12945280 = default(float);
        float __arm64_float_flags_left_12945292 = default(float);
        float __arm64_float_flags_left_12945316 = default(float);
        float __arm64_float_flags_left_12945344 = default(float);
        float __arm64_float_flags_left_12945356 = default(float);
        float __arm64_float_flags_left_12945368 = default(float);
        float __arm64_float_flags_left_12945384 = default(float);
        float __arm64_float_flags_right_12945280 = default(float);
        float __arm64_float_flags_right_12945292 = default(float);
        float __arm64_float_flags_right_12945316 = default(float);
        float __arm64_float_flags_right_12945344 = default(float);
        float __arm64_float_flags_right_12945356 = default(float);
        float __arm64_float_flags_right_12945368 = default(float);
        float __arm64_float_flags_right_12945384 = default(float);
        float __arm64_fp_left_12945380 = default(float);
        float __arm64_fp_right_12945380 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v18 = default(RuntimeVector128);
        RuntimeVector128 v19 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
        __arm64_float_flags_left_12945280 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945280 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12945280 != __arm64_float_flags_right_12945280) || ((__arm64_float_flags_left_12945280 != __arm64_float_flags_left_12945280) || (__arm64_float_flags_right_12945280 != __arm64_float_flags_right_12945280))))
        {
            goto label_0xC587A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58788UL);
        }
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12945292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945292 < __arm64_float_flags_right_12945292))
        {
            goto label_0xC58800;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58794UL);
        }
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC587C8;
        label_0xC587A0:
        ;
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12945316 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945316 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945316 < __arm64_float_flags_right_12945316))
        {
            goto label_0xC58800;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC587ACUL);
        }
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945344 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945344 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945344 <= __arm64_float_flags_right_12945344))
        {
            goto label_0xC58800;
        }
        else
        {
            goto label_0xC587C8;
        }
        label_0xC587C8:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945356 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945356 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945356 > __arm64_float_flags_right_12945356) || ((__arm64_float_flags_left_12945356 != __arm64_float_flags_left_12945356) || (__arm64_float_flags_right_12945356 != __arm64_float_flags_right_12945356))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12945368 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945368 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12945368 > __arm64_float_flags_right_12945368) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_fp_left_12945380 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_fp_right_12945380 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12945380 != __arm64_fp_left_12945380) ? __arm64_fp_left_12945380 : ((__arm64_fp_right_12945380 != __arm64_fp_right_12945380) ? __arm64_fp_right_12945380 : (((__arm64_fp_left_12945380 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12945380 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12945380), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12945380), 0))))), 0) : ((__arm64_fp_left_12945380 <= __arm64_fp_right_12945380) ? __arm64_fp_left_12945380 : __arm64_fp_right_12945380))))), 0));
        __arm64_float_flags_left_12945384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945384 >= __arm64_float_flags_right_12945384) || ((__arm64_float_flags_left_12945384 != __arm64_float_flags_left_12945384) || (__arm64_float_flags_right_12945384 != __arm64_float_flags_right_12945384))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        goto label_0xC58800;
        label_0xC58800:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmoothTowardsVec3` — RVA `0xc5880c`

- Lift status: **exact**; input span: 176 bytes; span to next metadata RVA: 176 bytes.
- Metadata signature: `public static Vector3 SmoothTowardsVec3(Vector3 a, Vector3 b, float smoothingTime, float deltaTime, float sqrEpsilon, float maxLeftFactor = 0.75) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong CFUtils_SmoothTowardsVec3_RVAc5880c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12945432 = default(float);
        float __arm64_float_flags_left_12945440 = default(float);
        float __arm64_float_flags_left_12945464 = default(float);
        float __arm64_float_flags_left_12945504 = default(float);
        float __arm64_float_flags_left_12945520 = default(float);
        float __arm64_float_flags_left_12945532 = default(float);
        float __arm64_float_flags_left_12945548 = default(float);
        float __arm64_float_flags_right_12945432 = default(float);
        float __arm64_float_flags_right_12945440 = default(float);
        float __arm64_float_flags_right_12945464 = default(float);
        float __arm64_float_flags_right_12945504 = default(float);
        float __arm64_float_flags_right_12945520 = default(float);
        float __arm64_float_flags_right_12945532 = default(float);
        float __arm64_float_flags_right_12945548 = default(float);
        float __arm64_fp_left_12945544 = default(float);
        float __arm64_fp_right_12945544 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v18 = default(RuntimeVector128);
        RuntimeVector128 v19 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v20 = default(RuntimeVector128);
        RuntimeVector128 v21 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        x8 = 0x432000UL;
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12945432 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945432 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12945432 != __arm64_float_flags_right_12945432) || ((__arm64_float_flags_left_12945432 != __arm64_float_flags_left_12945432) || (__arm64_float_flags_right_12945432 != __arm64_float_flags_right_12945432))))
        {
            goto label_0xC58838;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58820UL);
        }
        __arm64_float_flags_left_12945440 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945440 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945440 < __arm64_float_flags_right_12945440))
        {
            goto label_0xC588AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58828UL);
        }
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC58868;
        label_0xC58838:
        ;
        __arm64_float_flags_left_12945464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945464 < __arm64_float_flags_right_12945464))
        {
            goto label_0xC588AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58840UL);
        }
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v21 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0))))), 0));
        v21 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))))), 0));
        v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945504 <= __arm64_float_flags_right_12945504))
        {
            goto label_0xC588AC;
        }
        else
        {
            goto label_0xC58868;
        }
        label_0xC58868:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12945520 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945520 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945520 > __arm64_float_flags_right_12945520) || ((__arm64_float_flags_left_12945520 != __arm64_float_flags_left_12945520) || (__arm64_float_flags_right_12945520 != __arm64_float_flags_right_12945520))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12945532 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945532 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12945532 > __arm64_float_flags_right_12945532) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_fp_left_12945544 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_fp_right_12945544 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12945544 != __arm64_fp_left_12945544) ? __arm64_fp_left_12945544 : ((__arm64_fp_right_12945544 != __arm64_fp_right_12945544) ? __arm64_fp_right_12945544 : (((__arm64_fp_left_12945544 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12945544 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12945544), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12945544), 0))))), 0) : ((__arm64_fp_left_12945544 <= __arm64_fp_right_12945544) ? __arm64_fp_left_12945544 : __arm64_fp_right_12945544))))), 0));
        __arm64_float_flags_left_12945548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945548 >= __arm64_float_flags_right_12945548) || ((__arm64_float_flags_left_12945548 != __arm64_float_flags_left_12945548) || (__arm64_float_flags_right_12945548 != __arm64_float_flags_right_12945548))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        goto label_0xC588AC;
        label_0xC588AC:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmoothTowardsColor` — RVA `0xc588bc`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public static Color SmoothTowardsColor(Color a, Color b, float smoothingTime, float deltaTime, float maxLeftFactor = 0.75) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong CFUtils_SmoothTowardsColor_RVAc588bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12945608 = default(float);
        float __arm64_float_flags_left_12945632 = default(float);
        float __arm64_float_flags_left_12945644 = default(float);
        float __arm64_float_flags_left_12945660 = default(float);
        float __arm64_float_flags_right_12945608 = default(float);
        float __arm64_float_flags_right_12945632 = default(float);
        float __arm64_float_flags_right_12945644 = default(float);
        float __arm64_float_flags_right_12945660 = default(float);
        float __arm64_fp_left_12945656 = default(float);
        float __arm64_fp_right_12945656 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v18 = default(RuntimeVector128);
        RuntimeVector128 v19 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12945608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945608 < __arm64_float_flags_right_12945608))
        {
        }
        else
        {
            v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x8UL))))), 0));
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
            v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            __arm64_float_flags_left_12945632 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12945632 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0);
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945632 > __arm64_float_flags_right_12945632) || ((__arm64_float_flags_left_12945632 != __arm64_float_flags_left_12945632) || (__arm64_float_flags_right_12945632 != __arm64_float_flags_right_12945632))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12945644 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12945644 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12945644 > __arm64_float_flags_right_12945644) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
            v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            __arm64_fp_left_12945656 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_fp_right_12945656 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0);
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12945656 != __arm64_fp_left_12945656) ? __arm64_fp_left_12945656 : ((__arm64_fp_right_12945656 != __arm64_fp_right_12945656) ? __arm64_fp_right_12945656 : (((__arm64_fp_left_12945656 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12945656 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12945656), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12945656), 0))))), 0) : ((__arm64_fp_left_12945656 <= __arm64_fp_right_12945656) ? __arm64_fp_left_12945656 : __arm64_fp_right_12945656))))), 0));
            __arm64_float_flags_left_12945660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12945660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945660 >= __arm64_float_flags_right_12945660) || ((__arm64_float_flags_left_12945660 != __arm64_float_flags_left_12945660) || (__arm64_float_flags_right_12945660 != __arm64_float_flags_right_12945660))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        }
        label_0xC58930:
        ;
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmoothTowardsQuat` — RVA `0xc58944`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public static Quaternion SmoothTowardsQuat(Quaternion a, Quaternion b, float smoothingTime, float deltaTime, float maxLeftFactor = 0.75) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong CFUtils_SmoothTowardsQuat_RVAc58944(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12945752 = default(float);
        float __arm64_float_flags_left_12945776 = default(float);
        float __arm64_float_flags_left_12945788 = default(float);
        float __arm64_float_flags_right_12945752 = default(float);
        float __arm64_float_flags_right_12945776 = default(float);
        float __arm64_float_flags_right_12945788 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v18 = default(RuntimeVector128);
        RuntimeVector128 v19 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x20UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        x8 = 0x432000UL;
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x20UL))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12945752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945752 < __arm64_float_flags_right_12945752))
        {
        }
        else
        {
            v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x28UL))))), 0));
            v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x30UL))))), 0));
            x0 = 0x0UL;
            v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
            __arm64_float_flags_left_12945776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12945776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0);
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12945776 > __arm64_float_flags_right_12945776) || ((__arm64_float_flags_left_12945776 != __arm64_float_flags_left_12945776) || (__arm64_float_flags_right_12945776 != __arm64_float_flags_right_12945776))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12945788 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12945788 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0);
            v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12945788 > __arm64_float_flags_right_12945788) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))), 0));
            RuntimeMemory.WriteF32(sp, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x178AF84UL /* metadata target: Quaternion.Slerp */, x0, x1, x2, x3);
            v4 = v0;
            v5 = v1;
            v6 = v2;
            v7 = v3;
        }
        label_0xC5899C:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SmoothDamp` — RVA `0xc589b8`

- Lift status: **partial**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public static float SmoothDamp(float valFrom, float valTo, ref float vel, float smoothingTime, float deltaTime, float epsilon) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fabd' at 0xc589cc

```csharp
public static ulong CFUtils_SmoothDamp_RVAc589b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12945860 = default(float);
        float __arm64_float_flags_left_12945872 = default(float);
        float __arm64_float_flags_right_12945860 = default(float);
        float __arm64_float_flags_right_12945872 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
        v5 = v3;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12945860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945860 < __arm64_float_flags_right_12945860))
        {
            goto label_0xC589EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC589CCUL);
        }
        RuntimeCalls.Unsupported("fabd", 0xC589CCUL);
        __arm64_float_flags_left_12945872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12945872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12945872 <= __arm64_float_flags_right_12945872))
        {
            goto label_0xC589EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3A4UL))))), 0));
        v4 = v5;
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x178C860UL /* metadata target: Mathf.SmoothDamp */);
        label_0xC589EC:
        ;
        v0 = v1;
        RuntimeMemory.WritePtr(x0, unchecked((ulong)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ScaleColorAlpha` — RVA `0xc589f8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public static Color ScaleColorAlpha(Color color, float alphaScale) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong CFUtils_ScaleColorAlpha_RVAc589f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `CFUtils.GetComponentHereOrInParent` — RVA `0xc58a00`

- Lift status: **exact**; input span: 216 bytes; span to next metadata RVA: 216 bytes.
- Metadata signature: `public static Component GetComponentHereOrInParent(Component comp, Type compType) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong CFUtils_GetComponentHereOrInParent_RVAc58a00(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x299UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC58A3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x299UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC58A3C;
        label_0xC58A3C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC58A4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58A48UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC58A4C;
        label_0xC58A4C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        x21 = 0x0UL;
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC58AA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58A64UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC58AD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17921CCUL /* metadata target: Component.GetComponent */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x21 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC58A90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC58A90;
        label_0xC58A90:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC58AB8;
        }
        else
        {
            goto label_0xC58AA4;
        }
        label_0xC58AA4:
        ;
        x0 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC58AB8:
        ;
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x17925E0UL /* metadata target: Component.GetComponentInParent */);
        label_0xC58AD4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `CFUtils.IsStretchyRectTransform` — RVA `0xc58ad8`

- Lift status: **exact**; input span: 232 bytes; span to next metadata RVA: 232 bytes.
- Metadata signature: `public static bool IsStretchyRectTransform(Transform tr) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static uint CFUtils_IsStretchyRectTransform_RVAc58ad8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12946224 = default(ulong);
        ulong __arm64_flags_right_12946224 = default(ulong);
        float __arm64_float_flags_left_12946332 = default(float);
        float __arm64_float_flags_right_12946332 = default(float);
        ulong __arm64_pair_address_12946136 = default(ulong);
        ulong __arm64_pair_address_12946356 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12946136 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12946136, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12946136) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12946136;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x29AUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC58B14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x29AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC58B14;
        label_0xC58B14:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC58B38;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x1C8UL))));
        x10 = RuntimeMemory.ReadU64(x19);
        x9 = RuntimeMemory.ReadU64(x9);
        __arm64_flags_left_12946224 = x10;
        __arm64_flags_right_12946224 = x9;
        x19 = ((unchecked((ulong)((__arm64_flags_left_12946224) - (__arm64_flags_right_12946224))) == 0x0UL) ? x19 : 0x0UL);
        goto label_0xC58B38;
        label_0xC58B38:
        ;
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC58B48;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC58B44UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC58B48;
        label_0xC58B48:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC58BA8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC58B5CUL)));
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC58BBC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C674UL /* metadata target: RectTransform.get_anchorMax */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x179C558UL /* metadata target: RectTransform.get_anchorMin */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2ECUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12946332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        x0 = unchecked((ulong)((((__arm64_float_flags_left_12946332 >= __arm64_float_flags_right_12946332) || ((__arm64_float_flags_left_12946332 != __arm64_float_flags_left_12946332) || (__arm64_float_flags_right_12946332 != __arm64_float_flags_right_12946332))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC58BAC;
        label_0xC58BA8:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC58BAC;
        label_0xC58BAC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_12946356 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12946356)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12946356) + (0x8UL))))), 0));
        return unchecked((uint)(x0));
        label_0xC58BBC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `CFUtils.GetWorldAABB` — RVA `0xc58bc0`

- Lift status: **exact**; input span: 712 bytes; span to next metadata RVA: 712 bytes.
- Metadata signature: `public static Bounds GetWorldAABB(Matrix4x4 tf, Vector3 center, Vector3 size) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=42 (informational only).

```csharp
public static ulong CFUtils_GetWorldAABB_RVAc58bc0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12946508 = default(float);
        float __arm64_float_flags_left_12946520 = default(float);
        float __arm64_float_flags_left_12946532 = default(float);
        float __arm64_float_flags_left_12946572 = default(float);
        float __arm64_float_flags_left_12946580 = default(float);
        float __arm64_float_flags_left_12946588 = default(float);
        float __arm64_float_flags_left_12946596 = default(float);
        float __arm64_float_flags_left_12946604 = default(float);
        float __arm64_float_flags_left_12946612 = default(float);
        float __arm64_float_flags_left_12946644 = default(float);
        float __arm64_float_flags_left_12946652 = default(float);
        float __arm64_float_flags_left_12946660 = default(float);
        float __arm64_float_flags_left_12946668 = default(float);
        float __arm64_float_flags_left_12946676 = default(float);
        float __arm64_float_flags_left_12946692 = default(float);
        float __arm64_float_flags_left_12946720 = default(float);
        float __arm64_float_flags_left_12946728 = default(float);
        float __arm64_float_flags_left_12946736 = default(float);
        float __arm64_float_flags_left_12946744 = default(float);
        float __arm64_float_flags_left_12946752 = default(float);
        float __arm64_float_flags_left_12946764 = default(float);
        float __arm64_float_flags_left_12946792 = default(float);
        float __arm64_float_flags_left_12946800 = default(float);
        float __arm64_float_flags_left_12946808 = default(float);
        float __arm64_float_flags_left_12946816 = default(float);
        float __arm64_float_flags_left_12946824 = default(float);
        float __arm64_float_flags_left_12946836 = default(float);
        float __arm64_float_flags_left_12946864 = default(float);
        float __arm64_float_flags_left_12946872 = default(float);
        float __arm64_float_flags_left_12946880 = default(float);
        float __arm64_float_flags_left_12946888 = default(float);
        float __arm64_float_flags_left_12946896 = default(float);
        float __arm64_float_flags_left_12946908 = default(float);
        float __arm64_float_flags_left_12946936 = default(float);
        float __arm64_float_flags_left_12946944 = default(float);
        float __arm64_float_flags_left_12946952 = default(float);
        float __arm64_float_flags_left_12946960 = default(float);
        float __arm64_float_flags_left_12946968 = default(float);
        float __arm64_float_flags_left_12946976 = default(float);
        float __arm64_float_flags_right_12946508 = default(float);
        float __arm64_float_flags_right_12946520 = default(float);
        float __arm64_float_flags_right_12946532 = default(float);
        float __arm64_float_flags_right_12946572 = default(float);
        float __arm64_float_flags_right_12946580 = default(float);
        float __arm64_float_flags_right_12946588 = default(float);
        float __arm64_float_flags_right_12946596 = default(float);
        float __arm64_float_flags_right_12946604 = default(float);
        float __arm64_float_flags_right_12946612 = default(float);
        float __arm64_float_flags_right_12946644 = default(float);
        float __arm64_float_flags_right_12946652 = default(float);
        float __arm64_float_flags_right_12946660 = default(float);
        float __arm64_float_flags_right_12946668 = default(float);
        float __arm64_float_flags_right_12946676 = default(float);
        float __arm64_float_flags_right_12946692 = default(float);
        float __arm64_float_flags_right_12946720 = default(float);
        float __arm64_float_flags_right_12946728 = default(float);
        float __arm64_float_flags_right_12946736 = default(float);
        float __arm64_float_flags_right_12946744 = default(float);
        float __arm64_float_flags_right_12946752 = default(float);
        float __arm64_float_flags_right_12946764 = default(float);
        float __arm64_float_flags_right_12946792 = default(float);
        float __arm64_float_flags_right_12946800 = default(float);
        float __arm64_float_flags_right_12946808 = default(float);
        float __arm64_float_flags_right_12946816 = default(float);
        float __arm64_float_flags_right_12946824 = default(float);
        float __arm64_float_flags_right_12946836 = default(float);
        float __arm64_float_flags_right_12946864 = default(float);
        float __arm64_float_flags_right_12946872 = default(float);
        float __arm64_float_flags_right_12946880 = default(float);
        float __arm64_float_flags_right_12946888 = default(float);
        float __arm64_float_flags_right_12946896 = default(float);
        float __arm64_float_flags_right_12946908 = default(float);
        float __arm64_float_flags_right_12946936 = default(float);
        float __arm64_float_flags_right_12946944 = default(float);
        float __arm64_float_flags_right_12946952 = default(float);
        float __arm64_float_flags_right_12946960 = default(float);
        float __arm64_float_flags_right_12946968 = default(float);
        float __arm64_float_flags_right_12946976 = default(float);
        ulong __arm64_pair_address_12946372 = default(ulong);
        ulong __arm64_pair_address_12946376 = default(ulong);
        ulong __arm64_pair_address_12946380 = default(ulong);
        ulong __arm64_pair_address_12946384 = default(ulong);
        ulong __arm64_pair_address_12946428 = default(ulong);
        ulong __arm64_pair_address_12946464 = default(ulong);
        ulong __arm64_pair_address_12946684 = default(ulong);
        ulong __arm64_pair_address_12946832 = default(ulong);
        ulong __arm64_pair_address_12947036 = default(ulong);
        ulong __arm64_pair_address_12947040 = default(ulong);
        ulong __arm64_pair_address_12947044 = default(ulong);
        ulong __arm64_pair_address_12947056 = default(ulong);
        ulong __arm64_pair_address_12947060 = default(ulong);
        ulong __arm64_pair_address_12947064 = default(ulong);
        ulong __arm64_pair_address_12947068 = default(ulong);
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
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x70UL)));
        __arm64_pair_address_12946372 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12946372, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12946372) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_12946376 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12946376, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12946376) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12946380 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12946380, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12946380) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12946384 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12946384, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12946384) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12946428 = unchecked((ulong)((sp) + (0x4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12946428, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12946428) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v0 = v13;
        v1 = v10;
        v2 = v7;
        x1 = 0x0UL;
        x20 = x0;
        x19 = x8;
        __arm64_pair_address_12946464 = unchecked((ulong)((sp) + (0x58UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12946464, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12946464) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        v14 = v0;
        v15 = v1;
        v8 = v2;
        x0 = x20;
        v0 = v13;
        v1 = v10;
        v2 = v9;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        __arm64_float_flags_left_12946508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946508 < __arm64_float_flags_right_12946508) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946508 > __arm64_float_flags_right_12946508) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946520 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946520 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946520 < __arm64_float_flags_right_12946520) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946520 > __arm64_float_flags_right_12946520) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946532 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946532 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946532 < __arm64_float_flags_right_12946532) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946532 > __arm64_float_flags_right_12946532) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x8UL))))), 0));
        x0 = x20;
        v0 = v13;
        v1 = v12;
        x1 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0xCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        __arm64_float_flags_left_12946572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946572 < __arm64_float_flags_right_12946572) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946580 < __arm64_float_flags_right_12946580) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946588 < __arm64_float_flags_right_12946588) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946596 > __arm64_float_flags_right_12946596) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946604 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946604 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946604 > __arm64_float_flags_right_12946604) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946612 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946612 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946612 > __arm64_float_flags_right_12946612) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x58UL))))), 0));
        x0 = x20;
        v0 = v13;
        v1 = v12;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        __arm64_float_flags_left_12946644 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946644 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946644 < __arm64_float_flags_right_12946644) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946652 < __arm64_float_flags_right_12946652) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946660 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946660 < __arm64_float_flags_right_12946660) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946668 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946668 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946668 > __arm64_float_flags_right_12946668) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946676 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946676 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946676 > __arm64_float_flags_right_12946676) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_pair_address_12946684 = unchecked((ulong)((sp) + (0x4UL)));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12946684)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12946684) + (0x4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x5CUL))))), 0));
        __arm64_float_flags_left_12946692 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946692 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946692 > __arm64_float_flags_right_12946692) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        x0 = x20;
        v0 = v15;
        v2 = v12;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        __arm64_float_flags_left_12946720 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946720 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946720 < __arm64_float_flags_right_12946720) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946728 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946728 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946728 < __arm64_float_flags_right_12946728) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946736 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946736 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946736 < __arm64_float_flags_right_12946736) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946744 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946744 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946744 > __arm64_float_flags_right_12946744) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946752 > __arm64_float_flags_right_12946752) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        __arm64_float_flags_left_12946764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946764 > __arm64_float_flags_right_12946764) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        x0 = x20;
        v0 = v15;
        v2 = v12;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        __arm64_float_flags_left_12946792 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946792 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946792 < __arm64_float_flags_right_12946792) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946800 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946800 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946800 < __arm64_float_flags_right_12946800) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946808 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946808 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946808 < __arm64_float_flags_right_12946808) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946816 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946816 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946816 > __arm64_float_flags_right_12946816) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946824 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946824 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946824 > __arm64_float_flags_right_12946824) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_pair_address_12946832 = unchecked((ulong)((sp) + (0x58UL)));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12946832)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12946832) + (0x4UL))))), 0));
        __arm64_float_flags_left_12946836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946836 > __arm64_float_flags_right_12946836) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        x0 = x20;
        v0 = v15;
        v2 = v14;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        __arm64_float_flags_left_12946864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946864 < __arm64_float_flags_right_12946864) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946872 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946872 < __arm64_float_flags_right_12946872) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946880 < __arm64_float_flags_right_12946880) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946888 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946888 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946888 > __arm64_float_flags_right_12946888) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946896 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946896 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946896 > __arm64_float_flags_right_12946896) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        __arm64_float_flags_left_12946908 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946908 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946908 > __arm64_float_flags_right_12946908) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        x0 = x20;
        v0 = v15;
        v2 = v14;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        __arm64_float_flags_left_12946936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946936 < __arm64_float_flags_right_12946936) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946944 < __arm64_float_flags_right_12946944) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946952 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946952 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946952 < __arm64_float_flags_right_12946952) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946960 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946960 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946960 > __arm64_float_flags_right_12946960) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946968 > __arm64_float_flags_right_12946968) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12946976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12946976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12946976 > __arm64_float_flags_right_12946976) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12947036 = x19;
        RuntimeMemory.WriteF32(__arm64_pair_address_12947036, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12947036) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        __arm64_pair_address_12947040 = unchecked((ulong)((x19) + (0x8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12947040, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12947040) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        __arm64_pair_address_12947044 = unchecked((ulong)((x19) + (0x10UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12947044, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12947044) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        __arm64_pair_address_12947056 = unchecked((ulong)((sp) + (0x40UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12947056)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12947056) + (0x8UL))))), 0));
        __arm64_pair_address_12947060 = unchecked((ulong)((sp) + (0x30UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12947060)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12947060) + (0x8UL))))), 0));
        __arm64_pair_address_12947064 = unchecked((ulong)((sp) + (0x20UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12947064)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12947064) + (0x8UL))))), 0));
        __arm64_pair_address_12947068 = unchecked((ulong)((sp) + (0x10UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12947068)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12947068) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.GetWorldAABB` — RVA `0xc58e88`

- Lift status: **exact**; input span: 92 bytes; span to next metadata RVA: 92 bytes.
- Metadata signature: `public static Bounds GetWorldAABB(Matrix4x4 tf, Bounds localBounds) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong CFUtils_GetWorldAABB_RVAc58e88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12947088 = default(ulong);
        ulong __arm64_pair_address_12947092 = default(ulong);
        ulong __arm64_pair_address_12947104 = default(ulong);
        ulong __arm64_pair_address_12947108 = default(ulong);
        ulong __arm64_pair_address_12947112 = default(ulong);
        ulong __arm64_pair_address_12947116 = default(ulong);
        ulong __arm64_pair_address_12947120 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x70UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        __arm64_pair_address_12947088 = unchecked((ulong)((x0) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12947088);
#else
        v1 = __ReadVector128(__arm64_pair_address_12947088);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12947088) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12947088) + (0x10UL))));
#endif
        __arm64_pair_address_12947092 = x0;
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_12947092);
#else
        v3 = __ReadVector128(__arm64_pair_address_12947092);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12947092) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12947092) + (0x10UL))));
#endif
        x19 = x8;
        __arm64_pair_address_12947104 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12947104, v1);
#else
        __WriteVector128(__arm64_pair_address_12947104, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12947104) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12947104) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12947108 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12947108, v3);
#else
        __WriteVector128(__arm64_pair_address_12947108, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12947108) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12947108) + (0x10UL))), v2);
#endif
        __arm64_pair_address_12947112 = unchecked((ulong)((x1) + (0x8UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947112)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947112) + (0x4UL))))), 0));
        __arm64_pair_address_12947116 = unchecked((ulong)((x1) + (0x10UL)));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947116)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947116) + (0x4UL))))), 0));
        __arm64_pair_address_12947120 = x1;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947120)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947120) + (0x4UL))))), 0));
        x0 = sp;
        x0 = RuntimeCalls.InvokeDirect(0xC58BC0UL /* metadata target: CFUtils.GetWorldAABB */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x58UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x48UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x48UL))));
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x10UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x19, v0);
#else
        __WriteVector128(x19, v0);
#endif
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.GetWorldRect` — RVA `0xc58ee4`

- Lift status: **partial**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public static Rect GetWorldRect(Matrix4x4 tf, Bounds localBounds) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fsub' at 0xc58f34; reason: Unsupported instruction 'fadd' at 0xc58f38; reason: Unsupported instruction 'fsub' at 0xc58f3c; reason: Unsupported instruction 'mov' at 0xc58f40; reason: Unsupported instruction 'mov' at 0xc58f44

```csharp
public static ulong CFUtils_GetWorldRect_RVAc58ee4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12947180 = default(ulong);
        ulong __arm64_pair_address_12947184 = default(ulong);
        ulong __arm64_pair_address_12947196 = default(ulong);
        ulong __arm64_pair_address_12947200 = default(ulong);
        ulong __arm64_pair_address_12947204 = default(ulong);
        ulong __arm64_pair_address_12947208 = default(ulong);
        ulong __arm64_pair_address_12947212 = default(ulong);
        ulong __arm64_pair_address_12947216 = default(ulong);
        ulong __arm64_pair_address_12947220 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xB0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), x30);
        __arm64_pair_address_12947180 = unchecked((ulong)((x0) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(__arm64_pair_address_12947180);
#else
        v4 = __ReadVector128(__arm64_pair_address_12947180);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12947180) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12947180) + (0x10UL))));
#endif
        __arm64_pair_address_12947184 = x0;
#if IL2CPPREC_RUNTIME_VECTOR128
        v6 = RuntimeMemory.ReadVector128(__arm64_pair_address_12947184);
#else
        v6 = __ReadVector128(__arm64_pair_address_12947184);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v5 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12947184) + (0x10UL))));
#else
        v5 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12947184) + (0x10UL))));
#endif
        x8 = unchecked((ulong)((sp) + (0x88UL)));
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        __arm64_pair_address_12947196 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12947196, v4);
#else
        __WriteVector128(__arm64_pair_address_12947196, v4);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12947196) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12947196) + (0x10UL))), v3);
#endif
        __arm64_pair_address_12947200 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12947200, v6);
#else
        __WriteVector128(__arm64_pair_address_12947200, v6);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12947200) + (0x10UL))), v5);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12947200) + (0x10UL))), v5);
#endif
        __arm64_pair_address_12947204 = unchecked((ulong)((x1) + (0x8UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947204)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947204) + (0x4UL))))), 0));
        __arm64_pair_address_12947208 = unchecked((ulong)((x1) + (0x10UL)));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947208)), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947208) + (0x4UL))))), 0));
        __arm64_pair_address_12947212 = x1;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947212)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947212) + (0x4UL))))), 0));
        __arm64_pair_address_12947216 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12947216, v6);
#else
        __WriteVector128(__arm64_pair_address_12947216, v6);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12947216) + (0x10UL))), v5);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12947216) + (0x10UL))), v5);
#endif
        __arm64_pair_address_12947220 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12947220, v4);
#else
        __WriteVector128(__arm64_pair_address_12947220, v4);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12947220) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12947220) + (0x10UL))), v3);
#endif
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC58BC0UL /* metadata target: CFUtils.GetWorldAABB */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x88UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x94UL))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        RuntimeCalls.Unsupported("fsub", 0xC58F34UL);
        RuntimeCalls.Unsupported("fadd", 0xC58F38UL);
        RuntimeCalls.Unsupported("fsub", 0xC58F3CUL);
        RuntimeCalls.Unsupported("mov", 0xC58F40UL);
        RuntimeCalls.Unsupported("mov", 0xC58F44UL);
        sp = unchecked((ulong)((sp) + (0xB0UL)));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ClampEllipseInsideEllipse` — RVA `0xc58f50`

- Lift status: **exact**; input span: 496 bytes; span to next metadata RVA: 496 bytes.
- Metadata signature: `public static Vector2 ClampEllipseInsideEllipse(Rect rect, Rect limiterRect) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong CFUtils_ClampEllipseInsideEllipse_RVAc58f50(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12947332 = default(float);
        float __arm64_float_flags_left_12947344 = default(float);
        float __arm64_float_flags_left_12947392 = default(float);
        float __arm64_float_flags_left_12947456 = default(float);
        float __arm64_float_flags_left_12947540 = default(float);
        float __arm64_float_flags_left_12947560 = default(float);
        float __arm64_float_flags_left_12947684 = default(float);
        float __arm64_float_flags_left_12947692 = default(float);
        float __arm64_float_flags_right_12947332 = default(float);
        float __arm64_float_flags_right_12947344 = default(float);
        float __arm64_float_flags_right_12947392 = default(float);
        float __arm64_float_flags_right_12947456 = default(float);
        float __arm64_float_flags_right_12947540 = default(float);
        float __arm64_float_flags_right_12947560 = default(float);
        float __arm64_float_flags_right_12947684 = default(float);
        float __arm64_float_flags_right_12947692 = default(float);
        ulong __arm64_load_address_12947768 = default(ulong);
        ulong __arm64_pair_address_12947284 = default(ulong);
        ulong __arm64_pair_address_12947288 = default(ulong);
        ulong __arm64_pair_address_12947292 = default(ulong);
        ulong __arm64_pair_address_12947448 = default(ulong);
        ulong __arm64_pair_address_12947640 = default(ulong);
        ulong __arm64_pair_address_12947756 = default(ulong);
        ulong __arm64_pair_address_12947760 = default(ulong);
        ulong __arm64_pair_address_12947764 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)));
        __arm64_pair_address_12947284 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12947284, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12947284) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12947288 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12947288, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12947288) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12947292 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12947292, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12947292) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12947332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        if ((__arm64_float_flags_left_12947332 >= __arm64_float_flags_right_12947332))
        {
            goto label_0xC59000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58F90UL);
        }
        __arm64_float_flags_left_12947344 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947344 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12947344 >= __arm64_float_flags_right_12947344))
        {
            goto label_0xC59000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC58F98UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12947392 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947392 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12947392 >= __arm64_float_flags_right_12947392) || ((__arm64_float_flags_left_12947392 != __arm64_float_flags_left_12947392) || (__arm64_float_flags_right_12947392 != __arm64_float_flags_right_12947392))))
        {
            goto label_0xC59010;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC58FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC58FE8;
        label_0xC58FE8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12947448 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947448)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947448) + (0x4UL))))), 0));
        goto label_0xC59128;
        label_0xC59000:
        ;
        __arm64_float_flags_left_12947456 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947456 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12947456 < __arm64_float_flags_right_12947456) || ((__arm64_float_flags_left_12947456 != __arm64_float_flags_left_12947456) || (__arm64_float_flags_right_12947456 != __arm64_float_flags_right_12947456))))
        {
            goto label_0xC59068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5900CUL);
        }
        goto label_0xC590E4;
        label_0xC59010:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59030;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC59030;
        label_0xC59030:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59048;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC59044UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC59048;
        label_0xC59048:
        ;
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_12947540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12947540 <= __arm64_float_flags_right_12947540) || ((__arm64_float_flags_left_12947540 != __arm64_float_flags_left_12947540) || (__arm64_float_flags_right_12947540 != __arm64_float_flags_right_12947540))))
        {
            goto label_0xC59088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5905CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC590BC;
        label_0xC59068:
        ;
        __arm64_float_flags_left_12947560 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947560 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12947560 >= __arm64_float_flags_right_12947560))
        {
            goto label_0xC590D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC59084UL);
        }
        goto label_0xC590E4;
        label_0xC59088:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC590A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC590A8;
        label_0xC590A8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12947640 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12947640)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12947640) + (0x4UL))))), 0));
        goto label_0xC590BC;
        label_0xC590BC:
        ;
        goto label_0xC59128;
        label_0xC590D0:
        ;
        goto label_0xC590E4;
        label_0xC590E4:
        ;
        __arm64_float_flags_left_12947684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12947684 >= __arm64_float_flags_right_12947684))
        {
            goto label_0xC5910C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC590ECUL);
        }
        __arm64_float_flags_left_12947692 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947692 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12947692 >= __arm64_float_flags_right_12947692))
        {
            goto label_0xC59114;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC59108UL);
        }
        goto label_0xC59128;
        label_0xC5910C:
        ;
        goto label_0xC59128;
        label_0xC59114:
        ;
        goto label_0xC59128;
        label_0xC59128:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_12947756 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12947756)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12947756) + (0x8UL))))), 0));
        __arm64_pair_address_12947760 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12947760)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12947760) + (0x8UL))))), 0));
        __arm64_pair_address_12947764 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12947764)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12947764) + (0x8UL))))), 0));
        __arm64_load_address_12947768 = sp;
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12947768)), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ClampRectInsideEllipse` — RVA `0xc59140`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public static Vector2 ClampRectInsideEllipse(Rect rect, Rect limiterRect) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong CFUtils_ClampRectInsideEllipse_RVAc59140(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC58F50UL /* metadata target: CFUtils.ClampEllipseInsideEllipse */);
        return default(ulong);
    }
```

## `CFUtils.ClampRectInsideRect` — RVA `0xc59144`

- Lift status: **partial**; input span: 296 bytes; span to next metadata RVA: 296 bytes.
- Metadata signature: `public static Vector2 ClampRectInsideRect(Rect rect, Rect limiterRect) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=18 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ge' at 0xc591cc; reason: Unknown IR expression at 0xc591cc

```csharp
public static ulong CFUtils_ClampRectInsideRect_RVAc59144(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12947904 = default(float);
        float __arm64_float_flags_left_12947928 = default(float);
        float __arm64_float_flags_left_12947952 = default(float);
        float __arm64_float_flags_left_12947968 = default(float);
        float __arm64_float_flags_left_12947988 = default(float);
        float __arm64_float_flags_left_12948020 = default(float);
        float __arm64_float_flags_right_12947904 = default(float);
        float __arm64_float_flags_right_12947928 = default(float);
        float __arm64_float_flags_right_12947952 = default(float);
        float __arm64_float_flags_right_12947968 = default(float);
        float __arm64_float_flags_right_12947988 = default(float);
        float __arm64_float_flags_right_12948020 = default(float);
        ulong __arm64_pair_address_12947784 = default(ulong);
        ulong __arm64_pair_address_12947788 = default(ulong);
        ulong __arm64_pair_address_12947792 = default(ulong);
        ulong __arm64_pair_address_12947796 = default(ulong);
        ulong __arm64_pair_address_12948052 = default(ulong);
        ulong __arm64_pair_address_12948056 = default(ulong);
        ulong __arm64_pair_address_12948060 = default(ulong);
        ulong __arm64_pair_address_12948064 = default(ulong);
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
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x60UL)));
        __arm64_pair_address_12947784 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12947784, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12947784) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_12947788 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12947788, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12947788) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12947792 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12947792, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12947792) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12947796 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12947796, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12947796) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v10 = v7;
        v11 = v4;
        v12 = v3;
        v13 = v0;
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC591A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0xCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        v9 = v5;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        v5 = v9;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC591A8;
        label_0xC591A8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(x8);
        __arm64_float_flags_left_12947904 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947904 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeCalls.Unsupported("b.ge", 0xC591CCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC591F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC591D0UL);
        }
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12947928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12947928 <= __arm64_float_flags_right_12947928) || ((__arm64_float_flags_left_12947928 != __arm64_float_flags_left_12947928) || (__arm64_float_flags_right_12947928 != __arm64_float_flags_right_12947928))))
        {
            goto label_0xC591E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC591E0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        goto label_0xC591FC;
        label_0xC591E8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12947952 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947952 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12947952 >= __arm64_float_flags_right_12947952) || ((__arm64_float_flags_left_12947952 != __arm64_float_flags_left_12947952) || (__arm64_float_flags_right_12947952 != __arm64_float_flags_right_12947952))))
        {
            goto label_0xC59244;
        }
        else
        {
            goto label_0xC591F8;
        }
        label_0xC591F8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC591FC;
        label_0xC591FC:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12947968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947968 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        if ((__arm64_float_flags_left_12947968 >= __arm64_float_flags_right_12947968))
        {
            goto label_0xC59224;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5920CUL);
        }
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12947988 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12947988 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12947988 <= __arm64_float_flags_right_12947988) || ((__arm64_float_flags_left_12947988 != __arm64_float_flags_left_12947988) || (__arm64_float_flags_right_12947988 != __arm64_float_flags_right_12947988))))
        {
            goto label_0xC5922C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5921CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        goto label_0xC59250;
        label_0xC59224:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        goto label_0xC59250;
        label_0xC5922C:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12948020 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948020 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12948020 >= __arm64_float_flags_right_12948020) || ((__arm64_float_flags_left_12948020 != __arm64_float_flags_left_12948020) || (__arm64_float_flags_right_12948020 != __arm64_float_flags_right_12948020))))
        {
            goto label_0xC5924C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5923CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC59250;
        label_0xC59244:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        goto label_0xC591FC;
        label_0xC5924C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4UL))))), 0));
        goto label_0xC59250;
        label_0xC59250:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        __arm64_pair_address_12948052 = unchecked((ulong)((sp) + (0x40UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12948052)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12948052) + (0x8UL))))), 0));
        __arm64_pair_address_12948056 = unchecked((ulong)((sp) + (0x30UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12948056)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12948056) + (0x8UL))))), 0));
        __arm64_pair_address_12948060 = unchecked((ulong)((sp) + (0x20UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12948060)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12948060) + (0x8UL))))), 0));
        __arm64_pair_address_12948064 = unchecked((ulong)((sp) + (0x10UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12948064)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12948064) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x60UL)));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.ClampPerAxisInsideUnitSquare` — RVA `0xc5926c`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public static Vector2 ClampPerAxisInsideUnitSquare(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong CFUtils_ClampPerAxisInsideUnitSquare_RVAc5926c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `CFUtils.IsDirDiagonal` — RVA `0xc59290`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public static bool IsDirDiagonal(Dir dir) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static uint CFUtils_IsDirDiagonal_RVAc59290(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12948112 = default(uint);
        uint __arm64_flags_result_12948112 = default(uint);
        uint __arm64_flags_right_12948112 = default(uint);
        __arm64_flags_left_12948112 = unchecked((uint)(x0));
        __arm64_flags_right_12948112 = unchecked((uint)0x1UL);
        __arm64_flags_result_12948112 = unchecked((uint)((__arm64_flags_left_12948112) & (__arm64_flags_right_12948112)));
        x0 = unchecked((ulong)(((__arm64_flags_result_12948112 == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `CFUtils.VecToAngle` — RVA `0xc5929c`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public static float VecToAngle(Vector2 vec) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong CFUtils_VecToAngle_RVAc5929c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C90UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x554UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC592B8UL /* metadata target: CFUtils.NormalizeAnglePositive */);
        return default(ulong);
    }
```

## `CFUtils.NormalizeAnglePositive` — RVA `0xc592b8`

- Lift status: **partial**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public static float NormalizeAnglePositive(float a) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintm' at 0xc59324; reason: Unsupported instruction 'frintm' at 0xc592ec

```csharp
public static ulong CFUtils_NormalizeAnglePositive_RVAc592b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12948160 = default(float);
        float __arm64_float_flags_left_12948168 = default(float);
        float __arm64_float_flags_left_12948184 = default(float);
        float __arm64_float_flags_left_12948220 = default(float);
        float __arm64_float_flags_left_12948276 = default(float);
        float __arm64_float_flags_right_12948160 = default(float);
        float __arm64_float_flags_right_12948168 = default(float);
        float __arm64_float_flags_right_12948184 = default(float);
        float __arm64_float_flags_right_12948220 = default(float);
        float __arm64_float_flags_right_12948276 = default(float);
        float __arm64_fp_left_12948216 = default(float);
        float __arm64_fp_left_12948272 = default(float);
        float __arm64_fp_right_12948216 = default(float);
        float __arm64_fp_right_12948272 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948160 >= __arm64_float_flags_right_12948160))
        {
            label_0xC59318:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            RuntimeCalls.Unsupported("frintm", 0xC59324UL);
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            __arm64_fp_left_12948272 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_fp_right_12948272 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12948272 != __arm64_fp_left_12948272) ? __arm64_fp_left_12948272 : ((__arm64_fp_right_12948272 != __arm64_fp_right_12948272) ? __arm64_fp_right_12948272 : (((__arm64_fp_left_12948272 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12948272 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12948272), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12948272), 0))))), 0) : ((__arm64_fp_left_12948272 <= __arm64_fp_right_12948272) ? __arm64_fp_left_12948272 : __arm64_fp_right_12948272))))), 0));
            __arm64_float_flags_left_12948276 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12948276 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12948276 >= __arm64_float_flags_right_12948276) || ((__arm64_float_flags_left_12948276 != __arm64_float_flags_left_12948276) || (__arm64_float_flags_right_12948276 != __arm64_float_flags_right_12948276))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
            return x0;
        }
        else
        {
            __arm64_float_flags_left_12948168 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12948168 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
            if ((__arm64_float_flags_left_12948168 >= __arm64_float_flags_right_12948168))
            {
            }
            else
            {
                x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
                __arm64_float_flags_left_12948184 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12948184 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                if (((__arm64_float_flags_left_12948184 > __arm64_float_flags_right_12948184) || ((__arm64_float_flags_left_12948184 != __arm64_float_flags_left_12948184) || (__arm64_float_flags_right_12948184 != __arm64_float_flags_right_12948184))))
                {
                }
                else
                {
                    x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
                    v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                    RuntimeCalls.Unsupported("frintm", 0xC592ECUL);
                    v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                    __arm64_fp_left_12948216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                    __arm64_fp_right_12948216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12948216 != __arm64_fp_left_12948216) ? __arm64_fp_left_12948216 : ((__arm64_fp_right_12948216 != __arm64_fp_right_12948216) ? __arm64_fp_right_12948216 : (((__arm64_fp_left_12948216 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12948216 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12948216), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12948216), 0))))), 0) : ((__arm64_fp_left_12948216 <= __arm64_fp_right_12948216) ? __arm64_fp_left_12948216 : __arm64_fp_right_12948216))))), 0));
                    __arm64_float_flags_left_12948220 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                    __arm64_float_flags_right_12948220 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12948220 >= __arm64_float_flags_right_12948220) || ((__arm64_float_flags_left_12948220 != __arm64_float_flags_left_12948220) || (__arm64_float_flags_right_12948220 != __arm64_float_flags_right_12948220))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
                }
                label_0xC59308:
                ;
                x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            }
            label_0xC59314:
            ;
            return x0;
        }
        return default(ulong);
    }
```

## `CFUtils.VecToAngle` — RVA `0xc59344`

- Lift status: **exact**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `public static float VecToAngle(Vector2 vec, float defaultAngle, float deadZoneSq) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).

```csharp
public static ulong CFUtils_VecToAngle_RVAc59344(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12948324 = default(float);
        float __arm64_float_flags_left_12948352 = default(float);
        float __arm64_float_flags_left_12948428 = default(float);
        float __arm64_float_flags_right_12948324 = default(float);
        float __arm64_float_flags_right_12948352 = default(float);
        float __arm64_float_flags_right_12948428 = default(float);
        ulong __arm64_load_address_12948460 = default(ulong);
        ulong __arm64_load_address_12948552 = default(ulong);
        ulong __arm64_pair_address_12948296 = default(ulong);
        ulong __arm64_pair_address_12948452 = default(ulong);
        ulong __arm64_pair_address_12948516 = default(ulong);
        ulong __arm64_pair_address_12948544 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        __arm64_pair_address_12948296 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12948296, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12948296) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        v8 = v1;
        v9 = v0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12948324 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948324 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948324 < __arm64_float_flags_right_12948324))
        {
            goto label_0xC593E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12948352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12948352 <= __arm64_float_flags_right_12948352) || ((__arm64_float_flags_left_12948352 != __arm64_float_flags_left_12948352) || (__arm64_float_flags_right_12948352 != __arm64_float_flags_right_12948352))))
        {
            goto label_0xC59428;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC593A8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC593A8;
        label_0xC593A8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC593C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC593BCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC593C0;
        label_0xC593C0:
        ;
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_12948428 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948428 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12948428 <= __arm64_float_flags_right_12948428) || ((__arm64_float_flags_left_12948428 != __arm64_float_flags_left_12948428) || (__arm64_float_flags_right_12948428 != __arm64_float_flags_right_12948428))))
        {
            goto label_0xC593F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC593D4UL);
        }
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC59428;
        label_0xC593E0:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12948452 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12948452)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12948452) + (0x8UL))))), 0));
        __arm64_load_address_12948460 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12948460)), 0));
        return x0;
        label_0xC593F4:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC59414;
        label_0xC59414:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12948516 = x8;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12948516)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12948516) + (0x4UL))))), 0));
        goto label_0xC59428;
        label_0xC59428:
        ;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C90UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x554UL))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12948544 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12948544)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12948544) + (0x8UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_load_address_12948552 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12948552)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12948552) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC592B8UL /* metadata target: CFUtils.NormalizeAnglePositive */);
        return default(ulong);
    }
```

## `CFUtils.DirToAngle` — RVA `0xc59450`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public static float DirToAngle(Dir d) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong CFUtils_DirToAngle_RVAc59450(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `CFUtils.DirFromAngle` — RVA `0xc59474`

- Lift status: **partial**; input span: 280 bytes; span to next metadata RVA: 280 bytes.
- Metadata signature: `public static Dir DirFromAngle(float ang, bool as8way) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=24 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc59550; reason: Unknown IR expression at 0xc59550

```csharp
public static uint CFUtils_DirFromAngle_RVAc59474(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12948608 = default(uint);
        uint __arm64_flags_result_12948608 = default(uint);
        uint __arm64_flags_right_12948608 = default(uint);
        float __arm64_float_flags_left_12948648 = default(float);
        float __arm64_float_flags_left_12948664 = default(float);
        float __arm64_float_flags_left_12948680 = default(float);
        float __arm64_float_flags_left_12948696 = default(float);
        float __arm64_float_flags_left_12948712 = default(float);
        float __arm64_float_flags_left_12948728 = default(float);
        float __arm64_float_flags_left_12948752 = default(float);
        float __arm64_float_flags_left_12948772 = default(float);
        float __arm64_float_flags_left_12948788 = default(float);
        float __arm64_float_flags_left_12948808 = default(float);
        float __arm64_float_flags_right_12948648 = default(float);
        float __arm64_float_flags_right_12948664 = default(float);
        float __arm64_float_flags_right_12948680 = default(float);
        float __arm64_float_flags_right_12948696 = default(float);
        float __arm64_float_flags_right_12948712 = default(float);
        float __arm64_float_flags_right_12948728 = default(float);
        float __arm64_float_flags_right_12948752 = default(float);
        float __arm64_float_flags_right_12948772 = default(float);
        float __arm64_float_flags_right_12948788 = default(float);
        float __arm64_float_flags_right_12948808 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(0x42340000UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x41B40000UL))));
        __arm64_flags_left_12948608 = unchecked((uint)(x0));
        __arm64_flags_right_12948608 = unchecked((uint)0x1UL);
        __arm64_flags_result_12948608 = unchecked((uint)((__arm64_flags_left_12948608) & (__arm64_flags_right_12948608)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((__arm64_flags_result_12948608 == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeCalls.InvokeDirect(0xC592B8UL /* metadata target: CFUtils.NormalizeAnglePositive */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5951C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x42340000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948648 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948648 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948648 < __arm64_float_flags_right_12948648))
        {
            goto label_0xC59558;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x42B40000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948664 < __arm64_float_flags_right_12948664))
        {
            goto label_0xC59568;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x43070000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948680 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948680 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948680 < __arm64_float_flags_right_12948680))
        {
            goto label_0xC59560;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948696 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948696 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948696 < __arm64_float_flags_right_12948696))
        {
            goto label_0xC59574;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x43610000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948712 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948712 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948712 < __arm64_float_flags_right_12948712))
        {
            goto label_0xC5957C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x43870000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948728 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948728 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948728 < __arm64_float_flags_right_12948728))
        {
            goto label_0xC59584;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3C4UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        __arm64_float_flags_left_12948752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        x0 = unchecked((ulong)((((__arm64_float_flags_left_12948752 >= __arm64_float_flags_right_12948752) || ((__arm64_float_flags_left_12948752 != __arm64_float_flags_left_12948752) || (__arm64_float_flags_right_12948752 != __arm64_float_flags_right_12948752))) ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
        goto label_0xC5956C;
        label_0xC5951C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x42B40000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948772 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948772 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948772 < __arm64_float_flags_right_12948772))
        {
            goto label_0xC59558;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_12948788 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948788 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12948788 < __arm64_float_flags_right_12948788))
        {
            goto label_0xC59560;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x43870000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        __arm64_float_flags_left_12948808 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948808 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        RuntimeCalls.Unsupported("csel", 0xC59550UL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        goto label_0xC5956C;
        label_0xC59558:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5956C;
        label_0xC59560:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC5956C;
        label_0xC59568:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        goto label_0xC5956C;
        label_0xC5956C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC59574:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        goto label_0xC5956C;
        label_0xC5957C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        goto label_0xC5956C;
        label_0xC59584:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        goto label_0xC5956C;
        return default(uint);
    }
```

## `CFUtils.DirFromAngleEx` — RVA `0xc5958c`

- Lift status: **partial**; input span: 196 bytes; span to next metadata RVA: 196 bytes.
- Metadata signature: `public static Dir DirFromAngleEx(float ang, bool as8way, Dir lastDir, float magnetPow) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=9 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fcsel' at 0xc595c4; reason: Unknown IR expression at 0xc595c4; reason: Unsupported instruction 'frintm' at 0xc595e8; reason: Unsupported instruction 'fcsel' at 0xc59600; reason: Unknown IR expression at 0xc59600; reason: Unsupported instruction 'fcsel' at 0xc59618; reason: Unknown IR expression at 0xc59618

```csharp
public static uint CFUtils_DirFromAngleEx_RVAc5958c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12948916 = default(uint);
        uint __arm64_flags_left_12949032 = default(uint);
        uint __arm64_flags_result_12949032 = default(uint);
        uint __arm64_flags_right_12948916 = default(uint);
        uint __arm64_flags_right_12949032 = default(uint);
        float __arm64_float_flags_left_12948888 = default(float);
        float __arm64_float_flags_left_12948984 = default(float);
        float __arm64_float_flags_left_12949004 = default(float);
        float __arm64_float_flags_left_12949020 = default(float);
        float __arm64_float_flags_left_12949048 = default(float);
        float __arm64_float_flags_right_12948888 = default(float);
        float __arm64_float_flags_right_12948984 = default(float);
        float __arm64_float_flags_right_12949004 = default(float);
        float __arm64_float_flags_right_12949020 = default(float);
        float __arm64_float_flags_right_12949048 = default(float);
        float __arm64_fp_left_12948944 = default(float);
        float __arm64_fp_left_12948980 = default(float);
        float __arm64_fp_right_12948944 = default(float);
        float __arm64_fp_right_12948980 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        if ((unchecked((uint)(x1)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC59648;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        __arm64_float_flags_left_12948888 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948888 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12948888 <= __arm64_float_flags_right_12948888) || ((__arm64_float_flags_left_12948888 != __arm64_float_flags_left_12948888) || (__arm64_float_flags_right_12948888 != __arm64_float_flags_right_12948888))))
        {
            goto label_0xC59648;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) - (unchecked((uint)(0x1UL)))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x42340000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_flags_left_12948916 = unchecked((uint)(x8));
        __arm64_flags_right_12948916 = unchecked((uint)0x8UL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        RuntimeCalls.Unsupported("fcsel", 0xC595C4UL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        __arm64_fp_left_12948944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_fp_right_12948944 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12948944 != __arm64_fp_left_12948944) ? __arm64_fp_left_12948944 : ((__arm64_fp_right_12948944 != __arm64_fp_right_12948944) ? __arm64_fp_right_12948944 : (((__arm64_fp_left_12948944 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12948944 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12948944), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12948944), 0))))), 0) : ((__arm64_fp_left_12948944 <= __arm64_fp_right_12948944) ? __arm64_fp_left_12948944 : __arm64_fp_right_12948944))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC595E8UL);
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        __arm64_fp_left_12948980 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_fp_right_12948980 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0);
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12948980 != __arm64_fp_left_12948980) ? __arm64_fp_left_12948980 : ((__arm64_fp_right_12948980 != __arm64_fp_right_12948980) ? __arm64_fp_right_12948980 : (((__arm64_fp_left_12948980 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12948980 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12948980), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12948980), 0))))), 0) : ((__arm64_fp_left_12948980 <= __arm64_fp_right_12948980) ? __arm64_fp_left_12948980 : __arm64_fp_right_12948980))))), 0));
        __arm64_float_flags_left_12948984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12948984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        RuntimeCalls.Unsupported("fcsel", 0xC59600UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12949004 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12949004 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        x9 = unchecked((ulong)(unchecked((uint)(0x41B40000UL))));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fcsel", 0xC59618UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12949020 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12949020 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12949020 >= __arm64_float_flags_right_12949020) || ((__arm64_float_flags_left_12949020 != __arm64_float_flags_left_12949020) || (__arm64_float_flags_right_12949020 != __arm64_float_flags_right_12949020))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))), 0));
        __arm64_flags_left_12949032 = unchecked((uint)(x0));
        __arm64_flags_right_12949032 = unchecked((uint)0x1UL);
        __arm64_flags_result_12949032 = unchecked((uint)((__arm64_flags_left_12949032) & (__arm64_flags_right_12949032)));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((__arm64_flags_result_12949032 == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12949048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12949048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12949048 >= __arm64_float_flags_right_12949048) || ((__arm64_float_flags_left_12949048 != __arm64_float_flags_left_12949048) || (__arm64_float_flags_right_12949048 != __arm64_float_flags_right_12949048))))
        {
            goto label_0xC59648;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)(x1))));
        return unchecked((uint)(x0));
        label_0xC59648:
        ;
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59474UL /* metadata target: CFUtils.DirFromAngle */)));
        return default(uint);
    }
```

## `CFUtils.DirDeltaAngle` — RVA `0xc59650`

- Lift status: **partial**; input span: 352 bytes; span to next metadata RVA: 352 bytes.
- Metadata signature: `public static int DirDeltaAngle(Dir dirFrom, Dir dirTo) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=24 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fcsel' at 0xc596a0; reason: Unknown IR expression at 0xc596a0; reason: Unsupported instruction 'frintm' at 0xc596b8; reason: Unsupported instruction 'frintp' at 0xc59778; reason: Unsupported instruction 'frintm' at 0xc59784; reason: Unsupported instruction 'csel' at 0xc597a4; reason: Unknown IR expression at 0xc597a4

```csharp
public static uint CFUtils_DirDeltaAngle_RVAc59650(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_12949344 = default(double);
        double __arm64_fcvtz_source_12949400 = default(double);
        uint __arm64_flags_left_12949124 = default(uint);
        uint __arm64_flags_left_12949144 = default(uint);
        ulong __arm64_flags_left_12949352 = default(ulong);
        ulong __arm64_flags_result_12949352 = default(ulong);
        uint __arm64_flags_right_12949124 = default(uint);
        uint __arm64_flags_right_12949144 = default(uint);
        ulong __arm64_flags_right_12949352 = default(ulong);
        float __arm64_float_flags_left_12949204 = default(float);
        float __arm64_float_flags_left_12949220 = default(float);
        float __arm64_float_flags_left_12949292 = default(float);
        double __arm64_float_flags_left_12949304 = default(double);
        double __arm64_float_flags_left_12949328 = default(double);
        double __arm64_float_flags_left_12949404 = default(double);
        float __arm64_float_flags_right_12949204 = default(float);
        float __arm64_float_flags_right_12949220 = default(float);
        float __arm64_float_flags_right_12949292 = default(float);
        double __arm64_float_flags_right_12949304 = default(double);
        double __arm64_float_flags_right_12949328 = default(double);
        double __arm64_float_flags_right_12949404 = default(double);
        float __arm64_fp_left_12949200 = default(float);
        float __arm64_fp_right_12949200 = default(float);
        ulong __arm64_pair_address_12949092 = default(ulong);
        ulong __arm64_pair_address_12949392 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC597AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5965CUL)));
        }
        if ((unchecked((uint)(x1)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC597AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        sp = unchecked((ulong)((sp) - (0x30UL)));
        __arm64_pair_address_12949092 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12949092, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12949092) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x42340000UL))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) - (unchecked((uint)(0x1UL)))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_flags_left_12949124 = unchecked((uint)(x8));
        __arm64_flags_right_12949124 = unchecked((uint)0x8UL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x10))))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((__arm64_flags_left_12949124 >= __arm64_flags_right_12949124))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_flags_left_12949144 = unchecked((uint)(x10));
        __arm64_flags_right_12949144 = unchecked((uint)0x8UL);
        x9 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        RuntimeCalls.Unsupported("fcsel", 0xC596A0UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC596B8UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        x19 = 0x1BAB000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x242UL))))))));
        __arm64_fp_left_12949200 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_fp_right_12949200 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12949200 != __arm64_fp_left_12949200) ? __arm64_fp_left_12949200 : ((__arm64_fp_right_12949200 != __arm64_fp_right_12949200) ? __arm64_fp_right_12949200 : (((__arm64_fp_left_12949200 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12949200 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12949200), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12949200), 0))))), 0) : ((__arm64_fp_left_12949200 <= __arm64_fp_right_12949200) ? __arm64_fp_left_12949200 : __arm64_fp_right_12949200))))), 0));
        __arm64_float_flags_left_12949204 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12949204 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12949204 >= __arm64_float_flags_right_12949204) || ((__arm64_float_flags_left_12949204 != __arm64_float_flags_left_12949204) || (__arm64_float_flags_right_12949204 != __arm64_float_flags_right_12949204))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12949220 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12949220 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12949220 > __arm64_float_flags_right_12949220) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59704;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC59704;
        label_0xC59704:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5971C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59718UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5971C;
        label_0xC5971C:
        ;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_12949292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12949292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12949292 >= __arm64_float_flags_right_12949292))
        {
            goto label_0xC5974C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59734UL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_12949304 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12949304 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12949304 != __arm64_float_flags_right_12949304) || ((__arm64_float_flags_left_12949304 != __arm64_float_flags_left_12949304) || (__arm64_float_flags_right_12949304 != __arm64_float_flags_right_12949304))))
        {
            goto label_0xC59774;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59740UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC59760;
        label_0xC5974C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_12949328 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12949328 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_12949328 != __arm64_float_flags_right_12949328) || ((__arm64_float_flags_left_12949328 != __arm64_float_flags_left_12949328) || (__arm64_float_flags_right_12949328 != __arm64_float_flags_right_12949328))))
        {
            goto label_0xC59780;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59758UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC59760;
        label_0xC59760:
        ;
        __arm64_fcvtz_source_12949344 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_12949344 != __arm64_fcvtz_source_12949344) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_12949344 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_12949344 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_12949344)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_12949352 = x8;
        __arm64_flags_right_12949352 = 0x1UL;
        __arm64_flags_result_12949352 = unchecked((ulong)((__arm64_flags_left_12949352) & (__arm64_flags_right_12949352)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_12949352 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC59788;
        label_0xC59774:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC59778UL);
        goto label_0xC59788;
        label_0xC59780:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC59784UL);
        goto label_0xC59788;
        label_0xC59788:
        ;
        x8 = 0x7FF0000000000000UL;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12949392 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12949392)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12949392) + (0x8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_12949400 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_12949400 != __arm64_fcvtz_source_12949400) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_12949400 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_12949400 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_12949400)))))))));
        __arm64_float_flags_left_12949404 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_12949404 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC597A4UL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        sp = unchecked((ulong)((sp) + (0x30UL)));
        goto label_0xC597AC;
        label_0xC597AC:
        ;
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `CFUtils.DirToNormal` — RVA `0xc597b0`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public static Vector2 DirToNormal(Dir dir) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong CFUtils_DirToNormal_RVAc597b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12949432 = default(uint);
        uint __arm64_flags_right_12949432 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12949432 = unchecked((uint)(x8));
        __arm64_flags_right_12949432 = unchecked((uint)0x8UL);
        if ((__arm64_flags_left_12949432 >= __arm64_flags_right_12949432))
        {
            label_0xC597DC:
            ;
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC597FC:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
            x8 = RuntimeMemory.ReadU64(x8);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x9 = unchecked((ulong)((x8) + (0x4UL)));
        }
        else
        {
            x9 = 0x452000UL;
            x10 = 0x452000UL;
            x9 = unchecked((ulong)((x9) + (0x160UL)));
            x10 = unchecked((ulong)((x10) + (0x140UL)));
            x9 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
            x8 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        }
        label_0xC59810:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x9)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.DirToTangent` — RVA `0xc59820`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public static Vector2 DirToTangent(Dir dir) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong CFUtils_DirToTangent_RVAc59820(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12949544 = default(uint);
        uint __arm64_flags_right_12949544 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12949544 = unchecked((uint)(x8));
        __arm64_flags_right_12949544 = unchecked((uint)0x8UL);
        if ((__arm64_flags_left_12949544 >= __arm64_flags_right_12949544))
        {
            label_0xC5984C:
            ;
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC5986C:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
            x8 = RuntimeMemory.ReadU64(x8);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x9 = unchecked((ulong)((x8) + (0x4UL)));
        }
        else
        {
            x9 = 0x452000UL;
            x10 = 0x452000UL;
            x9 = unchecked((ulong)((x9) + (0x1C0UL)));
            x10 = unchecked((ulong)((x10) + (0x160UL)));
            x9 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
            x8 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        }
        label_0xC59880:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x9)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.GetOppositeDir` — RVA `0xc59890`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public static Dir GetOppositeDir(Dir dir) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint CFUtils_GetOppositeDir_RVAc59890(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12949652 = default(uint);
        uint __arm64_flags_right_12949652 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12949652 = unchecked((uint)(x8));
        __arm64_flags_right_12949652 = unchecked((uint)0x7UL);
        if (((__arm64_flags_left_12949652 >= __arm64_flags_right_12949652) && (!((unchecked((uint)((__arm64_flags_left_12949652) - (__arm64_flags_right_12949652))) == unchecked((uint)0x0UL))))))
        {
            label_0xC598AC:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x9 = 0x452000UL;
            x9 = unchecked((ulong)((x9) + (0x220UL)));
            x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `CFUtils.DirToVector` — RVA `0xc598b4`

- Lift status: **exact**; input span: 464 bytes; span to next metadata RVA: 464 bytes.
- Metadata signature: `public static Vector2 DirToVector(Dir dir, bool circular) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=102 (informational only).

```csharp
public static ulong CFUtils_DirToVector_RVAc598b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12949696 = default(uint);
        uint __arm64_flags_right_12949696 = default(uint);
        ulong __arm64_pair_address_12949684 = default(ulong);
        ulong __arm64_pair_address_12949848 = default(ulong);
        ulong __arm64_pair_address_12950140 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12949684 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12949684, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12949684) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12949684;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12949696 = unchecked((uint)(x8));
        __arm64_flags_right_12949696 = unchecked((uint)0x7UL);
        if (((__arm64_flags_left_12949696 >= __arm64_flags_right_12949696) && (!((unchecked((uint)((__arm64_flags_left_12949696) - (__arm64_flags_right_12949696))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC59928;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x9 = unchecked((ulong)((x9) + (0x120UL)));
        x10 = 0xC598E8UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC59928:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59948;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC59948;
        label_0xC59948:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12949848 = x8;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12949848)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12949848) + (0x4UL))))), 0));
        goto label_0xC59A70;
        label_0xC59A70:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_pair_address_12950140 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12950140)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12950140) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.VecToDir` — RVA `0xc59a84`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public static Dir VecToDir(Vector2 vec, bool as8way) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong CFUtils_VecToDir_RVAc59a84(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C90UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x554UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC592B8UL /* metadata target: CFUtils.NormalizeAnglePositive */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)(0x1UL)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC59474UL /* metadata target: CFUtils.DirFromAngle */);
        return default(ulong);
    }
```

## `CFUtils.VecToDir` — RVA `0xc59aac`

- Lift status: **exact**; input span: 280 bytes; span to next metadata RVA: 280 bytes.
- Metadata signature: `public static Dir VecToDir(Vector2 vec, Dir defaultDir, float deadZoneSq, bool as8way) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=30 (informational only).

```csharp
public static ulong CFUtils_VecToDir_RVAc59aac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12950224 = default(float);
        float __arm64_float_flags_left_12950256 = default(float);
        float __arm64_float_flags_left_12950324 = default(float);
        float __arm64_float_flags_right_12950224 = default(float);
        float __arm64_float_flags_right_12950256 = default(float);
        float __arm64_float_flags_right_12950324 = default(float);
        ulong __arm64_pair_address_12950188 = default(ulong);
        ulong __arm64_pair_address_12950192 = default(ulong);
        ulong __arm64_pair_address_12950352 = default(ulong);
        ulong __arm64_pair_address_12950356 = default(ulong);
        ulong __arm64_pair_address_12950412 = default(ulong);
        ulong __arm64_pair_address_12950456 = default(ulong);
        ulong __arm64_pair_address_12950460 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12950188 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12950188, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12950188) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12950188;
        __arm64_pair_address_12950192 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12950192, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12950192) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        v8 = v1;
        v9 = v0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12950224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12950224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12950224 <= __arm64_float_flags_right_12950224))
        {
            goto label_0xC59B48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        __arm64_float_flags_left_12950256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12950256 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12950256 <= __arm64_float_flags_right_12950256) || ((__arm64_float_flags_left_12950256 != __arm64_float_flags_left_12950256) || (__arm64_float_flags_right_12950256 != __arm64_float_flags_right_12950256))))
        {
            goto label_0xC59B90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59B18;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC59B18;
        label_0xC59B18:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59B30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC59B2CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC59B30;
        label_0xC59B30:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_12950324 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12950324 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12950324 <= __arm64_float_flags_right_12950324) || ((__arm64_float_flags_left_12950324 != __arm64_float_flags_left_12950324) || (__arm64_float_flags_right_12950324 != __arm64_float_flags_right_12950324))))
        {
            goto label_0xC59B5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC59B3CUL);
        }
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC59B90;
        label_0xC59B48:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_12950352 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12950352)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12950352) + (0x8UL))))), 0));
        __arm64_pair_address_12950356 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12950356)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12950356) + (0x8UL))))), 0));
        return x0;
        label_0xC59B5C:
        ;
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59B7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC59B7C;
        label_0xC59B7C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12950412 = x8;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12950412)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12950412) + (0x4UL))))), 0));
        goto label_0xC59B90;
        label_0xC59B90:
        ;
        v0 = v9;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C90UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x554UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC592B8UL /* metadata target: CFUtils.NormalizeAnglePositive */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)(0x1UL)))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_12950456 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12950456)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12950456) + (0x8UL))))), 0));
        __arm64_pair_address_12950460 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12950460)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12950460) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12950460) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0xC59474UL /* metadata target: CFUtils.DirFromAngle */);
        return default(ulong);
    }
```

## `CFUtils.DigitalToDir` — RVA `0xc59bc4`

- Lift status: **partial**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public static Dir DigitalToDir(bool digiU, bool digiR, bool digiD, bool digiL) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=13 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xc59be0; reason: Unknown IR expression at 0xc59be0; reason: Unsupported instruction 'cinc' at 0xc59c18; reason: Unknown IR expression at 0xc59c18; reason: Unsupported instruction 'csel' at 0xc59c1c; reason: Unknown IR expression at 0xc59c1c; reason: Unsupported instruction 'csinc' at 0xc59bec; reason: Unknown IR expression at 0xc59bec

```csharp
public static uint CFUtils_DigitalToDir_RVAc59bc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12950488 = default(uint);
        uint __arm64_flags_left_12950500 = default(uint);
        uint __arm64_flags_left_12950512 = default(uint);
        uint __arm64_flags_left_12950528 = default(uint);
        uint __arm64_flags_left_12950560 = default(uint);
        uint __arm64_flags_left_12950572 = default(uint);
        uint __arm64_flags_result_12950500 = default(uint);
        uint __arm64_flags_result_12950512 = default(uint);
        uint __arm64_flags_result_12950528 = default(uint);
        uint __arm64_flags_result_12950560 = default(uint);
        uint __arm64_flags_result_12950572 = default(uint);
        uint __arm64_flags_right_12950488 = default(uint);
        uint __arm64_flags_right_12950500 = default(uint);
        uint __arm64_flags_right_12950512 = default(uint);
        uint __arm64_flags_right_12950528 = default(uint);
        uint __arm64_flags_right_12950560 = default(uint);
        uint __arm64_flags_right_12950572 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(x2)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(x3)))))));
        x12 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(0x1UL)))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) ^ (unchecked((uint)(x3)))))));
        __arm64_flags_left_12950488 = unchecked((uint)(x12));
        __arm64_flags_right_12950488 = unchecked((uint)(x8));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) ^ (unchecked((uint)(x1)))))));
        RuntimeCalls.Unsupported("b.eq", 0xC59BE0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            label_0xC59C00:
            ;
            __arm64_flags_left_12950528 = unchecked((uint)(x10));
            __arm64_flags_right_12950528 = unchecked((uint)0x1UL);
            __arm64_flags_result_12950528 = unchecked((uint)((__arm64_flags_left_12950528) & (__arm64_flags_right_12950528)));
            x10 = unchecked((ulong)(unchecked((uint)(0x5UL))));
            x11 = unchecked((ulong)(unchecked((uint)(0x7UL))));
            x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) ^ (unchecked((uint)(x2)))))));
            x12 = unchecked((ulong)(unchecked((uint)(0x4UL))));
            x13 = unchecked((ulong)(unchecked((uint)(0x3UL))));
            RuntimeCalls.Unsupported("cinc", 0xC59C18UL);
            x10 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x10)))));
            RuntimeCalls.Unsupported("csel", 0xC59C1CUL);
            x11 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x11)) : unchecked((uint)0x0UL))));
            __arm64_flags_left_12950560 = unchecked((uint)(x8));
            __arm64_flags_right_12950560 = unchecked((uint)0x1UL);
            __arm64_flags_result_12950560 = unchecked((uint)((__arm64_flags_left_12950560) & (__arm64_flags_right_12950560)));
            x8 = unchecked((ulong)(((!((__arm64_flags_result_12950560 == unchecked((uint)0x0UL)))) ? unchecked((uint)(x12)) : unchecked((uint)(x10)))));
            x10 = unchecked((ulong)(((!((__arm64_flags_result_12950560 == unchecked((uint)0x0UL)))) ? unchecked((uint)(x13)) : unchecked((uint)(x11)))));
            __arm64_flags_left_12950572 = unchecked((uint)(x9));
            __arm64_flags_right_12950572 = unchecked((uint)0x1UL);
            __arm64_flags_result_12950572 = unchecked((uint)((__arm64_flags_left_12950572) & (__arm64_flags_right_12950572)));
            x0 = unchecked((ulong)(((!((__arm64_flags_result_12950572 == unchecked((uint)0x0UL)))) ? unchecked((uint)(x8)) : unchecked((uint)(x10)))));
            return unchecked((uint)(x0));
        }
        else
        {
            __arm64_flags_left_12950500 = unchecked((uint)(x10));
            __arm64_flags_right_12950500 = unchecked((uint)0x1UL);
            __arm64_flags_result_12950500 = unchecked((uint)((__arm64_flags_left_12950500) & (__arm64_flags_right_12950500)));
            x9 = unchecked((ulong)(unchecked((uint)(0x8UL))));
            RuntimeCalls.Unsupported("csinc", 0xC59BECUL);
            x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)((unchecked((uint)0x0UL)) + (unchecked((uint)0x1UL)))))));
            __arm64_flags_left_12950512 = unchecked((uint)(x8));
            __arm64_flags_right_12950512 = unchecked((uint)0x1UL);
            __arm64_flags_result_12950512 = unchecked((uint)((__arm64_flags_left_12950512) & (__arm64_flags_right_12950512)));
            x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
            RuntimeCalls.Unsupported("csel", 0xC59BF8UL);
            x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `CFUtils.CircularToSquareJoystickVec` — RVA `0xc59c38`

- Lift status: **exact**; input span: 304 bytes; span to next metadata RVA: 304 bytes.
- Metadata signature: `public static Vector2 CircularToSquareJoystickVec(Vector2 circularVec) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=36 (informational only).

```csharp
public static ulong CFUtils_CircularToSquareJoystickVec_RVAc59c38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12950624 = default(float);
        float __arm64_float_flags_left_12950748 = default(float);
        float __arm64_float_flags_left_12950860 = default(float);
        float __arm64_float_flags_right_12950624 = default(float);
        float __arm64_float_flags_right_12950748 = default(float);
        float __arm64_float_flags_right_12950860 = default(float);
        ulong __arm64_pair_address_12950584 = default(ulong);
        ulong __arm64_pair_address_12950588 = default(ulong);
        ulong __arm64_pair_address_12950680 = default(ulong);
        ulong __arm64_pair_address_12950816 = default(ulong);
        ulong __arm64_pair_address_12950876 = default(ulong);
        ulong __arm64_pair_address_12950880 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12950584 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12950584, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12950584) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12950584;
        __arm64_pair_address_12950588 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12950588, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12950588) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x8 = 0x432000UL;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v8 = v1;
        v9 = v0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12950624 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12950624 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12950624 >= __arm64_float_flags_right_12950624) || ((__arm64_float_flags_left_12950624 != __arm64_float_flags_left_12950624) || (__arm64_float_flags_right_12950624 != __arm64_float_flags_right_12950624))))
        {
            label_0xC59CA0:
            ;
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x243UL))))))));
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
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC59CC0:
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
            label_0xC59CD8:
            ;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))))), 0));
            __arm64_float_flags_left_12950748 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12950748 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_12950748 <= __arm64_float_flags_right_12950748) || ((__arm64_float_flags_left_12950748 != __arm64_float_flags_left_12950748) || (__arm64_float_flags_right_12950748 != __arm64_float_flags_right_12950748))))
            {
                label_0xC59CF0:
                ;
                x19 = 0x1BAB000UL;
                x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
                if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = 0x1A8C000UL;
                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                    // Likely IL2CPP class initialization helper (guarded call).
                    x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                    x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
                }
                label_0xC59D10:
                ;
                x8 = 0x1A8C000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
                x8 = RuntimeMemory.ReadU64(x8);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                __arm64_pair_address_12950816 = x8;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12950816)), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12950816) + (0x4UL))))), 0));
            }
            else
            {
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            }
            label_0xC59D24:
            ;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            __arm64_float_flags_left_12950860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12950860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            if ((__arm64_float_flags_left_12950860 < __arm64_float_flags_right_12950860))
            {
            }
        }
        else
        {
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC59C88:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
            x8 = RuntimeMemory.ReadU64(x8);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            __arm64_pair_address_12950680 = x8;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12950680)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12950680) + (0x4UL))))), 0));
        }
        label_0xC59D58:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12950876 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12950876)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12950876) + (0x8UL))))), 0));
        __arm64_pair_address_12950880 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12950880)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12950880) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.SquareToCircularJoystickVec` — RVA `0xc59d68`

- Lift status: **exact**; input span: 304 bytes; span to next metadata RVA: 304 bytes.
- Metadata signature: `public static Vector2 SquareToCircularJoystickVec(Vector2 squareVec) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=36 (informational only).

```csharp
public static ulong CFUtils_SquareToCircularJoystickVec_RVAc59d68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12950928 = default(float);
        float __arm64_float_flags_left_12951052 = default(float);
        float __arm64_float_flags_left_12951164 = default(float);
        float __arm64_float_flags_right_12950928 = default(float);
        float __arm64_float_flags_right_12951052 = default(float);
        float __arm64_float_flags_right_12951164 = default(float);
        ulong __arm64_pair_address_12950888 = default(ulong);
        ulong __arm64_pair_address_12950892 = default(ulong);
        ulong __arm64_pair_address_12950984 = default(ulong);
        ulong __arm64_pair_address_12951120 = default(ulong);
        ulong __arm64_pair_address_12951180 = default(ulong);
        ulong __arm64_pair_address_12951184 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12950888 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12950888, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12950888) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12950888;
        __arm64_pair_address_12950892 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12950892, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12950892) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x8 = 0x432000UL;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v8 = v1;
        v9 = v0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12950928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12950928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12950928 >= __arm64_float_flags_right_12950928) || ((__arm64_float_flags_left_12950928 != __arm64_float_flags_left_12950928) || (__arm64_float_flags_right_12950928 != __arm64_float_flags_right_12950928))))
        {
            label_0xC59DD0:
            ;
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x243UL))))))));
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
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC59DF0:
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
            label_0xC59E08:
            ;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))))), 0));
            __arm64_float_flags_left_12951052 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12951052 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_12951052 <= __arm64_float_flags_right_12951052) || ((__arm64_float_flags_left_12951052 != __arm64_float_flags_left_12951052) || (__arm64_float_flags_right_12951052 != __arm64_float_flags_right_12951052))))
            {
                label_0xC59E20:
                ;
                x19 = 0x1BAB000UL;
                x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
                if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = 0x1A8C000UL;
                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                    // Likely IL2CPP class initialization helper (guarded call).
                    x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                    x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
                }
                label_0xC59E40:
                ;
                x8 = 0x1A8C000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
                x8 = RuntimeMemory.ReadU64(x8);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                __arm64_pair_address_12951120 = x8;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12951120)), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12951120) + (0x4UL))))), 0));
            }
            else
            {
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            }
            label_0xC59E54:
            ;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            __arm64_float_flags_left_12951164 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12951164 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            if ((__arm64_float_flags_left_12951164 < __arm64_float_flags_right_12951164))
            {
            }
        }
        else
        {
            x19 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC59DB8:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
            x8 = RuntimeMemory.ReadU64(x8);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            __arm64_pair_address_12950984 = x8;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12950984)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12950984) + (0x4UL))))), 0));
        }
        label_0xC59E88:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12951180 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12951180)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12951180) + (0x8UL))))), 0));
        __arm64_pair_address_12951184 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12951184)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12951184) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `CFUtils.GetLineNumber` — RVA `0xc59e98`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public static int GetLineNumber(string str, int index) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static uint CFUtils_GetLineNumber_RVAc59e98(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12951236 = default(uint);
        uint __arm64_flags_left_12951276 = default(uint);
        uint __arm64_flags_right_12951236 = default(uint);
        uint __arm64_flags_right_12951276 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x0 == 0x0UL))
        {
            goto label_0xC59F04;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x1 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13FA46CUL /* metadata target: String.IndexOf */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59EF4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59EC4UL)));
        }
        __arm64_flags_left_12951236 = unchecked((uint)(x0));
        __arm64_flags_right_12951236 = unchecked((uint)(x19));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12951236) - (__arm64_flags_right_12951236))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12951236)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12951236)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12951236) - (__arm64_flags_right_12951236))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12951236)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC59EF4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC59ED0;
        label_0xC59ED0:
        ;
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(0x1UL)))))));
        x1 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x0 = x20;
        x3 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x13FA46CUL /* metadata target: String.IndexOf */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59EF4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59EECUL)));
        }
        __arm64_flags_left_12951276 = unchecked((uint)(x0));
        __arm64_flags_right_12951276 = unchecked((uint)(x19));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12951276) - (__arm64_flags_right_12951276))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12951276)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12951276)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12951276) - (__arm64_flags_right_12951276))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12951276)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC59ED0;
        }
        else
        {
            goto label_0xC59EF4;
        }
        label_0xC59EF4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC59F04:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `CFUtils.GetEnumMaxValue` — RVA `0xc59f08`

- Lift status: **partial**; input span: 756 bytes; span to next metadata RVA: 756 bytes.
- Metadata signature: `public static int GetEnumMaxValue(Type enumType) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=110 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc59fdc; reason: Unknown IR expression at 0xc59fdc; reason: Unsupported instruction 'b.ne' at 0xc5a038; reason: Unknown IR expression at 0xc5a038; reason: Unsupported instruction 'b.ne' at 0xc5a0e4; reason: Unknown IR expression at 0xc5a0e4; reason: Unsupported instruction 'b.ne' at 0xc5a1b8; reason: Unknown IR expression at 0xc5a1b8

```csharp
public static uint CFUtils_GetEnumMaxValue_RVAc59f08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12951500 = default(ulong);
        ulong __arm64_flags_left_12951508 = default(ulong);
        ulong __arm64_flags_left_12951592 = default(ulong);
        ulong __arm64_flags_left_12951600 = default(ulong);
        ulong __arm64_flags_left_12951676 = default(ulong);
        uint __arm64_flags_left_12951692 = default(uint);
        uint __arm64_flags_left_12951700 = default(uint);
        ulong __arm64_flags_left_12951764 = default(ulong);
        ulong __arm64_flags_left_12951772 = default(ulong);
        uint __arm64_flags_left_12951888 = default(uint);
        ulong __arm64_flags_left_12951976 = default(ulong);
        ulong __arm64_flags_left_12951984 = default(ulong);
        ulong __arm64_flags_result_12951508 = default(ulong);
        ulong __arm64_flags_result_12951600 = default(ulong);
        ulong __arm64_flags_result_12951772 = default(ulong);
        ulong __arm64_flags_result_12951984 = default(ulong);
        ulong __arm64_flags_right_12951500 = default(ulong);
        ulong __arm64_flags_right_12951508 = default(ulong);
        ulong __arm64_flags_right_12951592 = default(ulong);
        ulong __arm64_flags_right_12951600 = default(ulong);
        ulong __arm64_flags_right_12951676 = default(ulong);
        uint __arm64_flags_right_12951692 = default(uint);
        uint __arm64_flags_right_12951700 = default(uint);
        ulong __arm64_flags_right_12951764 = default(ulong);
        ulong __arm64_flags_right_12951772 = default(ulong);
        uint __arm64_flags_right_12951888 = default(uint);
        ulong __arm64_flags_right_12951976 = default(ulong);
        ulong __arm64_flags_right_12951984 = default(ulong);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x29BUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xEC0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59F64;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xED0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x29BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC59F64;
        label_0xC59F64:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC59F74;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59F70UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC59F74;
        label_0xC59F74:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x15793B8UL /* metadata target: Enum.GetValues */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A130;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xEC8UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x156B670UL /* metadata target: Array.GetEnumerator */, x0, x1, x2, x3);
        x20 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A134;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xED0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x1C0UL))));
        x19 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC59FB0;
        label_0xC59FB0:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = RuntimeMemory.ReadU64(x21);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC59FE0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC59FC8;
        label_0xC59FC8:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12951500 = x11;
        __arm64_flags_right_12951500 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12951500) - (__arm64_flags_right_12951500))) == 0x0UL))
        {
            goto label_0xC59FF0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC59FD4UL)));
        }
        __arm64_flags_left_12951508 = x9;
        __arm64_flags_right_12951508 = 0x1UL;
        __arm64_flags_result_12951508 = unchecked((ulong)((__arm64_flags_left_12951508) - (__arm64_flags_right_12951508)));
        x9 = __arm64_flags_result_12951508;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC59FDCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC59FC8;
        }
        else
        {
            goto label_0xC59FE0;
        }
        label_0xC59FE0:
        ;
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC59FFC;
        label_0xC59FF0:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC59FFC;
        label_0xC59FFC:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5A0A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = RuntimeMemory.ReadU64(x21);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5A03C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC5A024;
        label_0xC5A024:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12951592 = x11;
        __arm64_flags_right_12951592 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12951592) - (__arm64_flags_right_12951592))) == 0x0UL))
        {
            goto label_0xC5A04C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5A030UL)));
        }
        __arm64_flags_left_12951600 = x9;
        __arm64_flags_right_12951600 = 0x1UL;
        __arm64_flags_result_12951600 = unchecked((ulong)((__arm64_flags_left_12951600) - (__arm64_flags_right_12951600)));
        x9 = __arm64_flags_result_12951600;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC5A038UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC5A024;
        }
        else
        {
            goto label_0xC5A03C;
        }
        label_0xC5A03C:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A05C;
        label_0xC5A04C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(x10)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x4UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC5A05C;
        label_0xC5A05C:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A12C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x40UL))));
        __arm64_flags_left_12951676 = x8;
        __arm64_flags_right_12951676 = x9;
        if ((!((unchecked((ulong)((__arm64_flags_left_12951676) - (__arm64_flags_right_12951676))) == 0x0UL))))
        {
            goto label_0xC5A128;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5A084UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA68UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(x0)));
        __arm64_flags_left_12951692 = unchecked((uint)(x19));
        __arm64_flags_right_12951692 = unchecked((uint)(x8));
        x9 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_12951692) - (__arm64_flags_right_12951692))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12951692) - (__arm64_flags_right_12951692))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12951692)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12951692)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12951692) - (__arm64_flags_right_12951692))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12951692)) < unchecked((int)0x0UL)))))) ? unchecked((uint)(x19)) : unchecked((uint)(x8)))));
        __arm64_flags_left_12951700 = unchecked((uint)(x19));
        __arm64_flags_right_12951700 = unchecked((uint)0x0UL);
        x19 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12951700) - (__arm64_flags_right_12951700))) == unchecked((uint)0x0UL)) ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        goto label_0xC59FB0;
        label_0xC5A0A0:
        ;
        x21 = 0x0UL;
        goto label_0xC5A0A4;
        label_0xC5A0A4:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A110;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(x22);
        x20 = x0;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5A0E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC5A0D0;
        label_0xC5A0D0:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12951764 = x11;
        __arm64_flags_right_12951764 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12951764) - (__arm64_flags_right_12951764))) == 0x0UL))
        {
            goto label_0xC5A0F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5A0DCUL)));
        }
        __arm64_flags_left_12951772 = x9;
        __arm64_flags_right_12951772 = 0x1UL;
        __arm64_flags_result_12951772 = unchecked((ulong)((__arm64_flags_left_12951772) - (__arm64_flags_right_12951772)));
        x9 = __arm64_flags_result_12951772;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC5A0E4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC5A0D0;
        }
        else
        {
            goto label_0xC5A0E8;
        }
        label_0xC5A0E8:
        ;
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A104;
        label_0xC5A0F8:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC5A104;
        label_0xC5A104:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A110;
        label_0xC5A110:
        ;
        if ((x21 != 0x0UL))
        {
            goto label_0xC5A138;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)(x19))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC5A128:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A12C;
        label_0xC5A12C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A130;
        label_0xC5A130:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A134;
        label_0xC5A134:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A138;
        label_0xC5A138:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x19 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC5A150;
        label_0xC5A150:
        ;
        __arm64_flags_left_12951888 = unchecked((uint)(x1));
        __arm64_flags_right_12951888 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12951888) - (__arm64_flags_right_12951888))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC5A168;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5A158UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x21 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A0A4;
        label_0xC5A168:
        ;
        x19 = x0;
        x21 = 0x0UL;
        goto label_0xC5A178;
        label_0xC5A178:
        ;
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A1E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU16(unchecked((ulong)((x8) + (0x12EUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5A1BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB0UL))));
        x10 = unchecked((ulong)((x10) + (0x8UL)));
        goto label_0xC5A1A4;
        label_0xC5A1A4:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12951976 = x11;
        __arm64_flags_right_12951976 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12951976) - (__arm64_flags_right_12951976))) == 0x0UL))
        {
            goto label_0xC5A1CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5A1B0UL)));
        }
        __arm64_flags_left_12951984 = x9;
        __arm64_flags_right_12951984 = 0x1UL;
        __arm64_flags_result_12951984 = unchecked((ulong)((__arm64_flags_left_12951984) - (__arm64_flags_right_12951984)));
        x9 = __arm64_flags_result_12951984;
        x10 = unchecked((ulong)((x10) + (0x10UL)));
        RuntimeCalls.Unsupported("b.ne", 0xC5A1B8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC5A1A4;
        }
        else
        {
            goto label_0xC5A1BC;
        }
        label_0xC5A1BC:
        ;
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB80110UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A1D8;
        label_0xC5A1CC:
        ;
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(x10)))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x4UL))))))));
        x0 = unchecked((ulong)((x8) + (0x138UL)));
        goto label_0xC5A1D8;
        label_0xC5A1D8:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A1E4;
        label_0xC5A1E4:
        ;
        if ((x21 != 0x0UL))
        {
            goto label_0xC5A1F0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC5A1F0;
        label_0xC5A1F0:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `CFUtils.CycleInt` — RVA `0xc5a1fc`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public static int CycleInt(int curId, int dir, int maxId) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint CFUtils_CycleInt_RVAc5a1fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12952060 = default(uint);
        uint __arm64_flags_left_12952068 = default(uint);
        uint __arm64_flags_result_12952060 = default(uint);
        uint __arm64_flags_right_12952060 = default(uint);
        uint __arm64_flags_right_12952068 = default(uint);
        ulong x8 = default(ulong);
        __arm64_flags_left_12952060 = unchecked((uint)(x1));
        __arm64_flags_right_12952060 = unchecked((uint)(x0));
        __arm64_flags_result_12952060 = unchecked((uint)((__arm64_flags_left_12952060) + (__arm64_flags_right_12952060)));
        x8 = unchecked((ulong)(__arm64_flags_result_12952060));
        if ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12952060) + (__arm64_flags_right_12952060))))) < unchecked((int)0x0UL)))
        {
            label_0xC5A210:
            ;
            x0 = unchecked((ulong)(unchecked((uint)(x2))));
            return unchecked((uint)(x0));
        }
        else
        {
            __arm64_flags_left_12952068 = unchecked((uint)(x8));
            __arm64_flags_right_12952068 = unchecked((uint)(x2));
            x0 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_12952068) - (__arm64_flags_right_12952068))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12952068) - (__arm64_flags_right_12952068))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12952068)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12952068)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12952068) - (__arm64_flags_right_12952068))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12952068)) < unchecked((int)0x0UL)))))) ? unchecked((uint)0x0UL) : unchecked((uint)(x8)))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `CFUtils.SetEventSystemSelectedObject` — RVA `0xc5a218`

- Lift status: **exact**; input span: 300 bytes; span to next metadata RVA: 300 bytes.
- Metadata signature: `public static void SetEventSystemSelectedObject(GameObject o) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=49 (informational only).

```csharp
public static ulong CFUtils_SetEventSystemSelectedObject_RVAc5a218(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12952296 = default(uint);
        ulong __arm64_flags_left_12952316 = default(ulong);
        uint __arm64_flags_right_12952296 = default(uint);
        ulong __arm64_flags_right_12952316 = default(ulong);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x29CUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x5D0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A264;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xED8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x29CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5A264;
        label_0xC5A264:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A27C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A278UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5A27C;
        label_0xC5A27C:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x199C464UL /* metadata target: EventSystem.get_current */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A29C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5A29C;
        label_0xC5A29C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5A304;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A2B0UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC5A340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x30UL))), x19);
        x0 = x21;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5A304;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = 0x1A8C000UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xED8UL))));
        x9 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(x10);
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x130UL))))))));
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        __arm64_flags_left_12952296 = unchecked((uint)(x11));
        __arm64_flags_right_12952296 = unchecked((uint)(x10));
        if ((!((__arm64_flags_left_12952296 >= __arm64_flags_right_12952296))))
        {
            goto label_0xC5A304;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC8UL))));
        x9 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12952316 = x9;
        __arm64_flags_right_12952316 = x8;
        if ((unchecked((ulong)((__arm64_flags_left_12952316) - (__arm64_flags_right_12952316))) == 0x0UL))
        {
            goto label_0xC5A310;
        }
        else
        {
            goto label_0xC5A304;
        }
        label_0xC5A304:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC5A310:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x199AF48UL /* metadata target: EventSystem.SetSelectedGameObject */, x0, x1, x2, x3);
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x199AF48UL /* metadata target: EventSystem.SetSelectedGameObject */);
        label_0xC5A340:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
