# `AmbientOcclusionComponent` — TypeDefIndex 3504

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `RenderTargetIdentifier[]` | `m_MRT` |

## `AmbientOcclusionComponent.get_occlusionSource` — RVA `0xccd8c4`

- Lift status: **exact**; input span: 164 bytes; span to next metadata RVA: 164 bytes.
- Metadata signature: `private AmbientOcclusionComponent.OcclusionSource get_occlusionSource() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static uint AmbientOcclusionComponent_get_occlusionSource_RVAccd8c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x59BUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD8F0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x59BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCD8F0;
        label_0xCCD8F0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD964;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE49CUL /* metadata target: PostProcessingContext.get_isGBufferAvailable */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD91C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCCD908UL)));
        }
        if ((x8 == 0x0UL))
        {
            goto label_0xCCD964;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x21UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD920;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        goto label_0xCCD958;
        label_0xCCD91C:
        ;
        if ((x8 == 0x0UL))
        {
            goto label_0xCCD964;
        }
        else
        {
            goto label_0xCCD920;
        }
        label_0xCCD920:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x23UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD94C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD964;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE49CUL /* metadata target: PostProcessingContext.get_isGBufferAvailable */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD954;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCD964;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x21UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD954;
        }
        else
        {
            goto label_0xCCD94C;
        }
        label_0xCCD94C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCCD958;
        label_0xCCD954:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCCD958;
        label_0xCCD958:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCCD964:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `AmbientOcclusionComponent.get_ambientOnlySupported` — RVA `0xccd968`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `private bool get_ambientOnlySupported() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static uint AmbientOcclusionComponent_get_ambientOnlySupported_RVAccd968(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13425112 = default(uint);
        uint __arm64_flags_result_13425112 = default(uint);
        uint __arm64_flags_right_13425112 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x59CUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCD994;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x59CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCD994;
        label_0xCCD994:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD9F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4C4UL /* metadata target: PostProcessingContext.get_isHdr */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD9E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCD9F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x22UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD9E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCD9F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE49CUL /* metadata target: PostProcessingContext.get_isGBufferAvailable */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCD9E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCD9F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x21UL))))))));
        __arm64_flags_left_13425112 = unchecked((uint)(x8));
        __arm64_flags_right_13425112 = unchecked((uint)0x1UL);
        __arm64_flags_result_13425112 = unchecked((uint)((__arm64_flags_left_13425112) & (__arm64_flags_right_13425112)));
        x0 = unchecked((ulong)(((__arm64_flags_result_13425112 == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCCD9E8;
        label_0xCCD9E4:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCCD9E8;
        label_0xCCD9E8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCCD9F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `AmbientOcclusionComponent.get_active` — RVA `0xccd9f8`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static uint AmbientOcclusionComponent_get_active_RVAccd9f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13425228 = default(uint);
        uint __arm64_flags_right_13425228 = default(uint);
        float __arm64_float_flags_left_13425208 = default(float);
        float __arm64_float_flags_right_13425208 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x59DUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCDA24;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x59DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCDA24;
        label_0xCCDA24:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCDA68;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCDA58;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCCDA34UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
        __arm64_float_flags_left_13425208 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13425208 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13425208 <= __arm64_float_flags_right_13425208) || ((__arm64_float_flags_left_13425208 != __arm64_float_flags_left_13425208) || (__arm64_float_flags_right_13425208 != __arm64_float_flags_right_13425208))))
        {
            goto label_0xCCDA58;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCDA68;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13425228 = unchecked((uint)(x8));
        __arm64_flags_right_13425228 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13425228) - (__arm64_flags_right_13425228))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCCDA5C;
        label_0xCCDA58:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCCDA5C;
        label_0xCCDA5C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCCDA68:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `AmbientOcclusionComponent.GetCameraFlags` — RVA `0xccda6c`

- Lift status: **partial**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=5 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xccda84; reason: Unknown IR expression at 0xccda84

```csharp
public static uint AmbientOcclusionComponent_GetCameraFlags_RVAccda6c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13425276 = default(uint);
        uint __arm64_flags_left_13425296 = default(uint);
        uint __arm64_flags_right_13425276 = default(uint);
        uint __arm64_flags_right_13425296 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCCD8C4UL /* metadata target: AmbientOcclusionComponent.get_occlusionSource */, x0, x1, x2, x3);
        __arm64_flags_left_13425276 = unchecked((uint)(x0));
        __arm64_flags_right_13425276 = unchecked((uint)0x0UL);
        x0 = x19;
        RuntimeCalls.Unsupported("cset", 0xCCDA84UL);
        x20 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xCCD8C4UL /* metadata target: AmbientOcclusionComponent.get_occlusionSource */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) | (unchecked((uint)(0x2UL)))))));
        __arm64_flags_left_13425296 = unchecked((uint)(x0));
        __arm64_flags_right_13425296 = unchecked((uint)0x2UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13425296) - (__arm64_flags_right_13425296))) == unchecked((uint)0x0UL)) ? unchecked((uint)(x20)) : unchecked((uint)(x8)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `AmbientOcclusionComponent.GetName` — RVA `0xccdaa4`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public override string GetName() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong AmbientOcclusionComponent_GetName_RVAccdaa4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x59EUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC80UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC80UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x59EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCDAD4:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `AmbientOcclusionComponent.GetCameraEvent` — RVA `0xccdae4`

- Lift status: **partial**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=9 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xccdb1c; reason: Unknown IR expression at 0xccdb1c

```csharp
public static uint AmbientOcclusionComponent_GetCameraEvent_RVAccdae4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13425428 = default(uint);
        uint __arm64_flags_right_13425428 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCCD968UL /* metadata target: AmbientOcclusionComponent.get_ambientOnlySupported */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCDB24;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCDB30;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCDB30;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCDB30;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x15UL))));
        __arm64_flags_left_13425428 = unchecked((uint)(x8));
        __arm64_flags_right_13425428 = unchecked((uint)0x4UL);
        x8 = unchecked((ulong)(unchecked((uint)(0xCUL))));
        RuntimeCalls.Unsupported("csel", 0xCCDB1CUL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        goto label_0xCCDB28;
        label_0xCCDB24:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0xCUL))));
        goto label_0xCCDB28;
        label_0xCCDB28:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xCCDB30:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `AmbientOcclusionComponent.PopulateCommandBuffer` — RVA `0xccdb44`

- Lift status: **partial**; input span: 2484 bytes; span to next metadata RVA: 2484 bytes.
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=364 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fcsel' at 0xccdd00; reason: Unknown IR expression at 0xccdd00; reason: Unsupported instruction 'cinc' at 0xccde30; reason: Unknown IR expression at 0xccde30; reason: Unsupported instruction 'csel' at 0xcce330; reason: Unknown IR expression at 0xcce330

```csharp
public static ulong AmbientOcclusionComponent_PopulateCommandBuffer_RVAccdb44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_13425904 = default(ulong);
        uint __arm64_flags_left_13426120 = default(uint);
        ulong __arm64_flags_left_13426216 = default(ulong);
        uint __arm64_flags_left_13426572 = default(uint);
        uint __arm64_flags_left_13427068 = default(uint);
        uint __arm64_flags_left_13427488 = default(uint);
        ulong __arm64_flags_result_13425904 = default(ulong);
        ulong __arm64_flags_result_13426216 = default(ulong);
        uint __arm64_flags_result_13427488 = default(uint);
        ulong __arm64_flags_right_13425904 = default(ulong);
        uint __arm64_flags_right_13426120 = default(uint);
        ulong __arm64_flags_right_13426216 = default(ulong);
        uint __arm64_flags_right_13426572 = default(uint);
        uint __arm64_flags_right_13427068 = default(uint);
        uint __arm64_flags_right_13427488 = default(uint);
        ulong __arm64_pair_address_13425476 = default(ulong);
        ulong __arm64_pair_address_13425744 = default(ulong);
        ulong __arm64_pair_address_13426316 = default(ulong);
        ulong __arm64_pair_address_13426328 = default(ulong);
        ulong __arm64_pair_address_13426340 = default(ulong);
        ulong __arm64_pair_address_13426372 = default(ulong);
        ulong __arm64_pair_address_13426464 = default(ulong);
        ulong __arm64_pair_address_13426488 = default(ulong);
        ulong __arm64_pair_address_13426520 = default(ulong);
        ulong __arm64_pair_address_13426540 = default(ulong);
        ulong __arm64_pair_address_13426548 = default(ulong);
        ulong __arm64_pair_address_13426560 = default(ulong);
        ulong __arm64_pair_address_13426580 = default(ulong);
        ulong __arm64_pair_address_13426588 = default(ulong);
        ulong __arm64_pair_address_13426636 = default(ulong);
        ulong __arm64_pair_address_13426644 = default(ulong);
        ulong __arm64_pair_address_13426688 = default(ulong);
        ulong __arm64_pair_address_13426696 = default(ulong);
        ulong __arm64_pair_address_13426748 = default(ulong);
        ulong __arm64_pair_address_13426756 = default(ulong);
        ulong __arm64_pair_address_13426880 = default(ulong);
        ulong __arm64_pair_address_13426904 = default(ulong);
        ulong __arm64_pair_address_13426936 = default(ulong);
        ulong __arm64_pair_address_13426956 = default(ulong);
        ulong __arm64_pair_address_13426964 = default(ulong);
        ulong __arm64_pair_address_13426972 = default(ulong);
        ulong __arm64_pair_address_13427004 = default(ulong);
        ulong __arm64_pair_address_13427012 = default(ulong);
        ulong __arm64_pair_address_13427120 = default(ulong);
        ulong __arm64_pair_address_13427144 = default(ulong);
        ulong __arm64_pair_address_13427176 = default(ulong);
        ulong __arm64_pair_address_13427196 = default(ulong);
        ulong __arm64_pair_address_13427204 = default(ulong);
        ulong __arm64_pair_address_13427212 = default(ulong);
        ulong __arm64_pair_address_13427244 = default(ulong);
        ulong __arm64_pair_address_13427252 = default(ulong);
        ulong __arm64_pair_address_13427316 = default(ulong);
        ulong __arm64_pair_address_13427340 = default(ulong);
        ulong __arm64_pair_address_13427440 = default(ulong);
        ulong __arm64_pair_address_13427444 = default(ulong);
        ulong __arm64_pair_address_13427448 = default(ulong);
        ulong __arm64_pair_address_13427452 = default(ulong);
        ulong __arm64_pair_address_13427628 = default(ulong);
        ulong __arm64_pair_address_13427648 = default(ulong);
        ulong __arm64_pair_address_13427656 = default(ulong);
        ulong __arm64_pair_address_13427664 = default(ulong);
        ulong __arm64_pair_address_13427696 = default(ulong);
        ulong __arm64_pair_address_13427704 = default(ulong);
        ulong __arm64_pair_address_13427744 = default(ulong);
        ulong __arm64_pair_address_13427768 = default(ulong);
        ulong __arm64_pair_address_13427800 = default(ulong);
        ulong __arm64_pair_address_13427820 = default(ulong);
        ulong __arm64_pair_address_13427828 = default(ulong);
        ulong __arm64_pair_address_13427836 = default(ulong);
        ulong __arm64_pair_address_13427868 = default(ulong);
        ulong __arm64_pair_address_13427876 = default(ulong);
        ulong __arm64_pair_address_13427948 = default(ulong);
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
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x28 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13425476 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13425476, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13425476) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13425476;
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
        sp = unchecked((ulong)((sp) - (0x520UL)));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x59FUL))))))));
        x19 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCDBE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x59FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCDBE0;
        label_0xCCDBE0:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x510UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x4E0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x4B0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x480UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x450UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x420UL))), 0x0UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x500UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x500UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4F0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4F0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4D0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4D0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4C0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4C0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4A0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4A0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x490UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x490UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x440UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x440UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x400UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x400UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xCB8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1CUL))));
        __arm64_pair_address_13425744 = unchecked((ulong)((x8) + (0x14UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13425744)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13425744) + (0x4UL))))), 0));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA0UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x28 = 0x1A8E000UL;
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xC88UL))));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177B0DCUL /* metadata target: Material.set_shaderKeywords */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCDCB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCDCB0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCCDCB8;
        label_0xCCDCB8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x20;
        v0 = v9;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = x20;
        v0 = v8;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        __arm64_flags_left_13425904 = x23;
        __arm64_flags_right_13425904 = 0x100000000UL;
        __arm64_flags_result_13425904 = unchecked((ulong)((__arm64_flags_left_13425904) & (__arm64_flags_right_13425904)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeCalls.Unsupported("fcsel", 0xCCDD00UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x0 = x20;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCDD28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCDD20UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCCDD28;
        label_0xCCDD28:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)(x23))));
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE49CUL /* metadata target: PostProcessingContext.get_isGBufferAvailable */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCDDE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779C90UL /* metadata target: RenderSettings.get_fog */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCDDE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCDD74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCDD6CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCCDD74;
        label_0xCCDD74:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = 0x0UL;
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x1779F1CUL /* metadata target: RenderSettings.get_fogDensity */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x1779CF4UL /* metadata target: RenderSettings.get_fogStartDistance */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = 0x0UL;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x1779D54UL /* metadata target: RenderSettings.get_fogEndDistance */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v2 = v0;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        v0 = v8;
        v1 = v9;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779DB4UL /* metadata target: RenderSettings.get_fogMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13426120 = unchecked((uint)(x8));
        __arm64_flags_right_13426120 = unchecked((uint)0x2UL);
        if (((__arm64_flags_left_13426120 >= __arm64_flags_right_13426120) && (!((unchecked((uint)((__arm64_flags_left_13426120) - (__arm64_flags_right_13426120))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xCCDDF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x19B6000UL;
        x9 = unchecked((ulong)((x9) + (0xF18UL)));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))));
        goto label_0xCCDDE8;
        label_0xCCDDE0:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC98UL))));
        goto label_0xCCDDE8;
        label_0xCCDDE8:
        ;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, x3);
        goto label_0xCCDDF8;
        label_0xCCDDF8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(x28);
        __arm64_flags_left_13426216 = x23;
        __arm64_flags_right_13426216 = 0x100000000UL;
        __arm64_flags_result_13426216 = unchecked((ulong)((__arm64_flags_left_13426216) & (__arm64_flags_right_13426216)));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("cinc", 0xCCDE30UL);
        x26 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x9)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCDE44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCDE3CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCCDE44;
        label_0xCCDE44:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x24))))) / (unchecked((int)(unchecked((uint)(x26)))))))))));
        x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x25))))) / (unchecked((int)(unchecked((uint)(x26)))))))))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x23 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x6 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x29 = unchecked((ulong)((sp) + (0x2E8UL)));
        RuntimeMemory.WritePtr(sp, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13426316 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426316);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426316);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426316) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426316) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        x0 = x21;
        __arm64_pair_address_13426328 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426328, v0);
#else
        __WriteVector128(__arm64_pair_address_13426328, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426328) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426328) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3F0UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0xCCD8C4UL /* metadata target: AmbientOcclusionComponent.get_occlusionSource */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13426340 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426340);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426340);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426340) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426340) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3F0UL))));
        x4 = unchecked((ulong)(unchecked((uint)(x0))));
        x2 = unchecked((ulong)((sp) + (0x370UL)));
        x0 = x19;
        x1 = 0x0UL;
        x3 = x20;
        x5 = 0x0UL;
        __arm64_pair_address_13426372 = unchecked((ulong)((sp) + (0x370UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426372, v0);
#else
        __WriteVector128(__arm64_pair_address_13426372, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426372) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426372) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x390UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7CE8UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(x24))));
        x3 = unchecked((ulong)(unchecked((uint)(x25))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x26 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x6 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WritePtr(sp, 0x0UL);
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13426464 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426464);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426464);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426464) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426464) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        x2 = unchecked((ulong)((sp) + (0x340UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x27))));
        x3 = 0x0UL;
        __arm64_pair_address_13426488 = unchecked((ulong)((sp) + (0x340UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426488, v0);
#else
        __WriteVector128(__arm64_pair_address_13426488, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426488) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426488) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x360UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((sp) + (0x310UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x330UL))));
        __arm64_pair_address_13426520 = unchecked((ulong)((sp) + (0x310UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426520);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426520);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426520) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426520) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x26))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3C0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x2E8UL)));
        __arm64_pair_address_13426540 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426540, v0);
#else
        __WriteVector128(__arm64_pair_address_13426540, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426540) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426540) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13426548 = x29;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426548);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426548);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426548) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426548) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x308UL))));
        x0 = x21;
        __arm64_pair_address_13426560 = unchecked((ulong)((sp) + (0x310UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426560, v0);
#else
        __WriteVector128(__arm64_pair_address_13426560, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426560) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426560) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x330UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0xCCD8C4UL /* metadata target: AmbientOcclusionComponent.get_occlusionSource */, x0, x1, x2, x3);
        __arm64_flags_left_13426572 = unchecked((uint)(x0));
        __arm64_flags_right_13426572 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13426572) - (__arm64_flags_right_13426572))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCDFCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCDF94UL);
        }
        __arm64_pair_address_13426580 = unchecked((ulong)((sp) + (0x310UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426580);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426580);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426580) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426580) + (0x10UL))));
#endif
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x330UL))));
        __arm64_pair_address_13426588 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426588);
#else
        v2 = __ReadVector128(__arm64_pair_address_13426588);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426588) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426588) + (0x10UL))));
#endif
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        x8 = unchecked((ulong)((sp) + (0x4C0UL)));
        x9 = unchecked((ulong)((sp) + (0x4F0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x4UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4F0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4F0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x500UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x500UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x510UL))), x10);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4C0UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4C0UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4D0UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4D0UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x4E0UL))), x11);
        goto label_0xCCE000;
        label_0xCCDFCC:
        ;
        __arm64_pair_address_13426636 = unchecked((ulong)((sp) + (0x310UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426636);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426636);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426636) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426636) + (0x10UL))));
#endif
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x330UL))));
        __arm64_pair_address_13426644 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426644);
#else
        v2 = __ReadVector128(__arm64_pair_address_13426644);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426644) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426644) + (0x10UL))));
#endif
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        x8 = unchecked((ulong)((sp) + (0x460UL)));
        x9 = unchecked((ulong)((sp) + (0x490UL)));
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
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x4B0UL))), x10);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x480UL))), x11);
        x4 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xCCE000;
        label_0xCCE000:
        ;
        __arm64_pair_address_13426688 = x9;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426688);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426688);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426688) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426688) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        __arm64_pair_address_13426696 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426696);
#else
        v2 = __ReadVector128(__arm64_pair_address_13426696);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426696) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426696) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x1 = unchecked((ulong)((sp) + (0x2C0UL)));
        x2 = unchecked((ulong)((sp) + (0x290UL)));
        x0 = x19;
        x3 = x20;
        x5 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x450UL))), x9);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x440UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x440UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v0);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x420UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x410UL))), v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x400UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x400UL))), v2);
#endif
        __arm64_pair_address_13426748 = unchecked((ulong)((sp) + (0x2C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426748, v2);
#else
        __WriteVector128(__arm64_pair_address_13426748, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426748) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426748) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2E0UL))), x8);
        __arm64_pair_address_13426756 = unchecked((ulong)((sp) + (0x290UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426756, v0);
#else
        __WriteVector128(__arm64_pair_address_13426756, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426756) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426756) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2B0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCE074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCE06CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCCE074;
        label_0xCCE074:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x23 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x1CUL))))));
        x2 = unchecked((ulong)(unchecked((uint)(x24))));
        x3 = unchecked((ulong)(unchecked((uint)(x25))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x6 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WritePtr(sp, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = unchecked((ulong)(unchecked((uint)(x26))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x8 = unchecked((ulong)((sp) + (0x3D0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13426880 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426880);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426880);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426880) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426880) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3F0UL))));
        x2 = unchecked((ulong)((sp) + (0x260UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x3 = 0x0UL;
        __arm64_pair_address_13426904 = unchecked((ulong)((sp) + (0x260UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426904, v0);
#else
        __WriteVector128(__arm64_pair_address_13426904, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426904) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426904) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x280UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x26))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        __arm64_pair_address_13426936 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426936);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426936);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426936) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426936) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3F0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        __arm64_pair_address_13426956 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13426956, v0);
#else
        __WriteVector128(__arm64_pair_address_13426956, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13426956) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13426956) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13426964 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426964);
#else
        v0 = __ReadVector128(__arm64_pair_address_13426964);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426964) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426964) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        __arm64_pair_address_13426972 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13426972);
#else
        v2 = __ReadVector128(__arm64_pair_address_13426972);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13426972) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13426972) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3F0UL))));
        x1 = unchecked((ulong)((sp) + (0x230UL)));
        x2 = unchecked((ulong)((sp) + (0x200UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = x19;
        x3 = x20;
        x5 = 0x0UL;
        __arm64_pair_address_13427004 = unchecked((ulong)((sp) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427004, v0);
#else
        __WriteVector128(__arm64_pair_address_13427004, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427004) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427004) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x220UL))), x8);
        __arm64_pair_address_13427012 = unchecked((ulong)((sp) + (0x230UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427012, v2);
#else
        __WriteVector128(__arm64_pair_address_13427012, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427012) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427012) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x250UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13427068 = unchecked((uint)(x8));
        __arm64_flags_right_13427068 = unchecked((uint)0x4UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13427068) - (__arm64_flags_right_13427068))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCE254;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x28);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCE198;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCE190UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCCE198;
        label_0xCCE198:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = 0x0UL;
        x22 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x8 = unchecked((ulong)((sp) + (0x3D0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13427120 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427120);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427120);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427120) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427120) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3F0UL))));
        x2 = unchecked((ulong)((sp) + (0x1D0UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x22))));
        x3 = 0x0UL;
        __arm64_pair_address_13427144 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427144, v0);
#else
        __WriteVector128(__arm64_pair_address_13427144, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427144) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427144) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1F0UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        __arm64_pair_address_13427176 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427176);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427176);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427176) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427176) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3F0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        __arm64_pair_address_13427196 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427196, v0);
#else
        __WriteVector128(__arm64_pair_address_13427196, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427196) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427196) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13427204 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427204);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427204);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427204) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427204) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        __arm64_pair_address_13427212 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427212);
#else
        v2 = __ReadVector128(__arm64_pair_address_13427212);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427212) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427212) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3F0UL))));
        x1 = unchecked((ulong)((sp) + (0x1A0UL)));
        x2 = unchecked((ulong)((sp) + (0x170UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = x19;
        x3 = x20;
        x5 = 0x0UL;
        __arm64_pair_address_13427244 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427244, v0);
#else
        __WriteVector128(__arm64_pair_address_13427244, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427244) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427244) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x190UL))), x8);
        __arm64_pair_address_13427252 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427252, v2);
#else
        __WriteVector128(__arm64_pair_address_13427252, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427252) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427252) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1C0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE43CUL /* metadata target: PostProcessingContext.Interrupt */, x0, x1, x2, x3);
        goto label_0xCCE4C0;
        label_0xCCE254:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xCCD968UL /* metadata target: AmbientOcclusionComponent.get_ambientOnlySupported */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCE308;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        x8 = unchecked((ulong)((sp) + (0x3D0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13427316 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427316);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427316);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427316) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427316) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3F0UL))));
        x2 = unchecked((ulong)((sp) + (0x140UL)));
        x0 = x19;
        x1 = x21;
        x3 = 0x0UL;
        __arm64_pair_address_13427340 = unchecked((ulong)((sp) + (0x140UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427340, v0);
#else
        __WriteVector128(__arm64_pair_address_13427340, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427340) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427340) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x160UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7598UL /* metadata target: CommandBuffer.SetRenderTarget */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDED90UL /* metadata target: GraphicsUtils.get_quad */, x0, x1, x2, x3);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x32BUL))))))));
        x21 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCE2C4;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x32BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCE2C4;
        label_0xCCE2C4:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x200UL))));
        x2 = unchecked((ulong)((sp) + (0x100UL)));
        x5 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(x8);
        x1 = x21;
        x3 = x20;
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x6 = 0x0UL;
        __arm64_pair_address_13427440 = unchecked((ulong)((x8) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427440);
#else
        v1 = __ReadVector128(__arm64_pair_address_13427440);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427440) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427440) + (0x10UL))));
#endif
        __arm64_pair_address_13427444 = unchecked((ulong)((x8) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427444);
#else
        v2 = __ReadVector128(__arm64_pair_address_13427444);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427444) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427444) + (0x10UL))));
#endif
        __arm64_pair_address_13427448 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427448, v1);
#else
        __WriteVector128(__arm64_pair_address_13427448, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427448) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427448) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13427452 = unchecked((ulong)((sp) + (0x100UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427452, v2);
#else
        __WriteVector128(__arm64_pair_address_13427452, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427452) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427452) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A7CB8UL /* metadata target: CommandBuffer.DrawMesh */, x0, x1, x2, x3);
        goto label_0xCCE4C0;
        label_0xCCE308:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4C4UL /* metadata target: PostProcessingContext.get_isHdr */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(x28);
        __arm64_flags_left_13427488 = unchecked((uint)(x8));
        __arm64_flags_right_13427488 = unchecked((uint)0x1UL);
        __arm64_flags_result_13427488 = unchecked((uint)((__arm64_flags_left_13427488) & (__arm64_flags_right_13427488)));
        x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        RuntimeCalls.Unsupported("csel", 0xCCE330UL);
        x25 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x10)) : unchecked((uint)(x8)))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCE340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCE338UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x28);
        goto label_0xCCE340;
        label_0xCCE340:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x8;
        x1 = 0x0UL;
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x24UL))))));
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE4F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x3 = unchecked((ulong)(unchecked((uint)(x0))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)(x25))));
        x7 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        __arm64_pair_address_13427628 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427628);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427628);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427628) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427628) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3F0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        __arm64_pair_address_13427648 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427648, v0);
#else
        __WriteVector128(__arm64_pair_address_13427648, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427648) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427648) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13427656 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427656);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427656);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427656) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427656) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        __arm64_pair_address_13427664 = unchecked((ulong)((sp) + (0x3D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427664);
#else
        v2 = __ReadVector128(__arm64_pair_address_13427664);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427664) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427664) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3F0UL))));
        x1 = unchecked((ulong)((sp) + (0xD0UL)));
        x2 = unchecked((ulong)((sp) + (0xA0UL)));
        x0 = x19;
        x3 = x22;
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = 0x0UL;
        __arm64_pair_address_13427696 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427696, v0);
#else
        __WriteVector128(__arm64_pair_address_13427696, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427696) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427696) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xC0UL))), x8);
        __arm64_pair_address_13427704 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427704, v2);
#else
        __WriteVector128(__arm64_pair_address_13427704, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427704) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427704) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xF0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x8 = unchecked((ulong)((sp) + (0x3A0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13427744 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427744);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427744);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427744) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427744) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        x2 = unchecked((ulong)((sp) + (0x70UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        __arm64_pair_address_13427768 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427768, v0);
#else
        __WriteVector128(__arm64_pair_address_13427768, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427768) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427768) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x90UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((sp) + (0x310UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x330UL))));
        __arm64_pair_address_13427800 = unchecked((ulong)((sp) + (0x310UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427800);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427800);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427800) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427800) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3C0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x310UL)));
        __arm64_pair_address_13427820 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427820, v0);
#else
        __WriteVector128(__arm64_pair_address_13427820, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427820) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427820) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13427828 = unchecked((ulong)((sp) + (0x310UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427828);
#else
        v0 = __ReadVector128(__arm64_pair_address_13427828);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427828) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427828) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x330UL))));
        __arm64_pair_address_13427836 = unchecked((ulong)((sp) + (0x3A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13427836);
#else
        v2 = __ReadVector128(__arm64_pair_address_13427836);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13427836) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13427836) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3C0UL))));
        x1 = unchecked((ulong)((sp) + (0x40UL)));
        x2 = unchecked((ulong)((sp) + (0x10UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = x19;
        x3 = x20;
        x5 = 0x0UL;
        __arm64_pair_address_13427868 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427868, v0);
#else
        __WriteVector128(__arm64_pair_address_13427868, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427868) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427868) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x8);
        __arm64_pair_address_13427876 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13427876, v2);
#else
        __WriteVector128(__arm64_pair_address_13427876, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13427876) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13427876) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x60UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCCE4C0;
        label_0xCCE4C0:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        sp = unchecked((ulong)((sp) + (0x520UL)));
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
        __arm64_pair_address_13427948 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13427948)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13427948) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13427948) + (0x70UL)));
        return x0;
        label_0xCCE4F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `AmbientOcclusionComponent.ctor` — RVA `0xcce4f8`

- Lift status: **exact**; input span: 292 bytes; span to next metadata RVA: 292 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=36 (informational only).

```csharp
public static ulong AmbientOcclusionComponent_ctor_RVAcce4f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13428164 = default(uint);
        uint __arm64_flags_right_13428164 = default(uint);
        ulong __arm64_pair_address_13428072 = default(ulong);
        ulong __arm64_pair_address_13428084 = default(ulong);
        ulong __arm64_pair_address_13428092 = default(ulong);
        ulong __arm64_pair_address_13428112 = default(ulong);
        ulong __arm64_pair_address_13428132 = default(ulong);
        ulong __arm64_pair_address_13428152 = default(ulong);
        ulong __arm64_pair_address_13428176 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5A0UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xCC0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCC8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCC0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5A0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCE53C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x0;
        x0 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
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
        __arm64_pair_address_13428072 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13428072, v0);
#else
        __WriteVector128(__arm64_pair_address_13428072, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13428072) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13428072) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), x8);
        if ((x20 == 0x0UL))
        {
        }
        else
        {
            __arm64_pair_address_13428084 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13428084);
#else
            v0 = __ReadVector128(__arm64_pair_address_13428084);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13428084) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13428084) + (0x10UL))));
#endif
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
            __arm64_pair_address_13428092 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_13428092, v0);
#else
            __WriteVector128(__arm64_pair_address_13428092, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13428092) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13428092) + (0x10UL))), v1);
#endif
            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x8);
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
            if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                __arm64_pair_address_13428112 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13428112);
#else
                v1 = __ReadVector128(__arm64_pair_address_13428112);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13428112) + (0x10UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13428112) + (0x10UL))));
#endif
                x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                x1 = 0x0UL;
                RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x40UL))), x8);
                __arm64_pair_address_13428132 = unchecked((ulong)((x20) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13428132, v1);
#else
                __WriteVector128(__arm64_pair_address_13428132, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13428132) + (0x10UL))), v0);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13428132) + (0x10UL))), v0);
#endif
                x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
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
                __arm64_pair_address_13428152 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13428152, v0);
#else
                __WriteVector128(__arm64_pair_address_13428152, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13428152) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13428152) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x8);
                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
                __arm64_flags_left_13428164 = unchecked((uint)(x8));
                __arm64_flags_right_13428164 = unchecked((uint)0x1UL);
                if (((!((__arm64_flags_left_13428164 >= __arm64_flags_right_13428164))) || (unchecked((uint)((__arm64_flags_left_13428164) - (__arm64_flags_right_13428164))) == unchecked((uint)0x0UL))))
                {
                }
                else
                {
                    x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
                    __arm64_pair_address_13428176 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                    v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13428176);
#else
                    v1 = __ReadVector128(__arm64_pair_address_13428176);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13428176) + (0x10UL))));
#else
                    v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13428176) + (0x10UL))));
#endif
                    x21 = 0x1A8E000UL;
                    x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xCC8UL))));
                    x0 = x19;
                    RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x68UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x58UL))), v0);
#else
                    __WriteVector128(unchecked((ulong)((x20) + (0x58UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v1);
#else
                    __WriteVector128(unchecked((ulong)((x20) + (0x48UL))), v1);
#endif
                    RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
                    x1 = x20;
                    x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
                    x1 = RuntimeMemory.ReadU64(x21);
                    x0 = x19;
                    x0 = RuntimeCalls.InvokeDirect(0x11689ECUL, x0, x1, x2, x3);
                    x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
                    x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
                    x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
                    x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
                    return x0;
                }
            }
            label_0xCCE614:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        }
        label_0xCCE618:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
