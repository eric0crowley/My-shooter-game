# `ChromaticAberrationComponent` — TypeDefIndex 3512

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `Texture2D` | `m_SpectrumLut` |

## `ChromaticAberrationComponent.get_active` — RVA `0xcd0664`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public override bool get_active() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static uint ChromaticAberrationComponent_get_active_RVAcd0664(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13436600 = default(uint);
        uint __arm64_flags_right_13436600 = default(uint);
        float __arm64_float_flags_left_13436580 = default(float);
        float __arm64_float_flags_right_13436580 = default(float);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5B2UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD0690;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE58UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5B2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD0690;
        label_0xCD0690:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD06D4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD06C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCD06A0UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        __arm64_float_flags_left_13436580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13436580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_13436580 <= __arm64_float_flags_right_13436580) || ((__arm64_float_flags_left_13436580 != __arm64_float_flags_left_13436580) || (__arm64_float_flags_right_13436580 != __arm64_float_flags_right_13436580))))
        {
            goto label_0xCD06C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD06D4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x30UL))))))));
        __arm64_flags_left_13436600 = unchecked((uint)(x8));
        __arm64_flags_right_13436600 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13436600) - (__arm64_flags_right_13436600))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xCD06C8;
        label_0xCD06C4:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCD06C8;
        label_0xCD06C8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xCD06D4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `ChromaticAberrationComponent.OnDisable` — RVA `0xcd06d8`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public override void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong ChromaticAberrationComponent_OnDisable_RVAcd06d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCDF294UL /* metadata target: GraphicsUtils.Destroy */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(x19, 0x0UL);
        x0 = x19;
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `ChromaticAberrationComponent.Prepare` — RVA `0xcd0700`

- Lift status: **exact**; input span: 636 bytes; span to next metadata RVA: 636 bytes.
- Metadata signature: `public override void Prepare(Material uberMaterial) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=100 (informational only).

```csharp
public static ulong ChromaticAberrationComponent_Prepare_RVAcd0700(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13437088 = default(uint);
        uint __arm64_flags_left_13437108 = default(uint);
        uint __arm64_flags_right_13437088 = default(uint);
        uint __arm64_flags_right_13437108 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
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
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x5B3UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD077C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x5B3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD077C;
        label_0xCD077C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD0974;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x18UL)))) + (0x8UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD07A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD079CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD07A0;
        label_0xCD07A0:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD08F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD07C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD07C4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCD07C8;
        label_0xCD07C8:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD08EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE68UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x5 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177F454UL /* metadata target: Texture2D.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCD0974;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE80UL))));
        x0 = x21;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17983B0UL /* metadata target: Object.set_name */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177E294UL /* metadata target: Texture.set_filterMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177E214UL /* metadata target: Texture.set_wrapMode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177E2D8UL /* metadata target: Texture.set_anisoLevel */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(0x34UL))));
        x0 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798C88UL /* metadata target: Object.set_hideFlags */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x20;
        x1 = x21;
        RuntimeMemory.WriteU64(x20, x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE60UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0974;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x1 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD0978;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x433000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x1E0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x1E0UL))));
#endif
        __arm64_flags_left_13437088 = unchecked((uint)(x8));
        __arm64_flags_right_13437088 = unchecked((uint)0x1UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x20UL))), v0);
#endif
        if ((unchecked((uint)((__arm64_flags_left_13437088) - (__arm64_flags_right_13437088))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD0978;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x433000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x1B0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x1B0UL))));
#endif
        __arm64_flags_left_13437108 = unchecked((uint)(x8));
        __arm64_flags_right_13437108 = unchecked((uint)0x2UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x30UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x30UL))), v0);
#endif
        if (((!((__arm64_flags_left_13437108 >= __arm64_flags_right_13437108))) || (unchecked((uint)((__arm64_flags_left_13437108) - (__arm64_flags_right_13437108))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCD0978;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x760UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x760UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x1) + (0x40UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x1) + (0x40UL))), v0);
#endif
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0974;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177F708UL /* metadata target: Texture2D.SetPixels */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0974;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177F858UL /* metadata target: Texture2D.Apply */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD08EC;
        label_0xCD08EC:
        ;
        x21 = RuntimeMemory.ReadU64(x20);
        goto label_0xCD08F0;
        label_0xCD08F0:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xCD0974;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE78UL))));
        x20 = 0x1A8E000UL;
        x0 = x19;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x177ADF0UL /* metadata target: Material.EnableKeyword */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD0928;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD0920UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x20);
        goto label_0xCD0928;
        label_0xCD0928:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x490UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x22))), 0)), 0));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = x19;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177B718UL /* metadata target: Material.SetFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x2 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x4UL))))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x177AA38UL /* metadata target: Material.SetTexture */);
        label_0xCD0974:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCD0978;
        label_0xCD0978:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `ChromaticAberrationComponent.ctor` — RVA `0xcd097c`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong ChromaticAberrationComponent_ctor_RVAcd097c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x5B4UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE88UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD09B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x5B4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD09B0;
        label_0xCD09B0:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x11689F8UL);
        return default(ulong);
    }
```
