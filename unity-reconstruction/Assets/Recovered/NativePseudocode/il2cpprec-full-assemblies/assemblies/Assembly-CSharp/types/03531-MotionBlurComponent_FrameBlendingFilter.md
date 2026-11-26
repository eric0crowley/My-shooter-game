# `MotionBlurComponent.FrameBlendingFilter` — TypeDefIndex 3531

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `bool` | `m_UseCompression` |
| `0x14` | `RenderTextureFormat` | `m_RawTextureFormat` |
| `0x18` | `MotionBlurComponent.FrameBlendingFilter.Frame[]` | `m_FrameList` |
| `0x20` | `int` | `m_LastFrameCount` |

## `MotionBlurComponent.FrameBlendingFilter.ctor` — RVA `0xcd5778`

- Lift status: **exact**; input span: 120 bytes; span to next metadata RVA: 120 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_ctor_RVAcd5778(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5E8UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x1C8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD57AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5E8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD57AC;
        label_0xCD57AC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xCD74B0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.CheckSupportCompression */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0xCD74E4UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.GetPreferredRenderTextureFormat */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x14UL))), unchecked((uint)(x0)));
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x0);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.Dispose` — RVA `0xcd591c`

- Lift status: **partial**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public void Dispose() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=12 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xcd5950; reason: Unsupported instruction 'b.hs' at 0xcd5954; reason: Unknown IR expression at 0xcd5954; reason: Unsupported instruction 'cmp' at 0xcd5970; reason: Unsupported instruction 'b.lt' at 0xcd5974; reason: Unknown IR expression at 0xcd5974

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_Dispose_RVAcd591c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13457724 = default(uint);
        uint __arm64_flags_right_13457724 = default(uint);
        ulong __arm64_pair_address_13457708 = default(ulong);
        ulong __arm64_pair_address_13457752 = default(ulong);
        ulong __arm64_pair_address_13457760 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x40UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13457708 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13457708, v0);
#else
        __WriteVector128(__arm64_pair_address_13457708, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13457708) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13457708) + (0x10UL))), v0);
#endif
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xCD598C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        __arm64_flags_left_13457724 = unchecked((uint)(x8));
        __arm64_flags_right_13457724 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13457724) - (__arm64_flags_right_13457724))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13457724)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13457724)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13457724) - (__arm64_flags_right_13457724))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13457724)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCD5978;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x21 = unchecked((ulong)((x19) + (0x20UL)));
        goto label_0xCD5950;
        label_0xCD5950:
        ;
        RuntimeCalls.Unsupported("cmp", 0xCD5950UL);
        RuntimeCalls.Unsupported("b.hs", 0xCD5954UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD5988;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5958UL);
        }
        __arm64_pair_address_13457752 = x21;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13457752);
#else
        v1 = __ReadVector128(__arm64_pair_address_13457752);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13457752) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13457752) + (0x10UL))));
#endif
        x21 = unchecked((ulong)((__arm64_pair_address_13457752) + (0x20UL)));
        x0 = sp;
        __arm64_pair_address_13457760 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13457760, v1);
#else
        __WriteVector128(__arm64_pair_address_13457760, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13457760) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13457760) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xCD75B0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.Release */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xCD5970UL);
        RuntimeCalls.Unsupported("b.lt", 0xCD5974UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD5950;
        }
        else
        {
            goto label_0xCD5978;
        }
        label_0xCD5978:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return x0;
        label_0xCD5988:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCD598C;
        label_0xCD598C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.BlendFrames` — RVA `0xcd6954`

- Lift status: **exact**; input span: 1252 bytes; span to next metadata RVA: 1252 bytes.
- Metadata signature: `public void BlendFrames(CommandBuffer cb, float strength, RenderTargetIdentifier source, RenderTargetIdentifier destination, Material material) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=188 (informational only).

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_BlendFrames_RVAcd6954(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13461844 = default(ulong);
        ulong __arm64_pair_address_13461980 = default(ulong);
        ulong __arm64_pair_address_13461984 = default(ulong);
        ulong __arm64_pair_address_13461992 = default(ulong);
        ulong __arm64_pair_address_13461996 = default(ulong);
        ulong __arm64_pair_address_13462000 = default(ulong);
        ulong __arm64_pair_address_13462004 = default(ulong);
        ulong __arm64_pair_address_13462008 = default(ulong);
        ulong __arm64_pair_address_13462012 = default(ulong);
        ulong __arm64_pair_address_13462132 = default(ulong);
        ulong __arm64_pair_address_13462140 = default(ulong);
        ulong __arm64_pair_address_13462152 = default(ulong);
        ulong __arm64_pair_address_13462176 = default(ulong);
        ulong __arm64_pair_address_13462216 = default(ulong);
        ulong __arm64_pair_address_13462240 = default(ulong);
        ulong __arm64_pair_address_13462280 = default(ulong);
        ulong __arm64_pair_address_13462304 = default(ulong);
        ulong __arm64_pair_address_13462344 = default(ulong);
        ulong __arm64_pair_address_13462368 = default(ulong);
        ulong __arm64_pair_address_13462408 = default(ulong);
        ulong __arm64_pair_address_13462432 = default(ulong);
        ulong __arm64_pair_address_13462472 = default(ulong);
        ulong __arm64_pair_address_13462496 = default(ulong);
        ulong __arm64_pair_address_13462536 = default(ulong);
        ulong __arm64_pair_address_13462560 = default(ulong);
        ulong __arm64_pair_address_13462600 = default(ulong);
        ulong __arm64_pair_address_13462624 = default(ulong);
        ulong __arm64_pair_address_13462816 = default(ulong);
        ulong __arm64_pair_address_13462844 = default(ulong);
        ulong __arm64_pair_address_13462860 = default(ulong);
        ulong __arm64_pair_address_13462868 = default(ulong);
        ulong __arm64_pair_address_13462876 = default(ulong);
        ulong __arm64_pair_address_13462884 = default(ulong);
        ulong __arm64_pair_address_13462896 = default(ulong);
        ulong __arm64_pair_address_13462904 = default(ulong);
        ulong __arm64_pair_address_13462924 = default(ulong);
        ulong __arm64_pair_address_13462932 = default(ulong);
        ulong __arm64_pair_address_13462944 = default(ulong);
        ulong __arm64_pair_address_13462952 = default(ulong);
        ulong __arm64_pair_address_13462968 = default(ulong);
        ulong __arm64_pair_address_13462976 = default(ulong);
        ulong __arm64_pair_address_13462988 = default(ulong);
        ulong __arm64_pair_address_13462996 = default(ulong);
        ulong __arm64_pair_address_13463028 = default(ulong);
        ulong __arm64_pair_address_13463036 = default(ulong);
        ulong __arm64_pair_address_13463040 = default(ulong);
        ulong __arm64_pair_address_13463048 = default(ulong);
        ulong __arm64_pair_address_13463084 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13461844 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13461844, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13461844) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13461844;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x440UL)));
        x24 = 0x1BAB000UL;
        x25 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x5E9UL))))))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x1E0UL))));
        x19 = x4;
        x21 = x3;
        x23 = x2;
        v8 = v0;
        x20 = x1;
        x22 = x0;
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
            RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x5E9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD69B0:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x3B0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x380UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x350UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x320UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x2F0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x2C0UL))), 0x0UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v0);
#endif
        __arm64_pair_address_13461980 = unchecked((ulong)((sp) + (0x3F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13461980, v0);
#else
        __WriteVector128(__arm64_pair_address_13461980, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461980) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461980) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13461984 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13461984, v0);
#else
        __WriteVector128(__arm64_pair_address_13461984, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461984) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461984) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x3C0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x3C0UL))), v0);
#endif
        __arm64_pair_address_13461992 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13461992, v0);
#else
        __WriteVector128(__arm64_pair_address_13461992, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461992) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461992) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13461996 = unchecked((ulong)((sp) + (0x360UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13461996, v0);
#else
        __WriteVector128(__arm64_pair_address_13461996, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13461996) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13461996) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13462000 = unchecked((ulong)((sp) + (0x330UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13462000, v0);
#else
        __WriteVector128(__arm64_pair_address_13462000, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462000) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462000) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13462004 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13462004, v0);
#else
        __WriteVector128(__arm64_pair_address_13462004, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462004) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462004) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13462008 = unchecked((ulong)((sp) + (0x2D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13462008, v0);
#else
        __WriteVector128(__arm64_pair_address_13462008, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462008) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462008) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13462012 = unchecked((ulong)((sp) + (0x2A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13462012, v0);
#else
        __WriteVector128(__arm64_pair_address_13462012, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462012) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462012) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        x0 = x22;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xCD7AE0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.GetFrameRelative */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFEUL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD7AE0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.GetFrameRelative */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFDUL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD7AE0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.GetFrameRelative */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFCUL))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD7AE0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.GetFrameRelative */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x0 = RuntimeMemory.ReadU64(x25);
        }
        label_0xCD6A5C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x420UL))));
        x1 = 0x0UL;
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x38UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
        __arm64_pair_address_13462132 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462132);
#else
        v0 = __ReadVector128(__arm64_pair_address_13462132);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462132) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462132) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
        __arm64_pair_address_13462140 = unchecked((ulong)((sp) + (0x270UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13462140, v0);
#else
        __WriteVector128(__arm64_pair_address_13462140, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462140) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462140) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x290UL))), x8);
        if ((x20 == 0x0UL))
        {
            label_0xCD6E34:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            __arm64_pair_address_13462152 = unchecked((ulong)((sp) + (0x270UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462152);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462152);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462152) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462152) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x290UL))));
            x2 = unchecked((ulong)((sp) + (0x210UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462176 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462176, v0);
#else
            __WriteVector128(__arm64_pair_address_13462176, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462176) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462176) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x230UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x400UL))));
            x1 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x3CUL))))));
            x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
            __arm64_pair_address_13462216 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462216);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462216);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462216) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462216) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
            x2 = unchecked((ulong)((sp) + (0x1E0UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462240 = unchecked((ulong)((sp) + (0x1E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462240, v0);
#else
            __WriteVector128(__arm64_pair_address_13462240, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462240) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462240) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x200UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3E0UL))));
            x1 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x40UL))))));
            x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
            __arm64_pair_address_13462280 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462280);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462280);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462280) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462280) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
            x2 = unchecked((ulong)((sp) + (0x1B0UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462304 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462304, v0);
#else
            __WriteVector128(__arm64_pair_address_13462304, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462304) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462304) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1D0UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
            x1 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x44UL))))));
            x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
            __arm64_pair_address_13462344 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462344);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462344);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462344) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462344) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
            x2 = unchecked((ulong)((sp) + (0x180UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462368 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462368, v0);
#else
            __WriteVector128(__arm64_pair_address_13462368, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462368) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462368) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1A0UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x428UL))));
            x1 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x48UL))))));
            x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
            __arm64_pair_address_13462408 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462408);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462408);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462408) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462408) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
            x2 = unchecked((ulong)((sp) + (0x150UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462432 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462432, v0);
#else
            __WriteVector128(__arm64_pair_address_13462432, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462432) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462432) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x170UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x408UL))));
            x1 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4CUL))))));
            x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
            __arm64_pair_address_13462472 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462472);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462472);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462472) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462472) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
            x2 = unchecked((ulong)((sp) + (0x120UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462496 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462496, v0);
#else
            __WriteVector128(__arm64_pair_address_13462496, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462496) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462496) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x140UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3E8UL))));
            x1 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x50UL))))));
            x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
            __arm64_pair_address_13462536 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462536);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462536);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462536) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462536) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
            x2 = unchecked((ulong)((sp) + (0xF0UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462560 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462560, v0);
#else
            __WriteVector128(__arm64_pair_address_13462560, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462560) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462560) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x110UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C8UL))));
            x1 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x54UL))))));
            x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
            __arm64_pair_address_13462600 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462600);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462600);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462600) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462600) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
            x2 = unchecked((ulong)((sp) + (0xC0UL)));
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x3 = 0x0UL;
            __arm64_pair_address_13462624 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462624, v0);
#else
            __WriteVector128(__arm64_pair_address_13462624, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462624) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462624) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xE0UL))), x8);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = unchecked((ulong)((sp) + (0x420UL)));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x58UL))))));
            x0 = RuntimeCalls.InvokeDirect(0xCD7B44UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.CalculateWeight */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x2 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = unchecked((ulong)((sp) + (0x400UL)));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x5CUL))))));
            x0 = RuntimeCalls.InvokeDirect(0xCD7B44UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.CalculateWeight */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x2 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = unchecked((ulong)((sp) + (0x3E0UL)));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x60UL))))));
            x0 = RuntimeCalls.InvokeDirect(0xCD7B44UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.CalculateWeight */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x2 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            x0 = unchecked((ulong)((sp) + (0x3C0UL)));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x64UL))))));
            x0 = RuntimeCalls.InvokeDirect(0xCD7B44UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.CalculateWeight */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x0 = x20;
            x1 = unchecked((ulong)(unchecked((uint)(x24))));
            x2 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(x25);
            __arm64_pair_address_13462816 = x23;
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462816);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462816);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462816) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462816) + (0x10UL))));
#endif
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x20UL))));
            x2 = unchecked((ulong)((sp) + (0x90UL)));
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x0 = x20;
            x3 = 0x0UL;
            x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
            __arm64_pair_address_13462844 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462844, v0);
#else
            __WriteVector128(__arm64_pair_address_13462844, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462844) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462844) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xB0UL))), x9);
            x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x20UL))));
            __arm64_pair_address_13462860 = x23;
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462860);
#else
            v1 = __ReadVector128(__arm64_pair_address_13462860);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462860) + (0x10UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462860) + (0x10UL))));
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x260UL))), x8);
            __arm64_pair_address_13462868 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462868, v1);
#else
            __WriteVector128(__arm64_pair_address_13462868, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462868) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462868) + (0x10UL))), v0);
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
            __arm64_pair_address_13462876 = x21;
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462876);
#else
            v1 = __ReadVector128(__arm64_pair_address_13462876);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462876) + (0x10UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462876) + (0x10UL))));
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x8);
            __arm64_pair_address_13462884 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13462884, v1);
#else
            __WriteVector128(__arm64_pair_address_13462884, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462884) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462884) + (0x10UL))), v0);
#endif
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10UL))))))));
            if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
            {
                label_0xCD6DA0:
                ;
                __arm64_pair_address_13462944 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462944);
#else
                v0 = __ReadVector128(__arm64_pair_address_13462944);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462944) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462944) + (0x10UL))));
#endif
                x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
                __arm64_pair_address_13462952 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462952);
#else
                v2 = __ReadVector128(__arm64_pair_address_13462952);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462952) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462952) + (0x10UL))));
#endif
                x11 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
                x8 = unchecked((ulong)((sp) + (0x300UL)));
                x9 = unchecked((ulong)((sp) + (0x330UL)));
                __arm64_pair_address_13462968 = unchecked((ulong)((sp) + (0x330UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13462968, v0);
#else
                __WriteVector128(__arm64_pair_address_13462968, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462968) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462968) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x350UL))), x10);
                __arm64_pair_address_13462976 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13462976, v2);
#else
                __WriteVector128(__arm64_pair_address_13462976, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462976) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462976) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x320UL))), x11);
            }
            else
            {
                __arm64_pair_address_13462896 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462896);
#else
                v0 = __ReadVector128(__arm64_pair_address_13462896);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462896) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462896) + (0x10UL))));
#endif
                x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
                __arm64_pair_address_13462904 = unchecked((ulong)((sp) + (0x240UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462904);
#else
                v2 = __ReadVector128(__arm64_pair_address_13462904);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462904) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462904) + (0x10UL))));
#endif
                x11 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x260UL))));
                x8 = unchecked((ulong)((sp) + (0x360UL)));
                x9 = unchecked((ulong)((sp) + (0x390UL)));
                __arm64_pair_address_13462924 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13462924, v0);
#else
                __WriteVector128(__arm64_pair_address_13462924, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462924) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462924) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3B0UL))), x10);
                __arm64_pair_address_13462932 = unchecked((ulong)((sp) + (0x360UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13462932, v2);
#else
                __WriteVector128(__arm64_pair_address_13462932, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13462932) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13462932) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x380UL))), x11);
            }
            label_0xCD6DCC:
            ;
            __arm64_pair_address_13462988 = x9;
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462988);
#else
            v0 = __ReadVector128(__arm64_pair_address_13462988);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462988) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462988) + (0x10UL))));
#endif
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
            __arm64_pair_address_13462996 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13462996);
#else
            v2 = __ReadVector128(__arm64_pair_address_13462996);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13462996) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13462996) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
            x1 = unchecked((ulong)((sp) + (0x30UL)));
            x2 = sp;
            x0 = x20;
            x3 = x19;
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2F0UL))), x9);
            __arm64_pair_address_13463028 = unchecked((ulong)((sp) + (0x2D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13463028, v0);
#else
            __WriteVector128(__arm64_pair_address_13463028, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463028) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463028) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2C0UL))), x8);
            __arm64_pair_address_13463036 = unchecked((ulong)((sp) + (0x2A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13463036, v2);
#else
            __WriteVector128(__arm64_pair_address_13463036, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463036) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463036) + (0x10UL))), v3);
#endif
            __arm64_pair_address_13463040 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13463040, v2);
#else
            __WriteVector128(__arm64_pair_address_13463040, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463040) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463040) + (0x10UL))), v3);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x8);
            __arm64_pair_address_13463048 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13463048, v0);
#else
            __WriteVector128(__arm64_pair_address_13463048, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463048) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463048) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x9);
            x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
            sp = unchecked((ulong)((sp) + (0x440UL)));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
            x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            __arm64_pair_address_13463084 = sp;
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13463084)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13463084) + (0x8UL))))), 0));
            return x0;
        }
        return default(ulong);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.PushFrame` — RVA `0xcd6e38`

- Lift status: **partial**; input span: 288 bytes; span to next metadata RVA: 288 bytes.
- Metadata signature: `public void PushFrame(CommandBuffer cb, RenderTargetIdentifier source, int width, int height, Material material) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=39 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.hs' at 0xcd6eac; reason: Unknown IR expression at 0xcd6eac; reason: Unsupported instruction 'b.hs' at 0xcd6efc; reason: Unknown IR expression at 0xcd6efc

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_PushFrame_RVAcd6e38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13463152 = default(uint);
        uint __arm64_flags_left_13463200 = default(uint);
        uint __arm64_flags_left_13463280 = default(uint);
        uint __arm64_flags_right_13463152 = default(uint);
        uint __arm64_flags_right_13463200 = default(uint);
        uint __arm64_flags_right_13463280 = default(uint);
        ulong __arm64_pair_address_13463196 = default(ulong);
        ulong __arm64_pair_address_13463208 = default(ulong);
        ulong __arm64_pair_address_13463216 = default(ulong);
        ulong __arm64_pair_address_13463256 = default(ulong);
        ulong __arm64_pair_address_13463276 = default(ulong);
        ulong __arm64_pair_address_13463288 = default(ulong);
        ulong __arm64_pair_address_13463300 = default(ulong);
        ulong __arm64_pair_address_13463336 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = 0x0UL;
        x24 = x5;
        x20 = unchecked((ulong)(unchecked((uint)(x4))));
        x22 = unchecked((ulong)(unchecked((uint)(x3))));
        x25 = x2;
        x23 = x1;
        x0 = RuntimeCalls.InvokeDirect(0x179AEB8UL /* metadata target: Time.get_frameCount */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        __arm64_flags_left_13463152 = unchecked((uint)(x0));
        __arm64_flags_right_13463152 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_13463152) - (__arm64_flags_right_13463152))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD6F38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6F50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x10UL))))))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x0))))) / (unchecked((int)(unchecked((uint)(x10)))))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)((unchecked((uint)(x9))) * (unchecked((uint)(x10))))))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD6EE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x20UL))));
        __arm64_pair_address_13463196 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13463196);
#else
        v1 = __ReadVector128(__arm64_pair_address_13463196);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13463196) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13463196) + (0x10UL))));
#endif
        __arm64_flags_left_13463200 = unchecked((uint)(x9));
        __arm64_flags_right_13463200 = unchecked((uint)(x10));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x11);
        __arm64_pair_address_13463208 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13463208, v1);
#else
        __WriteVector128(__arm64_pair_address_13463208, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463208) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463208) + (0x10UL))), v0);
#endif
        RuntimeCalls.Unsupported("b.hs", 0xCD6EACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD6F54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD6EB0UL);
        }
        __arm64_pair_address_13463216 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13463216);
#else
        v0 = __ReadVector128(__arm64_pair_address_13463216);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13463216) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13463216) + (0x10UL))));
#endif
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x9 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x9))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x5UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x2 = unchecked((ulong)((sp) + (0x30UL)));
        x1 = x23;
        x3 = unchecked((ulong)(unchecked((uint)(x22))));
        x4 = unchecked((ulong)(unchecked((uint)(x20))));
        x5 = x24;
        __arm64_pair_address_13463256 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13463256, v0);
#else
        __WriteVector128(__arm64_pair_address_13463256, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463256) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463256) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x10);
        x0 = RuntimeCalls.InvokeDirect(0xCD7680UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.MakeRecord */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD6F34;
        label_0xCD6EE8:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x20UL))));
        __arm64_pair_address_13463276 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13463276);
#else
        v1 = __ReadVector128(__arm64_pair_address_13463276);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13463276) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13463276) + (0x10UL))));
#endif
        __arm64_flags_left_13463280 = unchecked((uint)(x9));
        __arm64_flags_right_13463280 = unchecked((uint)(x10));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x11);
        __arm64_pair_address_13463288 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13463288, v1);
#else
        __WriteVector128(__arm64_pair_address_13463288, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463288) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463288) + (0x10UL))), v0);
#endif
        RuntimeCalls.Unsupported("b.hs", 0xCD6EFCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD6F54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x5 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x14UL))))));
        __arm64_pair_address_13463300 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13463300);
#else
        v0 = __ReadVector128(__arm64_pair_address_13463300);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13463300) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13463300) + (0x10UL))));
#endif
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x9 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x9))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x5UL))))))))))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x2 = sp;
        x1 = x23;
        x3 = unchecked((ulong)(unchecked((uint)(x22))));
        x4 = unchecked((ulong)(unchecked((uint)(x20))));
        __arm64_pair_address_13463336 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13463336, v0);
#else
        __WriteVector128(__arm64_pair_address_13463336, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13463336) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13463336) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x10);
        x0 = RuntimeCalls.InvokeDirect(0xCD7970UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.MakeRecordRaw */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD6F34;
        label_0xCD6F34:
        ;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x20UL))), unchecked((uint)(x21)));
        goto label_0xCD6F38;
        label_0xCD6F38:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0xD0UL)));
        return x0;
        label_0xCD6F50:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD6F54;
        label_0xCD6F54:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.CheckSupportCompression` — RVA `0xcd74b0`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `private static bool CheckSupportCompression() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint MotionBlurComponent_FrameBlendingFilter_CheckSupportCompression_RVAcd74b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13464780 = default(uint);
        uint __arm64_flags_right_13464780 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xCD74D8:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        else
        {
            x0 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179A8BCUL /* metadata target: SystemInfo.get_supportedRenderTargetCount */, x0, x1, x2, x3);
            __arm64_flags_left_13464780 = unchecked((uint)(x0));
            __arm64_flags_right_13464780 = unchecked((uint)0x1UL);
            x0 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_13464780) - (__arm64_flags_right_13464780))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13464780) - (__arm64_flags_right_13464780))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13464780)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13464780)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13464780) - (__arm64_flags_right_13464780))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13464780)) < unchecked((int)0x0UL)))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        label_0xCD74DC:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.GetPreferredRenderTextureFormat` — RVA `0xcd74e4`

- Lift status: **partial**; input span: 204 bytes; span to next metadata RVA: 204 bytes.
- Metadata signature: `private static RenderTextureFormat GetPreferredRenderTextureFormat() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=30 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xcd7564; reason: Unsupported instruction 'b.hs' at 0xcd7568; reason: Unknown IR expression at 0xcd7568; reason: Unsupported instruction 'cmp' at 0xcd7588; reason: Unsupported instruction 'b.lt' at 0xcd758c; reason: Unknown IR expression at 0xcd758c

```csharp
public static uint MotionBlurComponent_FrameBlendingFilter_GetPreferredRenderTextureFormat_RVAcd74e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13464912 = default(uint);
        uint __arm64_flags_right_13464912 = default(uint);
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8F000UL;
        x19 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5EAUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x2B8UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x2C0UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD752C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5EAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD752C;
        label_0xCD752C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = RuntimeMemory.ReadU64(x19);
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x148E41CUL /* metadata target: RuntimeHelpers.InitializeArray */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCD75AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        __arm64_flags_left_13464912 = unchecked((uint)(x8));
        __arm64_flags_right_13464912 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13464912) - (__arm64_flags_right_13464912))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13464912)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13464912)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13464912) - (__arm64_flags_right_13464912))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13464912)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCD7590;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x22 = unchecked((ulong)((x19) + (0x20UL)));
        goto label_0xCD7564;
        label_0xCD7564:
        ;
        RuntimeCalls.Unsupported("cmp", 0xCD7564UL);
        RuntimeCalls.Unsupported("b.hs", 0xCD7568UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD75A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (x21))))));
        x1 = 0x0UL;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x179A984UL /* metadata target: SystemInfo.SupportsRenderTextureFormat */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7594;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xCD7588UL);
        RuntimeCalls.Unsupported("b.lt", 0xCD758CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD7564;
        }
        else
        {
            goto label_0xCD7590;
        }
        label_0xCD7590:
        ;
        x20 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        goto label_0xCD7594;
        label_0xCD7594:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCD75A8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xCD75AC;
        label_0xCD75AC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.GetFrameRelative` — RVA `0xcd7ae0`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `private MotionBlurComponent.FrameBlendingFilter.Frame GetFrameRelative(int offset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_GetFrameRelative_RVAcd7ae0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13466392 = default(uint);
        uint __arm64_flags_right_13466392 = default(uint);
        ulong __arm64_pair_address_13466408 = default(ulong);
        ulong __arm64_pair_address_13466412 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
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
        x21 = x0;
        x0 = 0x0UL;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x179AEB8UL /* metadata target: Time.get_frameCount */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            label_0xCD7B3C:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
            x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(x20)))))));
            x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x10)))))));
            x11 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) / (unchecked((int)(unchecked((uint)(x10)))))))))));
            x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)((unchecked((uint)(x11))) * (unchecked((uint)(x10))))))))));
            __arm64_flags_left_13466392 = unchecked((uint)(x9));
            __arm64_flags_right_13466392 = unchecked((uint)(x10));
            if ((__arm64_flags_left_13466392 >= __arm64_flags_right_13466392))
            {
            }
            else
            {
                x9 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x9))))));
                x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x5UL))))))))))));
                __arm64_pair_address_13466408 = unchecked((ulong)((x8) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13466408);
#else
                v1 = __ReadVector128(__arm64_pair_address_13466408);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13466408) + (0x10UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13466408) + (0x10UL))));
#endif
                __arm64_pair_address_13466412 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13466412, v1);
#else
                __WriteVector128(__arm64_pair_address_13466412, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13466412) + (0x10UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13466412) + (0x10UL))), v0);
#endif
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
                x30 = RuntimeMemory.ReadU64(sp);
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
                return x0;
            }
        }
        label_0xCD7B40:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```
