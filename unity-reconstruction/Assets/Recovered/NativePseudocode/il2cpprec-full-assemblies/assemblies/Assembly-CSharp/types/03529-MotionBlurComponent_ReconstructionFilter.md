# `MotionBlurComponent.ReconstructionFilter` — TypeDefIndex 3529

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `RenderTextureFormat` | `m_VectorRTFormat` |
| `0x14` | `RenderTextureFormat` | `m_PackedRTFormat` |

## `MotionBlurComponent.ReconstructionFilter.ctor` — RVA `0xcd56d4`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static uint MotionBlurComponent_ReconstructionFilter_ctor_RVAcd56d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x250UL))))), 0));
        x1 = 0x0UL;
        x19 = x0;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x14UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x14UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        }
        label_0xCD5704:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `MotionBlurComponent.ReconstructionFilter.IsSupported` — RVA `0xcd58ac`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsSupported() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MotionBlurComponent_ReconstructionFilter_IsSupported_RVAcd58ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x179A814UL /* metadata target: SystemInfo.get_supportsMotionVectors */);
        return default(ulong);
    }
```

## `MotionBlurComponent.ReconstructionFilter.ProcessImage` — RVA `0xcd6044`

- Lift status: **partial**; input span: 2320 bytes; span to next metadata RVA: 2320 bytes.
- Metadata signature: `public void ProcessImage(PostProcessingContext context, CommandBuffer cb, ref MotionBlurModel.Settings settings, RenderTargetIdentifier source, RenderTargetIdentifier destination, Material material) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=351 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cinc' at 0xcd6254; reason: Unknown IR expression at 0xcd6254; reason: Unsupported instruction 'csel' at 0xcd6374; reason: Unknown IR expression at 0xcd6374; reason: Unsupported instruction 'csel' at 0xcd6380; reason: Unknown IR expression at 0xcd6380; reason: Unsupported instruction 'csel' at 0xcd64a4; reason: Unknown IR expression at 0xcd64a4

```csharp
public static ulong MotionBlurComponent_ReconstructionFilter_ProcessImage_RVAcd6044(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fcvtz_source_13459680 = default(float);
        float __arm64_fcvtz_source_13461008 = default(float);
        uint __arm64_flags_left_13459708 = default(uint);
        uint __arm64_flags_left_13460036 = default(uint);
        uint __arm64_flags_left_13460044 = default(uint);
        uint __arm64_flags_left_13460332 = default(uint);
        uint __arm64_flags_left_13460344 = default(uint);
        uint __arm64_flags_left_13460636 = default(uint);
        uint __arm64_flags_left_13460648 = default(uint);
        uint __arm64_flags_left_13461624 = default(uint);
        uint __arm64_flags_left_13461636 = default(uint);
        uint __arm64_flags_left_13461648 = default(uint);
        uint __arm64_flags_right_13459708 = default(uint);
        uint __arm64_flags_right_13460036 = default(uint);
        uint __arm64_flags_right_13460044 = default(uint);
        uint __arm64_flags_right_13460332 = default(uint);
        uint __arm64_flags_right_13460344 = default(uint);
        uint __arm64_flags_right_13460636 = default(uint);
        uint __arm64_flags_right_13460648 = default(uint);
        uint __arm64_flags_right_13461624 = default(uint);
        uint __arm64_flags_right_13461636 = default(uint);
        uint __arm64_flags_right_13461648 = default(uint);
        float __arm64_float_flags_left_13459684 = default(float);
        float __arm64_float_flags_left_13461024 = default(float);
        float __arm64_float_flags_right_13459684 = default(float);
        float __arm64_float_flags_right_13461024 = default(float);
        ulong __arm64_load_address_13461832 = default(ulong);
        ulong __arm64_pair_address_13460264 = default(ulong);
        ulong __arm64_pair_address_13460272 = default(ulong);
        ulong __arm64_pair_address_13460444 = default(ulong);
        ulong __arm64_pair_address_13460476 = default(ulong);
        ulong __arm64_pair_address_13460508 = default(ulong);
        ulong __arm64_pair_address_13460552 = default(ulong);
        ulong __arm64_pair_address_13460560 = default(ulong);
        ulong __arm64_pair_address_13460720 = default(ulong);
        ulong __arm64_pair_address_13460744 = default(ulong);
        ulong __arm64_pair_address_13460776 = default(ulong);
        ulong __arm64_pair_address_13460796 = default(ulong);
        ulong __arm64_pair_address_13460804 = default(ulong);
        ulong __arm64_pair_address_13460812 = default(ulong);
        ulong __arm64_pair_address_13460844 = default(ulong);
        ulong __arm64_pair_address_13460852 = default(ulong);
        ulong __arm64_pair_address_13461164 = default(ulong);
        ulong __arm64_pair_address_13461188 = default(ulong);
        ulong __arm64_pair_address_13461220 = default(ulong);
        ulong __arm64_pair_address_13461240 = default(ulong);
        ulong __arm64_pair_address_13461248 = default(ulong);
        ulong __arm64_pair_address_13461256 = default(ulong);
        ulong __arm64_pair_address_13461288 = default(ulong);
        ulong __arm64_pair_address_13461296 = default(ulong);
        ulong __arm64_pair_address_13461432 = default(ulong);
        ulong __arm64_pair_address_13461456 = default(ulong);
        ulong __arm64_pair_address_13461492 = default(ulong);
        ulong __arm64_pair_address_13461512 = default(ulong);
        ulong __arm64_pair_address_13461520 = default(ulong);
        ulong __arm64_pair_address_13461528 = default(ulong);
        ulong __arm64_pair_address_13461560 = default(ulong);
        ulong __arm64_pair_address_13461568 = default(ulong);
        ulong __arm64_pair_address_13461668 = default(ulong);
        ulong __arm64_pair_address_13461696 = default(ulong);
        ulong __arm64_pair_address_13461712 = default(ulong);
        ulong __arm64_pair_address_13461728 = default(ulong);
        ulong __arm64_pair_address_13461736 = default(ulong);
        ulong __arm64_pair_address_13461764 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x4C0UL)));
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5E7UL))))))));
        x20 = x6;
        x27 = x5;
        x22 = x4;
        x28 = x3;
        x19 = x2;
        x26 = x1;
        x25 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5E7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD60A0:
        ;
        if ((x26 == 0x0UL))
        {
        }
        else
        {
            x23 = 0x1A8F000UL;
            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x1E0UL))));
            x0 = x26;
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40A00000UL)), 0)), 0));
            x8 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
            x0 = RuntimeMemory.ReadU64(x23);
            x9 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
            x10 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
            __arm64_fcvtz_source_13459680 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            x8 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13459680 != __arm64_fcvtz_source_13459680) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13459680 >= global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x4F000000UL)), 0)) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13459680 < global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xCF000000UL)), 0)) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13459680)))))))));
            __arm64_float_flags_left_13459684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_13459684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            x24 = unchecked((ulong)(((__arm64_float_flags_left_13459684 == __arm64_float_flags_right_13459684) ? unchecked((uint)(x10)) : unchecked((uint)(x8)))));
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x28)), 0));
            x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) - (unchecked((uint)(0x1UL)))))));
            x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) + (unchecked((uint)(0x6UL)))))));
            __arm64_flags_left_13459708 = unchecked((uint)(x9));
            __arm64_flags_right_13459708 = unchecked((uint)0x0UL);
            x21 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13459708) - (__arm64_flags_right_13459708))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13459708)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13459708)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13459708) - (__arm64_flags_right_13459708))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13459708)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x10)) : unchecked((uint)(x9)))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            }
            label_0xCD610C:
            ;
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x28);
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x4C8UL))), x27);
            if ((x19 == 0x0UL))
            {
            }
            else
            {
                x8 = RuntimeMemory.ReadU64(x23);
                x9 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
                x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)(0xFFFFFFF8UL)))))));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                x0 = x19;
                x2 = 0x0UL;
                x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
                x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x8UL)))))));
                x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x24))))))), 0));
                x0 = x19;
                v0 = v8;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x2 = 0x0UL;
                x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
                x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
                x0 = x19;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x2 = 0x0UL;
                x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
                x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = x26;
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
                x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                x27 = unchecked((ulong)(unchecked((uint)(x0))));
                x0 = x26;
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                x6 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x14UL))))));
                x3 = unchecked((ulong)(unchecked((uint)(x0))));
                x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x24))));
                x2 = unchecked((ulong)(unchecked((uint)(x27))));
                x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
                RuntimeMemory.WritePtr(sp, 0x0UL);
                x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                x8 = unchecked((ulong)((sp) + (0x490UL)));
                x0 = unchecked((ulong)(unchecked((uint)(x24))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x490UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((sp) + (0x490UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x4A0UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x4A0UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x4B0UL))));
                x2 = unchecked((ulong)((sp) + (0x460UL)));
                x0 = x19;
                x1 = 0x0UL;
                x3 = x20;
                x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                x5 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x480UL))), x8);
                x0 = RuntimeCalls.InvokeDirect(0x17A7CE8UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = x26;
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
                x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                x28 = unchecked((ulong)(unchecked((uint)(x0))));
                x0 = x26;
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                x6 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x10UL))))));
                __arm64_flags_left_13460036 = unchecked((uint)(x28));
                __arm64_flags_right_13460036 = unchecked((uint)0x0UL);
                x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13460036) - (__arm64_flags_right_13460036))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13460036)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13460036)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13460036) - (__arm64_flags_right_13460036))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13460036)) < unchecked((int)0x0UL))))) ? unchecked((uint)((unchecked((uint)(x28))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x28)))));
                __arm64_flags_left_13460044 = unchecked((uint)(x0));
                __arm64_flags_right_13460044 = unchecked((uint)0x0UL);
                x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x8))))) >> (int)(unchecked((int)(0x1UL)))))))));
                RuntimeCalls.Unsupported("cinc", 0xCD6254UL);
                x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x0)))));
                x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x8))))) >> (int)(unchecked((int)(0x1UL)))))))));
                x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x27))));
                x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
                RuntimeMemory.WritePtr(sp, 0x0UL);
                x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = unchecked((ulong)(unchecked((uint)(x24))));
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x28 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                x8 = unchecked((ulong)((sp) + (0x490UL)));
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x490UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((sp) + (0x490UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x4A0UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x4A0UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x4B0UL))));
                x2 = unchecked((ulong)((sp) + (0x430UL)));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x28))));
                x3 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x440UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x440UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x450UL))), x8);
                x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = unchecked((ulong)((sp) + (0x400UL)));
                x0 = unchecked((ulong)(unchecked((uint)(x24))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x420UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#endif
                x0 = unchecked((ulong)(unchecked((uint)(x27))));
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x4B0UL))), x8);
                x8 = unchecked((ulong)((sp) + (0x400UL)));
                x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x490UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x490UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4A0UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x4A0UL))), v1);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x420UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x490UL))));
#else
                v2 = __ReadVector128(unchecked((ulong)((sp) + (0x490UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x4A0UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((sp) + (0x4A0UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x4B0UL))));
                x1 = unchecked((ulong)((sp) + (0x3D0UL)));
                x2 = unchecked((ulong)((sp) + (0x3A0UL)));
                x4 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x0 = x19;
                x3 = x20;
                x5 = 0x0UL;
                __arm64_pair_address_13460264 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460264, v0);
#else
                __WriteVector128(__arm64_pair_address_13460264, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460264) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460264) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3C0UL))), x8);
                __arm64_pair_address_13460272 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460272, v2);
#else
                __WriteVector128(__arm64_pair_address_13460272, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460272) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460272) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3F0UL))), x9);
                x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = x26;
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x28 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
                x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                x29 = unchecked((ulong)(unchecked((uint)(x0))));
                x0 = x26;
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                x6 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x10UL))))));
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) + (unchecked((uint)(0x3UL)))))));
                __arm64_flags_left_13460332 = unchecked((uint)(x29));
                __arm64_flags_right_13460332 = unchecked((uint)0x0UL);
                x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(0x3UL)))))));
                RuntimeCalls.Unsupported("csel", 0xCD6374UL);
                x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x29)))));
                __arm64_flags_left_13460344 = unchecked((uint)(x0));
                __arm64_flags_right_13460344 = unchecked((uint)0x0UL);
                x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x8))))) >> (int)(unchecked((int)(0x2UL)))))))));
                RuntimeCalls.Unsupported("csel", 0xCD6380UL);
                x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x0)))));
                x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x8))))) >> (int)(unchecked((int)(0x2UL)))))))));
                x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x28))));
                x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
                RuntimeMemory.WritePtr(sp, 0x0UL);
                x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = unchecked((ulong)(unchecked((uint)(x27))));
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x29 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                x8 = unchecked((ulong)((sp) + (0x400UL)));
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x420UL))));
                x2 = unchecked((ulong)((sp) + (0x370UL)));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x29))));
                x3 = 0x0UL;
                __arm64_pair_address_13460444 = unchecked((ulong)((sp) + (0x370UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460444, v0);
#else
                __WriteVector128(__arm64_pair_address_13460444, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460444) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460444) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x390UL))), x8);
                x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = unchecked((ulong)((sp) + (0x340UL)));
                x0 = unchecked((ulong)(unchecked((uint)(x27))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x360UL))));
                __arm64_pair_address_13460476 = unchecked((ulong)((sp) + (0x340UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13460476);
#else
                v0 = __ReadVector128(__arm64_pair_address_13460476);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13460476) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13460476) + (0x10UL))));
#endif
                x0 = unchecked((ulong)(unchecked((uint)(x28))));
                x1 = 0x0UL;
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x420UL))), x8);
                x8 = unchecked((ulong)((sp) + (0x340UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x400UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x400UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v1);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                __arm64_pair_address_13460508 = unchecked((ulong)((sp) + (0x340UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13460508);
#else
                v0 = __ReadVector128(__arm64_pair_address_13460508);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13460508) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13460508) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x360UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#else
                v2 = __ReadVector128(unchecked((ulong)((sp) + (0x400UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((sp) + (0x410UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x420UL))));
                x1 = unchecked((ulong)((sp) + (0x310UL)));
                x2 = unchecked((ulong)((sp) + (0x2E0UL)));
                x4 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                x0 = x19;
                x3 = x20;
                x5 = 0x0UL;
                __arm64_pair_address_13460552 = unchecked((ulong)((sp) + (0x2E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460552, v0);
#else
                __WriteVector128(__arm64_pair_address_13460552, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460552) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460552) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x300UL))), x8);
                __arm64_pair_address_13460560 = unchecked((ulong)((sp) + (0x310UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460560, v2);
#else
                __WriteVector128(__arm64_pair_address_13460560, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460560) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460560) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x330UL))), x9);
                x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x27))));
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = x26;
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x1CUL))))));
                x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                x29 = unchecked((ulong)(unchecked((uint)(x0))));
                x0 = x26;
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                x6 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x10UL))))));
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) + (unchecked((uint)(0x7UL)))))));
                __arm64_flags_left_13460636 = unchecked((uint)(x29));
                __arm64_flags_right_13460636 = unchecked((uint)0x0UL);
                x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(0x7UL)))))));
                RuntimeCalls.Unsupported("csel", 0xCD64A4UL);
                x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x29)))));
                __arm64_flags_left_13460648 = unchecked((uint)(x0));
                __arm64_flags_right_13460648 = unchecked((uint)0x0UL);
                x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x8))))) >> (int)(unchecked((int)(0x3UL)))))))));
                RuntimeCalls.Unsupported("csel", 0xCD64B0UL);
                x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x0)))));
                x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x8))))) >> (int)(unchecked((int)(0x3UL)))))))));
                x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x27))));
                x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
                RuntimeMemory.WritePtr(sp, 0x0UL);
                x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = unchecked((ulong)(unchecked((uint)(x28))));
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x29 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                x8 = unchecked((ulong)((sp) + (0x340UL)));
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                __arm64_pair_address_13460720 = unchecked((ulong)((sp) + (0x340UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13460720);
#else
                v0 = __ReadVector128(__arm64_pair_address_13460720);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13460720) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13460720) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x360UL))));
                x2 = unchecked((ulong)((sp) + (0x2B0UL)));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x29))));
                x3 = 0x0UL;
                __arm64_pair_address_13460744 = unchecked((ulong)((sp) + (0x2B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460744, v0);
#else
                __WriteVector128(__arm64_pair_address_13460744, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460744) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460744) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2D0UL))), x8);
                x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = unchecked((ulong)((sp) + (0x280UL)));
                x0 = unchecked((ulong)(unchecked((uint)(x28))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x2A0UL))));
                __arm64_pair_address_13460776 = unchecked((ulong)((sp) + (0x280UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13460776);
#else
                v0 = __ReadVector128(__arm64_pair_address_13460776);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13460776) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13460776) + (0x10UL))));
#endif
                x0 = unchecked((ulong)(unchecked((uint)(x27))));
                x1 = 0x0UL;
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x360UL))), x8);
                x8 = unchecked((ulong)((sp) + (0x280UL)));
                __arm64_pair_address_13460796 = unchecked((ulong)((sp) + (0x340UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460796, v0);
#else
                __WriteVector128(__arm64_pair_address_13460796, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460796) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460796) + (0x10UL))), v1);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                __arm64_pair_address_13460804 = unchecked((ulong)((sp) + (0x280UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13460804);
#else
                v0 = __ReadVector128(__arm64_pair_address_13460804);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13460804) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13460804) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x2A0UL))));
                __arm64_pair_address_13460812 = unchecked((ulong)((sp) + (0x340UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13460812);
#else
                v2 = __ReadVector128(__arm64_pair_address_13460812);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13460812) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13460812) + (0x10UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x360UL))));
                x1 = unchecked((ulong)((sp) + (0x250UL)));
                x2 = unchecked((ulong)((sp) + (0x220UL)));
                x4 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                x0 = x19;
                x3 = x20;
                x5 = 0x0UL;
                __arm64_pair_address_13460844 = unchecked((ulong)((sp) + (0x220UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460844, v0);
#else
                __WriteVector128(__arm64_pair_address_13460844, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460844) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460844) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x240UL))), x8);
                __arm64_pair_address_13460852 = unchecked((ulong)((sp) + (0x250UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13460852, v2);
#else
                __WriteVector128(__arm64_pair_address_13460852, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13460852) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13460852) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x270UL))), x9);
                x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x28))));
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x28 = 0x1BAB000UL;
                x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (0x32AUL))))))));
                if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x0 = 0x1A8C000UL;
                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
                    // Likely IL2CPP class initialization helper (guarded call).
                    x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                    x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x28) + (0x32AUL))), unchecked((byte)(unchecked((uint)(x8)))));
                }
                label_0xCD65B0:
                ;
                x8 = 0x1A8C000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
                x9 = RuntimeMemory.ReadU64(x23);
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x21))))))), 0));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3E000000UL)), 0)), 0));
                x8 = RuntimeMemory.ReadU64(x8);
                v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                x0 = x19;
                v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x8UL))))), 0));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
                x2 = 0x0UL;
                RuntimeCalls.Unsupported("fmul", 0xCD65F0UL);
                x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
                v1 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0xBFUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0xBFUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
                RuntimeCalls.Unsupported("fmul", 0xCD65FCUL);
                RuntimeCalls.Unsupported("mov", 0xCD6600UL);
                x0 = RuntimeCalls.InvokeDirect(0x17A7438UL /* metadata target: CommandBuffer.SetGlobalVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                x10 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
                __arm64_fcvtz_source_13461008 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
                x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13461008 != __arm64_fcvtz_source_13461008) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13461008 >= global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x4F000000UL)), 0)) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13461008 < global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xCF000000UL)), 0)) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13461008)))))))));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x10))), 0)), 0));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x9))))))), 0));
                __arm64_float_flags_left_13461024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
                __arm64_float_flags_right_13461024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                x0 = x19;
                x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x24UL))))));
                x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFCF000000UL))));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
                RuntimeCalls.Unsupported("fcsel", 0xCD6634UL);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = x26;
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x28 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x28UL))))));
                x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                x29 = unchecked((ulong)(unchecked((uint)(x0))));
                x0 = x26;
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                x6 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x10UL))))));
                x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x29))))) / (unchecked((int)(unchecked((uint)(x21)))))))))));
                x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x0))))) / (unchecked((int)(unchecked((uint)(x21)))))))))));
                x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x28))));
                x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
                RuntimeMemory.WritePtr(sp, 0x0UL);
                x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = unchecked((ulong)(unchecked((uint)(x27))));
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x29 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                x8 = unchecked((ulong)((sp) + (0x280UL)));
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                __arm64_pair_address_13461164 = unchecked((ulong)((sp) + (0x280UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461164);
#else
                v0 = __ReadVector128(__arm64_pair_address_13461164);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461164) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461164) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x2A0UL))));
                x2 = unchecked((ulong)((sp) + (0x1F0UL)));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x29))));
                x3 = 0x0UL;
                __arm64_pair_address_13461188 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461188, v0);
#else
                __WriteVector128(__arm64_pair_address_13461188, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461188) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461188) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x210UL))), x8);
                x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = unchecked((ulong)((sp) + (0x1C0UL)));
                x0 = unchecked((ulong)(unchecked((uint)(x27))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1E0UL))));
                __arm64_pair_address_13461220 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461220);
#else
                v0 = __ReadVector128(__arm64_pair_address_13461220);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461220) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461220) + (0x10UL))));
#endif
                x0 = unchecked((ulong)(unchecked((uint)(x28))));
                x1 = 0x0UL;
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2A0UL))), x8);
                x8 = unchecked((ulong)((sp) + (0x1C0UL)));
                __arm64_pair_address_13461240 = unchecked((ulong)((sp) + (0x280UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461240, v0);
#else
                __WriteVector128(__arm64_pair_address_13461240, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461240) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461240) + (0x10UL))), v1);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                __arm64_pair_address_13461248 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461248);
#else
                v0 = __ReadVector128(__arm64_pair_address_13461248);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461248) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461248) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1E0UL))));
                __arm64_pair_address_13461256 = unchecked((ulong)((sp) + (0x280UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461256);
#else
                v2 = __ReadVector128(__arm64_pair_address_13461256);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461256) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461256) + (0x10UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x2A0UL))));
                x1 = unchecked((ulong)((sp) + (0x190UL)));
                x2 = unchecked((ulong)((sp) + (0x160UL)));
                x4 = unchecked((ulong)(unchecked((uint)(0x3UL))));
                x0 = x19;
                x3 = x20;
                x5 = 0x0UL;
                __arm64_pair_address_13461288 = unchecked((ulong)((sp) + (0x160UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461288, v0);
#else
                __WriteVector128(__arm64_pair_address_13461288, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461288) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461288) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x180UL))), x8);
                __arm64_pair_address_13461296 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461296, v2);
#else
                __WriteVector128(__arm64_pair_address_13461296, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461296) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461296) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1B0UL))), x9);
                x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x27))));
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = x26;
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x2CUL))))));
                x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                x29 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x0))))) / (unchecked((int)(unchecked((uint)(x21)))))))))));
                x0 = x26;
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                x6 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x10UL))))));
                x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x0))))) / (unchecked((int)(unchecked((uint)(x21)))))))))));
                x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x27))));
                x2 = unchecked((ulong)(unchecked((uint)(x29))));
                x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
                RuntimeMemory.WritePtr(sp, 0x0UL);
                x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                x8 = RuntimeMemory.ReadU64(x23);
                x0 = unchecked((ulong)(unchecked((uint)(x28))));
                x1 = 0x0UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x25 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                x8 = unchecked((ulong)((sp) + (0x1C0UL)));
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                __arm64_pair_address_13461432 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461432);
#else
                v0 = __ReadVector128(__arm64_pair_address_13461432);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461432) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461432) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1E0UL))));
                x2 = unchecked((ulong)((sp) + (0x130UL)));
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x25))));
                x3 = 0x0UL;
                __arm64_pair_address_13461456 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461456, v0);
#else
                __WriteVector128(__arm64_pair_address_13461456, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461456) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461456) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x150UL))), x8);
                x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = unchecked((ulong)((sp) + (0x108UL)));
                x0 = unchecked((ulong)(unchecked((uint)(x28))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                x21 = unchecked((ulong)((sp) + (0x108UL)));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x128UL))));
                __arm64_pair_address_13461492 = x21;
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461492);
#else
                v0 = __ReadVector128(__arm64_pair_address_13461492);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461492) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461492) + (0x10UL))));
#endif
                x0 = unchecked((ulong)(unchecked((uint)(x27))));
                x1 = 0x0UL;
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1E0UL))), x8);
                x8 = unchecked((ulong)((sp) + (0x108UL)));
                __arm64_pair_address_13461512 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461512, v0);
#else
                __WriteVector128(__arm64_pair_address_13461512, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461512) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461512) + (0x10UL))), v1);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                __arm64_pair_address_13461520 = x21;
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461520);
#else
                v0 = __ReadVector128(__arm64_pair_address_13461520);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461520) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461520) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x128UL))));
                __arm64_pair_address_13461528 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461528);
#else
                v2 = __ReadVector128(__arm64_pair_address_13461528);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461528) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461528) + (0x10UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1E0UL))));
                x1 = unchecked((ulong)((sp) + (0xE0UL)));
                x2 = unchecked((ulong)((sp) + (0xB0UL)));
                x4 = unchecked((ulong)(unchecked((uint)(0x4UL))));
                x0 = x19;
                x3 = x20;
                x5 = 0x0UL;
                __arm64_pair_address_13461560 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461560, v0);
#else
                __WriteVector128(__arm64_pair_address_13461560, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461560) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461560) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xD0UL))), x8);
                __arm64_pair_address_13461568 = unchecked((ulong)((sp) + (0xE0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461568, v2);
#else
                __WriteVector128(__arm64_pair_address_13461568, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461568) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461568) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x100UL))), x9);
                x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x28))));
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
                x8 = RuntimeMemory.ReadU64(x23);
                x10 = unchecked((ulong)(unchecked((uint)(0x40UL))));
                x0 = x19;
                x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x4UL))))));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x2 = 0x0UL;
                __arm64_flags_left_13461624 = unchecked((uint)(x9));
                __arm64_flags_right_13461624 = unchecked((uint)0x0UL);
                x9 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13461624) - (__arm64_flags_right_13461624))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13461624)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13461624)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13461624) - (__arm64_flags_right_13461624))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13461624)) < unchecked((int)0x0UL))))) ? unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x9)))));
                x9 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) >> (int)(unchecked((int)(0x1UL)))))))));
                __arm64_flags_left_13461636 = unchecked((uint)(x9));
                __arm64_flags_right_13461636 = unchecked((uint)0x40UL);
                x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x30UL))))));
                RuntimeCalls.Unsupported("csel", 0xCD688CUL);
                x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x10)))));
                __arm64_flags_left_13461648 = unchecked((uint)(x8));
                __arm64_flags_right_13461648 = unchecked((uint)0x1UL);
                x8 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_13461648) - (__arm64_flags_right_13461648))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13461648) - (__arm64_flags_right_13461648))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13461648)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13461648)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13461648) - (__arm64_flags_right_13461648))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13461648)) < unchecked((int)0x0UL)))))) ? unchecked((uint)(x8)) : unchecked((uint)((unchecked((uint)0x0UL)) + (unchecked((uint)0x1UL)))))));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
                x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(x23);
                __arm64_pair_address_13461668 = x22;
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461668);
#else
                v0 = __ReadVector128(__arm64_pair_address_13461668);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461668) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461668) + (0x10UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
                x2 = unchecked((ulong)((sp) + (0x80UL)));
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                x0 = x19;
                x3 = 0x0UL;
                x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                __arm64_pair_address_13461696 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461696, v0);
#else
                __WriteVector128(__arm64_pair_address_13461696, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461696) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461696) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), x9);
                x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
                __arm64_pair_address_13461712 = x22;
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461712);
#else
                v1 = __ReadVector128(__arm64_pair_address_13461712);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461712) + (0x10UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461712) + (0x10UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x4C8UL))));
                x1 = unchecked((ulong)((sp) + (0x50UL)));
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x70UL))), x8);
                __arm64_pair_address_13461728 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461728, v1);
#else
                __WriteVector128(__arm64_pair_address_13461728, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461728) + (0x10UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461728) + (0x10UL))), v0);
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
                __arm64_pair_address_13461736 = x9;
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13461736);
#else
                v1 = __ReadVector128(__arm64_pair_address_13461736);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13461736) + (0x10UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13461736) + (0x10UL))));
#endif
                x2 = unchecked((ulong)((sp) + (0x20UL)));
                x4 = unchecked((ulong)(unchecked((uint)(0x5UL))));
                x0 = x19;
                x3 = x20;
                x5 = 0x0UL;
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x8);
                __arm64_pair_address_13461764 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13461764, v1);
#else
                __WriteVector128(__arm64_pair_address_13461764, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461764) + (0x10UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461764) + (0x10UL))), v0);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x24))));
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x0 = x19;
                x1 = unchecked((ulong)(unchecked((uint)(x27))));
                x2 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                sp = unchecked((ulong)((sp) + (0x4C0UL)));
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
                x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
                x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
                x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
                x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
                x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
                x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
                x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
                __arm64_load_address_13461832 = sp;
                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13461832)), 0));
                sp = unchecked((ulong)((__arm64_load_address_13461832) + (0x70UL)));
                return x0;
            }
        }
        label_0xCD6950:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `MotionBlurComponent.ReconstructionFilter.CheckTextureFormatSupport` — RVA `0xcd748c`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `private void CheckTextureFormatSupport() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint MotionBlurComponent_ReconstructionFilter_CheckTextureFormatSupport_RVAcd748c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x14UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x14UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        }
        label_0xCD74A8:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```
