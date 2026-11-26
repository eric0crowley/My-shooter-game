# `FogComponent` — TypeDefIndex 3522

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `FogComponent.get_active` — RVA `0xcd46c8`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static uint FogComponent_get_active_RVAcd46c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13453104 = default(uint);
        uint __arm64_flags_right_13453104 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5D3UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD46F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5D3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD46F4;
        label_0xCD46F4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD474C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD473C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD474C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE49CUL /* metadata target: PostProcessingContext.get_isGBufferAvailable */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD473C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1779C90UL /* metadata target: RenderSettings.get_fog */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD473C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD474C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13453104 = unchecked((uint)(x8));
        __arm64_flags_right_13453104 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13453104) - (__arm64_flags_right_13453104))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCD4740;
        label_0xCD473C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCD4740;
        label_0xCD4740:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCD474C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `FogComponent.GetName` — RVA `0xcd4750`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public override string GetName() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong FogComponent_GetName_RVAcd4750(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x5D4UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x5D4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD4780:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `FogComponent.GetCameraFlags` — RVA `0xcd4790`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint FogComponent_GetCameraFlags_RVAcd4790(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `FogComponent.GetCameraEvent` — RVA `0xcd4798`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override CameraEvent GetCameraEvent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint FogComponent_GetCameraEvent_RVAcd4798(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0xDUL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `FogComponent.PopulateCommandBuffer` — RVA `0xcd47a0`

- Lift status: **partial**; input span: 1140 bytes; span to next metadata RVA: 1140 bytes.
- Metadata signature: `public override void PopulateCommandBuffer(CommandBuffer cb) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=167 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xcd49f8; reason: Unknown IR expression at 0xcd49f8

```csharp
public static ulong FogComponent_PopulateCommandBuffer_RVAcd47a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13453740 = default(uint);
        uint __arm64_flags_left_13453800 = default(uint);
        uint __arm64_flags_result_13453800 = default(uint);
        uint __arm64_flags_right_13453740 = default(uint);
        uint __arm64_flags_right_13453800 = default(uint);
        ulong __arm64_pair_address_13453216 = default(ulong);
        ulong __arm64_pair_address_13453220 = default(ulong);
        ulong __arm64_pair_address_13453376 = default(ulong);
        ulong __arm64_pair_address_13453380 = default(ulong);
        ulong __arm64_pair_address_13453384 = default(ulong);
        ulong __arm64_pair_address_13453388 = default(ulong);
        ulong __arm64_pair_address_13453392 = default(ulong);
        ulong __arm64_pair_address_13453396 = default(ulong);
        ulong __arm64_pair_address_13453940 = default(ulong);
        ulong __arm64_pair_address_13453956 = default(ulong);
        ulong __arm64_pair_address_13453980 = default(ulong);
        ulong __arm64_pair_address_13453988 = default(ulong);
        ulong __arm64_pair_address_13454012 = default(ulong);
        ulong __arm64_pair_address_13454020 = default(ulong);
        ulong __arm64_pair_address_13454060 = default(ulong);
        ulong __arm64_pair_address_13454080 = default(ulong);
        ulong __arm64_pair_address_13454100 = default(ulong);
        ulong __arm64_pair_address_13454112 = default(ulong);
        ulong __arm64_pair_address_13454120 = default(ulong);
        ulong __arm64_pair_address_13454140 = default(ulong);
        ulong __arm64_pair_address_13454148 = default(ulong);
        ulong __arm64_pair_address_13454160 = default(ulong);
        ulong __arm64_pair_address_13454168 = default(ulong);
        ulong __arm64_pair_address_13454188 = default(ulong);
        ulong __arm64_pair_address_13454196 = default(ulong);
        ulong __arm64_pair_address_13454204 = default(ulong);
        ulong __arm64_pair_address_13454212 = default(ulong);
        ulong __arm64_pair_address_13454244 = default(ulong);
        ulong __arm64_pair_address_13454252 = default(ulong);
        ulong __arm64_pair_address_13454256 = default(ulong);
        ulong __arm64_pair_address_13454264 = default(ulong);
        ulong __arm64_pair_address_13454340 = default(ulong);
        ulong __arm64_pair_address_13454344 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
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
        __arm64_pair_address_13453216 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13453216, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13453216) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_13453216;
        __arm64_pair_address_13453220 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13453220, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13453220) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x290UL)));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5D5UL))))))));
        x19 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC90UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCA8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCB0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5D5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCD4824:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x280UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x250UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x220UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1F0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1C0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x190UL))), 0x0UL);
        __arm64_pair_address_13453376 = unchecked((ulong)((sp) + (0x260UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13453376, v0);
#else
        __WriteVector128(__arm64_pair_address_13453376, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13453376) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13453376) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13453380 = unchecked((ulong)((sp) + (0x230UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13453380, v0);
#else
        __WriteVector128(__arm64_pair_address_13453380, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13453380) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13453380) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13453384 = unchecked((ulong)((sp) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13453384, v0);
#else
        __WriteVector128(__arm64_pair_address_13453384, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13453384) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13453384) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13453388 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13453388, v0);
#else
        __WriteVector128(__arm64_pair_address_13453388, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13453388) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13453388) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13453392 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13453392, v0);
#else
        __WriteVector128(__arm64_pair_address_13453392, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13453392) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13453392) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13453396 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13453396, v0);
#else
        __WriteVector128(__arm64_pair_address_13453396, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13453396) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13453396) + (0x10UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
            if ((x9 == 0x0UL))
            {
            }
            else
            {
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
                if ((x0 == 0x0UL))
                {
                }
                else
                {
                    x9 = 0x1A8F000UL;
                    x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xF8UL))));
                    x25 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x11UL))))))));
                    x2 = 0x0UL;
                    x1 = RuntimeMemory.ReadU64(x9);
                    x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
                    if ((x0 == 0x0UL))
                    {
                    }
                    else
                    {
                        x24 = 0x1A8F000UL;
                        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xF0UL))));
                        x1 = 0x0UL;
                        x2 = 0x0UL;
                        x20 = x0;
                        x0 = RuntimeCalls.InvokeDirect(0x177B0DCUL /* metadata target: Material.set_shaderKeywords */, x0, x1, x2, x3);
                        x0 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0xCDEC1CUL /* metadata target: GraphicsUtils.get_isLinearColorSpace */, x0, x1, x2, x3);
                        x22 = unchecked((ulong)(unchecked((uint)(x0))));
                        x0 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x1779E18UL /* metadata target: RenderSettings.get_fogColor */, x0, x1, x2, x3);
                        v9 = v0;
                        v10 = v1;
                        v11 = v2;
                        v8 = v3;
                        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
                        {
                        }
                        else
                        {
                            v0 = v9;
                            x0 = 0x0UL;
                            x0 = RuntimeCalls.InvokeDirect(0x178BC18UL /* metadata target: Mathf.GammaToLinearSpace */, x0, x1, x2, x3);
                            v9 = v0;
                            v0 = v10;
                            x0 = 0x0UL;
                            x0 = RuntimeCalls.InvokeDirect(0x178BC18UL /* metadata target: Mathf.GammaToLinearSpace */, x0, x1, x2, x3);
                            v10 = v0;
                            v0 = v11;
                            x0 = 0x0UL;
                            x0 = RuntimeCalls.InvokeDirect(0x178BC18UL /* metadata target: Mathf.GammaToLinearSpace */, x0, x1, x2, x3);
                            v11 = v0;
                        }
                        label_0xCD48FC:
                        ;
                        x0 = RuntimeMemory.ReadU64(x24);
                        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
                        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                        {
                        }
                        else
                        {
                            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
                            x0 = RuntimeMemory.ReadU64(x24);
                        }
                        label_0xCD4910:
                        ;
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
                        x0 = x20;
                        v0 = v9;
                        v1 = v10;
                        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
                        v2 = v11;
                        v3 = v8;
                        x2 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x177A78CUL /* metadata target: Material.SetColor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x8 = RuntimeMemory.ReadU64(x24);
                        x0 = 0x0UL;
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                        x22 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
                        x0 = RuntimeCalls.InvokeDirect(0x1779F1CUL /* metadata target: RenderSettings.get_fogDensity */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x0 = x20;
                        x1 = unchecked((ulong)(unchecked((uint)(x22))));
                        x2 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x8 = RuntimeMemory.ReadU64(x24);
                        x0 = 0x0UL;
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                        x22 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
                        x0 = RuntimeCalls.InvokeDirect(0x1779CF4UL /* metadata target: RenderSettings.get_fogStartDistance */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x0 = x20;
                        x1 = unchecked((ulong)(unchecked((uint)(x22))));
                        x2 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x8 = RuntimeMemory.ReadU64(x24);
                        x0 = 0x0UL;
                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                        x22 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
                        x0 = RuntimeCalls.InvokeDirect(0x1779D54UL /* metadata target: RenderSettings.get_fogEndDistance */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x0 = x20;
                        x1 = unchecked((ulong)(unchecked((uint)(x22))));
                        x2 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x0 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0x1779DB4UL /* metadata target: RenderSettings.get_fogMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
                        __arm64_flags_left_13453740 = unchecked((uint)(x8));
                        __arm64_flags_right_13453740 = unchecked((uint)0x2UL);
                        if (((__arm64_flags_left_13453740 >= __arm64_flags_right_13453740) && (!((unchecked((uint)((__arm64_flags_left_13453740) - (__arm64_flags_right_13453740))) == unchecked((uint)0x0UL))))))
                        {
                        }
                        else
                        {
                            x9 = 0x19B6000UL;
                            x9 = unchecked((ulong)((x9) + (0xF18UL)));
                            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))));
                            x0 = x20;
                            x2 = 0x0UL;
                            x1 = RuntimeMemory.ReadU64(x8);
                            x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, x3);
                        }
                        label_0xCD49D0:
                        ;
                        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
                        if ((x0 == 0x0UL))
                        {
                        }
                        else
                        {
                            x1 = 0x0UL;
                            x0 = RuntimeCalls.InvokeDirect(0xCDE4C4UL /* metadata target: PostProcessingContext.get_isHdr */, x0, x1, x2, x3);
                            x8 = unchecked((ulong)(unchecked((uint)(x0))));
                            x0 = RuntimeMemory.ReadU64(x24);
                            __arm64_flags_left_13453800 = unchecked((uint)(x8));
                            __arm64_flags_right_13453800 = unchecked((uint)0x1UL);
                            __arm64_flags_result_13453800 = unchecked((uint)((__arm64_flags_left_13453800) & (__arm64_flags_right_13453800)));
                            x8 = unchecked((ulong)(unchecked((uint)(0x7UL))));
                            x10 = unchecked((ulong)(unchecked((uint)(0x9UL))));
                            x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
                            RuntimeCalls.Unsupported("csel", 0xCD49F8UL);
                            x22 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x10)) : unchecked((uint)(x8)))));
                            if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
                            {
                            }
                            else
                            {
                                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
                                x0 = RuntimeMemory.ReadU64(x24);
                            }
                            label_0xCD4A08:
                            ;
                            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
                            if ((x8 == 0x0UL))
                            {
                            }
                            else
                            {
                                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
                                x0 = x8;
                                x1 = 0x0UL;
                                x23 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x10UL))))));
                                x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
                                if ((x8 == 0x0UL))
                                {
                                }
                                else
                                {
                                    x21 = unchecked((ulong)(unchecked((uint)(x0))));
                                    x0 = x8;
                                    x1 = 0x0UL;
                                    x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                                    if ((x19 == 0x0UL))
                                    {
                                    }
                                    else
                                    {
                                        x3 = unchecked((ulong)(unchecked((uint)(x0))));
                                        x4 = unchecked((ulong)(unchecked((uint)(0x18UL))));
                                        x5 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                                        x0 = x19;
                                        x1 = unchecked((ulong)(unchecked((uint)(x23))));
                                        x2 = unchecked((ulong)(unchecked((uint)(x21))));
                                        x6 = unchecked((ulong)(unchecked((uint)(x22))));
                                        x7 = 0x0UL;
                                        x0 = RuntimeCalls.InvokeDirect(0x17A720CUL /* metadata target: CommandBuffer.GetTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                                        x8 = unchecked((ulong)((sp) + (0x110UL)));
                                        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                                        x1 = 0x0UL;
                                        x0 = RuntimeCalls.InvokeDirect(0x17A6294UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                                        __arm64_pair_address_13453940 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13453940);
#else
                                        v0 = __ReadVector128(__arm64_pair_address_13453940);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13453940) + (0x10UL))));
#else
                                        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13453940) + (0x10UL))));
#endif
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x130UL))));
                                        x9 = RuntimeMemory.ReadU64(x24);
                                        x1 = 0x0UL;
                                        __arm64_pair_address_13453956 = unchecked((ulong)((sp) + (0x140UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13453956, v0);
#else
                                        __WriteVector128(__arm64_pair_address_13453956, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13453956) + (0x10UL))), v1);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13453956) + (0x10UL))), v1);
#endif
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x160UL))), x8);
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
                                        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                                        x8 = unchecked((ulong)((sp) + (0x110UL)));
                                        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
                                        __arm64_pair_address_13453980 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13453980);
#else
                                        v0 = __ReadVector128(__arm64_pair_address_13453980);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13453980) + (0x10UL))));
#else
                                        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13453980) + (0x10UL))));
#endif
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x130UL))));
                                        __arm64_pair_address_13453988 = unchecked((ulong)((sp) + (0x140UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13453988);
#else
                                        v2 = __ReadVector128(__arm64_pair_address_13453988);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13453988) + (0x10UL))));
#else
                                        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13453988) + (0x10UL))));
#endif
                                        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x160UL))));
                                        x1 = unchecked((ulong)((sp) + (0xE0UL)));
                                        x2 = unchecked((ulong)((sp) + (0xB0UL)));
                                        x0 = x19;
                                        x3 = 0x0UL;
                                        __arm64_pair_address_13454012 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454012, v0);
#else
                                        __WriteVector128(__arm64_pair_address_13454012, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454012) + (0x10UL))), v1);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454012) + (0x10UL))), v1);
#endif
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xD0UL))), x8);
                                        __arm64_pair_address_13454020 = unchecked((ulong)((sp) + (0xE0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454020, v2);
#else
                                        __WriteVector128(__arm64_pair_address_13454020, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454020) + (0x10UL))), v3);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454020) + (0x10UL))), v3);
#endif
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x100UL))), x9);
                                        x0 = RuntimeCalls.InvokeDirect(0x17A7D84UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                                        x8 = RuntimeMemory.ReadU64(x24);
                                        x1 = 0x0UL;
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
                                        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                                        x8 = unchecked((ulong)((sp) + (0x80UL)));
                                        x0 = RuntimeCalls.InvokeDirect(0x17A62B8UL /* metadata target: RenderTargetIdentifier.op_Implicit */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
                                        __arm64_pair_address_13454060 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13454060);
#else
                                        v0 = __ReadVector128(__arm64_pair_address_13454060);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13454060) + (0x10UL))));
#else
                                        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13454060) + (0x10UL))));
#endif
                                        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                                        x1 = 0x0UL;
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x130UL))), x8);
                                        x8 = unchecked((ulong)((sp) + (0x58UL)));
                                        __arm64_pair_address_13454080 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454080, v0);
#else
                                        __WriteVector128(__arm64_pair_address_13454080, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454080) + (0x10UL))), v1);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454080) + (0x10UL))), v1);
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
                                        __arm64_pair_address_13454100 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454100, v0);
#else
                                        __WriteVector128(__arm64_pair_address_13454100, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454100) + (0x10UL))), v1);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454100) + (0x10UL))), v1);
#endif
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), x8);
                                        if ((unchecked((uint)((unchecked((uint)(x25))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
                                        {
                                            label_0xCD4B50:
                                            ;
                                            __arm64_pair_address_13454160 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13454160);
#else
                                            v0 = __ReadVector128(__arm64_pair_address_13454160);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13454160) + (0x10UL))));
#else
                                            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13454160) + (0x10UL))));
#endif
                                            x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
                                            __arm64_pair_address_13454168 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13454168);
#else
                                            v2 = __ReadVector128(__arm64_pair_address_13454168);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13454168) + (0x10UL))));
#else
                                            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13454168) + (0x10UL))));
#endif
                                            x11 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x130UL))));
                                            x8 = unchecked((ulong)((sp) + (0x230UL)));
                                            x9 = unchecked((ulong)((sp) + (0x260UL)));
                                            x4 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                                            __arm64_pair_address_13454188 = unchecked((ulong)((sp) + (0x260UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(__arm64_pair_address_13454188, v0);
#else
                                            __WriteVector128(__arm64_pair_address_13454188, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454188) + (0x10UL))), v1);
#else
                                            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454188) + (0x10UL))), v1);
#endif
                                            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x280UL))), x10);
                                            __arm64_pair_address_13454196 = unchecked((ulong)((sp) + (0x230UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(__arm64_pair_address_13454196, v2);
#else
                                            __WriteVector128(__arm64_pair_address_13454196, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454196) + (0x10UL))), v3);
#else
                                            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454196) + (0x10UL))), v3);
#endif
                                            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x250UL))), x11);
                                        }
                                        else
                                        {
                                            __arm64_pair_address_13454112 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13454112);
#else
                                            v0 = __ReadVector128(__arm64_pair_address_13454112);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13454112) + (0x10UL))));
#else
                                            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13454112) + (0x10UL))));
#endif
                                            x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
                                            __arm64_pair_address_13454120 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13454120);
#else
                                            v2 = __ReadVector128(__arm64_pair_address_13454120);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13454120) + (0x10UL))));
#else
                                            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13454120) + (0x10UL))));
#endif
                                            x11 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x130UL))));
                                            x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
                                            x8 = unchecked((ulong)((sp) + (0x1D0UL)));
                                            x9 = unchecked((ulong)((sp) + (0x200UL)));
                                            __arm64_pair_address_13454140 = unchecked((ulong)((sp) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(__arm64_pair_address_13454140, v0);
#else
                                            __WriteVector128(__arm64_pair_address_13454140, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454140) + (0x10UL))), v1);
#else
                                            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454140) + (0x10UL))), v1);
#endif
                                            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x220UL))), x10);
                                            __arm64_pair_address_13454148 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(__arm64_pair_address_13454148, v2);
#else
                                            __WriteVector128(__arm64_pair_address_13454148, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454148) + (0x10UL))), v3);
#else
                                            __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454148) + (0x10UL))), v3);
#endif
                                            RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1F0UL))), x11);
                                        }
                                        label_0xCD4B7C:
                                        ;
                                        __arm64_pair_address_13454204 = x9;
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13454204);
#else
                                        v0 = __ReadVector128(__arm64_pair_address_13454204);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13454204) + (0x10UL))));
#else
                                        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13454204) + (0x10UL))));
#endif
                                        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
                                        __arm64_pair_address_13454212 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13454212);
#else
                                        v2 = __ReadVector128(__arm64_pair_address_13454212);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13454212) + (0x10UL))));
#else
                                        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13454212) + (0x10UL))));
#endif
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
                                        x1 = unchecked((ulong)((sp) + (0x30UL)));
                                        x2 = sp;
                                        x0 = x19;
                                        x3 = x20;
                                        x5 = 0x0UL;
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1C0UL))), x9);
                                        __arm64_pair_address_13454244 = unchecked((ulong)((sp) + (0x1A0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454244, v0);
#else
                                        __WriteVector128(__arm64_pair_address_13454244, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454244) + (0x10UL))), v1);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454244) + (0x10UL))), v1);
#endif
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x190UL))), x8);
                                        __arm64_pair_address_13454252 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454252, v2);
#else
                                        __WriteVector128(__arm64_pair_address_13454252, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454252) + (0x10UL))), v3);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454252) + (0x10UL))), v3);
#endif
                                        __arm64_pair_address_13454256 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454256, v2);
#else
                                        __WriteVector128(__arm64_pair_address_13454256, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454256) + (0x10UL))), v3);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454256) + (0x10UL))), v3);
#endif
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x8);
                                        __arm64_pair_address_13454264 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(__arm64_pair_address_13454264, v0);
#else
                                        __WriteVector128(__arm64_pair_address_13454264, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13454264) + (0x10UL))), v1);
#else
                                        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13454264) + (0x10UL))), v1);
#endif
                                        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x9);
                                        x0 = RuntimeCalls.InvokeDirect(0x17A7E10UL /* metadata target: CommandBuffer.Blit */, x0, x1, x2, x3);
                                        x0 = RuntimeMemory.ReadU64(x24);
                                        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
                                        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
                                        {
                                        }
                                        else
                                        {
                                            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
                                            x0 = RuntimeMemory.ReadU64(x24);
                                        }
                                        label_0xCD4BD8:
                                        ;
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
                                        x0 = x19;
                                        x2 = 0x0UL;
                                        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
                                        x0 = RuntimeCalls.InvokeDirect(0x17A73A0UL /* metadata target: CommandBuffer.ReleaseTemporaryRT */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                        sp = unchecked((ulong)((sp) + (0x290UL)));
                                        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
                                        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
                                        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
                                        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
                                        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
                                        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
                                        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
                                        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
                                        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
                                        __arm64_pair_address_13454340 = unchecked((ulong)((sp) + (0x10UL)));
                                        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13454340)), 0));
                                        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13454340) + (0x8UL))))), 0));
                                        __arm64_pair_address_13454344 = sp;
                                        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13454344)), 0));
                                        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13454344) + (0x8UL))))), 0));
                                        sp = unchecked((ulong)((__arm64_pair_address_13454344) + (0x70UL)));
                                        return x0;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        label_0xCD4C10:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `FogComponent.ctor` — RVA `0xcd4c14`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong FogComponent_ctor_RVAcd4c14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5D6UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x100UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD4C48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x100UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5D6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD4C48;
        label_0xCD4C48:
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
