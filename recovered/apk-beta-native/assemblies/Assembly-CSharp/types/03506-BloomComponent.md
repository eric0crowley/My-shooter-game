# `BloomComponent` — TypeDefIndex 3506

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `RenderTexture[]` | `m_BlurBuffer1` |
| `0x28` | `RenderTexture[]` | `m_BlurBuffer2` |

## `BloomComponent.get_active` — RVA `0xcce830`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static uint BloomComponent_get_active_RVAcce830(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13428868 = default(uint);
        uint __arm64_flags_right_13428868 = default(uint);
        float __arm64_float_flags_left_13428848 = default(float);
        float __arm64_float_flags_right_13428848 = default(float);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5A2UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCE85C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD20UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5A2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCE85C;
        label_0xCCE85C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE8A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCE890;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCCE86CUL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x18UL))))), 0));
        __arm64_float_flags_left_13428848 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13428848 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13428848 <= __arm64_float_flags_right_13428848) || ((__arm64_float_flags_left_13428848 != __arm64_float_flags_left_13428848) || (__arm64_float_flags_right_13428848 != __arm64_float_flags_right_13428848))))
        {
            goto label_0xCCE890;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCE8A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13428868 = unchecked((uint)(x8));
        __arm64_flags_right_13428868 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13428868) - (__arm64_flags_right_13428868))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCCE894;
        label_0xCCE890:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCCE894;
        label_0xCCE894:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCCE8A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `BloomComponent.Prepare` — RVA `0xcce8a4`

- Lift status: **partial**; input span: 2416 bytes; span to next metadata RVA: 2416 bytes.
- Metadata signature: `public void Prepare(RenderTexture source, Material uberMaterial, Texture autoExposure) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=357 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xccea64; reason: Unknown IR expression at 0xccea64; reason: Unsupported instruction 'csel' at 0xcceadc; reason: Unknown IR expression at 0xcceadc; reason: Unsupported instruction 'cinc' at 0xccecdc; reason: Unknown IR expression at 0xccecdc; reason: Unsupported instruction 'b.ne' at 0xccedb4; reason: Unknown IR expression at 0xccedb4

```csharp
public static ulong BloomComponent_Prepare_RVAcce8a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fcvtz_source_13429448 = default(float);
        uint __arm64_flags_left_13429256 = default(uint);
        uint __arm64_flags_left_13429292 = default(uint);
        uint __arm64_flags_left_13429336 = default(uint);
        uint __arm64_flags_left_13429460 = default(uint);
        uint __arm64_flags_left_13429472 = default(uint);
        uint __arm64_flags_left_13429620 = default(uint);
        uint __arm64_flags_left_13429960 = default(uint);
        uint __arm64_flags_left_13429968 = default(uint);
        ulong __arm64_flags_left_13430056 = default(ulong);
        ulong __arm64_flags_left_13430084 = default(ulong);
        ulong __arm64_flags_left_13430100 = default(ulong);
        ulong __arm64_flags_left_13430172 = default(ulong);
        ulong __arm64_flags_left_13430188 = default(ulong);
        uint __arm64_flags_left_13430204 = default(uint);
        uint __arm64_flags_left_13430232 = default(uint);
        uint __arm64_flags_left_13430444 = default(uint);
        uint __arm64_flags_left_13430480 = default(uint);
        uint __arm64_flags_left_13430556 = default(uint);
        uint __arm64_flags_left_13430572 = default(uint);
        ulong __arm64_flags_left_13430620 = default(ulong);
        ulong __arm64_flags_left_13430688 = default(ulong);
        ulong __arm64_flags_left_13430728 = default(ulong);
        ulong __arm64_flags_left_13430788 = default(ulong);
        ulong __arm64_flags_left_13430856 = default(ulong);
        ulong __arm64_flags_left_13430896 = default(ulong);
        ulong __arm64_flags_left_13430932 = default(ulong);
        ulong __arm64_flags_left_13430960 = default(ulong);
        uint __arm64_flags_result_13429336 = default(uint);
        uint __arm64_flags_result_13429620 = default(uint);
        uint __arm64_flags_result_13430572 = default(uint);
        uint __arm64_flags_right_13429256 = default(uint);
        uint __arm64_flags_right_13429292 = default(uint);
        uint __arm64_flags_right_13429336 = default(uint);
        uint __arm64_flags_right_13429460 = default(uint);
        uint __arm64_flags_right_13429472 = default(uint);
        uint __arm64_flags_right_13429620 = default(uint);
        uint __arm64_flags_right_13429960 = default(uint);
        uint __arm64_flags_right_13429968 = default(uint);
        ulong __arm64_flags_right_13430056 = default(ulong);
        ulong __arm64_flags_right_13430084 = default(ulong);
        ulong __arm64_flags_right_13430100 = default(ulong);
        ulong __arm64_flags_right_13430172 = default(ulong);
        ulong __arm64_flags_right_13430188 = default(ulong);
        uint __arm64_flags_right_13430204 = default(uint);
        uint __arm64_flags_right_13430232 = default(uint);
        uint __arm64_flags_right_13430444 = default(uint);
        uint __arm64_flags_right_13430480 = default(uint);
        uint __arm64_flags_right_13430556 = default(uint);
        uint __arm64_flags_right_13430572 = default(uint);
        ulong __arm64_flags_right_13430620 = default(ulong);
        ulong __arm64_flags_right_13430688 = default(ulong);
        ulong __arm64_flags_right_13430728 = default(ulong);
        ulong __arm64_flags_right_13430788 = default(ulong);
        ulong __arm64_flags_right_13430856 = default(ulong);
        ulong __arm64_flags_right_13430896 = default(ulong);
        ulong __arm64_flags_right_13430932 = default(ulong);
        ulong __arm64_flags_right_13430960 = default(ulong);
        float __arm64_float_flags_left_13429452 = default(float);
        float __arm64_float_flags_left_13431100 = default(float);
        float __arm64_float_flags_right_13429452 = default(float);
        float __arm64_float_flags_right_13431100 = default(float);
        ulong __arm64_pair_address_13428904 = default(ulong);
        ulong __arm64_pair_address_13428908 = default(ulong);
        ulong __arm64_pair_address_13428912 = default(ulong);
        ulong __arm64_pair_address_13429132 = default(ulong);
        ulong __arm64_pair_address_13429136 = default(ulong);
        ulong __arm64_pair_address_13431272 = default(ulong);
        ulong __arm64_pair_address_13431276 = default(ulong);
        ulong __arm64_pair_address_13431280 = default(ulong);
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
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        __arm64_pair_address_13428904 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13428904, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13428904) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13428908 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13428908, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13428908) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13428912 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13428912, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13428912) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x5A3UL))))))));
        x23 = x3;
        x24 = x1;
        x21 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x2);
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCE968;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x248UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x5A3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCE968;
        label_0xCCE968:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8E000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD38UL))));
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        __arm64_pair_address_13429132 = unchecked((ulong)((x8) + (0x18UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13429132)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13429132) + (0x4UL))))), 0));
        __arm64_pair_address_13429136 = unchecked((ulong)((x8) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13429136)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13429136) + (0x4UL))))), 0));
        x1 = RuntimeMemory.ReadU64(x9);
        x19 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x28UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x38UL))))), 0));
        x2 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x10);
        x0 = RuntimeCalls.InvokeDirect(0xCDF3ECUL /* metadata target: MaterialFactory.Get */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD28UL))));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177B0DCUL /* metadata target: Material.set_shaderKeywords */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCE9DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCE9D4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        goto label_0xCCE9DC;
        label_0xCCE9DC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x22;
        x2 = x23;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4E0UL /* metadata target: PostProcessingContext.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        __arm64_flags_left_13429256 = unchecked((uint)(x0));
        __arm64_flags_right_13429256 = unchecked((uint)0x0UL);
        x23 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429256) - (__arm64_flags_right_13429256))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13429256)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13429256)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429256) - (__arm64_flags_right_13429256))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13429256)) < unchecked((int)0x0UL))))) ? unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x0)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x248UL))));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDE4FCUL /* metadata target: PostProcessingContext.get_height */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        __arm64_flags_left_13429292 = unchecked((uint)(x0));
        __arm64_flags_right_13429292 = unchecked((uint)0x0UL);
        x20 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429292) - (__arm64_flags_right_13429292))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13429292)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13429292)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429292) - (__arm64_flags_right_13429292))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13429292)) < unchecked((int)0x0UL))))) ? unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x0)))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEA44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCEA44;
        label_0xCCEA44:
        ;
        x0 = 0x0UL;
        x20 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x20))))) >> (int)(unchecked((int)(0x1UL)))))))));
        x0 = RuntimeCalls.InvokeDirect(0x176D5F4UL /* metadata target: Application.get_isMobilePlatform */, x0, x1, x2, x3);
        x26 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x620UL))))))));
        __arm64_flags_left_13429336 = unchecked((uint)(x0));
        __arm64_flags_right_13429336 = unchecked((uint)0x1UL);
        __arm64_flags_result_13429336 = unchecked((uint)((__arm64_flags_left_13429336) & (__arm64_flags_right_13429336)));
        x9 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        RuntimeCalls.Unsupported("csel", 0xCCEA64UL);
        x25 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x10)) : unchecked((uint)(x9)))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEA80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x620UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCEA80;
        label_0xCCEA80:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x20))))))), 0));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEA9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEA98UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCEA9C;
        label_0xCCEA9C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x4000000000000000UL))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1548980UL /* metadata target: Math.Log */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC1000000UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        __arm64_fcvtz_source_13429448 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13429448 != __arm64_fcvtz_source_13429448) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13429448 >= global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x4F000000UL)), 0)) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13429448 < global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xCF000000UL)), 0)) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13429448)))))))));
        __arm64_float_flags_left_13429452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13429452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x26 = unchecked((ulong)(((__arm64_float_flags_left_13429452 == __arm64_float_flags_right_13429452) ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
        __arm64_flags_left_13429460 = unchecked((uint)(x26));
        __arm64_flags_right_13429460 = unchecked((uint)0x10UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        RuntimeCalls.Unsupported("csel", 0xCCEADCUL);
        x28 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x26)) : unchecked((uint)(x8)))));
        __arm64_flags_left_13429472 = unchecked((uint)(x28));
        __arm64_flags_right_13429472 = unchecked((uint)0x1UL);
        x8 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_13429472) - (__arm64_flags_right_13429472))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429472) - (__arm64_flags_right_13429472))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13429472)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13429472)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429472) - (__arm64_flags_right_13429472))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13429472)) < unchecked((int)0x0UL)))))) ? unchecked((uint)(x28)) : unchecked((uint)((unchecked((uint)0x0UL)) + (unchecked((uint)0x1UL)))))));
        v0 = v10;
        x0 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x2CUL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x178BC18UL /* metadata target: Mathf.GammaToLinearSpace */, x0, x1, x2, x3);
        x27 = 0x1A8E000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xD28UL))));
        v10 = v0;
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEB18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEB10UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        goto label_0xCCEB18;
        label_0xCCEB18:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x22;
        v0 = v10;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x27);
        x9 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x41CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3E800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x8UL))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x22;
        x2 = 0x0UL;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x27);
        __arm64_flags_left_13429620 = unchecked((uint)(x19));
        __arm64_flags_right_13429620 = unchecked((uint)0x1UL);
        __arm64_flags_result_13429620 = unchecked((uint)((__arm64_flags_left_13429620) & (__arm64_flags_right_13429620)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_flags_result_13429620 == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xCUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x26))))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEBB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEBB0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        goto label_0xCCEBB8;
        label_0xCCEBB8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x22;
        v0 = v10;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCEBEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD30UL))));
        x0 = x22;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, x3);
        goto label_0xCCEBEC;
        label_0xCCEBEC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEBFCUL);
        }
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x28UL))), unchecked((uint)(x28)));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD40UL))));
        x19 = 0x1A8D000UL;
        x1 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x23))))) >> (int)(unchecked((int)(0x1UL)))))))));
        x6 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC68UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(x25))));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x0UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x28 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xCDF858UL /* metadata target: RenderTextureFactory.Get */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x19);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEC54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCEC54;
        label_0xCCEC54:
        ;
        x0 = x24;
        x1 = x19;
        x2 = x22;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x2CUL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        x29 = 0x0UL;
        x24 = x19;
        x19 = unchecked((ulong)(unchecked((uint)(x8))));
        x23 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x24);
        goto label_0xCCEC88;
        label_0xCCEC88:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEC90UL);
        }
        if ((x24 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x24);
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x0 = x24;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x24);
        x27 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x24;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x26 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD40UL))));
        __arm64_flags_left_13429960 = unchecked((uint)(x27));
        __arm64_flags_right_13429960 = unchecked((uint)0x0UL);
        x9 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429960) - (__arm64_flags_right_13429960))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13429960)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13429960)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13429960) - (__arm64_flags_right_13429960))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13429960)) < unchecked((int)0x0UL))))) ? unchecked((uint)((unchecked((uint)(x27))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x27)))));
        __arm64_flags_left_13429968 = unchecked((uint)(x0));
        __arm64_flags_right_13429968 = unchecked((uint)0x0UL);
        x8 = RuntimeMemory.ReadU64(x8);
        x1 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) >> (int)(unchecked((int)(0x1UL)))))))));
        RuntimeCalls.Unsupported("cinc", 0xCCECDCUL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x0)))));
        x2 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x9))))) >> (int)(unchecked((int)(0x1UL)))))))));
        x6 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x26;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(x25))));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x0UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xCDF858UL /* metadata target: RenderTextureFactory.Get */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCCED24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x26;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF208;
        }
        else
        {
            goto label_0xCCED24;
        }
        label_0xCCED24:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13430056 = x29;
        __arm64_flags_right_13430056 = x8;
        if ((__arm64_flags_left_13430056 >= __arm64_flags_right_13430056))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)(x23)))))));
        x1 = x26;
        RuntimeMemory.WriteU64(x0, x26);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        __arm64_flags_left_13430084 = x23;
        __arm64_flags_right_13430084 = 0x20UL;
        x26 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_13430084) - (__arm64_flags_right_13430084))) == 0x0UL))) ? unchecked((uint)((unchecked((uint)(x28))) + (unchecked((uint)0x1UL)))) : unchecked((uint)(x28)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430100 = x29;
        __arm64_flags_right_13430100 = x9;
        if ((__arm64_flags_left_13430100 >= __arm64_flags_right_13430100))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8D000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC68UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCED78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCED74UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCED78;
        label_0xCCED78:
        ;
        x0 = x24;
        x1 = x27;
        x2 = x22;
        x3 = unchecked((ulong)(unchecked((uint)(x26))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13430172 = x29;
        __arm64_flags_right_13430172 = x8;
        if ((__arm64_flags_left_13430172 >= __arm64_flags_right_13430172))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        x29 = unchecked((ulong)((x29) + (0x1UL)));
        __arm64_flags_left_13430188 = x19;
        __arm64_flags_right_13430188 = x29;
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x8UL)))))));
        RuntimeCalls.Unsupported("b.ne", 0xCCEDB4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCCEC88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x28UL))))));
        __arm64_flags_left_13430204 = unchecked((uint)(x8));
        __arm64_flags_right_13430204 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13430204) - (__arm64_flags_right_13430204))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13430204)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13430204)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13430204) - (__arm64_flags_right_13430204))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13430204)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCCEF40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x2CUL))))));
        x23 = 0x1A8E000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD28UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x2UL)))))));
        goto label_0xCCEDD4;
        label_0xCCEDD4:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13430232 = unchecked((uint)(x8));
        __arm64_flags_right_13430232 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13430232 >= __arm64_flags_right_13430232))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x29 = unchecked((ulong)(unchecked((uint)(x8))));
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEE00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEDF8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x23);
        goto label_0xCCEE00;
        label_0xCCEE00:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x22;
        x2 = x26;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEE20UL);
        }
        if ((x26 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x26);
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x0 = x26;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x9) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x8, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x28 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x26;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x198UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x198UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x27 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD40UL))));
        x2 = unchecked((ulong)(unchecked((uint)(x0))));
        x6 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x7 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x27;
        x1 = unchecked((ulong)(unchecked((uint)(x28))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = unchecked((ulong)(unchecked((uint)(x25))));
        x5 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x0UL))), x8);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xCDF858UL /* metadata target: RenderTextureFactory.Get */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x19 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCCEEA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x26;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF208;
        }
        else
        {
            goto label_0xCCEEA8;
        }
        label_0xCCEEA8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        __arm64_flags_left_13430444 = unchecked((uint)(x29));
        __arm64_flags_right_13430444 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13430444 >= __arm64_flags_right_13430444))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x19) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x26);
        x1 = x26;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430480 = unchecked((uint)(x29));
        __arm64_flags_right_13430480 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13430480 >= __arm64_flags_right_13430480))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8D000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC68UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEEF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEEF4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCEEF8;
        label_0xCCEEF8:
        ;
        x3 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x24;
        x1 = x26;
        x2 = x22;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177861CUL /* metadata target: Graphics.Blit */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430556 = unchecked((uint)(x29));
        __arm64_flags_right_13430556 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13430556 >= __arm64_flags_right_13430556))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        __arm64_flags_left_13430572 = unchecked((uint)(x29));
        __arm64_flags_right_13430572 = unchecked((uint)0x1UL);
        __arm64_flags_result_13430572 = unchecked((uint)((__arm64_flags_left_13430572) - (__arm64_flags_right_13430572)));
        x8 = unchecked((ulong)(__arm64_flags_result_13430572));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13430572) - (__arm64_flags_right_13430572))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13430572)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13430572)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13430572) - (__arm64_flags_right_13430572))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13430572)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCCEF40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xCCEDD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEF3CUL);
        }
        goto label_0xCCF200;
        label_0xCCEF40:
        ;
        x20 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xCCEF50;
        label_0xCCEF50:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430620 = x19;
        __arm64_flags_right_13430620 = x9;
        if ((__arm64_flags_left_13430620 >= __arm64_flags_right_13430620))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEF78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEF74UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCEF78;
        label_0xCCEF78:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCEFBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430688 = x19;
        __arm64_flags_right_13430688 = x10;
        if ((__arm64_flags_left_13430688 >= __arm64_flags_right_13430688))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF93CUL /* metadata target: RenderTextureFactory.Release */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCEFBC;
        label_0xCCEFBC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430728 = x19;
        __arm64_flags_right_13430728 = x9;
        if ((__arm64_flags_left_13430728 >= __arm64_flags_right_13430728))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCEFE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCEFE0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCEFE4;
        label_0xCCEFE4:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCF064;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430788 = x19;
        __arm64_flags_right_13430788 = x9;
        if ((__arm64_flags_left_13430788 >= __arm64_flags_right_13430788))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF020;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCF01CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCF020;
        label_0xCCF020:
        ;
        x0 = x22;
        x1 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCF064;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430856 = x19;
        __arm64_flags_right_13430856 = x10;
        if ((__arm64_flags_left_13430856 >= __arm64_flags_right_13430856))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23))))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF93CUL /* metadata target: RenderTextureFactory.Release */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCF064;
        label_0xCCF064:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430896 = x19;
        __arm64_flags_right_13430896 = x9;
        if ((__arm64_flags_left_13430896 >= __arm64_flags_right_13430896))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23)))))));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x0, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13430932 = x19;
        __arm64_flags_right_13430932 = x9;
        if ((__arm64_flags_left_13430932 >= __arm64_flags_right_13430932))
        {
            goto label_0xCCF204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x23)))))));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(x0, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x8UL)))))));
        __arm64_flags_left_13430960 = x23;
        __arm64_flags_right_13430960 = 0xA0UL;
        x19 = unchecked((ulong)((x19) + (0x1UL)));
        RuntimeCalls.Unsupported("b.ne", 0xCCF0B8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCCEF50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF93CUL /* metadata target: RenderTextureFactory.Release */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF0F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCF0F0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCCF0F4;
        label_0xCCF0F4:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xCCF200;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x2 = x24;
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = v10;
        v1 = v9;
        x2 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x1CUL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B7E8UL /* metadata target: Material.SetVector */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_float_flags_left_13431100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13431100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13431100 <= __arm64_float_flags_right_13431100) || ((__arm64_float_flags_left_13431100 != __arm64_float_flags_left_13431100) || (__arm64_float_flags_right_13431100 != __arm64_float_flags_right_13431100))))
        {
            goto label_0xCCF1C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF154;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCF150UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCCF154;
        label_0xCCF154:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCF1C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF180;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCF178UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        goto label_0xCCF180;
        label_0xCCF180:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x19;
        x2 = x20;
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        v0 = v8;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x24UL))))));
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD50UL))));
        goto label_0xCCF1C8;
        label_0xCCF1C0:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD48UL))));
        goto label_0xCCF1C8;
        label_0xCCF1C8:
        ;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        __arm64_pair_address_13431272 = unchecked((ulong)((sp) + (0x50UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13431272)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13431272) + (0x8UL))))), 0));
        __arm64_pair_address_13431276 = unchecked((ulong)((sp) + (0x40UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13431276)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13431276) + (0x8UL))))), 0));
        __arm64_pair_address_13431280 = unchecked((ulong)((sp) + (0x30UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13431280)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13431280) + (0x8UL))))), 0));
        x2 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */);
        label_0xCCF200:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCCF204;
        label_0xCCF204:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCCF208;
        label_0xCCF208:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BloomComponent.ctor` — RVA `0xccf220`

- Lift status: **exact**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong BloomComponent_ctor_RVAccf220(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x5A4UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD58UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD60UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCF26C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x5A4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCF26C;
        label_0xCCF26C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x10UL))));
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
        return RuntimeCalls.InvokeDirect(0x11689F8UL);
        return default(ulong);
    }
```
