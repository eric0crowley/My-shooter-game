# `MotionBlurComponent.FrameBlendingFilter.Frame` — TypeDefIndex 3530

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x0` | `RenderTexture` | `lumaTexture` |
| `0x8` | `RenderTexture` | `chromaTexture` |
| `0x10` | `float` | `m_Time` |
| `0x18` | `RenderTargetIdentifier[]` | `m_MRT` |

## `MotionBlurComponent.FrameBlendingFilter.Frame.Release` — RVA `0xcd75b0`

- Lift status: **exact**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `public void Release() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=32 (informational only).

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_Frame_Release_RVAcd75b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5EDUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD75E8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5EDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD75E8;
        label_0xCD75E8:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(x19);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD75FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD75F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD75FC;
        label_0xCD75FC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD761C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, x3);
        goto label_0xCD761C;
        label_0xCD761C:
        ;
        x20 = x19;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x8UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7634;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7630UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD7634;
        label_0xCD7634:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD7654;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, x3);
        goto label_0xCD7654;
        label_0xCD7654:
        ;
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x19, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x8UL))), 0x0UL);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.Frame.MakeRecord` — RVA `0xcd7680`

- Lift status: **exact**; input span: 752 bytes; span to next metadata RVA: 752 bytes.
- Metadata signature: `public void MakeRecord(CommandBuffer cb, RenderTargetIdentifier source, int width, int height, Material material) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=108 (informational only).

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_Frame_MakeRecord_RVAcd7680(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13465636 = default(uint);
        uint __arm64_flags_right_13465636 = default(uint);
        ulong __arm64_pair_address_13465516 = default(ulong);
        ulong __arm64_pair_address_13465524 = default(ulong);
        ulong __arm64_pair_address_13465536 = default(ulong);
        ulong __arm64_pair_address_13465544 = default(ulong);
        ulong __arm64_pair_address_13465564 = default(ulong);
        ulong __arm64_pair_address_13465576 = default(ulong);
        ulong __arm64_pair_address_13465596 = default(ulong);
        ulong __arm64_pair_address_13465604 = default(ulong);
        ulong __arm64_pair_address_13465616 = default(ulong);
        ulong __arm64_pair_address_13465624 = default(ulong);
        ulong __arm64_pair_address_13465648 = default(ulong);
        ulong __arm64_pair_address_13465700 = default(ulong);
        ulong __arm64_pair_address_13465712 = default(ulong);
        ulong __arm64_pair_address_13465720 = default(ulong);
        ulong __arm64_pair_address_13465740 = default(ulong);
        ulong __arm64_pair_address_13465800 = default(ulong);
        ulong __arm64_pair_address_13465900 = default(ulong);
        ulong __arm64_pair_address_13465904 = default(ulong);
        ulong __arm64_pair_address_13465908 = default(ulong);
        ulong __arm64_pair_address_13465912 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
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
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x1B0UL)));
        x25 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x5EEUL))))))));
        x20 = x5;
        x23 = unchecked((ulong)(unchecked((uint)(x4))));
        x24 = unchecked((ulong)(unchecked((uint)(x3))));
        x22 = x2;
        x21 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD76DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x5EEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD76DC;
        label_0xCD76DC:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCD75B0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.Release */, x0, x1, x2, x3);
        x3 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1783E4CUL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        RuntimeMemory.WriteU64(x19, unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x3 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1783E4CUL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0x8UL))), x1);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x19);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD7968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177E294UL /* metadata target: Texture.set_filterMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x23);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD7968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177E294UL /* metadata target: Texture.set_filterMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x24 = x19;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x18UL))));
        if ((x25 != 0x0UL))
        {
            goto label_0xCD779C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCC0UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = x0;
        RuntimeMemory.WriteU64(x24, x0);
        x0 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x25 = RuntimeMemory.ReadU64(x24);
        goto label_0xCD779C;
        label_0xCD779C:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13465516 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465516);
#else
        v0 = __ReadVector128(__arm64_pair_address_13465516);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465516) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465516) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x170UL))));
        __arm64_pair_address_13465524 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465524, v0);
#else
        __WriteVector128(__arm64_pair_address_13465524, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465524) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465524) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1A0UL))), x8);
        if ((x25 == 0x0UL))
        {
            goto label_0xCD7968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD77C0UL);
        }
        __arm64_pair_address_13465536 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465536);
#else
        v0 = __ReadVector128(__arm64_pair_address_13465536);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465536) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465536) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1A0UL))));
        __arm64_pair_address_13465544 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465544, v0);
#else
        __WriteVector128(__arm64_pair_address_13465544, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465544) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465544) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x140UL))), x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD796C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x140UL))));
        __arm64_pair_address_13465564 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465564);
#else
        v1 = __ReadVector128(__arm64_pair_address_13465564);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465564) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465564) + (0x10UL))));
#endif
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x25) + (0x40UL))), x8);
        __arm64_pair_address_13465576 = unchecked((ulong)((x25) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465576, v1);
#else
        __WriteVector128(__arm64_pair_address_13465576, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465576) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465576) + (0x10UL))), v0);
#endif
        x0 = RuntimeMemory.ReadU64(x23);
        x24 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13465596 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465596);
#else
        v0 = __ReadVector128(__arm64_pair_address_13465596);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465596) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465596) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
        __arm64_pair_address_13465604 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465604, v0);
#else
        __WriteVector128(__arm64_pair_address_13465604, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465604) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465604) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x170UL))), x8);
        if ((x24 == 0x0UL))
        {
            goto label_0xCD7968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7810UL);
        }
        __arm64_pair_address_13465616 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465616);
#else
        v0 = __ReadVector128(__arm64_pair_address_13465616);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465616) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465616) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x170UL))));
        __arm64_pair_address_13465624 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465624, v0);
#else
        __WriteVector128(__arm64_pair_address_13465624, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465624) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465624) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xE0UL))), x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x24) + (0x18UL))))));
        __arm64_flags_left_13465636 = unchecked((uint)(x8));
        __arm64_flags_right_13465636 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13465636 >= __arm64_flags_right_13465636))) || (unchecked((uint)((__arm64_flags_left_13465636) - (__arm64_flags_right_13465636))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCD796C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        __arm64_pair_address_13465648 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465648);
#else
        v1 = __ReadVector128(__arm64_pair_address_13465648);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465648) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465648) + (0x10UL))));
#endif
        x23 = 0x1A8F000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x1E0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x24) + (0x68UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x24) + (0x58UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x24) + (0x58UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x24) + (0x48UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x24) + (0x48UL))), v1);
#endif
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD785C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7854UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x23);
        goto label_0xCD785C;
        label_0xCD785C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
        __arm64_pair_address_13465700 = x22;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465700);
#else
        v1 = __ReadVector128(__arm64_pair_address_13465700);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465700) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465700) + (0x10UL))));
#endif
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x110UL))), x9);
        __arm64_pair_address_13465712 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465712, v1);
#else
        __WriteVector128(__arm64_pair_address_13465712, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465712) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465712) + (0x10UL))), v0);
#endif
        if ((x21 == 0x0UL))
        {
            goto label_0xCD7968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7878UL);
        }
        __arm64_pair_address_13465720 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465720);
#else
        v0 = __ReadVector128(__arm64_pair_address_13465720);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465720) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465720) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
        x2 = unchecked((ulong)((sp) + (0x90UL)));
        x0 = x21;
        x3 = 0x0UL;
        __arm64_pair_address_13465740 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465740, v0);
#else
        __WriteVector128(__arm64_pair_address_13465740, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465740) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465740) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xB0UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x68UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x68UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x78UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x78UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x88UL))));
        x2 = unchecked((ulong)((sp) + (0x40UL)));
        x0 = x21;
        x1 = x22;
        x3 = 0x0UL;
        __arm64_pair_address_13465800 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465800, v0);
#else
        __WriteVector128(__arm64_pair_address_13465800, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465800) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465800) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x60UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7598UL /* metadata target: CommandBuffer.SetRenderTarget */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDED90UL /* metadata target: GraphicsUtils.get_quad */, x0, x1, x2, x3);
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x32BUL))))))));
        x22 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7900;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x200UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x32BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD7900;
        label_0xCD7900:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x200UL))));
        x2 = sp;
        x0 = x21;
        x8 = RuntimeMemory.ReadU64(x8);
        x1 = x22;
        x3 = x20;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13465900 = unchecked((ulong)((x8) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465900);
#else
        v1 = __ReadVector128(__arm64_pair_address_13465900);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465900) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465900) + (0x10UL))));
#endif
        __arm64_pair_address_13465904 = unchecked((ulong)((x8) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13465904);
#else
        v2 = __ReadVector128(__arm64_pair_address_13465904);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13465904) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13465904) + (0x10UL))));
#endif
        __arm64_pair_address_13465908 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465908, v1);
#else
        __WriteVector128(__arm64_pair_address_13465908, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465908) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465908) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13465912 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13465912, v2);
#else
        __WriteVector128(__arm64_pair_address_13465912, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13465912) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13465912) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A7CB8UL /* metadata target: CommandBuffer.DrawMesh */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x10UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        sp = unchecked((ulong)((sp) + (0x1B0UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCD7968:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCD796C;
        label_0xCD796C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.Frame.MakeRecordRaw` — RVA `0xcd7970`

- Lift status: **exact**; input span: 368 bytes; span to next metadata RVA: 368 bytes.
- Metadata signature: `public void MakeRecordRaw(CommandBuffer cb, RenderTargetIdentifier source, int width, int height, RenderTextureFormat format) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=52 (informational only).

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_Frame_MakeRecordRaw_RVAcd7970(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13466152 = default(ulong);
        ulong __arm64_pair_address_13466164 = default(ulong);
        ulong __arm64_pair_address_13466172 = default(ulong);
        ulong __arm64_pair_address_13466192 = default(ulong);
        ulong __arm64_pair_address_13466208 = default(ulong);
        ulong __arm64_pair_address_13466220 = default(ulong);
        ulong __arm64_pair_address_13466248 = default(ulong);
        ulong __arm64_pair_address_13466272 = default(ulong);
        ulong __arm64_pair_address_13466280 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
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
        sp = unchecked((ulong)((sp) - (0x160UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x110UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))), x19);
        x25 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x5EFUL))))))));
        x22 = unchecked((ulong)(unchecked((uint)(x5))));
        x23 = unchecked((ulong)(unchecked((uint)(x4))));
        x24 = unchecked((ulong)(unchecked((uint)(x3))));
        x21 = x2;
        x20 = x1;
        x19 = x0;
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
            RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x5EFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD79C0:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCD75B0UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Frame.Release */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)(x22))));
        x0 = RuntimeCalls.InvokeDirect(0x1783E74UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        RuntimeMemory.WriteU64(x19, unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x19);
        if ((x0 == 0x0UL))
        {
        }
        else
        {
            x22 = 0x1A8F000UL;
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1E0UL))));
            x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
            x2 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x177E294UL /* metadata target: Texture.set_filterMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
            x0 = RuntimeMemory.ReadU64(x22);
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
                x0 = RuntimeMemory.ReadU64(x22);
            }
            label_0xCD7A20:
            ;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
            __arm64_pair_address_13466152 = x21;
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13466152);
#else
            v1 = __ReadVector128(__arm64_pair_address_13466152);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13466152) + (0x10UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13466152) + (0x10UL))));
#endif
            x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x100UL))), x9);
            __arm64_pair_address_13466164 = unchecked((ulong)((sp) + (0xE0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13466164, v1);
#else
            __WriteVector128(__arm64_pair_address_13466164, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13466164) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13466164) + (0x10UL))), v0);
#endif
            if ((x20 == 0x0UL))
            {
            }
            else
            {
                __arm64_pair_address_13466172 = unchecked((ulong)((sp) + (0xE0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13466172);
#else
                v0 = __ReadVector128(__arm64_pair_address_13466172);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13466172) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13466172) + (0x10UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
                x2 = unchecked((ulong)((sp) + (0xB0UL)));
                x0 = x20;
                x3 = 0x0UL;
                __arm64_pair_address_13466192 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13466192, v0);
#else
                __WriteVector128(__arm64_pair_address_13466192, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13466192) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13466192) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xD0UL))), x8);
                x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
                __arm64_pair_address_13466208 = x21;
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13466208);
#else
                v1 = __ReadVector128(__arm64_pair_address_13466208);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13466208) + (0x10UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13466208) + (0x10UL))));
#endif
                x1 = 0x0UL;
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), x8);
                __arm64_pair_address_13466220 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13466220, v1);
#else
                __WriteVector128(__arm64_pair_address_13466220, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13466220) + (0x10UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13466220) + (0x10UL))), v0);
#endif
                x0 = RuntimeMemory.ReadU64(x19);
                x0 = RuntimeCalls.InvokeDirect(0x17A62D4UL /* metadata target: RenderTargetIdentifier.op_Implicit */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x58UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((sp) + (0x58UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x68UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x68UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x78UL))));
                __arm64_pair_address_13466248 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13466248);
#else
                v2 = __ReadVector128(__arm64_pair_address_13466248);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13466248) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13466248) + (0x10UL))));
#endif
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
                x1 = unchecked((ulong)((sp) + (0x30UL)));
                x2 = sp;
                x0 = x20;
                x3 = 0x0UL;
                __arm64_pair_address_13466272 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13466272, v0);
#else
                __WriteVector128(__arm64_pair_address_13466272, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13466272) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13466272) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x8);
                __arm64_pair_address_13466280 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13466280, v2);
#else
                __WriteVector128(__arm64_pair_address_13466280, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13466280) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13466280) + (0x10UL))), v3);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x9);
                x0 = RuntimeCalls.InvokeDirect(0x17A7D84UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                x0 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
                RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x10UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x150UL))));
                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x150UL)))) + (0x8UL))));
                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x140UL))));
                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x8UL))));
                x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x130UL))));
                x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x8UL))));
                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x120UL))));
                x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))));
                x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
                return x0;
            }
        }
        label_0xCD7ADC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `MotionBlurComponent.FrameBlendingFilter.Frame.CalculateWeight` — RVA `0xcd7b44`

- Lift status: **partial**; input span: 232 bytes; span to next metadata RVA: 232 bytes.
- Metadata signature: `public float CalculateWeight(float strength, float currentTime) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=19 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmaxnm' at 0xcd7ba0; reason: Unsupported instruction 'fabd' at 0xcd7bc0; reason: Unsupported instruction 'fcsel' at 0xcd7c04; reason: Unknown IR expression at 0xcd7c04

```csharp
public static ulong MotionBlurComponent_FrameBlendingFilter_Frame_CalculateWeight_RVAcd7b44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13466552 = default(float);
        float __arm64_float_flags_left_13466564 = default(float);
        float __arm64_float_flags_left_13466596 = default(float);
        float __arm64_float_flags_right_13466552 = default(float);
        float __arm64_float_flags_right_13466564 = default(float);
        float __arm64_float_flags_right_13466596 = default(float);
        float __arm64_fp_left_13466588 = default(float);
        float __arm64_fp_right_13466588 = default(float);
        ulong __arm64_load_address_13466636 = default(ulong);
        ulong __arm64_load_address_13466660 = default(ulong);
        ulong __arm64_pair_address_13466440 = default(ulong);
        ulong __arm64_pair_address_13466620 = default(ulong);
        ulong __arm64_pair_address_13466652 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        __arm64_pair_address_13466440 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13466440, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13466440) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2CAUL))))))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x10UL))))), 0));
        v8 = v1;
        x19 = x0;
        v9 = v0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7B84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD80UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2CAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD7B84;
        label_0xCD7B84:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD80UL))));
        x9 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x474UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        x8 = RuntimeMemory.ReadU64(x8);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        RuntimeCalls.Unsupported("fmaxnm", 0xCD7BA0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_13466552 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13466552 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_13466552 > __arm64_float_flags_right_13466552) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        RuntimeCalls.Unsupported("fabd", 0xCD7BC0UL);
        __arm64_float_flags_left_13466564 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13466564 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13466564 < __arm64_float_flags_right_13466564))
        {
            goto label_0xCD7C14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7BCCUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x10UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC2800000UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x42A00000UL))));
        __arm64_fp_left_13466588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_fp_right_13466588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_13466588 != __arm64_fp_left_13466588) ? __arm64_fp_left_13466588 : ((__arm64_fp_right_13466588 != __arm64_fp_right_13466588) ? __arm64_fp_right_13466588 : (((__arm64_fp_left_13466588 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_13466588 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_13466588), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_13466588), 0))))), 0) : ((__arm64_fp_left_13466588 <= __arm64_fp_right_13466588) ? __arm64_fp_left_13466588 : __arm64_fp_right_13466588))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_13466596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13466596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_13466620 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13466620)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13466620) + (0x8UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fcsel", 0xCD7C04UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_load_address_13466636 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13466636)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13466636) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0x19B0CF0UL);
        label_0xCD7C14:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_13466652 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13466652)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13466652) + (0x8UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_load_address_13466660 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13466660)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13466660) + (0x30UL)));
        return x0;
        return default(ulong);
    }
```
