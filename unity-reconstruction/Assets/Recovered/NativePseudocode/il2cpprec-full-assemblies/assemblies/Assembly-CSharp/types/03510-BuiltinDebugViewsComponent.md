# `BuiltinDebugViewsComponent` — TypeDefIndex 3510

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `BuiltinDebugViewsComponent.ArrowArray` | `m_Arrows` |

## `BuiltinDebugViewsComponent.get_active` — RVA `0xccf4d0`

- Lift status: **exact**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static uint BuiltinDebugViewsComponent_get_active_RVAccf4d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13432080 = default(uint);
        uint __arm64_flags_right_13432080 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5A6UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5A6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCF4FC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            label_0xCCF520:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
            __arm64_flags_left_13432080 = unchecked((uint)(x8));
            __arm64_flags_right_13432080 = unchecked((uint)0x3UL);
            x0 = unchecked((ulong)(((!((__arm64_flags_left_13432080 >= __arm64_flags_right_13432080))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `BuiltinDebugViewsComponent.GetCameraFlags` — RVA `0xccf524`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static uint BuiltinDebugViewsComponent_GetCameraFlags_RVAccf524(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13432160 = default(uint);
        uint __arm64_flags_right_13432160 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5A7UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5A7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCF550:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            label_0xCCF588:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
            x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
            __arm64_flags_left_13432160 = unchecked((uint)(x8));
            __arm64_flags_right_13432160 = unchecked((uint)0x2UL);
            if (((__arm64_flags_left_13432160 >= __arm64_flags_right_13432160) && (!((unchecked((uint)((__arm64_flags_left_13432160) - (__arm64_flags_right_13432160))) == unchecked((uint)0x0UL))))))
            {
                label_0xCCF578:
                ;
                x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            }
            else
            {
                x9 = 0x452000UL;
                x9 = unchecked((ulong)((x9) + (0x290UL)));
                x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))));
            }
            label_0xCCF57C:
            ;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `BuiltinDebugViewsComponent.GetCameraEvent` — RVA `0xccf58c`

- Lift status: **partial**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=12 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xccf5d4; reason: Unknown IR expression at 0xccf5d4

```csharp
public static uint BuiltinDebugViewsComponent_GetCameraEvent_RVAccf58c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13432268 = default(uint);
        uint __arm64_flags_right_13432268 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5A8UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5A8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCF5B8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            label_0xCCF5E0:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x9 = unchecked((ulong)(unchecked((uint)(0xCUL))));
            __arm64_flags_left_13432268 = unchecked((uint)(x8));
            __arm64_flags_right_13432268 = unchecked((uint)0x3UL);
            x8 = unchecked((ulong)(unchecked((uint)(0x12UL))));
            RuntimeCalls.Unsupported("csel", 0xCCF5D4UL);
            x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `BuiltinDebugViewsComponent.GetName` — RVA `0xccf5e4`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public override string GetName() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_GetName_RVAccf5e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x5A9UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xDC0UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDC0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x5A9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCF614:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.PopulateCommandBuffer` — RVA `0xccf624`

- Lift status: **exact**; input span: 288 bytes; span to next metadata RVA: 288 bytes.
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=40 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_PopulateCommandBuffer_RVAccf624(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13432544 = default(uint);
        uint __arm64_flags_left_13432552 = default(uint);
        uint __arm64_flags_left_13432560 = default(uint);
        uint __arm64_flags_right_13432544 = default(uint);
        uint __arm64_flags_right_13432552 = default(uint);
        uint __arm64_flags_right_13432560 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5AAUL))))))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5AAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCF670;
        label_0xCCF670:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCCF740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xDD0UL))));
        x22 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177B0DCUL /* metadata target: Material.set_shaderKeywords */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE49CUL /* metadata target: PostProcessingContext.get_isGBufferAvailable */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCF6E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDC8UL))));
        x0 = x21;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, x3);
        goto label_0xCCF6E0;
        label_0xCCF6E0:
        ;
        __arm64_flags_left_13432544 = unchecked((uint)(x22));
        __arm64_flags_right_13432544 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_13432544) - (__arm64_flags_right_13432544))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCF708;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCF6E8UL);
        }
        __arm64_flags_left_13432552 = unchecked((uint)(x22));
        __arm64_flags_right_13432552 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13432552) - (__arm64_flags_right_13432552))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCF718;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCF6F0UL);
        }
        __arm64_flags_left_13432560 = unchecked((uint)(x22));
        __arm64_flags_right_13432560 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13432560) - (__arm64_flags_right_13432560))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCF724;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCCF744UL /* metadata target: BuiltinDebugViewsComponent.DepthPass */, x0, x1, x2, x3);
        goto label_0xCCF724;
        label_0xCCF708:
        ;
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCCF920UL /* metadata target: BuiltinDebugViewsComponent.MotionVectorsPass */, x0, x1, x2, x3);
        goto label_0xCCF724;
        label_0xCCF718:
        ;
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCCF85CUL /* metadata target: BuiltinDebugViewsComponent.DepthNormalsPass */, x0, x1, x2, x3);
        goto label_0xCCF724;
        label_0xCCF724:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xCDE43CUL /* metadata target: PostProcessingContext.Interrupt */);
        label_0xCCF740:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.DepthPass` — RVA `0xccf744`

- Lift status: **exact**; input span: 280 bytes; span to next metadata RVA: 280 bytes.
- Metadata signature: `private void DepthPass(CommandBuffer cb) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=44 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_DepthPass_RVAccf744(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13432888 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x80UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x50UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5ABUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5ABUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCF794:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x8 = 0x1A8E000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDD0UL))));
                x2 = 0x0UL;
                x1 = RuntimeMemory.ReadU64(x8);
                x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
                if ((x8 == 0x0UL))
                {
                }
                else
                {
                    x21 = 0x1A8E000UL;
                    x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xDD8UL))));
                    x20 = x0;
                    v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x18UL))))), 0));
                    x0 = RuntimeMemory.ReadU64(x21);
                    x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
                    if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
                    {
                    }
                    else
                    {
                        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
                    }
                    label_0xCCF7E0:
                    ;
                    if ((x19 == 0x0UL))
                    {
                    }
                    else
                    {
                        x8 = RuntimeMemory.ReadU64(x21);
                        x0 = x19;
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                        x2 = 0x0UL;
                        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
                        x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                        x1 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x28UL))));
#else
                        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x28UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x38UL))));
#else
                        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x38UL))));
#endif
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
                        x2 = sp;
                        x0 = x19;
                        x1 = 0x0UL;
                        x3 = x20;
                        __arm64_pair_address_13432888 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                        RuntimeMemory.WriteVector128(__arm64_pair_address_13432888, v0);
#else
                        __WriteVector128(__arm64_pair_address_13432888, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13432888) + (0x10UL))), v1);
#else
                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13432888) + (0x10UL))), v1);
#endif
                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x8);
                        x0 = RuntimeCalls.InvokeDirect(0x17A7CE8UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
                        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
                        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
                        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
                        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x50UL))))), 0));
                        return x0;
                    }
                }
            }
        }
        label_0xCCF858:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.DepthNormalsPass` — RVA `0xccf85c`

- Lift status: **exact**; input span: 196 bytes; span to next metadata RVA: 196 bytes.
- Metadata signature: `private void DepthNormalsPass(CommandBuffer cb) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_DepthNormalsPass_RVAccf85c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13433044 = default(ulong);
        ulong __arm64_pair_address_13433056 = default(ulong);
        ulong __arm64_pair_address_13433088 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5ACUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5ACUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCF890:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x8 = 0x1A8E000UL;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDD0UL))));
                x2 = 0x0UL;
                x1 = RuntimeMemory.ReadU64(x8);
                x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
                x20 = x0;
                x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x28UL))));
#else
                v0 = __ReadVector128(unchecked((ulong)((sp) + (0x28UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x38UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((sp) + (0x38UL))));
#endif
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
                __arm64_pair_address_13433044 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_13433044, v0);
#else
                __WriteVector128(__arm64_pair_address_13433044, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433044) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433044) + (0x10UL))), v1);
#endif
                RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x70UL))), x8);
                if ((x19 == 0x0UL))
                {
                }
                else
                {
                    __arm64_pair_address_13433056 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                    v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433056);
#else
                    v0 = __ReadVector128(__arm64_pair_address_13433056);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433056) + (0x10UL))));
#else
                    v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433056) + (0x10UL))));
#endif
                    x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
                    x2 = sp;
                    x0 = x19;
                    x1 = 0x0UL;
                    x3 = x20;
                    __arm64_pair_address_13433088 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(__arm64_pair_address_13433088, v0);
#else
                    __WriteVector128(__arm64_pair_address_13433088, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                    RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433088) + (0x10UL))), v1);
#else
                    __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433088) + (0x10UL))), v1);
#endif
                    RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x8);
                    x0 = RuntimeCalls.InvokeDirect(0x17A7CE8UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                    x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
                    x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
                    x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
                    x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
                    return x0;
                }
            }
        }
        label_0xCCF91C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.MotionVectorsPass` — RVA `0xccf920`

- Lift status: **exact**; input span: 1416 bytes; span to next metadata RVA: 1416 bytes.
- Metadata signature: `private void MotionVectorsPass(CommandBuffer cb) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=221 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_MotionVectorsPass_RVAccf920(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13433608 = default(float);
        float __arm64_float_flags_left_13433616 = default(float);
        float __arm64_float_flags_left_13433976 = default(float);
        float __arm64_float_flags_left_13433984 = default(float);
        float __arm64_float_flags_right_13433608 = default(float);
        float __arm64_float_flags_right_13433616 = default(float);
        float __arm64_float_flags_right_13433976 = default(float);
        float __arm64_float_flags_right_13433984 = default(float);
        ulong __arm64_load_address_13434524 = default(ulong);
        ulong __arm64_pair_address_13433124 = default(ulong);
        ulong __arm64_pair_address_13433128 = default(ulong);
        ulong __arm64_pair_address_13433280 = default(ulong);
        ulong __arm64_pair_address_13433284 = default(ulong);
        ulong __arm64_pair_address_13433464 = default(ulong);
        ulong __arm64_pair_address_13433488 = default(ulong);
        ulong __arm64_pair_address_13433520 = default(ulong);
        ulong __arm64_pair_address_13433540 = default(ulong);
        ulong __arm64_pair_address_13433548 = default(ulong);
        ulong __arm64_pair_address_13433556 = default(ulong);
        ulong __arm64_pair_address_13433588 = default(ulong);
        ulong __arm64_pair_address_13433596 = default(ulong);
        ulong __arm64_pair_address_13433812 = default(ulong);
        ulong __arm64_pair_address_13433836 = default(ulong);
        ulong __arm64_pair_address_13433868 = default(ulong);
        ulong __arm64_pair_address_13433888 = default(ulong);
        ulong __arm64_pair_address_13433896 = default(ulong);
        ulong __arm64_pair_address_13433904 = default(ulong);
        ulong __arm64_pair_address_13433936 = default(ulong);
        ulong __arm64_pair_address_13433944 = default(ulong);
        ulong __arm64_pair_address_13434272 = default(ulong);
        ulong __arm64_pair_address_13434276 = default(ulong);
        ulong __arm64_pair_address_13434280 = default(ulong);
        ulong __arm64_pair_address_13434284 = default(ulong);
        ulong __arm64_pair_address_13434336 = default(ulong);
        ulong __arm64_pair_address_13434360 = default(ulong);
        ulong __arm64_pair_address_13434392 = default(ulong);
        ulong __arm64_pair_address_13434412 = default(ulong);
        ulong __arm64_pair_address_13434420 = default(ulong);
        ulong __arm64_pair_address_13434428 = default(ulong);
        ulong __arm64_pair_address_13434452 = default(ulong);
        ulong __arm64_pair_address_13434460 = default(ulong);
        ulong __arm64_pair_address_13434516 = default(ulong);
        ulong __arm64_pair_address_13434520 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF80UL)));
        __arm64_pair_address_13433124 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13433124, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13433124) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13433128 = unchecked((ulong)((sp) + (0x18UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13433128, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13433128) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x240UL)));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5ADUL))))))));
        x19 = x1;
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF988;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5ADUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCF988;
        label_0xCCF988:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDD0UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = 0x1A8E000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xDD8UL))));
        x21 = x0;
        __arm64_pair_address_13433280 = unchecked((ulong)((x8) + (0x1CUL)));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13433280)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13433280) + (0x4UL))))), 0));
        __arm64_pair_address_13433284 = unchecked((ulong)((x8) + (0x24UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13433284)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13433284) + (0x4UL))))), 0));
        x0 = RuntimeMemory.ReadU64(x26);
        x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x2CUL))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x30UL))))), 0));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF9E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCF9DCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        goto label_0xCCF9E4;
        label_0xCCF9E4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x8;
        x1 = 0x0UL;
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x4UL))))));
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = unchecked((ulong)(unchecked((uint)(x23))));
        x25 = unchecked((ulong)((sp) + (0x1B8UL)));
        x0 = RuntimeCalls.InvokeDirect(0x17A72F4UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x19;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x23 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13433464 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433464);
#else
        v0 = __ReadVector128(__arm64_pair_address_13433464);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433464) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433464) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x230UL))));
        x2 = unchecked((ulong)((sp) + (0x1E0UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x3 = 0x0UL;
        __arm64_pair_address_13433488 = unchecked((ulong)((sp) + (0x1E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433488, v0);
#else
        __WriteVector128(__arm64_pair_address_13433488, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433488) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433488) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x200UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D8UL))));
        __arm64_pair_address_13433520 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433520);
#else
        v0 = __ReadVector128(__arm64_pair_address_13433520);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433520) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433520) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x230UL))), x8);
        __arm64_pair_address_13433540 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433540, v0);
#else
        __WriteVector128(__arm64_pair_address_13433540, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433540) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433540) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13433548 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433548);
#else
        v0 = __ReadVector128(__arm64_pair_address_13433548);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433548) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433548) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D8UL))));
        __arm64_pair_address_13433556 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433556);
#else
        v2 = __ReadVector128(__arm64_pair_address_13433556);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433556) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433556) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x230UL))));
        x1 = unchecked((ulong)((sp) + (0x190UL)));
        x2 = unchecked((ulong)((sp) + (0x160UL)));
        x0 = x19;
        x3 = x21;
        __arm64_pair_address_13433588 = unchecked((ulong)((sp) + (0x160UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433588, v0);
#else
        __WriteVector128(__arm64_pair_address_13433588, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433588) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433588) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x180UL))), x8);
        __arm64_pair_address_13433596 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433596, v2);
#else
        __WriteVector128(__arm64_pair_address_13433596, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433596) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433596) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1B0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        __arm64_float_flags_left_13433608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13433608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13433608 <= __arm64_float_flags_right_13433608) || ((__arm64_float_flags_left_13433608 != __arm64_float_flags_left_13433608) || (__arm64_float_flags_right_13433608 != __arm64_float_flags_right_13433608))))
        {
            goto label_0xCCFC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCFB10UL);
        }
        __arm64_float_flags_left_13433616 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13433616 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13433616 <= __arm64_float_flags_right_13433616) || ((__arm64_float_flags_left_13433616 != __arm64_float_flags_left_13433616) || (__arm64_float_flags_right_13433616 != __arm64_float_flags_right_13433616))))
        {
            goto label_0xCCFC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCFB2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCFB24UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        goto label_0xCCFB2C;
        label_0xCCFB2C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x8;
        x1 = 0x0UL;
        x23 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x10UL))))));
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x3 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x2 = unchecked((ulong)(unchecked((uint)(x24))));
        x0 = RuntimeCalls.InvokeDirect(0x17A72F4UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x19;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x19;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13433812 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433812);
#else
        v0 = __ReadVector128(__arm64_pair_address_13433812);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433812) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433812) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x230UL))));
        x2 = unchecked((ulong)((sp) + (0x130UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x3 = 0x0UL;
        __arm64_pair_address_13433836 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433836, v0);
#else
        __WriteVector128(__arm64_pair_address_13433836, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433836) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433836) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x150UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D8UL))));
        __arm64_pair_address_13433868 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433868);
#else
        v0 = __ReadVector128(__arm64_pair_address_13433868);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433868) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433868) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x23))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x230UL))), x8);
        __arm64_pair_address_13433888 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433888, v0);
#else
        __WriteVector128(__arm64_pair_address_13433888, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433888) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433888) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13433896 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433896);
#else
        v0 = __ReadVector128(__arm64_pair_address_13433896);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433896) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433896) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D8UL))));
        __arm64_pair_address_13433904 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13433904);
#else
        v2 = __ReadVector128(__arm64_pair_address_13433904);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13433904) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13433904) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x230UL))));
        x1 = unchecked((ulong)((sp) + (0x100UL)));
        x2 = unchecked((ulong)((sp) + (0xD0UL)));
        x0 = x19;
        x3 = x21;
        __arm64_pair_address_13433936 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433936, v0);
#else
        __WriteVector128(__arm64_pair_address_13433936, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433936) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433936) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xF0UL))), x8);
        __arm64_pair_address_13433944 = unchecked((ulong)((sp) + (0x100UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13433944, v2);
#else
        __WriteVector128(__arm64_pair_address_13433944, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13433944) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13433944) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x120UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = unchecked((ulong)(unchecked((uint)(x23))));
        goto label_0xCCFC78;
        label_0xCCFC78:
        ;
        __arm64_float_flags_left_13433976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13433976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13433976 <= __arm64_float_flags_right_13433976) || ((__arm64_float_flags_left_13433976 != __arm64_float_flags_left_13433976) || (__arm64_float_flags_right_13433976 != __arm64_float_flags_right_13433976))))
        {
            goto label_0xCCFDB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCFC80UL);
        }
        __arm64_float_flags_left_13433984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13433984 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13433984 <= __arm64_float_flags_right_13433984) || ((__arm64_float_flags_left_13433984 != __arm64_float_flags_left_13433984) || (__arm64_float_flags_right_13433984 != __arm64_float_flags_right_13433984))))
        {
            goto label_0xCCFDB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCCFEA8UL /* metadata target: BuiltinDebugViewsComponent.PrepareArrows */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x27))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = x8;
        x1 = 0x0UL;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(x26);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x23))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCFCEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCFCE4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        goto label_0xCCFCEC;
        label_0xCCFCEC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x19;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A7438UL /* metadata target: CommandBuffer.SetGlobalVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x19;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x19;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x32BUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCFD74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x200UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x32BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCFD74;
        label_0xCCFD74:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x200UL))));
        x2 = unchecked((ulong)((sp) + (0x90UL)));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(x8);
        x1 = x22;
        x3 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13434272 = unchecked((ulong)((x8) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13434272);
#else
        v1 = __ReadVector128(__arm64_pair_address_13434272);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13434272) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13434272) + (0x10UL))));
#endif
        __arm64_pair_address_13434276 = unchecked((ulong)((x8) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13434276);
#else
        v2 = __ReadVector128(__arm64_pair_address_13434276);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13434276) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13434276) + (0x10UL))));
#endif
        __arm64_pair_address_13434280 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13434280, v1);
#else
        __WriteVector128(__arm64_pair_address_13434280, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13434280) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13434280) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13434284 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13434284, v2);
#else
        __WriteVector128(__arm64_pair_address_13434284, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13434284) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13434284) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A7CB8UL /* metadata target: CommandBuffer.DrawMesh */, x0, x1, x2, x3);
        goto label_0xCCFDB4;
        label_0xCCFDB4:
        ;
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCFDC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCFDC0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        goto label_0xCCFDC8;
        label_0xCCFDC8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13434336 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13434336);
#else
        v0 = __ReadVector128(__arm64_pair_address_13434336);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13434336) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13434336) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x230UL))));
        x2 = unchecked((ulong)((sp) + (0x60UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        __arm64_pair_address_13434360 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13434360, v0);
#else
        __WriteVector128(__arm64_pair_address_13434360, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13434360) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13434360) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D8UL))));
        __arm64_pair_address_13434392 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13434392);
#else
        v0 = __ReadVector128(__arm64_pair_address_13434392);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13434392) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13434392) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x230UL))), x8);
        __arm64_pair_address_13434412 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13434412, v0);
#else
        __WriteVector128(__arm64_pair_address_13434412, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13434412) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13434412) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13434420 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13434420);
#else
        v0 = __ReadVector128(__arm64_pair_address_13434420);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13434420) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13434420) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D8UL))));
        __arm64_pair_address_13434428 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13434428);
#else
        v2 = __ReadVector128(__arm64_pair_address_13434428);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13434428) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13434428) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x230UL))));
        x1 = unchecked((ulong)((sp) + (0x30UL)));
        x2 = sp;
        x0 = x19;
        x3 = 0x0UL;
        __arm64_pair_address_13434452 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13434452, v0);
#else
        __WriteVector128(__arm64_pair_address_13434452, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13434452) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13434452) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x8);
        __arm64_pair_address_13434460 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13434460, v2);
#else
        __WriteVector128(__arm64_pair_address_13434460, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13434460) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13434460) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7D84UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        sp = unchecked((ulong)((sp) + (0x240UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        __arm64_pair_address_13434516 = unchecked((ulong)((sp) + (0x18UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13434516)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13434516) + (0x8UL))))), 0));
        __arm64_pair_address_13434520 = unchecked((ulong)((sp) + (0x8UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13434520)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13434520) + (0x8UL))))), 0));
        __arm64_load_address_13434524 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13434524)), 0));
        return x0;
        label_0xCCFEA4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.PrepareArrows` — RVA `0xccfea8`

- Lift status: **exact**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `private void PrepareArrows() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=39 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_PrepareArrows_RVAccfea8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13434704 = default(uint);
        uint __arm64_flags_left_13434716 = default(uint);
        uint __arm64_flags_right_13434704 = default(uint);
        uint __arm64_flags_right_13434716 = default(uint);
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5AEUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCFEE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5AEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCFEE4;
        label_0xCCFEE4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCFFB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x2CUL))))));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        if ((x23 != 0x0UL))
        {
            goto label_0xCCFF44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDE0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        x1 = x23;
        RuntimeMemory.WriteU64(x19, x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x23 = RuntimeMemory.ReadU64(x19);
        if ((x23 == 0x0UL))
        {
            goto label_0xCCFFB0;
        }
        else
        {
            goto label_0xCCFF44;
        }
        label_0xCCFF44:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) * (unchecked((uint)(x20)))))));
        x21 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) / (unchecked((int)(unchecked((uint)(x22)))))))))));
        __arm64_flags_left_13434704 = unchecked((uint)(x8));
        __arm64_flags_right_13434704 = unchecked((uint)(x21));
        if ((!((unchecked((uint)((__arm64_flags_left_13434704) - (__arm64_flags_right_13434704))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCFF74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x1CUL))))));
        __arm64_flags_left_13434716 = unchecked((uint)(x8));
        __arm64_flags_right_13434716 = unchecked((uint)(x20));
        if ((!((unchecked((uint)((__arm64_flags_left_13434716) - (__arm64_flags_right_13434716))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCCFF74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCCFF74:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x10UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF294UL /* metadata target: GraphicsUtils.Destroy */, x0, x1, x2, x3);
        x0 = x23;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x23, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCFFB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xCCFFE4UL /* metadata target: BuiltinDebugViewsComponent.ArrowArray.BuildMesh */);
        label_0xCCFFB0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.OnDisable` — RVA `0xcd041c`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public override void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_OnDisable_RVAcd041c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCD044C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF294UL /* metadata target: GraphicsUtils.Destroy */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x20, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCD044C;
        label_0xCD044C:
        ;
        RuntimeMemory.WritePtr(x19, 0x0UL);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.ctor` — RVA `0xcd0464`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_ctor_RVAcd0464(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5AFUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD0498;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5AFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD0498;
        label_0xCD0498:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x11689ECUL);
        return default(ulong);
    }
```
