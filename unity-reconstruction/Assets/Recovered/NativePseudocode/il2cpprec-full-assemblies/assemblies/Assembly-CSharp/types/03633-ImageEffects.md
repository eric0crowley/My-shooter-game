# `ImageEffects` — TypeDefIndex 3633

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `ImageEffects.RenderDistortion` — RVA `0xce5e5c`

- Lift status: **exact**; input span: 608 bytes; span to next metadata RVA: 608 bytes.
- Metadata signature: `public static void RenderDistortion(Material material, RenderTexture source, RenderTexture destination, float angle, Vector2 center, Vector2 radius) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=85 (informational only).

```csharp
public static ulong ImageEffects_RenderDistortion_RVAce5e5c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13524752 = default(float);
        float __arm64_float_flags_right_13524752 = default(float);
        ulong __arm64_pair_address_13524576 = default(ulong);
        ulong __arm64_pair_address_13524580 = default(ulong);
        ulong __arm64_pair_address_13524584 = default(ulong);
        ulong __arm64_pair_address_13524588 = default(ulong);
        ulong __arm64_pair_address_13524720 = default(ulong);
        ulong __arm64_pair_address_13524836 = default(ulong);
        ulong __arm64_pair_address_13524960 = default(ulong);
        ulong __arm64_pair_address_13524964 = default(ulong);
        ulong __arm64_pair_address_13524968 = default(ulong);
        ulong __arm64_pair_address_13524972 = default(ulong);
        ulong __arm64_pair_address_13524976 = default(ulong);
        ulong __arm64_pair_address_13524980 = default(ulong);
        ulong __arm64_pair_address_13525020 = default(ulong);
        ulong __arm64_pair_address_13525024 = default(ulong);
        ulong __arm64_pair_address_13525044 = default(ulong);
        ulong __arm64_pair_address_13525048 = default(ulong);
        ulong __arm64_pair_address_13525060 = default(ulong);
        ulong __arm64_pair_address_13525064 = default(ulong);
        ulong __arm64_pair_address_13525152 = default(ulong);
        ulong __arm64_pair_address_13525156 = default(ulong);
        ulong __arm64_pair_address_13525160 = default(ulong);
        ulong __arm64_pair_address_13525164 = default(ulong);
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
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x160UL)));
        __arm64_pair_address_13524576 = unchecked((ulong)((sp) + (0xE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13524576, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13524576) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13524580 = unchecked((ulong)((sp) + (0xF0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13524580, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13524580) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13524584 = unchecked((ulong)((sp) + (0x100UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13524584, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13524584) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13524588 = unchecked((ulong)((sp) + (0x110UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13524588, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13524588) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x65EUL))))))));
        v8 = v4;
        v9 = v3;
        v11 = v2;
        v10 = v1;
        v12 = v0;
        x19 = x2;
        x20 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB38UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB40UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB48UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x65EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCE5EE4:
        ;
        if ((x20 == 0x0UL))
        {
        }
        else
        {
            x0 = x20;
            x1 = 0x0UL;
            __arm64_pair_address_13524720 = unchecked((ulong)((sp) + (0x14UL)));
            RuntimeMemory.WriteF32(__arm64_pair_address_13524720, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13524720) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x1CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x177E31CUL /* metadata target: Texture.get_texelSize */, x0, x1, x2, x3);
            x22 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x2C9UL))))))));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)))), 0));
            __arm64_float_flags_left_13524752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            __arm64_float_flags_right_13524752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13524752 < __arm64_float_flags_right_13524752) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13524752 < __arm64_float_flags_right_13524752) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x10UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xCE5F38:
            ;
            x22 = 0x1A8C000UL;
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1E8UL))));
            x9 = 0x432000UL;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x3E4UL))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            x8 = RuntimeMemory.ReadU64(x22);
            x0 = 0x0UL;
            v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            v2 = v12;
            __arm64_pair_address_13524836 = x8;
            v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13524836)), 0));
            v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13524836) + (0x4UL))))), 0));
            v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x178B12CUL /* metadata target: Quaternion.Internal_FromEulerRad */, x0, x1, x2, x3);
            x23 = 0x1BAB000UL;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1E1UL))))))));
            v8 = v0;
            v9 = v1;
            v10 = v2;
            v11 = v3;
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xCE5FA0:
            ;
            x8 = RuntimeMemory.ReadU64(x22);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCUL))));
            x0 = 0x0UL;
            RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            RuntimeMemory.WriteU64(sp, x9);
            x0 = RuntimeCalls.InvokeDirect(0x17862BCUL /* metadata target: Matrix4x4.TRS */, x0, x1, x2, x3);
            __arm64_pair_address_13524960 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13524960);
#else
            v1 = __ReadVector128(__arm64_pair_address_13524960);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13524960) + (0x10UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13524960) + (0x10UL))));
#endif
            __arm64_pair_address_13524964 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13524964);
#else
            v2 = __ReadVector128(__arm64_pair_address_13524964);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13524964) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13524964) + (0x10UL))));
#endif
            __arm64_pair_address_13524968 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13524968, v1);
#else
            __WriteVector128(__arm64_pair_address_13524968, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13524968) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13524968) + (0x10UL))), v0);
#endif
            __arm64_pair_address_13524972 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13524972, v2);
#else
            __WriteVector128(__arm64_pair_address_13524972, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13524972) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13524972) + (0x10UL))), v3);
#endif
            __arm64_pair_address_13524976 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13524976, v2);
#else
            __WriteVector128(__arm64_pair_address_13524976, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13524976) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13524976) + (0x10UL))), v3);
#endif
            __arm64_pair_address_13524980 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13524980, v1);
#else
            __WriteVector128(__arm64_pair_address_13524980, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13524980) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13524980) + (0x10UL))), v0);
#endif
            if ((x21 == 0x0UL))
            {
            }
            else
            {
                x8 = 0x1A8F000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB40UL))));
                x22 = 0x1A8F000UL;
                x23 = 0x1A8F000UL;
                x24 = 0x1A8D000UL;
                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xB48UL))));
                x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xB38UL))));
                x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xC68UL))));
                __arm64_pair_address_13525020 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13525020);
#else
                v0 = __ReadVector128(__arm64_pair_address_13525020);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13525020) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13525020) + (0x10UL))));
#endif
                __arm64_pair_address_13525024 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13525024);
#else
                v2 = __ReadVector128(__arm64_pair_address_13525024);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13525024) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13525024) + (0x10UL))));
#endif
                x1 = RuntimeMemory.ReadU64(x8);
                x2 = unchecked((ulong)((sp) + (0x20UL)));
                x0 = x21;
                x3 = 0x0UL;
                __arm64_pair_address_13525044 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13525044, v0);
#else
                __WriteVector128(__arm64_pair_address_13525044, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13525044) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13525044) + (0x10UL))), v1);
#endif
                __arm64_pair_address_13525048 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13525048, v2);
#else
                __WriteVector128(__arm64_pair_address_13525048, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13525048) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13525048) + (0x10UL))), v3);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x177B7ECUL /* metadata target: Material.SetMatrix */, x0, x1, x2, x3);
                x1 = RuntimeMemory.ReadU64(x22);
                __arm64_pair_address_13525060 = unchecked((ulong)((sp) + (0x10UL)));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13525060)), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13525060) + (0x4UL))))), 0));
                __arm64_pair_address_13525064 = unchecked((ulong)((sp) + (0x18UL)));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13525064)), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13525064) + (0x4UL))))), 0));
                x0 = x21;
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x177B76CUL /* metadata target: Material.SetVector */, x0, x1, x2, x3);
                x1 = RuntimeMemory.ReadU64(x23);
                x0 = x21;
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x177B698UL /* metadata target: Material.SetFloat */, x0, x1, x2, x3);
                x0 = RuntimeMemory.ReadU64(x24);
                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
                if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
                }
                label_0xCE607C:
                ;
                x0 = x20;
                x1 = x19;
                x2 = x21;
                x3 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17786BCUL /* metadata target: Graphics.Blit */, x0, x1, x2, x3);
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x150UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))));
                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x140UL))));
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x8UL))));
                x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x130UL))));
                x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x8UL))));
                x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x120UL))));
                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))));
                __arm64_pair_address_13525152 = unchecked((ulong)((sp) + (0x110UL)));
                v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13525152)), 0));
                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13525152) + (0x8UL))))), 0));
                __arm64_pair_address_13525156 = unchecked((ulong)((sp) + (0x100UL)));
                v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13525156)), 0));
                v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13525156) + (0x8UL))))), 0));
                __arm64_pair_address_13525160 = unchecked((ulong)((sp) + (0xF0UL)));
                v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13525160)), 0));
                v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13525160) + (0x8UL))))), 0));
                __arm64_pair_address_13525164 = unchecked((ulong)((sp) + (0xE0UL)));
                v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13525164)), 0));
                v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13525164) + (0x8UL))))), 0));
                return x0;
            }
        }
        label_0xCE60B8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `ImageEffects.Blit` — RVA `0xce60bc`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public static void Blit(RenderTexture source, RenderTexture dest) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong ImageEffects_Blit_RVAce60bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x65FUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC68UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE60F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x65FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE60F8;
        label_0xCE60F8:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE6108;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE6104UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE6108;
        label_0xCE6108:
        ;
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1778598UL /* metadata target: Graphics.Blit */);
        return default(ulong);
    }
```

## `ImageEffects.BlitWithMaterial` — RVA `0xce6124`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public static void BlitWithMaterial(Material material, RenderTexture source, RenderTexture dest) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong ImageEffects_BlitWithMaterial_RVAce6124(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x23 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x660UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC68UL))));
        x19 = x2;
        x21 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE6164;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x660UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE6164;
        label_0xCE6164:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE6174;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE6170UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE6174;
        label_0xCE6174:
        ;
        x0 = x21;
        x1 = x19;
        x2 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x17786BCUL /* metadata target: Graphics.Blit */);
        return default(ulong);
    }
```

## `ImageEffects.ctor` — RVA `0xce6194`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong ImageEffects_ctor_RVAce6194(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```
