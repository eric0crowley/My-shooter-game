# `MotionBlurComponent` — TypeDefIndex 3532

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `MotionBlurComponent.ReconstructionFilter` | `m_ReconstructionFilter` |
| `0x28` | `MotionBlurComponent.FrameBlendingFilter` | `m_FrameBlendingFilter` |
| `0x30` | `bool` | `m_FirstFrame` |

## `MotionBlurComponent.get_reconstructionFilter` — RVA `0xcd5668`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public MotionBlurComponent.ReconstructionFilter get_reconstructionFilter() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong MotionBlurComponent_get_reconstructionFilter_RVAcd5668(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5E0UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1B8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD5694:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 != 0x0UL))
        {
        }
        else
        {
            x8 = 0x1A8F000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1B8UL))));
            x0 = RuntimeMemory.ReadU64(x8);
            x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
            x20 = x0;
            x0 = RuntimeCalls.InvokeDirect(0xCD56D4UL /* metadata target: MotionBlurComponent.ReconstructionFilter.ctor */, x0, x1, x2, x3);
            x0 = x19;
            x1 = x20;
            RuntimeMemory.WriteU64(x19, x20);
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x0 = RuntimeMemory.ReadU64(x19);
        }
        label_0xCD56C8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `MotionBlurComponent.get_frameBlendingFilter` — RVA `0xcd570c`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public MotionBlurComponent.FrameBlendingFilter get_frameBlendingFilter() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong MotionBlurComponent_get_frameBlendingFilter_RVAcd570c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5E1UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD5738:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 != 0x0UL))
        {
        }
        else
        {
            x8 = 0x1A8F000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1C0UL))));
            x0 = RuntimeMemory.ReadU64(x8);
            x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
            x20 = x0;
            x0 = RuntimeCalls.InvokeDirect(0xCD5778UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.ctor */, x0, x1, x2, x3);
            x0 = x19;
            x1 = x20;
            RuntimeMemory.WriteU64(x19, x20);
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x0 = RuntimeMemory.ReadU64(x19);
        }
        label_0xCD576C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `MotionBlurComponent.get_active` — RVA `0xcd57f0`

- Lift status: **exact**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static uint MotionBlurComponent_get_active_RVAcd57f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13457524 = default(uint);
        uint __arm64_flags_left_13457564 = default(uint);
        uint __arm64_flags_right_13457524 = default(uint);
        uint __arm64_flags_right_13457564 = default(uint);
        float __arm64_float_flags_left_13457464 = default(float);
        float __arm64_float_flags_left_13457492 = default(float);
        float __arm64_float_flags_left_13457508 = default(float);
        float __arm64_float_flags_right_13457464 = default(float);
        float __arm64_float_flags_right_13457492 = default(float);
        float __arm64_float_flags_right_13457508 = default(float);
        ulong __arm64_load_address_13457544 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5E2UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD5820;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1D0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5E2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD5820;
        label_0xCD5820:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD58A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD587C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCD5830UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x1CUL))))), 0));
        __arm64_float_flags_left_13457464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13457464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13457464 <= __arm64_float_flags_right_13457464) || ((__arm64_float_flags_left_13457464 != __arm64_float_flags_left_13457464) || (__arm64_float_flags_right_13457464 != __arm64_float_flags_right_13457464))))
        {
            goto label_0xCD5864;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCD5668UL /* metadata target: MotionBlurComponent.get_reconstructionFilter */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD58A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A814UL /* metadata target: SystemInfo.get_supportsMotionVectors */, x0, x1, x2, x3);
        __arm64_float_flags_left_13457492 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13457492 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13457492 > __arm64_float_flags_right_13457492))
        {
            goto label_0xCD586C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCD585CUL)));
        }
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD587C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCD5860UL)));
        }
        goto label_0xCD586C;
        label_0xCD5864:
        ;
        __arm64_float_flags_left_13457508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13457508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13457508 <= __arm64_float_flags_right_13457508) || ((__arm64_float_flags_left_13457508 != __arm64_float_flags_left_13457508) || (__arm64_float_flags_right_13457508 != __arm64_float_flags_right_13457508))))
        {
            goto label_0xCD587C;
        }
        else
        {
            goto label_0xCD586C;
        }
        label_0xCD586C:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A774UL /* metadata target: SystemInfo.get_graphicsDeviceType */, x0, x1, x2, x3);
        __arm64_flags_left_13457524 = unchecked((uint)(x0));
        __arm64_flags_right_13457524 = unchecked((uint)0x8UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13457524) - (__arm64_flags_right_13457524))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCD5890;
        }
        else
        {
            goto label_0xCD587C;
        }
        label_0xCD587C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCD5880;
        label_0xCD5880:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_13457544 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13457544)), 0));
        return unchecked((uint)(x0));
        label_0xCD5890:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD58A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13457564 = unchecked((uint)(x8));
        __arm64_flags_right_13457564 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13457564) - (__arm64_flags_right_13457564))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCD5880;
        label_0xCD58A8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `MotionBlurComponent.GetName` — RVA `0xcd58b4`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public override string GetName() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong MotionBlurComponent_GetName_RVAcd58b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x5E3UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x1D8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1D8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x5E3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD58E4:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `MotionBlurComponent.ResetHistory` — RVA `0xcd58f4`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void ResetHistory() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong MotionBlurComponent_ResetHistory_RVAcd58f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD5908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5904UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xCD591CUL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Dispose */, x0, x1, x2, x3);
        goto label_0xCD5908;
        label_0xCD5908:
        ;
        RuntimeMemory.WritePtr(x19, 0x0UL);
        x0 = x19;
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `MotionBlurComponent.GetCameraFlags` — RVA `0xcd5990`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint MotionBlurComponent_GetCameraFlags_RVAcd5990(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `MotionBlurComponent.GetCameraEvent` — RVA `0xcd5998`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint MotionBlurComponent_GetCameraEvent_RVAcd5998(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x12UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `MotionBlurComponent.OnEnable` — RVA `0xcd59a0`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public override void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MotionBlurComponent_OnEnable_RVAcd59a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x30UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `MotionBlurComponent.PopulateCommandBuffer` — RVA `0xcd59ac`

- Lift status: **partial**; input span: 1688 bytes; span to next metadata RVA: 1688 bytes.
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=236 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xcd5abc; reason: Unknown IR expression at 0xcd5abc

```csharp
public static ulong MotionBlurComponent_PopulateCommandBuffer_RVAcd59ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13458092 = default(uint);
        uint __arm64_flags_result_13458092 = default(uint);
        uint __arm64_flags_right_13458092 = default(uint);
        float __arm64_float_flags_left_13458228 = default(float);
        float __arm64_float_flags_left_13458236 = default(float);
        float __arm64_float_flags_left_13458652 = default(float);
        float __arm64_float_flags_left_13459000 = default(float);
        float __arm64_float_flags_right_13458228 = default(float);
        float __arm64_float_flags_right_13458236 = default(float);
        float __arm64_float_flags_right_13458652 = default(float);
        float __arm64_float_flags_right_13459000 = default(float);
        ulong __arm64_pair_address_13457836 = default(ulong);
        ulong __arm64_pair_address_13458280 = default(ulong);
        ulong __arm64_pair_address_13458300 = default(ulong);
        ulong __arm64_pair_address_13458308 = default(ulong);
        ulong __arm64_pair_address_13458316 = default(ulong);
        ulong __arm64_pair_address_13458328 = default(ulong);
        ulong __arm64_pair_address_13458336 = default(ulong);
        ulong __arm64_pair_address_13458372 = default(ulong);
        ulong __arm64_pair_address_13458380 = default(ulong);
        ulong __arm64_pair_address_13458424 = default(ulong);
        ulong __arm64_pair_address_13458444 = default(ulong);
        ulong __arm64_pair_address_13458452 = default(ulong);
        ulong __arm64_pair_address_13458460 = default(ulong);
        ulong __arm64_pair_address_13458472 = default(ulong);
        ulong __arm64_pair_address_13458480 = default(ulong);
        ulong __arm64_pair_address_13458488 = default(ulong);
        ulong __arm64_pair_address_13458524 = default(ulong);
        ulong __arm64_pair_address_13458564 = default(ulong);
        ulong __arm64_pair_address_13458572 = default(ulong);
        ulong __arm64_pair_address_13458624 = default(ulong);
        ulong __arm64_pair_address_13458640 = default(ulong);
        ulong __arm64_pair_address_13458704 = default(ulong);
        ulong __arm64_pair_address_13458728 = default(ulong);
        ulong __arm64_pair_address_13458760 = default(ulong);
        ulong __arm64_pair_address_13458780 = default(ulong);
        ulong __arm64_pair_address_13458788 = default(ulong);
        ulong __arm64_pair_address_13458796 = default(ulong);
        ulong __arm64_pair_address_13458828 = default(ulong);
        ulong __arm64_pair_address_13458836 = default(ulong);
        ulong __arm64_pair_address_13458884 = default(ulong);
        ulong __arm64_pair_address_13458904 = default(ulong);
        ulong __arm64_pair_address_13458912 = default(ulong);
        ulong __arm64_pair_address_13458920 = default(ulong);
        ulong __arm64_pair_address_13458932 = default(ulong);
        ulong __arm64_pair_address_13458940 = default(ulong);
        ulong __arm64_pair_address_13458976 = default(ulong);
        ulong __arm64_pair_address_13458984 = default(ulong);
        ulong __arm64_pair_address_13459052 = default(ulong);
        ulong __arm64_pair_address_13459076 = default(ulong);
        ulong __arm64_pair_address_13459108 = default(ulong);
        ulong __arm64_pair_address_13459128 = default(ulong);
        ulong __arm64_pair_address_13459136 = default(ulong);
        ulong __arm64_pair_address_13459144 = default(ulong);
        ulong __arm64_pair_address_13459176 = default(ulong);
        ulong __arm64_pair_address_13459184 = default(ulong);
        ulong __arm64_pair_address_13459228 = default(ulong);
        ulong __arm64_pair_address_13459248 = default(ulong);
        ulong __arm64_pair_address_13459256 = default(ulong);
        ulong __arm64_pair_address_13459264 = default(ulong);
        ulong __arm64_pair_address_13459276 = default(ulong);
        ulong __arm64_pair_address_13459284 = default(ulong);
        ulong __arm64_pair_address_13459292 = default(ulong);
        ulong __arm64_pair_address_13459324 = default(ulong);
        ulong __arm64_pair_address_13459364 = default(ulong);
        ulong __arm64_pair_address_13459372 = default(ulong);
        ulong __arm64_pair_address_13459424 = default(ulong);
        ulong __arm64_pair_address_13459440 = default(ulong);
        ulong __arm64_pair_address_13459512 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
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
        __arm64_pair_address_13457836 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13457836, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13457836) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_13457836;
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
        sp = unchecked((ulong)((sp) - (0x420UL)));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5E4UL))))))));
        x19 = x1;
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD5A18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5E4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD5A18;
        label_0xCD5A18:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x30UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD5A28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5A20UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCD601C;
        label_0xCD5A28:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCB8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x14UL))));
        x28 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x1CUL))))));
        x23 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x410UL))), x27);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x418UL))), unchecked((uint)(x28)));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4C4UL /* metadata target: PostProcessingContext.get_isHdr */, x0, x1, x2, x3);
        x26 = 0x1A8F000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x1E0UL))));
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        __arm64_flags_left_13458092 = unchecked((uint)(x8));
        __arm64_flags_right_13458092 = unchecked((uint)0x1UL);
        __arm64_flags_result_13458092 = unchecked((uint)((__arm64_flags_left_13458092) & (__arm64_flags_right_13458092)));
        x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = RuntimeMemory.ReadU64(x26);
        x10 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        RuntimeCalls.Unsupported("csel", 0xCD5ABCUL);
        x24 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x10)) : unchecked((uint)(x8)))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD5AD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5AC8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        goto label_0xCD5AD0;
        label_0xCD5AD0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x8;
        x1 = 0x0UL;
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x34UL))))));
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = unchecked((ulong)(unchecked((uint)(x25))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x6 = unchecked((ulong)(unchecked((uint)(x24))));
        x7 = 0x0UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x28))), 0)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x27))), 0)), 0));
        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_13458228 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13458228 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13458228 <= __arm64_float_flags_right_13458228) || ((__arm64_float_flags_left_13458228 != __arm64_float_flags_left_13458228) || (__arm64_float_flags_right_13458228 != __arm64_float_flags_right_13458228))))
        {
            goto label_0xCD5CDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5B3CUL);
        }
        __arm64_float_flags_left_13458236 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13458236 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13458236 <= __arm64_float_flags_right_13458236) || ((__arm64_float_flags_left_13458236 != __arm64_float_flags_left_13458236) || (__arm64_float_flags_right_13458236 != __arm64_float_flags_right_13458236))))
        {
            goto label_0xCD5CDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD5668UL /* metadata target: MotionBlurComponent.get_reconstructionFilter */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        x24 = x0;
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        __arm64_pair_address_13458280 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458280);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458280);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458280) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458280) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x400UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x380UL)));
        __arm64_pair_address_13458300 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458300, v0);
#else
        __WriteVector128(__arm64_pair_address_13458300, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458300) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458300) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_pair_address_13458308 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458308);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458308);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458308) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458308) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3A0UL))));
        __arm64_pair_address_13458316 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458316, v0);
#else
        __WriteVector128(__arm64_pair_address_13458316, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458316) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458316) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3D0UL))), x8);
        if ((x24 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5B98UL);
        }
        __arm64_pair_address_13458328 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458328);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458328);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458328) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458328) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x400UL))));
        __arm64_pair_address_13458336 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458336);
#else
        v2 = __ReadVector128(__arm64_pair_address_13458336);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458336) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458336) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        x3 = unchecked((ulong)((sp) + (0x410UL)));
        x4 = unchecked((ulong)((sp) + (0x350UL)));
        x5 = unchecked((ulong)((sp) + (0x320UL)));
        x0 = x24;
        x1 = x23;
        x2 = x19;
        x6 = x20;
        __arm64_pair_address_13458372 = unchecked((ulong)((sp) + (0x350UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458372, v0);
#else
        __WriteVector128(__arm64_pair_address_13458372, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458372) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458372) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x370UL))), x8);
        __arm64_pair_address_13458380 = unchecked((ulong)((sp) + (0x320UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458380, v2);
#else
        __WriteVector128(__arm64_pair_address_13458380, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458380) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458380) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x340UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0xCD6044UL /* metadata target: MotionBlurComponent.ReconstructionFilter.ProcessImage */, x0, x1, x2, x3);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD570CUL /* metadata target: MotionBlurComponent.get_frameBlendingFilter */, x0, x1, x2, x3);
        x23 = x0;
        x8 = unchecked((ulong)((sp) + (0x2F0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x310UL))));
        __arm64_pair_address_13458424 = unchecked((ulong)((sp) + (0x2F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458424);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458424);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458424) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458424) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3A0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x2C0UL)));
        __arm64_pair_address_13458444 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458444, v0);
#else
        __WriteVector128(__arm64_pair_address_13458444, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458444) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458444) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13458452 = unchecked((ulong)((sp) + (0x2C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458452);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458452);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458452) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458452) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x2E0UL))));
        __arm64_pair_address_13458460 = unchecked((ulong)((sp) + (0x2F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458460, v0);
#else
        __WriteVector128(__arm64_pair_address_13458460, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458460) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458460) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x310UL))), x8);
        if ((x23 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5C28UL);
        }
        __arm64_pair_address_13458472 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458472);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458472);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458472) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458472) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3A0UL))));
        __arm64_pair_address_13458480 = unchecked((ulong)((sp) + (0x2F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458480);
#else
        v2 = __ReadVector128(__arm64_pair_address_13458480);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458480) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458480) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x310UL))));
        __arm64_pair_address_13458488 = unchecked((ulong)((sp) + (0x290UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458488, v0);
#else
        __WriteVector128(__arm64_pair_address_13458488, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458488) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458488) + (0x10UL))), v1);
#endif
        x2 = unchecked((ulong)((sp) + (0x290UL)));
        x3 = unchecked((ulong)((sp) + (0x260UL)));
        x0 = x23;
        x1 = x19;
        v0 = v8;
        x4 = x20;
        x24 = unchecked((ulong)((sp) + (0x238UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2B0UL))), x8);
        __arm64_pair_address_13458524 = unchecked((ulong)((sp) + (0x260UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458524, v2);
#else
        __WriteVector128(__arm64_pair_address_13458524, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458524) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458524) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x280UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0xCD6954UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.BlendFrames */, x0, x1, x2, x3);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD570CUL /* metadata target: MotionBlurComponent.get_frameBlendingFilter */, x0, x1, x2, x3);
        x23 = x0;
        x8 = unchecked((ulong)((sp) + (0x238UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13458564 = x24;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458564);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458564);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458564) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458564) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x258UL))));
        __arm64_pair_address_13458572 = unchecked((ulong)((sp) + (0x2C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458572, v0);
#else
        __WriteVector128(__arm64_pair_address_13458572, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458572) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458572) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x2E0UL))), x8);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5CC0UL);
        }
        __arm64_pair_address_13458624 = unchecked((ulong)((sp) + (0x2C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458624);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458624);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458624) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458624) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x2E0UL))));
        x4 = unchecked((ulong)(unchecked((uint)(x0))));
        x2 = unchecked((ulong)((sp) + (0x210UL)));
        __arm64_pair_address_13458640 = unchecked((ulong)((sp) + (0x210UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458640, v0);
#else
        __WriteVector128(__arm64_pair_address_13458640, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458640) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458640) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x230UL))), x8);
        goto label_0xCD5FF8;
        label_0xCD5CDC:
        ;
        __arm64_float_flags_left_13458652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13458652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13458652 <= __arm64_float_flags_right_13458652) || ((__arm64_float_flags_left_13458652 != __arm64_float_flags_left_13458652) || (__arm64_float_flags_right_13458652 != __arm64_float_flags_right_13458652))))
        {
            goto label_0xCD5E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD5CF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5CF0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        goto label_0xCD5CF8;
        label_0xCD5CF8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        x8 = unchecked((ulong)((sp) + (0x3E0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13458704 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458704);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458704);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458704) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458704) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x400UL))));
        x2 = unchecked((ulong)((sp) + (0x1E0UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x3 = 0x0UL;
        __arm64_pair_address_13458728 = unchecked((ulong)((sp) + (0x1E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458728, v0);
#else
        __WriteVector128(__arm64_pair_address_13458728, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458728) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458728) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x200UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        __arm64_pair_address_13458760 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458760);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458760);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458760) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458760) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x400UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        __arm64_pair_address_13458780 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458780, v0);
#else
        __WriteVector128(__arm64_pair_address_13458780, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458780) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458780) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13458788 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458788);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458788);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458788) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458788) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        __arm64_pair_address_13458796 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458796);
#else
        v2 = __ReadVector128(__arm64_pair_address_13458796);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458796) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458796) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x400UL))));
        x1 = unchecked((ulong)((sp) + (0x1B0UL)));
        x2 = unchecked((ulong)((sp) + (0x180UL)));
        x0 = x19;
        x3 = x23;
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = 0x0UL;
        __arm64_pair_address_13458828 = unchecked((ulong)((sp) + (0x180UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458828, v0);
#else
        __WriteVector128(__arm64_pair_address_13458828, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458828) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458828) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1A0UL))), x8);
        __arm64_pair_address_13458836 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458836, v2);
#else
        __WriteVector128(__arm64_pair_address_13458836, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458836) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458836) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1D0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(x22))));
        x0 = RuntimeCalls.InvokeDirect(0xCD5668UL /* metadata target: MotionBlurComponent.get_reconstructionFilter */, x0, x1, x2, x3);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x22))))) + (0x10UL))));
        x23 = x0;
        x8 = unchecked((ulong)((sp) + (0x380UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3A0UL))));
        __arm64_pair_address_13458884 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458884);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458884);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458884) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458884) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3D0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x2F0UL)));
        __arm64_pair_address_13458904 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458904, v0);
#else
        __WriteVector128(__arm64_pair_address_13458904, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458904) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458904) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13458912 = unchecked((ulong)((sp) + (0x2F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458912);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458912);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458912) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458912) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x310UL))));
        __arm64_pair_address_13458920 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458920, v0);
#else
        __WriteVector128(__arm64_pair_address_13458920, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458920) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458920) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3A0UL))), x8);
        if ((x23 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5DF4UL);
        }
        __arm64_pair_address_13458932 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458932);
#else
        v0 = __ReadVector128(__arm64_pair_address_13458932);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458932) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458932) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        __arm64_pair_address_13458940 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13458940);
#else
        v2 = __ReadVector128(__arm64_pair_address_13458940);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13458940) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13458940) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3A0UL))));
        x3 = unchecked((ulong)((sp) + (0x410UL)));
        x4 = unchecked((ulong)((sp) + (0x150UL)));
        x5 = unchecked((ulong)((sp) + (0x120UL)));
        x0 = x23;
        x1 = x22;
        x2 = x19;
        x6 = x20;
        __arm64_pair_address_13458976 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458976, v0);
#else
        __WriteVector128(__arm64_pair_address_13458976, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458976) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458976) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x170UL))), x8);
        __arm64_pair_address_13458984 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13458984, v2);
#else
        __WriteVector128(__arm64_pair_address_13458984, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13458984) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13458984) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x140UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0xCD6044UL /* metadata target: MotionBlurComponent.ReconstructionFilter.ProcessImage */, x0, x1, x2, x3);
        goto label_0xCD600C;
        label_0xCD5E38:
        ;
        __arm64_float_flags_left_13459000 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13459000 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13459000 <= __arm64_float_flags_right_13459000) || ((__arm64_float_flags_left_13459000 != __arm64_float_flags_left_13459000) || (__arm64_float_flags_right_13459000 != __arm64_float_flags_right_13459000))))
        {
            goto label_0xCD600C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD5E54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5E4CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x26);
        goto label_0xCD5E54;
        label_0xCD5E54:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x24 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        x8 = unchecked((ulong)((sp) + (0x3E0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13459052 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459052);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459052);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459052) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459052) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x400UL))));
        x2 = unchecked((ulong)((sp) + (0xF0UL)));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x24))));
        x3 = 0x0UL;
        __arm64_pair_address_13459076 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459076, v0);
#else
        __WriteVector128(__arm64_pair_address_13459076, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459076) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459076) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x110UL))), x8);
        x0 = RuntimeCalls.InvokeDirect(0x17A7EACUL /* metadata target: CommandBuffer.SetGlobalTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        __arm64_pair_address_13459108 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459108);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459108);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459108) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459108) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x400UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        __arm64_pair_address_13459128 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459128, v0);
#else
        __WriteVector128(__arm64_pair_address_13459128, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459128) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459128) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13459136 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459136);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459136);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459136) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459136) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        __arm64_pair_address_13459144 = unchecked((ulong)((sp) + (0x3E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459144);
#else
        v2 = __ReadVector128(__arm64_pair_address_13459144);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459144) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459144) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x400UL))));
        x1 = unchecked((ulong)((sp) + (0xC0UL)));
        x2 = unchecked((ulong)((sp) + (0x90UL)));
        x0 = x19;
        x3 = x23;
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = 0x0UL;
        __arm64_pair_address_13459176 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459176, v0);
#else
        __WriteVector128(__arm64_pair_address_13459176, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459176) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459176) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xB0UL))), x8);
        __arm64_pair_address_13459184 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459184, v2);
#else
        __WriteVector128(__arm64_pair_address_13459184, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459184) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459184) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xE0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD570CUL /* metadata target: MotionBlurComponent.get_frameBlendingFilter */, x0, x1, x2, x3);
        x23 = x0;
        x8 = unchecked((ulong)((sp) + (0x380UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3A0UL))));
        __arm64_pair_address_13459228 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459228);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459228);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459228) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459228) + (0x10UL))));
#endif
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3D0UL))), x8);
        x8 = unchecked((ulong)((sp) + (0x2F0UL)));
        __arm64_pair_address_13459248 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459248, v0);
#else
        __WriteVector128(__arm64_pair_address_13459248, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459248) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459248) + (0x10UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13459256 = unchecked((ulong)((sp) + (0x2F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459256);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459256);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459256) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459256) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x310UL))));
        __arm64_pair_address_13459264 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459264, v0);
#else
        __WriteVector128(__arm64_pair_address_13459264, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459264) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459264) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x3A0UL))), x8);
        if ((x23 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5F4CUL);
        }
        __arm64_pair_address_13459276 = unchecked((ulong)((sp) + (0x3B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459276);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459276);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459276) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459276) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3D0UL))));
        __arm64_pair_address_13459284 = unchecked((ulong)((sp) + (0x380UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459284);
#else
        v2 = __ReadVector128(__arm64_pair_address_13459284);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459284) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459284) + (0x10UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x3A0UL))));
        __arm64_pair_address_13459292 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459292, v0);
#else
        __WriteVector128(__arm64_pair_address_13459292, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459292) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459292) + (0x10UL))), v1);
#endif
        x2 = unchecked((ulong)((sp) + (0x60UL)));
        x3 = unchecked((ulong)((sp) + (0x30UL)));
        x0 = x23;
        x1 = x19;
        v0 = v8;
        x4 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x8);
        __arm64_pair_address_13459324 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459324, v2);
#else
        __WriteVector128(__arm64_pair_address_13459324, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459324) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459324) + (0x10UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0xCD6954UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.BlendFrames */, x0, x1, x2, x3);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xCD570CUL /* metadata target: MotionBlurComponent.get_frameBlendingFilter */, x0, x1, x2, x3);
        x23 = x0;
        x8 = unchecked((ulong)((sp) + (0x2C0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        __arm64_pair_address_13459364 = unchecked((ulong)((sp) + (0x2C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459364);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459364);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459364) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459364) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x2E0UL))));
        __arm64_pair_address_13459372 = unchecked((ulong)((sp) + (0x2F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459372, v0);
#else
        __WriteVector128(__arm64_pair_address_13459372, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459372) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459372) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x310UL))), x8);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCD6040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD5FE0UL);
        }
        __arm64_pair_address_13459424 = unchecked((ulong)((sp) + (0x2F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13459424);
#else
        v0 = __ReadVector128(__arm64_pair_address_13459424);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13459424) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13459424) + (0x10UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x310UL))));
        x4 = unchecked((ulong)(unchecked((uint)(x0))));
        x2 = sp;
        __arm64_pair_address_13459440 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13459440, v0);
#else
        __WriteVector128(__arm64_pair_address_13459440, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13459440) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13459440) + (0x10UL))), v1);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x8);
        goto label_0xCD5FF8;
        label_0xCD5FF8:
        ;
        x0 = x23;
        x1 = x19;
        x3 = unchecked((ulong)(unchecked((uint)(x22))));
        x5 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xCD6E38UL /* metadata target: MotionBlurComponent.FrameBlendingFilter.PushFrame */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD600C;
        label_0xCD600C:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD601C;
        label_0xCD601C:
        ;
        sp = unchecked((ulong)((sp) + (0x420UL)));
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
        __arm64_pair_address_13459512 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13459512)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13459512) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13459512) + (0x70UL)));
        return x0;
        label_0xCD6040:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `MotionBlurComponent.OnDisable` — RVA `0xcd6f58`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public override void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MotionBlurComponent_OnDisable_RVAcd6f58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD6F64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD6F60UL);
        }
        return RuntimeCalls.InvokeDirect(0xCD591CUL /* metadata target: MotionBlurComponent.FrameBlendingFilter.Dispose */);
        label_0xCD6F64:
        ;
        return x0;
        return default(ulong);
    }
```

## `MotionBlurComponent.ctor` — RVA `0xcd6f68`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong MotionBlurComponent_ctor_RVAcd6f68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5E5UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x1F0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD6F9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1F0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5E5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD6F9C;
        label_0xCD6F9C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x30UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x11689ECUL);
        return default(ulong);
    }
```
