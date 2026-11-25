# `TaaComponent` — TypeDefIndex 3537

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `RenderBuffer[]` | `m_MRT` |
| `0x28` | `int` | `m_SampleIndex` |
| `0x2C` | `bool` | `m_ResetHistory` |
| `0x30` | `RenderTexture` | `m_HistoryTexture` |
| `0x38` | `Vector2` | `<jitterVector>k__BackingField` |

## `TaaComponent.get_active` — RVA `0xcd9530`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static uint TaaComponent_get_active_RVAcd9530(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13473136 = default(uint);
        uint __arm64_flags_left_13473164 = default(uint);
        uint __arm64_flags_left_13473200 = default(uint);
        uint __arm64_flags_right_13473136 = default(uint);
        uint __arm64_flags_right_13473164 = default(uint);
        uint __arm64_flags_right_13473200 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5F6UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD955C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5F6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD955C;
        label_0xCD955C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD95BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD9594;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        __arm64_flags_left_13473136 = unchecked((uint)(x8));
        __arm64_flags_right_13473136 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13473136) - (__arm64_flags_right_13473136))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCD9594;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A814UL /* metadata target: SystemInfo.get_supportsMotionVectors */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD9594;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179A8BCUL /* metadata target: SystemInfo.get_supportedRenderTargetCount */, x0, x1, x2, x3);
        __arm64_flags_left_13473164 = unchecked((uint)(x0));
        __arm64_flags_right_13473164 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13473164) - (__arm64_flags_right_13473164))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13473164)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13473164)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13473164) - (__arm64_flags_right_13473164))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13473164)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCD95A4;
        }
        else
        {
            goto label_0xCD9594;
        }
        label_0xCD9594:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCD9598;
        label_0xCD9598:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCD95A4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD95BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13473200 = unchecked((uint)(x8));
        __arm64_flags_right_13473200 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13473200) - (__arm64_flags_right_13473200))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCD9598;
        label_0xCD95BC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `TaaComponent.GetCameraFlags` — RVA `0xcd95c0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override DepthTextureMode GetCameraFlags() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TaaComponent_GetCameraFlags_RVAcd95c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TaaComponent.get_jitterVector` — RVA `0xcd95c8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Vector2 get_jitterVector() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TaaComponent_get_jitterVector_RVAcd95c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13473224 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_13473224 = unchecked((ulong)((x0) + (0x38UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13473224)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13473224) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TaaComponent.set_jitterVector` — RVA `0xcd95d0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private void set_jitterVector(Vector2 value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TaaComponent_set_jitterVector_RVAcd95d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13473232 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_13473232 = unchecked((ulong)((x0) + (0x38UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13473232, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13473232) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `TaaComponent.ResetHistory` — RVA `0xcd95d8`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void ResetHistory() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TaaComponent_ResetHistory_RVAcd95d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x2CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `TaaComponent.SetProjectionMatrix` — RVA `0xcd95e4`

- Lift status: **exact**; input span: 624 bytes; span to next metadata RVA: 624 bytes.
- Metadata signature: `public void SetProjectionMatrix(Func<Vector2, Matrix4x4> jitteredFunc) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=80 (informational only).

```csharp
public static ulong TaaComponent_SetProjectionMatrix_RVAcd95e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13473256 = default(ulong);
        ulong __arm64_pair_address_13473260 = default(ulong);
        ulong __arm64_pair_address_13473348 = default(ulong);
        ulong __arm64_pair_address_13473352 = default(ulong);
        ulong __arm64_pair_address_13473416 = default(ulong);
        ulong __arm64_pair_address_13473420 = default(ulong);
        ulong __arm64_pair_address_13473436 = default(ulong);
        ulong __arm64_pair_address_13473440 = default(ulong);
        ulong __arm64_pair_address_13473500 = default(ulong);
        ulong __arm64_pair_address_13473504 = default(ulong);
        ulong __arm64_pair_address_13473508 = default(ulong);
        ulong __arm64_pair_address_13473512 = default(ulong);
        ulong __arm64_pair_address_13473520 = default(ulong);
        ulong __arm64_pair_address_13473524 = default(ulong);
        ulong __arm64_pair_address_13473532 = default(ulong);
        ulong __arm64_pair_address_13473536 = default(ulong);
        ulong __arm64_pair_address_13473604 = default(ulong);
        ulong __arm64_pair_address_13473608 = default(ulong);
        ulong __arm64_pair_address_13473616 = default(ulong);
        ulong __arm64_pair_address_13473620 = default(ulong);
        ulong __arm64_pair_address_13473836 = default(ulong);
        ulong __arm64_pair_address_13473856 = default(ulong);
        ulong __arm64_pair_address_13473860 = default(ulong);
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
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x1E0UL)));
        __arm64_pair_address_13473256 = unchecked((ulong)((sp) + (0x180UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13473256, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13473256) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13473260 = unchecked((ulong)((sp) + (0x190UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13473260, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13473260) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x1A0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1B0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1B0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1C0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1C0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1D0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1D0UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5F7UL))))))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD9640;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x430UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x438UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5F7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD9640;
        label_0xCD9640:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13473348 = unchecked((ulong)((sp) + (0x160UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473348, v0);
#else
        __WriteVector128(__arm64_pair_address_13473348, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473348) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473348) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13473352 = unchecked((ulong)((sp) + (0x140UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473352, v0);
#else
        __WriteVector128(__arm64_pair_address_13473352, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473352) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473352) + (0x10UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD9654UL);
        }
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x1CUL))))), 0));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCD9854UL /* metadata target: TaaComponent.GenerateRandomOffset */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x100UL)));
        x0 = x21;
        x1 = 0x0UL;
        v8 = v0;
        v10 = v1;
        x0 = RuntimeCalls.InvokeDirect(0x176F148UL /* metadata target: Camera.get_projectionMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_13473416 = unchecked((ulong)((sp) + (0x100UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473416);
#else
        v0 = __ReadVector128(__arm64_pair_address_13473416);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473416) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473416) + (0x10UL))));
#endif
        __arm64_pair_address_13473420 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473420);
#else
        v2 = __ReadVector128(__arm64_pair_address_13473420);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473420) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473420) + (0x10UL))));
#endif
        x1 = unchecked((ulong)((sp) + (0xC0UL)));
        x0 = x21;
        x2 = 0x0UL;
        __arm64_pair_address_13473436 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473436, v0);
#else
        __WriteVector128(__arm64_pair_address_13473436, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473436) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473436) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13473440 = unchecked((ulong)((sp) + (0xE0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473440, v2);
#else
        __WriteVector128(__arm64_pair_address_13473440, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473440) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473440) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x176F280UL /* metadata target: Camera.set_nonJitteredProjectionMatrix */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        if ((x20 == 0x0UL))
        {
            goto label_0xCD9708;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x8 = unchecked((ulong)((sp) + (0x80UL)));
        v0 = v9;
        v1 = v8;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        __arm64_pair_address_13473500 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473500);
#else
        v0 = __ReadVector128(__arm64_pair_address_13473500);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473500) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473500) + (0x10UL))));
#endif
        __arm64_pair_address_13473504 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473504);
#else
        v2 = __ReadVector128(__arm64_pair_address_13473504);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473504) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473504) + (0x10UL))));
#endif
        __arm64_pair_address_13473508 = unchecked((ulong)((sp) + (0x100UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473508, v0);
#else
        __WriteVector128(__arm64_pair_address_13473508, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473508) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473508) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13473512 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473512, v2);
#else
        __WriteVector128(__arm64_pair_address_13473512, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473512) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473512) + (0x10UL))), v3);
#endif
        if ((x21 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD96F0UL);
        }
        __arm64_pair_address_13473520 = unchecked((ulong)((sp) + (0x100UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473520);
#else
        v0 = __ReadVector128(__arm64_pair_address_13473520);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473520) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473520) + (0x10UL))));
#endif
        __arm64_pair_address_13473524 = unchecked((ulong)((sp) + (0x120UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473524);
#else
        v2 = __ReadVector128(__arm64_pair_address_13473524);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473524) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473524) + (0x10UL))));
#endif
        x1 = unchecked((ulong)((sp) + (0x40UL)));
        __arm64_pair_address_13473532 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473532, v0);
#else
        __WriteVector128(__arm64_pair_address_13473532, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473532) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473532) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13473536 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473536, v2);
#else
        __WriteVector128(__arm64_pair_address_13473536, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473536) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473536) + (0x10UL))), v3);
#endif
        goto label_0xCD9758;
        label_0xCD9708:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E8E8UL /* metadata target: Camera.get_orthographic */, x0, x1, x2, x3);
        x8 = unchecked((ulong)((sp) + (0x140UL)));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD9734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        v0 = v9;
        v1 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xCD9D10UL /* metadata target: TaaComponent.GetOrthographicProjectionMatrix */, x0, x1, x2, x3);
        goto label_0xCD9744;
        label_0xCD9734:
        ;
        x0 = x19;
        v0 = v9;
        v1 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xCD98E8UL /* metadata target: TaaComponent.GetPerspectiveProjectionMatrix */, x0, x1, x2, x3);
        goto label_0xCD9744;
        label_0xCD9744:
        ;
        __arm64_pair_address_13473604 = unchecked((ulong)((sp) + (0x140UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473604);
#else
        v0 = __ReadVector128(__arm64_pair_address_13473604);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473604) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473604) + (0x10UL))));
#endif
        __arm64_pair_address_13473608 = unchecked((ulong)((sp) + (0x160UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13473608);
#else
        v2 = __ReadVector128(__arm64_pair_address_13473608);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13473608) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13473608) + (0x10UL))));
#endif
        x1 = sp;
        __arm64_pair_address_13473616 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473616, v0);
#else
        __WriteVector128(__arm64_pair_address_13473616, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473616) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473616) + (0x10UL))), v1);
#endif
        __arm64_pair_address_13473620 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13473620, v2);
#else
        __WriteVector128(__arm64_pair_address_13473620, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13473620) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13473620) + (0x10UL))), v3);
#endif
        goto label_0xCD9758;
        label_0xCD9758:
        ;
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F1F8UL /* metadata target: Camera.set_projectionMatrix */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F308UL /* metadata target: Camera.set_useJitteredProjectionMatrixForTransparentRendering */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x438UL))));
        x23 = 0x1A8F000UL;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x430UL))));
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD97F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD97F0;
        label_0xCD97F0:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xCD9850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x20))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x21))))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = x22;
        v0 = v9;
        v1 = v8;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_13473836 = unchecked((ulong)((x19) + (0x38UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13473836, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13473836) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1D0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1D0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1C0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1C0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1B0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x1B0UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x1A0UL))));
        __arm64_pair_address_13473856 = unchecked((ulong)((sp) + (0x190UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13473856)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13473856) + (0x8UL))))), 0));
        __arm64_pair_address_13473860 = unchecked((ulong)((sp) + (0x180UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13473860)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13473860) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x1E0UL)));
        return x0;
        label_0xCD9850:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `TaaComponent.GenerateRandomOffset` — RVA `0xcd9854`

- Lift status: **partial**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `private Vector2 GenerateRandomOffset() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=11 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.hi' at 0xcd98c8; reason: Unknown IR expression at 0xcd98c8

```csharp
public static ulong TaaComponent_GenerateRandomOffset_RVAcd9854(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13473884 = default(uint);
        uint __arm64_flags_left_13473980 = default(uint);
        uint __arm64_flags_left_13474008 = default(uint);
        uint __arm64_flags_result_13473884 = default(uint);
        uint __arm64_flags_right_13473884 = default(uint);
        uint __arm64_flags_right_13473980 = default(uint);
        uint __arm64_flags_right_13474008 = default(uint);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x28UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_flags_left_13473884 = unchecked((uint)(x8));
        __arm64_flags_right_13473884 = unchecked((uint)0x3FFUL);
        __arm64_flags_result_13473884 = unchecked((uint)((__arm64_flags_left_13473884) & (__arm64_flags_right_13473884)));
        x9 = unchecked((ulong)(__arm64_flags_result_13473884));
        if ((__arm64_flags_result_13473884 == unchecked((uint)0x0UL)))
        {
            goto label_0xCD98D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD9864UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        x10 = unchecked((ulong)(unchecked((uint)(x9))));
        goto label_0xCD9870;
        label_0xCD9870:
        ;
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)(0x1UL)))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x11))))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) >> (int)(unchecked((int)(unchecked((uint)(0x1UL)))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD9870;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(0xAAABUL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40400000UL)), 0)), 0));
        x10 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xAAAAUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        goto label_0xCD98A0;
        label_0xCD98A0:
        ;
        x11 = unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) * (unchecked((ulong)(unchecked((uint)(x10)))))));
        x11 = unchecked((ulong)((x11) >> (int)(unchecked((int)(0x21UL)))));
        x12 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x1UL))))))))))));
        x12 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(x12)))))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x12))))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        __arm64_flags_left_13473980 = unchecked((uint)(x9));
        __arm64_flags_right_13473980 = unchecked((uint)0x2UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(x11))));
        RuntimeCalls.Unsupported("b.hi", 0xCD98C8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD98A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD98CCUL);
        }
        goto label_0xCD98D4;
        label_0xCD98D0:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xCD98D4;
        label_0xCD98D4:
        ;
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13474008 = unchecked((uint)(x9));
        __arm64_flags_right_13474008 = unchecked((uint)0x8UL);
        x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13474008) - (__arm64_flags_right_13474008))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13474008)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13474008)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13474008) - (__arm64_flags_right_13474008))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13474008)) < unchecked((int)0x0UL))))) ? unchecked((uint)0x0UL) : unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x28UL))), unchecked((uint)(x8)));
        return x0;
        return default(ulong);
    }
```

## `TaaComponent.GetPerspectiveProjectionMatrix` — RVA `0xcd98e8`

- Lift status: **exact**; input span: 1064 bytes; span to next metadata RVA: 1064 bytes.
- Metadata signature: `private Matrix4x4 GetPerspectiveProjectionMatrix(Vector2 offset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=166 (informational only).

```csharp
public static ulong TaaComponent_GetPerspectiveProjectionMatrix_RVAcd98e8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13474028 = default(ulong);
        ulong __arm64_pair_address_13474032 = default(ulong);
        ulong __arm64_pair_address_13474036 = default(ulong);
        ulong __arm64_pair_address_13474040 = default(ulong);
        ulong __arm64_pair_address_13474064 = default(ulong);
        ulong __arm64_pair_address_13474068 = default(ulong);
        ulong __arm64_pair_address_13474312 = default(ulong);
        ulong __arm64_pair_address_13474316 = default(ulong);
        ulong __arm64_pair_address_13475032 = default(ulong);
        ulong __arm64_pair_address_13475036 = default(ulong);
        ulong __arm64_pair_address_13475048 = default(ulong);
        ulong __arm64_pair_address_13475052 = default(ulong);
        ulong __arm64_pair_address_13475060 = default(ulong);
        ulong __arm64_pair_address_13475064 = default(ulong);
        ulong __arm64_pair_address_13475068 = default(ulong);
        ulong __arm64_pair_address_13475072 = default(ulong);
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
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xB0UL)));
        __arm64_pair_address_13474028 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13474028, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13474028) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13474032 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13474032, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13474032) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13474036 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13474036, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13474036) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13474040 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13474040, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13474040) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x19);
        v10 = v0;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_13474064 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13474064, v0);
#else
        __WriteVector128(__arm64_pair_address_13474064, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13474064) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13474064) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13474068 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13474068, v0);
#else
        __WriteVector128(__arm64_pair_address_13474068, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13474068) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13474068) + (0x10UL))), v0);
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x9 == 0x0UL))
        {
        }
        else
        {
            x20 = x0;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x1 = 0x0UL;
                v8 = v1;
                x19 = x8;
                x0 = RuntimeCalls.InvokeDirect(0x176E71CUL /* metadata target: Camera.get_fieldOfView */, x0, x1, x2, x3);
                x8 = 0x432000UL;
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x30CUL))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                x0 = RuntimeCalls.InvokeDirect(0x19B0D00UL, x0, x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                if ((x8 == 0x0UL))
                {
                }
                else
                {
                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                    if ((x0 == 0x0UL))
                    {
                    }
                    else
                    {
                        x1 = 0x0UL;
                        v9 = v0;
                        x0 = RuntimeCalls.InvokeDirect(0x176E9A4UL /* metadata target: Camera.get_aspect */, x0, x1, x2, x3);
                        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                        if ((x0 == 0x0UL))
                        {
                        }
                        else
                        {
                            x1 = 0x0UL;
                            v12 = v0;
                            x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                            if ((x8 == 0x0UL))
                            {
                            }
                            else
                            {
                                x22 = unchecked((ulong)(unchecked((uint)(x0))));
                                x0 = x8;
                                x1 = 0x0UL;
                                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                if ((x8 == 0x0UL))
                                {
                                }
                                else
                                {
                                    x21 = unchecked((ulong)(unchecked((uint)(x0))));
                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                    if ((x0 == 0x0UL))
                                    {
                                    }
                                    else
                                    {
                                        x1 = 0x0UL;
                                        x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                        if ((x8 == 0x0UL))
                                        {
                                        }
                                        else
                                        {
                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                            if ((x0 == 0x0UL))
                                            {
                                            }
                                            else
                                            {
                                                x1 = 0x0UL;
                                                v14 = v0;
                                                x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                if ((x8 == 0x0UL))
                                                {
                                                }
                                                else
                                                {
                                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                    if ((x0 == 0x0UL))
                                                    {
                                                    }
                                                    else
                                                    {
                                                        x1 = 0x0UL;
                                                        v15 = v0;
                                                        x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                        if ((x8 == 0x0UL))
                                                        {
                                                        }
                                                        else
                                                        {
                                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                            if ((x0 == 0x0UL))
                                                            {
                                                            }
                                                            else
                                                            {
                                                                x1 = 0x0UL;
                                                                v11 = v0;
                                                                x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                                v1 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
                                                                __arm64_pair_address_13474312 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                RuntimeMemory.WriteVector128(__arm64_pair_address_13474312, v1);
#else
                                                                __WriteVector128(__arm64_pair_address_13474312, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13474312) + (0x10UL))), v1);
#else
                                                                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13474312) + (0x10UL))), v1);
#endif
                                                                __arm64_pair_address_13474316 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                RuntimeMemory.WriteVector128(__arm64_pair_address_13474316, v1);
#else
                                                                __WriteVector128(__arm64_pair_address_13474316, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13474316) + (0x10UL))), v1);
#else
                                                                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13474316) + (0x10UL))), v1);
#endif
                                                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                if ((x8 == 0x0UL))
                                                                {
                                                                }
                                                                else
                                                                {
                                                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                    if ((x0 == 0x0UL))
                                                                    {
                                                                    }
                                                                    else
                                                                    {
                                                                        v13 = v0;
                                                                        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
                                                                        x1 = 0x0UL;
                                                                        x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                                        x0 = sp;
                                                                        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
                                                                        x2 = 0x0UL;
                                                                        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                        x0 = sp;
                                                                        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
                                                                        x2 = 0x0UL;
                                                                        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                        x0 = sp;
                                                                        x1 = unchecked((ulong)(unchecked((uint)(0x8UL))));
                                                                        x2 = 0x0UL;
                                                                        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                        x0 = sp;
                                                                        x1 = unchecked((ulong)(unchecked((uint)(0xCUL))));
                                                                        x2 = 0x0UL;
                                                                        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                        x0 = sp;
                                                                        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                                                                        x2 = 0x0UL;
                                                                        x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                        if ((x8 == 0x0UL))
                                                                        {
                                                                        }
                                                                        else
                                                                        {
                                                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                            if ((x0 == 0x0UL))
                                                                            {
                                                                            }
                                                                            else
                                                                            {
                                                                                x1 = 0x0UL;
                                                                                x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                                                x0 = sp;
                                                                                x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
                                                                                x2 = 0x0UL;
                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                x0 = sp;
                                                                                x1 = unchecked((ulong)(unchecked((uint)(0x9UL))));
                                                                                x2 = 0x0UL;
                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                x0 = sp;
                                                                                x1 = unchecked((ulong)(unchecked((uint)(0xDUL))));
                                                                                x2 = 0x0UL;
                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                x0 = sp;
                                                                                x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
                                                                                x2 = 0x0UL;
                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                x0 = sp;
                                                                                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                                                                                x1 = unchecked((ulong)(unchecked((uint)(0x6UL))));
                                                                                x2 = 0x0UL;
                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                if ((x8 == 0x0UL))
                                                                                {
                                                                                }
                                                                                else
                                                                                {
                                                                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                    if ((x0 == 0x0UL))
                                                                                    {
                                                                                    }
                                                                                    else
                                                                                    {
                                                                                        x1 = 0x0UL;
                                                                                        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
                                                                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                        if ((x8 == 0x0UL))
                                                                                        {
                                                                                        }
                                                                                        else
                                                                                        {
                                                                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                            if ((x0 == 0x0UL))
                                                                                            {
                                                                                            }
                                                                                            else
                                                                                            {
                                                                                                x1 = 0x0UL;
                                                                                                v8 = v0;
                                                                                                x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                                                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                                if ((x8 == 0x0UL))
                                                                                                {
                                                                                                }
                                                                                                else
                                                                                                {
                                                                                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                                    if ((x0 == 0x0UL))
                                                                                                    {
                                                                                                    }
                                                                                                    else
                                                                                                    {
                                                                                                        x1 = 0x0UL;
                                                                                                        v9 = v0;
                                                                                                        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
                                                                                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                                        if ((x8 == 0x0UL))
                                                                                                        {
                                                                                                        }
                                                                                                        else
                                                                                                        {
                                                                                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                                            if ((x0 == 0x0UL))
                                                                                                            {
                                                                                                            }
                                                                                                            else
                                                                                                            {
                                                                                                                x1 = 0x0UL;
                                                                                                                v10 = v0;
                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                                                                                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
                                                                                                                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)))), 0));
                                                                                                                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                                                                                                                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                                                                                                                x0 = sp;
                                                                                                                x1 = unchecked((ulong)(unchecked((uint)(0xAUL))));
                                                                                                                x2 = 0x0UL;
                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                                                if ((x8 == 0x0UL))
                                                                                                                {
                                                                                                                }
                                                                                                                else
                                                                                                                {
                                                                                                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                                                    if ((x0 == 0x0UL))
                                                                                                                    {
                                                                                                                    }
                                                                                                                    else
                                                                                                                    {
                                                                                                                        x1 = 0x0UL;
                                                                                                                        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
                                                                                                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                                                        if ((x8 == 0x0UL))
                                                                                                                        {
                                                                                                                        }
                                                                                                                        else
                                                                                                                        {
                                                                                                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                                                            if ((x0 == 0x0UL))
                                                                                                                            {
                                                                                                                            }
                                                                                                                            else
                                                                                                                            {
                                                                                                                                x1 = 0x0UL;
                                                                                                                                v8 = v0;
                                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                                                                                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                                                                if ((x8 == 0x0UL))
                                                                                                                                {
                                                                                                                                }
                                                                                                                                else
                                                                                                                                {
                                                                                                                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                                                                    if ((x0 == 0x0UL))
                                                                                                                                    {
                                                                                                                                    }
                                                                                                                                    else
                                                                                                                                    {
                                                                                                                                        x1 = 0x0UL;
                                                                                                                                        v9 = v0;
                                                                                                                                        x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
                                                                                                                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                                                                                                                        if ((x8 == 0x0UL))
                                                                                                                                        {
                                                                                                                                        }
                                                                                                                                        else
                                                                                                                                        {
                                                                                                                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                                                                                                                            if ((x0 == 0x0UL))
                                                                                                                                            {
                                                                                                                                            }
                                                                                                                                            else
                                                                                                                                            {
                                                                                                                                                x1 = 0x0UL;
                                                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                                                                                                                                x0 = sp;
                                                                                                                                                x1 = unchecked((ulong)(unchecked((uint)(0xEUL))));
                                                                                                                                                x2 = 0x0UL;
                                                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                                                                                x0 = sp;
                                                                                                                                                x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
                                                                                                                                                x2 = 0x0UL;
                                                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                                                                                x0 = sp;
                                                                                                                                                x1 = unchecked((ulong)(unchecked((uint)(0x7UL))));
                                                                                                                                                x2 = 0x0UL;
                                                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                                                                                x0 = sp;
                                                                                                                                                x1 = unchecked((ulong)(unchecked((uint)(0xBUL))));
                                                                                                                                                x2 = 0x0UL;
                                                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                                                                                x0 = sp;
                                                                                                                                                x1 = unchecked((ulong)(unchecked((uint)(0xFUL))));
                                                                                                                                                x2 = 0x0UL;
                                                                                                                                                x0 = RuntimeCalls.InvokeDirect(0x17867B4UL /* metadata target: Matrix4x4.set_Item */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                                                                                                                                                __arm64_pair_address_13475032 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13475032);
#else
                                                                                                                                                v1 = __ReadVector128(__arm64_pair_address_13475032);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13475032) + (0x10UL))));
#else
                                                                                                                                                v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13475032) + (0x10UL))));
#endif
                                                                                                                                                __arm64_pair_address_13475036 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13475036);
#else
                                                                                                                                                v3 = __ReadVector128(__arm64_pair_address_13475036);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13475036) + (0x10UL))));
#else
                                                                                                                                                v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13475036) + (0x10UL))));
#endif
                                                                                                                                                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
                                                                                                                                                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
                                                                                                                                                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
                                                                                                                                                __arm64_pair_address_13475048 = unchecked((ulong)((x19) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                RuntimeMemory.WriteVector128(__arm64_pair_address_13475048, v1);
#else
                                                                                                                                                __WriteVector128(__arm64_pair_address_13475048, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13475048) + (0x10UL))), v0);
#else
                                                                                                                                                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13475048) + (0x10UL))), v0);
#endif
                                                                                                                                                __arm64_pair_address_13475052 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                RuntimeMemory.WriteVector128(__arm64_pair_address_13475052, v3);
#else
                                                                                                                                                __WriteVector128(__arm64_pair_address_13475052, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                                                                                                                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13475052) + (0x10UL))), v2);
#else
                                                                                                                                                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13475052) + (0x10UL))), v2);
#endif
                                                                                                                                                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
                                                                                                                                                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
                                                                                                                                                __arm64_pair_address_13475060 = unchecked((ulong)((sp) + (0x70UL)));
                                                                                                                                                v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13475060)), 0));
                                                                                                                                                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13475060) + (0x8UL))))), 0));
                                                                                                                                                __arm64_pair_address_13475064 = unchecked((ulong)((sp) + (0x60UL)));
                                                                                                                                                v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13475064)), 0));
                                                                                                                                                v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13475064) + (0x8UL))))), 0));
                                                                                                                                                __arm64_pair_address_13475068 = unchecked((ulong)((sp) + (0x50UL)));
                                                                                                                                                v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13475068)), 0));
                                                                                                                                                v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13475068) + (0x8UL))))), 0));
                                                                                                                                                __arm64_pair_address_13475072 = unchecked((ulong)((sp) + (0x40UL)));
                                                                                                                                                v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13475072)), 0));
                                                                                                                                                v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13475072) + (0x8UL))))), 0));
                                                                                                                                                return x0;
                                                                                                                                            }
                                                                                                                                        }
                                                                                                                                    }
                                                                                                                                }
                                                                                                                            }
                                                                                                                        }
                                                                                                                    }
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        label_0xCD9D0C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `TaaComponent.GetOrthographicProjectionMatrix` — RVA `0xcd9d10`

- Lift status: **exact**; input span: 336 bytes; span to next metadata RVA: 336 bytes.
- Metadata signature: `private Matrix4x4 GetOrthographicProjectionMatrix(Vector2 offset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=52 (informational only).

```csharp
public static ulong TaaComponent_GetOrthographicProjectionMatrix_RVAcd9d10(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13475092 = default(ulong);
        ulong __arm64_pair_address_13475096 = default(ulong);
        ulong __arm64_pair_address_13475100 = default(ulong);
        ulong __arm64_pair_address_13475372 = default(ulong);
        ulong __arm64_pair_address_13475376 = default(ulong);
        ulong __arm64_pair_address_13475388 = default(ulong);
        ulong __arm64_pair_address_13475392 = default(ulong);
        ulong __arm64_pair_address_13475400 = default(ulong);
        ulong __arm64_pair_address_13475404 = default(ulong);
        ulong __arm64_pair_address_13475408 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        __arm64_pair_address_13475092 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13475092, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13475092) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13475096 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13475096, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13475096) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13475100 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13475100, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13475100) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x70UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x9 == 0x0UL))
        {
        }
        else
        {
            x20 = x0;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x1 = 0x0UL;
                v8 = v1;
                v9 = v0;
                x19 = x8;
                x0 = RuntimeCalls.InvokeDirect(0x176E860UL /* metadata target: Camera.get_orthographicSize */, x0, x1, x2, x3);
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                if ((x8 == 0x0UL))
                {
                }
                else
                {
                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                    if ((x0 == 0x0UL))
                    {
                    }
                    else
                    {
                        x1 = 0x0UL;
                        v10 = v0;
                        x0 = RuntimeCalls.InvokeDirect(0x176E9A4UL /* metadata target: Camera.get_aspect */, x0, x1, x2, x3);
                        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                        if ((x0 == 0x0UL))
                        {
                        }
                        else
                        {
                            x1 = 0x0UL;
                            v11 = v0;
                            x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
                            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                            if ((x8 == 0x0UL))
                            {
                            }
                            else
                            {
                                x21 = unchecked((ulong)(unchecked((uint)(x0))));
                                x0 = x8;
                                x1 = 0x0UL;
                                x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
                                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                if ((x8 == 0x0UL))
                                {
                                }
                                else
                                {
                                    x22 = unchecked((ulong)(unchecked((uint)(x0))));
                                    x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                    if ((x0 == 0x0UL))
                                    {
                                    }
                                    else
                                    {
                                        x1 = 0x0UL;
                                        x0 = RuntimeCalls.InvokeDirect(0x176E60CUL /* metadata target: Camera.get_nearClipPlane */, x0, x1, x2, x3);
                                        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
                                        if ((x8 == 0x0UL))
                                        {
                                        }
                                        else
                                        {
                                            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
                                            if ((x0 == 0x0UL))
                                            {
                                            }
                                            else
                                            {
                                                x1 = 0x0UL;
                                                x0 = RuntimeCalls.InvokeDirect(0x176E694UL /* metadata target: Camera.get_farClipPlane */, x0, x1, x2, x3);
                                                x0 = 0x0UL;
                                                x0 = RuntimeCalls.InvokeDirect(0x1786560UL /* metadata target: Matrix4x4.Ortho */, x0, x1, x2, x3);
                                                __arm64_pair_address_13475372 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                                v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13475372);
#else
                                                v1 = __ReadVector128(__arm64_pair_address_13475372);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13475372) + (0x10UL))));
#else
                                                v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13475372) + (0x10UL))));
#endif
                                                __arm64_pair_address_13475376 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                                                v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13475376);
#else
                                                v3 = __ReadVector128(__arm64_pair_address_13475376);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13475376) + (0x10UL))));
#else
                                                v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13475376) + (0x10UL))));
#endif
                                                x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
                                                x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
                                                x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
                                                __arm64_pair_address_13475388 = unchecked((ulong)((x19) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                                                RuntimeMemory.WriteVector128(__arm64_pair_address_13475388, v1);
#else
                                                __WriteVector128(__arm64_pair_address_13475388, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13475388) + (0x10UL))), v0);
#else
                                                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13475388) + (0x10UL))), v0);
#endif
                                                __arm64_pair_address_13475392 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
                                                RuntimeMemory.WriteVector128(__arm64_pair_address_13475392, v3);
#else
                                                __WriteVector128(__arm64_pair_address_13475392, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                                                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13475392) + (0x10UL))), v2);
#else
                                                __WriteVector128(unchecked((ulong)((__arm64_pair_address_13475392) + (0x10UL))), v2);
#endif
                                                x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
                                                x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
                                                __arm64_pair_address_13475400 = unchecked((ulong)((sp) + (0x60UL)));
                                                v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13475400)), 0));
                                                v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13475400) + (0x8UL))))), 0));
                                                __arm64_pair_address_13475404 = unchecked((ulong)((sp) + (0x50UL)));
                                                v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13475404)), 0));
                                                v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13475404) + (0x8UL))))), 0));
                                                __arm64_pair_address_13475408 = unchecked((ulong)((sp) + (0x40UL)));
                                                v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13475408)), 0));
                                                v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13475408) + (0x8UL))))), 0));
                                                return x0;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        label_0xCD9E5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TaaComponent.Render` — RVA `0xcd9e60`

- Lift status: **exact**; input span: 1096 bytes; span to next metadata RVA: 1096 bytes.
- Metadata signature: `public void Render(RenderTexture source, RenderTexture destination) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=174 (informational only).

```csharp
public static ulong TaaComponent_Render_RVAcd9e60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13475744 = default(uint);
        uint __arm64_flags_left_13475792 = default(uint);
        uint __arm64_flags_left_13476336 = default(uint);
        uint __arm64_flags_right_13475744 = default(uint);
        uint __arm64_flags_right_13475792 = default(uint);
        uint __arm64_flags_right_13476336 = default(uint);
        ulong __arm64_load_address_13476504 = default(ulong);
        ulong __arm64_pair_address_13475428 = default(ulong);
        ulong __arm64_pair_address_13475632 = default(ulong);
        ulong __arm64_pair_address_13476500 = default(ulong);
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
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x27 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        __arm64_pair_address_13475428 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13475428, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13475428) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5F8UL))))))));
        x22 = x2;
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD9EE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x430UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x440UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x438UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5F8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD9EE4;
        label_0xCD9EE4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x438UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177B0DCUL /* metadata target: Material.set_shaderKeywords */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = 0x1A8F000UL;
        x26 = 0x1A8D000UL;
        x25 = 0x1A8C000UL;
        __arm64_pair_address_13475632 = unchecked((ulong)((x8) + (0x20UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13475632)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13475632) + (0x4UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2CUL))))))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x28UL))))), 0));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x440UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xC68UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xD8UL))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD9FD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x25);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD9F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD9F5CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD9F60;
        label_0xCD9F60:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD9FD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        __arm64_flags_left_13475744 = unchecked((uint)(x23));
        __arm64_flags_right_13475744 = unchecked((uint)(x0));
        if ((!((unchecked((uint)((__arm64_flags_left_13475744) - (__arm64_flags_right_13475744))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCD9FD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        __arm64_flags_left_13475792 = unchecked((uint)(x23));
        __arm64_flags_right_13475792 = unchecked((uint)(x0));
        if ((unchecked((uint)((__arm64_flags_left_13475792) - (__arm64_flags_right_13475792))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDA0AC;
        }
        else
        {
            goto label_0xCD9FD8;
        }
        label_0xCD9FD8:
        ;
        x23 = x19;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x30UL))));
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD9FF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD9FECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD9FF0;
        label_0xCD9FF0:
        ;
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDA00C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, x3);
        goto label_0xCDA00C;
        label_0xCDA00C:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1781FFCUL /* metadata target: RenderTexture.get_format */, x0, x1, x2, x3);
        x3 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = unchecked((ulong)(unchecked((uint)(x25))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1783E74UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        RuntimeMemory.WriteU64(x23, unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x23);
        if ((x0 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17983B0UL /* metadata target: Object.set_name */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x26);
        x23 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDA094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDA090UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDA094;
        label_0xCDA094:
        ;
        x3 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x20;
        x1 = x23;
        x2 = x21;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDA0AC;
        label_0xCDA0AC:
        ;
        x23 = 0x1A8F000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x430UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDA0C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDA0C0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x23);
        goto label_0xCDA0C8;
        label_0xCDA0C8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
        x0 = x21;
        v0 = v10;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x23);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x21;
        v0 = v8;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v1 = v9;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x36CUL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x23);
        x0 = x21;
        x2 = x20;
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x23 = x19;
        x0 = x21;
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1781FFCUL /* metadata target: RenderTexture.get_format */, x0, x1, x2, x3);
        x3 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(x24))));
        x1 = unchecked((ulong)(unchecked((uint)(x25))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1783E74UL /* metadata target: RenderTexture.GetTemporary */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x27);
        x2 = 0x0UL;
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeCalls.InvokeDirect(0x17983B0UL /* metadata target: Object.set_name */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x22 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778408UL /* metadata target: RenderTexture.get_colorBuffer */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x25 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCDA2A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDA1D4UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((x25) + (0x20UL)))) + (0x0UL))), x0);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((x25) + (0x20UL)))) + (0x8UL))), x1);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778408UL /* metadata target: RenderTexture.get_colorBuffer */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x22 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        __arm64_flags_left_13476336 = unchecked((uint)(x8));
        __arm64_flags_right_13476336 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13476336 >= __arm64_flags_right_13476336))) || (unchecked((uint)((__arm64_flags_left_13476336) - (__arm64_flags_right_13476336))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCDA2A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDA1F8UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((x22) + (0x30UL)))) + (0x0UL))), x0);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((x22) + (0x30UL)))) + (0x8UL))), x1);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177840CUL /* metadata target: RenderTexture.get_depthBuffer */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(x26);
        x25 = x1;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDA224;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCDA220UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCDA224;
        label_0xCDA224:
        ;
        x0 = x22;
        x1 = x20;
        x2 = x25;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1778520UL /* metadata target: Graphics.SetRenderTarget */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCDA2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E8E8UL /* metadata target: Camera.get_orthographic */, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF000UL /* metadata target: GraphicsUtils.Blit */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, x3);
        x0 = x23;
        x1 = x24;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x2CUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_13476500 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13476500)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13476500) + (0x8UL))))), 0));
        __arm64_load_address_13476504 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13476504)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13476504) + (0x70UL)));
        return x0;
        label_0xCDA2A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCDA2A4;
        label_0xCDA2A4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TaaComponent.GetHaltonValue` — RVA `0xcda2a8`

- Lift status: **partial**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `private float GetHaltonValue(int index, int radix) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=2 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.gt' at 0xcda2dc; reason: Unknown IR expression at 0xcda2bc

```csharp
public static ulong TaaComponent_GetHaltonValue_RVAcda2a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13476520 = default(uint);
        uint __arm64_flags_left_13476560 = default(uint);
        uint __arm64_flags_right_13476520 = default(uint);
        uint __arm64_flags_right_13476560 = default(uint);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_13476520 = unchecked((uint)(x1));
        __arm64_flags_right_13476520 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13476520) - (__arm64_flags_right_13476520))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13476520)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13476520)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13476520) - (__arm64_flags_right_13476520))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13476520)) < unchecked((int)0x0UL))))))
        {
            label_0xCDA2E4:
            ;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            return x0;
        }
        else
        {
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x2))))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
            label_0xCDA2BC:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x1))))) / (unchecked((int)(unchecked((uint)(x2)))))))))));
            x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) - (unchecked((uint)((unchecked((uint)(x8))) * (unchecked((uint)(x2))))))))));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x9))))))), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            __arm64_flags_left_13476560 = unchecked((uint)(x8));
            __arm64_flags_right_13476560 = unchecked((uint)0x0UL);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            x1 = unchecked((ulong)(unchecked((uint)(x8))));
            RuntimeCalls.Unsupported("b.gt", 0xCDA2DCUL);
            while (__Unsupported<bool>("Unknown IR expression"))
            {
                x8 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x1))))) / (unchecked((int)(unchecked((uint)(x2)))))))))));
                x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) - (unchecked((uint)((unchecked((uint)(x8))) * (unchecked((uint)(x2))))))))));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x9))))))), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
                __arm64_flags_left_13476560 = unchecked((uint)(x8));
                __arm64_flags_right_13476560 = unchecked((uint)0x0UL);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
                x1 = unchecked((ulong)(unchecked((uint)(x8))));
                RuntimeCalls.Unsupported("b.gt", 0xCDA2DCUL);
            }
            return x0;
        }
        return default(ulong);
    }
```

## `TaaComponent.OnDisable` — RVA `0xcda2ec`

- Lift status: **exact**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public override void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong TaaComponent_OnDisable_RVAcda2ec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5F9UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5F9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCDA324:
        ;
        x20 = x19;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xCDA33C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeMemory.ReadU64(x20);
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x1782724UL /* metadata target: RenderTexture.ReleaseTemporary */, x0, x1, x2, x3);
        }
        label_0xCDA35C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x30UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x28UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x2CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `TaaComponent.ctor` — RVA `0xcda388`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong TaaComponent_ctor_RVAcda388(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x22 = 0x1A8F000UL;
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5FAUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x448UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x150UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCDA3D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x150UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x448UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5FAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCDA3D4;
        label_0xCDA3D4:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x2CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x11689F8UL);
        return default(ulong);
    }
```
