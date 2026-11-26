# `ScreenSpaceReflectionComponent` — TypeDefIndex 3535

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `bool` | `k_HighlightSuppression` |
| `0x21` | `bool` | `k_TraceBehindObjects` |
| `0x22` | `bool` | `k_TreatBackfaceHitAsMiss` |
| `0x23` | `bool` | `k_BilateralUpsample` |
| `0x28` | `int[]` | `m_ReflectionTextures` |

## `ScreenSpaceReflectionComponent.GetCameraFlags` — RVA `0xcd7c2c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint ScreenSpaceReflectionComponent_GetCameraFlags_RVAcd7c2c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `ScreenSpaceReflectionComponent.get_active` — RVA `0xcd7c34`

- Lift status: **exact**; input span: 124 bytes; span to next metadata RVA: 124 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static uint ScreenSpaceReflectionComponent_get_active_RVAcd7c34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13466768 = default(uint);
        uint __arm64_flags_right_13466768 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5F0UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7C60;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2C8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5F0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD7C60;
        label_0xCD7C60:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD7CAC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD7C9C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD7CAC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE49CUL /* metadata target: PostProcessingContext.get_isGBufferAvailable */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD7C9C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD7CAC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13466768 = unchecked((uint)(x8));
        __arm64_flags_right_13466768 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13466768) - (__arm64_flags_right_13466768))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCD7CA0;
        label_0xCD7C9C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCD7CA0;
        label_0xCD7CA0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCD7CAC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `ScreenSpaceReflectionComponent.OnEnable` — RVA `0xcd7cb0`

- Lift status: **exact**; input span: 328 bytes; span to next metadata RVA: 328 bytes.
- Metadata signature: `public override void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=46 (informational only).

```csharp
public static ulong ScreenSpaceReflectionComponent_OnEnable_RVAcd7cb0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13466964 = default(uint);
        uint __arm64_flags_left_13467008 = default(uint);
        uint __arm64_flags_left_13467052 = default(uint);
        uint __arm64_flags_left_13467096 = default(uint);
        uint __arm64_flags_right_13466964 = default(uint);
        uint __arm64_flags_right_13467008 = default(uint);
        uint __arm64_flags_right_13467052 = default(uint);
        uint __arm64_flags_right_13467096 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5F1UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x2D0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7D14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2D8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5F1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD7D14;
        label_0xCD7D14:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCD7DF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD7DF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2E8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x20UL))), unchecked((uint)(x0)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCD7DF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13466964 = unchecked((uint)(x8));
        __arm64_flags_right_13466964 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13466964 >= __arm64_flags_right_13466964))) || (unchecked((uint)((__arm64_flags_left_13466964) - (__arm64_flags_right_13466964))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCD7DF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x24UL))), unchecked((uint)(x0)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCD7DF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13467008 = unchecked((uint)(x8));
        __arm64_flags_right_13467008 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13467008 >= __arm64_flags_right_13467008))) || (unchecked((uint)((__arm64_flags_left_13467008) - (__arm64_flags_right_13467008))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCD7DF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x28UL))), unchecked((uint)(x0)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCD7DF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13467052 = unchecked((uint)(x8));
        __arm64_flags_right_13467052 = unchecked((uint)0x3UL);
        if (((!((__arm64_flags_left_13467052 >= __arm64_flags_right_13467052))) || (unchecked((uint)((__arm64_flags_left_13467052) - (__arm64_flags_right_13467052))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCD7DF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2E0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x2CUL))), unchecked((uint)(x0)));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177A220UL /* metadata target: Shader.PropertyToID */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCD7DF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        __arm64_flags_left_13467096 = unchecked((uint)(x8));
        __arm64_flags_right_13467096 = unchecked((uint)0x4UL);
        if (((!((__arm64_flags_left_13467096 >= __arm64_flags_right_13467096))) || (unchecked((uint)((__arm64_flags_left_13467096) - (__arm64_flags_right_13467096))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCD7DF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7DE0UL);
        }
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x30UL))), unchecked((uint)(x0)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCD7DF0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCD7DF4;
        label_0xCD7DF4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `ScreenSpaceReflectionComponent.GetName` — RVA `0xcd7df8`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public override string GetName() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong ScreenSpaceReflectionComponent_GetName_RVAcd7df8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x5F2UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x2F8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x5F2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD7E28:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `ScreenSpaceReflectionComponent.GetCameraEvent` — RVA `0xcd7e38`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint ScreenSpaceReflectionComponent_GetCameraEvent_RVAcd7e38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `ScreenSpaceReflectionComponent.PopulateCommandBuffer` — RVA `0xcd7e40`

- Lift status: **partial**; input span: 4100 bytes; span to next metadata RVA: 4100 bytes.
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=564 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cinc' at 0xcd7f34; reason: Unknown IR expression at 0xcd7f34; reason: Unsupported instruction 'cset' at 0xcd80ec; reason: Unknown IR expression at 0xcd80ec; reason: Unsupported instruction 'b.ne' at 0xcd83b4; reason: Unknown IR expression at 0xcd83b4

```csharp
public static ulong ScreenSpaceReflectionComponent_PopulateCommandBuffer_RVAcd7e40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13467428 = default(uint);
        uint __arm64_flags_left_13467636 = default(uint);
        uint __arm64_flags_left_13467864 = default(uint);
        uint __arm64_flags_left_13469524 = default(uint);
        ulong __arm64_flags_left_13469680 = default(ulong);
        ulong __arm64_flags_left_13469732 = default(ulong);
        ulong __arm64_flags_left_13470312 = default(ulong);
        ulong __arm64_flags_left_13470328 = default(ulong);
        ulong __arm64_flags_left_13470644 = default(ulong);
        uint __arm64_flags_result_13469524 = default(uint);
        uint __arm64_flags_right_13467428 = default(uint);
        uint __arm64_flags_right_13467636 = default(uint);
        uint __arm64_flags_right_13467864 = default(uint);
        uint __arm64_flags_right_13469524 = default(uint);
        ulong __arm64_flags_right_13469680 = default(ulong);
        ulong __arm64_flags_right_13469732 = default(ulong);
        ulong __arm64_flags_right_13470312 = default(ulong);
        ulong __arm64_flags_right_13470328 = default(ulong);
        ulong __arm64_flags_right_13470644 = default(ulong);
        float __arm64_float_flags_left_13468588 = default(float);
        float __arm64_float_flags_right_13468588 = default(float);
        ulong __arm64_pair_address_13467200 = default(ulong);
        ulong __arm64_pair_address_13467204 = default(ulong);
        ulong __arm64_pair_address_13467208 = default(ulong);
        ulong __arm64_pair_address_13467212 = default(ulong);
        ulong __arm64_pair_address_13467400 = default(ulong);
        ulong __arm64_pair_address_13467408 = default(ulong);
        ulong __arm64_pair_address_13467416 = default(ulong);
        ulong __arm64_pair_address_13468820 = default(ulong);
        ulong __arm64_pair_address_13469920 = default(ulong);
        ulong __arm64_pair_address_13469928 = default(ulong);
        ulong __arm64_pair_address_13469960 = default(ulong);
        ulong __arm64_pair_address_13469992 = default(ulong);
        ulong __arm64_pair_address_13470036 = default(ulong);
        ulong __arm64_pair_address_13470044 = default(ulong);
        ulong __arm64_pair_address_13470076 = default(ulong);
        ulong __arm64_pair_address_13470096 = default(ulong);
        ulong __arm64_pair_address_13470104 = default(ulong);
        ulong __arm64_pair_address_13470112 = default(ulong);
        ulong __arm64_pair_address_13470144 = default(ulong);
        ulong __arm64_pair_address_13470152 = default(ulong);
        ulong __arm64_pair_address_13470184 = default(ulong);
        ulong __arm64_pair_address_13470192 = default(ulong);
        ulong __arm64_pair_address_13470232 = default(ulong);
        ulong __arm64_pair_address_13470240 = default(ulong);
        ulong __arm64_pair_address_13470272 = default(ulong);
        ulong __arm64_pair_address_13470280 = default(ulong);
        ulong __arm64_pair_address_13470572 = default(ulong);
        ulong __arm64_pair_address_13470580 = default(ulong);
        ulong __arm64_pair_address_13470680 = default(ulong);
        ulong __arm64_pair_address_13470712 = default(ulong);
        ulong __arm64_pair_address_13470756 = default(ulong);
        ulong __arm64_pair_address_13470764 = default(ulong);
        ulong __arm64_pair_address_13470924 = default(ulong);
        ulong __arm64_pair_address_13470932 = default(ulong);
        ulong __arm64_pair_address_13471036 = default(ulong);
        ulong __arm64_pair_address_13471068 = default(ulong);
        ulong __arm64_pair_address_13471112 = default(ulong);
        ulong __arm64_pair_address_13471120 = default(ulong);
        ulong __arm64_pair_address_13471152 = default(ulong);
        ulong __arm64_pair_address_13471172 = default(ulong);
        ulong __arm64_pair_address_13471180 = default(ulong);
        ulong __arm64_pair_address_13471188 = default(ulong);
        ulong __arm64_pair_address_13471212 = default(ulong);
        ulong __arm64_pair_address_13471220 = default(ulong);
        ulong __arm64_pair_address_13471276 = default(ulong);
        ulong __arm64_pair_address_13471280 = default(ulong);
        ulong __arm64_pair_address_13471284 = default(ulong);
        ulong __arm64_pair_address_13471288 = default(ulong);
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
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
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
        __arm64_pair_address_13467200 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13467200, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13467200) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_13467200;
        __arm64_pair_address_13467204 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13467204, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13467204) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13467208 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13467208, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13467208) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13467212 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13467212, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13467212) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x6D0UL)));
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5F3UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7EAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x300UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x308UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5F3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD7EAC;
        label_0xCD7EAC:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6C0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6C0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6B0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6B0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6A0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6A0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x690UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x690UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x680UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x680UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x670UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x670UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x660UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x660UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x650UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x650UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x640UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x640UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x630UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x630UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x620UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x620UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x610UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x610UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x600UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x600UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5F0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5F0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5E0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5E0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5D0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5D0UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7F00UL);
        }
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x1CUL))))), 0));
        x26 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x28 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x20UL)))) + (0x4UL))))));
        __arm64_pair_address_13467400 = unchecked((ulong)((x8) + (0x28UL)));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13467400)), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13467400) + (0x4UL))))), 0));
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x30UL))))));
        __arm64_pair_address_13467408 = unchecked((ulong)((x8) + (0x34UL)));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13467408)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13467408) + (0x4UL))))), 0));
        x29 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x23 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x14UL)))) + (0x4UL))))));
        __arm64_pair_address_13467416 = unchecked((ulong)((x8) + (0x3CUL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13467416)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13467416) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x44UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        __arm64_flags_left_13467428 = unchecked((uint)(x23));
        __arm64_flags_right_13467428 = unchecked((uint)0x0UL);
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x8);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("cinc", 0xCD7F34UL);
        x21 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD7F5CUL);
        }
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x2CUL))), unchecked((uint)(x0)));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x24UL)))) + (0x0UL))), unchecked((uint)(x22)));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x24UL)))) + (0x4UL))), unchecked((uint)(x21)));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x308UL))));
        x21 = 0x1A8F000UL;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x300UL))));
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD7FD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD7FD0;
        label_0xCD7FD0:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        x2 = unchecked((ulong)(unchecked((uint)(x28))));
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x21);
        __arm64_flags_left_13467636 = unchecked((uint)(x29));
        __arm64_flags_right_13467636 = unchecked((uint)0x1UL);
        x2 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13467636) - (__arm64_flags_right_13467636))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = x22;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD8024;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD801CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD8024;
        label_0xCD8024:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x23UL))))))));
        x0 = x22;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD8050;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD8048UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD8050;
        label_0xCD8050:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x22UL))))))));
        x0 = x22;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD807C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD8074UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD807C;
        label_0xCD807C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) & (unchecked((uint)(0x1UL)))))));
        x0 = x22;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD80A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD80A0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD80A8;
        label_0xCD80A8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x21UL))))))));
        x0 = x22;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD80D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD80CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD80D4;
        label_0xCD80D4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        __arm64_flags_left_13467864 = unchecked((uint)(x23));
        __arm64_flags_right_13467864 = unchecked((uint)0x0UL);
        x0 = x22;
        x2 = unchecked((ulong)(unchecked((uint)(x26))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x3 = 0x0UL;
        RuntimeCalls.Unsupported("cset", 0xCD80ECUL);
        x28 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x1CUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        x2 = unchecked((ulong)(unchecked((uint)(x28))));
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD8140;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD8138UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD8140;
        label_0xCD8140:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x20UL))))))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x0 = x22;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x24UL))))));
        x3 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x177B644UL /* metadata target: Material.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x28 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD8164UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x27))))))), 0));
        x0 = x28;
        x1 = 0x0UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x25))))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x176E71CUL /* metadata target: Camera.get_fieldOfView */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x300UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x19B0D00UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x3CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD81C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD81BCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD81C4;
        label_0xCD81C4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x2CUL))))));
        x0 = x22;
        v0 = v9;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x28UL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        v0 = v10;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x2CUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        v0 = v15;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x30UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        v0 = v14;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x34UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        v0 = v13;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x38UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        v0 = v12;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x3CUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        v0 = v11;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x40UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x22;
        v0 = v8;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x44UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x20UL))))), 0));
        x0 = x22;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x48UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x28;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F148UL /* metadata target: Camera.get_projectionMatrix */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x690UL)));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x690UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x690UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6A0UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6A0UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6B0UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6B0UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6C0UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6C0UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x690UL)));
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x2 = 0x0UL;
        v10 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x690UL)));
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x2 = 0x0UL;
        v11 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x690UL)));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        v12 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x690UL)));
        x1 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x2 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x1CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x690UL)));
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x2 = 0x0UL;
        v13 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17868A4UL /* metadata target: Matrix4x4.get_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x18UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x3CUL))))), 0));
        x0 = x28;
        x1 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x14UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x38UL))))), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
        x0 = x28;
        x1 = 0x0UL;
        v10 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        __arm64_float_flags_left_13468588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13468588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v14 = v0;
        RuntimeCalls.Unsupported("b.ne", 0xCD83B4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD83C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD83B8UL);
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        goto label_0xCD8410;
        label_0xCD83C4:
        ;
        x0 = x28;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
        x0 = x28;
        x1 = 0x0UL;
        v10 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
        x0 = x28;
        x1 = 0x0UL;
        v12 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
        x0 = x28;
        x1 = 0x0UL;
        v13 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
        v11 = v0;
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0));
        goto label_0xCD8410;
        label_0xCD8410:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x3CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x24UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x24UL)))) + (0x4UL))))));
        x0 = RuntimeMemory.ReadU64(x21);
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x38UL))))), 0));
        x23 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) / (unchecked((int)(unchecked((uint)(x8)))))))))));
        x24 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x24))))) / (unchecked((int)(unchecked((uint)(x8)))))))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x14UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0000000UL)), 0)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x1CUL))))), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x18UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x28UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD846C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD8464UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD846C;
        label_0xCD846C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x23))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x24))))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4CUL))))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        __arm64_pair_address_13468820 = unchecked((ulong)((sp) + (0x38UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13468820)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13468820) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x22;
        v0 = v8;
        v1 = v9;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x50UL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x22;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x54UL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x28UL))))), 0));
        x0 = x22;
        v0 = v10;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v1 = v13;
        v2 = v15;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x58UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x2CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x20UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x22;
        v2 = v11;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x5CUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x680UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x680UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x670UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x670UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x660UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x660UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x650UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x650UL))), v0);
#endif
        x0 = unchecked((ulong)((sp) + (0x650UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v0 = v14;
        v3 = v14;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1787104UL /* metadata target: Matrix4x4.SetRow */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x650UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v1 = v12;
        v3 = v12;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1787104UL /* metadata target: Matrix4x4.SetRow */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x650UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x2 = 0x0UL;
        x26 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0x1787104UL /* metadata target: Matrix4x4.SetRow */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x650UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1787104UL /* metadata target: Matrix4x4.SetRow */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x650UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x650UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x660UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x660UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x670UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x670UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x680UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x680UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x550UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x550UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x560UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x560UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x690UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x690UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6A0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x6A0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x570UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x570UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x580UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x580UL))), v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6B0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x6B0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x6C0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x6C0UL))));
#endif
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = unchecked((ulong)((sp) + (0x550UL)));
        x1 = unchecked((ulong)((sp) + (0x510UL)));
        x2 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x510UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x510UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x520UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x520UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x530UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x530UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x540UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x540UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1786E8CUL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
        x8 = RuntimeMemory.ReadU64(x21);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x640UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x640UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x630UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x630UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x620UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x620UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x610UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x610UL))), v3);
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = unchecked((ulong)((sp) + (0x4D0UL)));
        x0 = x22;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x60UL))))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4D0UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4D0UL))), v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4E0UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4E0UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4F0UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4F0UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x500UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x500UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x177B888UL /* metadata target: Material.SetMatrix */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x28;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x25 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x64UL))))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x176F010UL /* metadata target: Camera.get_worldToCameraMatrix */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#endif
        x2 = unchecked((ulong)((sp) + (0x490UL)));
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x25))));
        x3 = 0x0UL;
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
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4B0UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4B0UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x4C0UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x4C0UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x177B888UL /* metadata target: Material.SetMatrix */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x28;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x25 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x68UL))))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x176F010UL /* metadata target: Camera.get_worldToCameraMatrix */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#endif
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = unchecked((ulong)((sp) + (0x5D0UL)));
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5D0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5D0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5E0UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5E0UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5F0UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5F0UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x600UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x600UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17864E0UL /* metadata target: Matrix4x4.get_inverse */, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x5B0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x5C0UL))));
#endif
        x2 = unchecked((ulong)((sp) + (0x450UL)));
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x25))));
        x3 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x450UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x450UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x460UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x470UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x480UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x480UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x177B888UL /* metadata target: Material.SetMatrix */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4C4UL /* metadata target: PostProcessingContext.get_isHdr */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        __arm64_flags_left_13469524 = unchecked((uint)(x0));
        __arm64_flags_right_13469524 = unchecked((uint)0x1UL);
        __arm64_flags_result_13469524 = unchecked((uint)((__arm64_flags_left_13469524) & (__arm64_flags_right_13469524)));
        x26 = unchecked((ulong)(((!((__arm64_flags_result_13469524 == unchecked((uint)0x0UL)))) ? unchecked((uint)(x26)) : unchecked((uint)0x0UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD8770;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD8770;
        label_0xCD8770:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        x3 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x25 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x74UL))))));
        x29 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x74UL)))) + (0x4UL))))));
        x28 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x7CUL))))));
        x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x7CUL)))) + (0x4UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x84UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x84UL)))) + (0x4UL))))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x25))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x3CUL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x2CUL))), unchecked((uint)(x8)));
        RuntimeMemory.WritePtr(sp, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x6 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x29))));
        x2 = unchecked((ulong)(unchecked((uint)(x23))));
        x3 = unchecked((ulong)(unchecked((uint)(x24))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WritePtr(sp, 0x0UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x38UL))), unchecked((uint)(x29)));
        x0 = RuntimeCalls.InvokeDirect(0x17A71E0UL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x29 = 0x0UL;
        goto label_0xCD87E4;
        label_0xCD87E4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13469680 = x29;
        __arm64_flags_right_13469680 = x9;
        if ((__arm64_flags_left_13469680 >= __arm64_flags_right_13469680))
        {
            goto label_0xCD8E40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x29) << (int)(unchecked((int)(0x2UL))))))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x23))))) >> (int)(unchecked((int)(unchecked((uint)(x29)))))))))));
        x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x24))))) >> (int)(unchecked((int)(unchecked((uint)(x29)))))))))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)(x26))));
        x7 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x29 = unchecked((ulong)((x29) + (0x1UL)));
        __arm64_flags_left_13469732 = x29;
        __arm64_flags_right_13469732 = 0x5UL;
        if ((!((unchecked((ulong)((__arm64_flags_left_13469732) - (__arm64_flags_right_13469732))) == 0x0UL))))
        {
            goto label_0xCD87E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x23UL))))))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x27))));
        x2 = unchecked((ulong)(unchecked((uint)(x23))));
        x5 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) ^ (unchecked((uint)(0x1UL)))))));
        x3 = unchecked((ulong)(unchecked((uint)(x24))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)(x26))));
        x7 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x3CUL))))));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x23))));
        x3 = unchecked((ulong)(unchecked((uint)(x24))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)(x26))));
        x7 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)((sp) + (0x420UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x25))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x5B0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x420UL)));
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x590UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x590UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5A0UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5A0UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x5B0UL))));
        x1 = unchecked((ulong)((sp) + (0x3F0UL)));
        x2 = unchecked((ulong)((sp) + (0x3C0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = x19;
        x3 = x22;
        x5 = 0x0UL;
        __arm64_pair_address_13469920 = unchecked((ulong)((sp) + (0x3C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13469920, v0);
#else
        __WriteVector128(__arm64_pair_address_13469920, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13469920) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13469920) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3E0UL))), x8);
        __arm64_pair_address_13469928 = unchecked((ulong)((sp) + (0x3F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13469928, v2);
#else
        __WriteVector128(__arm64_pair_address_13469928, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13469928) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13469928) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x410UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = unchecked((ulong)((sp) + (0x390UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
        __arm64_pair_address_13469960 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13469960);
#else
        v0 = __ReadVector128(__arm64_pair_address_13469960);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13469960) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13469960) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x38UL))))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x440UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13469992 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13469992);
#else
        v0 = __ReadVector128(__arm64_pair_address_13469992);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13469992) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13469992) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
        x1 = unchecked((ulong)((sp) + (0x360UL)));
        x2 = unchecked((ulong)((sp) + (0x330UL)));
        x0 = x19;
        x3 = x22;
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = 0x0UL;
        __arm64_pair_address_13470036 = unchecked((ulong)((sp) + (0x330UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470036, v0);
#else
        __WriteVector128(__arm64_pair_address_13470036, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470036) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470036) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x350UL))), x8);
        __arm64_pair_address_13470044 = unchecked((ulong)((sp) + (0x360UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470044, v2);
#else
        __WriteVector128(__arm64_pair_address_13470044, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470044) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470044) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x380UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = unchecked((ulong)((sp) + (0x300UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x320UL))));
        __arm64_pair_address_13470076 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470076);
#else
        v0 = __ReadVector128(__arm64_pair_address_13470076);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470076) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470076) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x27))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3B0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x300UL)));
        __arm64_pair_address_13470096 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470096, v0);
#else
        __WriteVector128(__arm64_pair_address_13470096, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470096) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470096) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13470104 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470104);
#else
        v0 = __ReadVector128(__arm64_pair_address_13470104);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470104) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470104) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x320UL))));
        __arm64_pair_address_13470112 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470112);
#else
        v2 = __ReadVector128(__arm64_pair_address_13470112);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470112) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470112) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
        x1 = unchecked((ulong)((sp) + (0x2D0UL)));
        x2 = unchecked((ulong)((sp) + (0x2A0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = x19;
        x3 = x22;
        x5 = 0x0UL;
        __arm64_pair_address_13470144 = unchecked((ulong)((sp) + (0x2A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470144, v0);
#else
        __WriteVector128(__arm64_pair_address_13470144, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470144) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470144) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2C0UL))), x8);
        __arm64_pair_address_13470152 = unchecked((ulong)((sp) + (0x2D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470152, v2);
#else
        __WriteVector128(__arm64_pair_address_13470152, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470152) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470152) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2F0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = unchecked((ulong)((sp) + (0x278UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x27))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x25 = unchecked((ulong)((sp) + (0x278UL)));
        __arm64_pair_address_13470184 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470184);
#else
        v0 = __ReadVector128(__arm64_pair_address_13470184);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470184) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470184) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x298UL))));
        __arm64_pair_address_13470192 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470192, v0);
#else
        __WriteVector128(__arm64_pair_address_13470192, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470192) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470192) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x320UL))), x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD8E40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x8 = unchecked((ulong)((sp) + (0x278UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13470232 = x25;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470232);
#else
        v0 = __ReadVector128(__arm64_pair_address_13470232);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470232) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470232) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x298UL))));
        __arm64_pair_address_13470240 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470240);
#else
        v2 = __ReadVector128(__arm64_pair_address_13470240);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470240) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470240) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x320UL))));
        x1 = unchecked((ulong)((sp) + (0x250UL)));
        x2 = unchecked((ulong)((sp) + (0x220UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = x19;
        x3 = x22;
        x5 = 0x0UL;
        __arm64_pair_address_13470272 = unchecked((ulong)((sp) + (0x220UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470272, v0);
#else
        __WriteVector128(__arm64_pair_address_13470272, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470272) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470272) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x240UL))), x8);
        __arm64_pair_address_13470280 = unchecked((ulong)((sp) + (0x250UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470280, v2);
#else
        __WriteVector128(__arm64_pair_address_13470280, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470280) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470280) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x270UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = 0x0UL;
        x29 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        goto label_0xCD8A68;
        label_0xCD8A68:
        ;
        __arm64_flags_left_13470312 = x27;
        __arm64_flags_right_13470312 = 0x10UL;
        if ((unchecked((ulong)((__arm64_flags_left_13470312) - (__arm64_flags_right_13470312))) == 0x0UL))
        {
            goto label_0xCD8C5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13470328 = x10;
        __arm64_flags_right_13470328 = x9;
        if ((__arm64_flags_left_13470328 >= __arm64_flags_right_13470328))
        {
            goto label_0xCD8E40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (x27)));
        x25 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x23))))) >> (int)(unchecked((int)(unchecked((uint)(x29)))))))))));
        x3 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x24))))) >> (int)(unchecked((int)(unchecked((uint)(x29)))))))))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x28))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)(x26))));
        x7 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD8AC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD8AB8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCD8AC0;
        label_0xCD8AC0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x6CUL))))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A7438UL /* metadata target: CommandBuffer.SetGlobalVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x21);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x29))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x70UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A73E4UL /* metadata target: CommandBuffer.SetGlobalFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)((sp) + (0x420UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x25))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x28))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x5B0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x420UL)));
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x590UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x590UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5A0UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5A0UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x5B0UL))));
        x1 = unchecked((ulong)((sp) + (0x1F0UL)));
        x2 = unchecked((ulong)((sp) + (0x1C0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x19;
        x3 = x22;
        x5 = 0x0UL;
        __arm64_pair_address_13470572 = unchecked((ulong)((sp) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470572, v0);
#else
        __WriteVector128(__arm64_pair_address_13470572, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470572) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470572) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1E0UL))), x8);
        __arm64_pair_address_13470580 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470580, v2);
#else
        __WriteVector128(__arm64_pair_address_13470580, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470580) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470580) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x210UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x19;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x6CUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x17A7438UL /* metadata target: CommandBuffer.SetGlobalVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD8C58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13470644 = x29;
        __arm64_flags_right_13470644 = x9;
        if ((__arm64_flags_left_13470644 >= __arm64_flags_right_13470644))
        {
            goto label_0xCD8E40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (x27)));
        x25 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x24UL))))));
        x8 = unchecked((ulong)((sp) + (0x390UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x28))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
        __arm64_pair_address_13470680 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470680);
#else
        v0 = __ReadVector128(__arm64_pair_address_13470680);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470680) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470680) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x25))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x440UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13470712 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13470712);
#else
        v0 = __ReadVector128(__arm64_pair_address_13470712);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13470712) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13470712) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
        x1 = unchecked((ulong)((sp) + (0x190UL)));
        x2 = unchecked((ulong)((sp) + (0x160UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x19;
        x3 = x22;
        x5 = 0x0UL;
        __arm64_pair_address_13470756 = unchecked((ulong)((sp) + (0x160UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470756, v0);
#else
        __WriteVector128(__arm64_pair_address_13470756, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470756) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470756) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x180UL))), x8);
        __arm64_pair_address_13470764 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470764, v2);
#else
        __WriteVector128(__arm64_pair_address_13470764, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470764) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470764) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1B0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x28))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x29 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) + (unchecked((uint)(0x1UL)))))));
        x27 = unchecked((ulong)((x27) + (0x4UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xCD8A68;
        }
        else
        {
            goto label_0xCD8C58;
        }
        label_0xCD8C58:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCD8C5C;
        label_0xCD8C5C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD8E40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x8 = unchecked((ulong)((sp) + (0x420UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x3CUL))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x5B0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x420UL)));
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x590UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x590UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x5A0UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x5A0UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x5A0UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x5B0UL))));
        x1 = unchecked((ulong)((sp) + (0x130UL)));
        x2 = unchecked((ulong)((sp) + (0x100UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x19;
        x3 = x22;
        x5 = 0x0UL;
        __arm64_pair_address_13470924 = unchecked((ulong)((sp) + (0x100UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470924, v0);
#else
        __WriteVector128(__arm64_pair_address_13470924, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470924) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470924) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x120UL))), x8);
        __arm64_pair_address_13470932 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13470932, v2);
#else
        __WriteVector128(__arm64_pair_address_13470932, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13470932) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13470932) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x150UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x1 = 0x0UL;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0x176EEDCUL /* metadata target: Camera.get_pixelWidth */, x0, x1, x2, x3);
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176EF18UL /* metadata target: Camera.get_pixelHeight */, x0, x1, x2, x3);
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x2CUL))))));
        x3 = unchecked((ulong)(unchecked((uint)(x0))));
        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)(x26))));
        x7 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)((sp) + (0x390UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
        __arm64_pair_address_13471036 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13471036);
#else
        v0 = __ReadVector128(__arm64_pair_address_13471036);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13471036) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13471036) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x440UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x420UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x430UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13471068 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13471068);
#else
        v0 = __ReadVector128(__arm64_pair_address_13471068);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13471068) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13471068) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x420UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((sp) + (0x430UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x440UL))));
        x1 = unchecked((ulong)((sp) + (0xD0UL)));
        x2 = unchecked((ulong)((sp) + (0xA0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x3 = x22;
        x5 = 0x0UL;
        __arm64_pair_address_13471112 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13471112, v0);
#else
        __WriteVector128(__arm64_pair_address_13471112, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13471112) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13471112) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xC0UL))), x8);
        __arm64_pair_address_13471120 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13471120, v2);
#else
        __WriteVector128(__arm64_pair_address_13471120, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13471120) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13471120) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xF0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x8 = unchecked((ulong)((sp) + (0x300UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x320UL))));
        __arm64_pair_address_13471152 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13471152);
#else
        v0 = __ReadVector128(__arm64_pair_address_13471152);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13471152) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13471152) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3B0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x300UL)));
        __arm64_pair_address_13471172 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13471172, v0);
#else
        __WriteVector128(__arm64_pair_address_13471172, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13471172) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13471172) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13471180 = unchecked((ulong)((sp) + (0x300UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13471180);
#else
        v0 = __ReadVector128(__arm64_pair_address_13471180);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13471180) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13471180) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x320UL))));
        __arm64_pair_address_13471188 = unchecked((ulong)((sp) + (0x390UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13471188);
#else
        v2 = __ReadVector128(__arm64_pair_address_13471188);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13471188) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13471188) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3B0UL))));
        x1 = unchecked((ulong)((sp) + (0x70UL)));
        x2 = unchecked((ulong)((sp) + (0x40UL)));
        x0 = x19;
        x3 = 0x0UL;
        __arm64_pair_address_13471212 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13471212, v0);
#else
        __WriteVector128(__arm64_pair_address_13471212, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13471212) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13471212) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x60UL))), x8);
        __arm64_pair_address_13471220 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13471220, v2);
#else
        __WriteVector128(__arm64_pair_address_13471220, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13471220) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13471220) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x90UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7D84UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        sp = unchecked((ulong)((sp) + (0x6D0UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_13471276 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13471276)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13471276) + (0x8UL))))), 0));
        __arm64_pair_address_13471280 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13471280)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13471280) + (0x8UL))))), 0));
        __arm64_pair_address_13471284 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13471284)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13471284) + (0x8UL))))), 0));
        __arm64_pair_address_13471288 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13471288)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13471288) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13471288) + (0xA0UL)));
        return x0;
        label_0xCD8E40:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `ScreenSpaceReflectionComponent.ctor` — RVA `0xcd8e44`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong ScreenSpaceReflectionComponent_ctor_RVAcd8e44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x22 = 0x1BAB000UL;
        x21 = 0x1A8E000UL;
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x5F4UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xDE8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x310UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD8E90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x310UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x5F4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD8E90;
        label_0xCD8E90:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x21UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x23UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x11689ECUL);
        return default(ulong);
    }
```
