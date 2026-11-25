# `TouchControlSpriteAnimatorBase` — TypeDefIndex 5104

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x38` | `RectTransform` | `rectTr` |
| `0x40` | `Image` | `image` |
| `0x48` | `CanvasGroup` | `canvasGroup` |
| `0x50` | `Vector3` | `initialTransl` |
| `0x5C` | `Vector3` | `initialScale` |
| `0x68` | `Quaternion` | `initialRotation` |
| `0x78` | `SpriteConfig` | `spriteNeutral` |
| `0x80` | `SpriteConfig` | `curSprite` |
| `0x88` | `SpriteConfig` | `nextSprite` |
| `0x90` | `float` | `spriteAnimElapsed` |
| `0x94` | `Vector2` | `animOffsetStart` |
| `0x9C` | `Vector2` | `animOffsetCur` |
| `0xA4` | `Vector2` | `animScaleStart` |
| `0xAC` | `Vector2` | `animScaleCur` |
| `0xB4` | `float` | `animRotationStart` |
| `0xB8` | `float` | `animRotationCur` |
| `0xBC` | `Color` | `animColorStart` |
| `0xCC` | `Color` | `animColorCur` |
| `0xDC` | `Vector2` | `extraOffset` |
| `0xE4` | `Vector2` | `extraScale` |
| `0xEC` | `float` | `extraRotation` |

## `TouchControlSpriteAnimatorBase.ctor` — RVA `0xc63a74`

- Lift status: **partial**; input span: 216 bytes; span to next metadata RVA: 216 bytes.
- Metadata signature: `public void .ctor(Type sourceType) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xc63af4; reason: Unsupported instruction 'fmov' at 0xc63af8

```csharp
public static ulong TouchControlSpriteAnimatorBase_ctor_RVAc63a74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x10 = default(ulong);
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
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x2E9UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB58UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB58UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x2E9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC63AB0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F5ACUL /* metadata target: ComponentBase.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x9 = 0x431000UL;
        x10 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xB80UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((x10) + (0xEF0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((x10) + (0xEF0UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("fmov", 0xC63AF4UL);
        RuntimeCalls.Unsupported("fmov", 0xC63AF8UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x43UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x20UL))), v0);
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x54UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x30UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x20) + (0x44UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((x20) + (0x44UL))), v3);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x78UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        if ((x8 == 0x0UL))
        {
            label_0xC63B48:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x710UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((x9) + (0x710UL))));
#endif
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v0);
#endif
            x30 = RuntimeMemory.ReadU64(sp);
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControlSpriteAnimatorBase.OnInitComponent` — RVA `0xc63b4c`

- Lift status: **partial**; input span: 692 bytes; span to next metadata RVA: 692 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=100 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xc63db4; reason: Unsupported instruction 'fmov' at 0xc63dc4

```csharp
public static ulong TouchControlSpriteAnimatorBase_OnInitComponent_RVAc63b4c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12991776 = default(ulong);
        ulong __arm64_pair_address_12991796 = default(ulong);
        ulong __arm64_pair_address_12991808 = default(ulong);
        ulong __arm64_pair_address_12991812 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
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
        x20 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2EAUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xBB0UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63BBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x150UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x158UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x160UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2EAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC63BBC;
        label_0xC63BBC:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC639DCUL /* metadata target: TouchControlAnimatorBase.OnInitComponent */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x20 = x19;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63BF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63BF4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC63BF8;
        label_0xC63BF8:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63C88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x150UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x40UL))), x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63C44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63C40UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC63C44;
        label_0xC63C44:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63C88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC63DFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x158UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x20, x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC63C88;
        label_0xC63C88:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63C9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63C98UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC63C9C;
        label_0xC63C9C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63CCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC63DFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2C8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC63CCC;
        label_0xC63CCC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC63DFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x160UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC63DFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x179CB18UL /* metadata target: Transform.get_localPosition */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12991776 = unchecked((ulong)((x19) + (0x50UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12991776, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12991776) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x58UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179DB40UL /* metadata target: Transform.get_localScale */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12991796 = unchecked((ulong)((x19) + (0x5CUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12991796, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12991796) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x64UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D7F0UL /* metadata target: Transform.get_localRotation */, x0, x1, x2, x3);
        __arm64_pair_address_12991808 = unchecked((ulong)((x19) + (0x68UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12991808, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12991808) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        __arm64_pair_address_12991812 = unchecked((ulong)((x19) + (0x70UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12991812, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12991812) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63D68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC63D68;
        label_0xC63D68:
        ;
        x20 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x138UL))));
        x21 = 0x1BAB000UL;
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xDCUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x94UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x94UL))), v0);
#endif
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x32AUL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63DA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x32AUL))), unchecked((byte)(unchecked((uint)(x9)))));
        goto label_0xC63DA8;
        label_0xC63DA8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x760UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x9) + (0x760UL))));
#endif
        RuntimeCalls.Unsupported("fmov", 0xC63DB4UL);
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x8UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xD4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xB4UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xB4UL))), v0);
#endif
        RuntimeCalls.Unsupported("fmov", 0xC63DC4UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xE4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        v2 = v2;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xECUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xA4UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xA4UL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xC4UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xC4UL))), v0);
#endif
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC63E00UL /* metadata target: TouchControlSpriteAnimatorBase.BeginSpriteAnim */);
        label_0xC63DFC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchControlSpriteAnimatorBase.BeginSpriteAnim` — RVA `0xc63e00`

- Lift status: **partial**; input span: 492 bytes; span to next metadata RVA: 492 bytes.
- Metadata signature: `protected void BeginSpriteAnim(SpriteConfig spriteConfig, bool skipAnim, bool forceStart = false) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=54 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmul' at 0xc63edc

```csharp
public static ulong TouchControlSpriteAnimatorBase_BeginSpriteAnim_RVAc63e00(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12992036 = default(ulong);
        ulong __arm64_flags_right_12992036 = default(ulong);
        ulong __arm64_pair_address_12992124 = default(ulong);
        ulong __arm64_pair_address_12992236 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x50UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x20 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        x19 = x0;
        x21 = x1;
        x22 = unchecked((ulong)(unchecked((uint)(x2))));
        __arm64_flags_left_12992036 = x8;
        __arm64_flags_right_12992036 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12992036) - (__arm64_flags_right_12992036))) == 0x0UL))
        {
            goto label_0xC63EF8;
        }
        else
        {
            goto label_0xC63E2C;
        }
        label_0xC63E2C:
        ;
        if ((x8 == 0x0UL))
        {
            goto label_0xC63E54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x43UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63E54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63E38UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63E54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63E3CUL);
        }
        if ((unchecked((uint)((unchecked((uint)(x3))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63E54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63E40UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x88UL))), x21);
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC63FD4;
        label_0xC63E54:
        ;
        x0 = x20;
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x80UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x90UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63F0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63E6CUL);
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xC63FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63E70UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x20UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x21) + (0x20UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x21) + (0x20UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x21) + (0x20UL))));
#endif
        x0 = 0x0UL;
        __arm64_pair_address_12992124 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12992124, v0);
#else
        __WriteVector128(__arm64_pair_address_12992124, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12992124) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12992124) + (0x10UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xCCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xCCUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x10UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xBCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xBCUL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63FD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63E94UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x21) + (0x38UL))))), 0));
        x20 = 0x1BAB000UL;
        v0 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x94UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x94UL))), v0);
#endif
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x32AUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63EC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x32AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC63EC0;
        label_0xC63EC0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x30UL))))), 0));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x8UL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC63EDCUL);
        v0 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xA4UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xA4UL))), v0);
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x34UL))))), 0));
        __arm64_pair_address_12992236 = unchecked((ulong)((x19) + (0xB4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12992236, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12992236) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC64070UL /* metadata target: TouchControlSpriteAnimatorBase.ApplySpriteAnimation */, x0, x1, x2, x3);
        goto label_0xC63FD4;
        label_0xC63EF8:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC63FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x43UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63E2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63F04UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63FD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63F08UL);
        }
        goto label_0xC63E2C;
        label_0xC63F0C:
        ;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x19) + (0xCCUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x19) + (0xCCUL))));
#endif
        x0 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xBCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xBCUL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63FD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x9CUL))));
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xACUL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xB8UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x94UL))), x9);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xA4UL))), x10);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xB4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xC63FE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x42UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x138UL))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63F88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x32AUL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63F74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x32AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = RuntimeMemory.ReadU64(x20);
        goto label_0xC63F74;
        label_0xC63F74:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0x8UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xA4UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC63FE8;
        }
        else
        {
            goto label_0xC63F88;
        }
        label_0xC63F88:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x40UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63FC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1E0UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC63FB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = RuntimeMemory.ReadU64(x20);
        goto label_0xC63FB4;
        label_0xC63FB4:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x94UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC63FE8;
        }
        else
        {
            goto label_0xC63FC8;
        }
        label_0xC63FC8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x41UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC63FD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC63FD0UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xB4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC63FD4;
        label_0xC63FD4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        sp = unchecked((ulong)((sp) + (0x50UL)));
        return x0;
        label_0xC63FE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControlSpriteAnimatorBase.OnDisableComponent` — RVA `0xc63fec`

- Lift status: **exact**; input span: 132 bytes; span to next metadata RVA: 132 bytes.
- Metadata signature: `protected override void OnDisableComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong TouchControlSpriteAnimatorBase_OnDisableComponent_RVAc63fec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12992536 = default(ulong);
        ulong __arm64_pair_address_12992568 = default(ulong);
        ulong __arm64_pair_address_12992600 = default(ulong);
        ulong __arm64_pair_address_12992604 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC64008;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC64008:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC6406C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC64018UL);
        }
        __arm64_pair_address_12992536 = unchecked((ulong)((x19) + (0x54UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12992536)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12992536) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x50UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179CBA4UL /* metadata target: Transform.set_localPosition */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC6406C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC64038UL);
        }
        __arm64_pair_address_12992568 = unchecked((ulong)((x19) + (0x60UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12992568)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12992568) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x5CUL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC6406C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC64058UL);
        }
        __arm64_pair_address_12992600 = unchecked((ulong)((x19) + (0x70UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12992600)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12992600) + (0x4UL))))), 0));
        __arm64_pair_address_12992604 = unchecked((ulong)((x19) + (0x68UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12992604)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12992604) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x179D874UL /* metadata target: Transform.set_localRotation */);
        label_0xC6406C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControlSpriteAnimatorBase.ApplySpriteAnimation` — RVA `0xc64070`

- Lift status: **partial**; input span: 788 bytes; span to next metadata RVA: 788 bytes.
- Metadata signature: `public void ApplySpriteAnimation() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=75 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmul' at 0xc64250; reason: Unsupported instruction 'fadd' at 0xc64258; reason: Unsupported instruction 'fmul' at 0xc6425c; reason: Unsupported instruction 'fadd' at 0xc64260; reason: Unsupported instruction 'mov' at 0xc64264; reason: Unsupported instruction 'fmul' at 0xc64368; reason: Unsupported instruction 'fmul' at 0xc6436c; reason: Unsupported instruction 'mov' at 0xc64370

```csharp
public static ulong TouchControlSpriteAnimatorBase_ApplySpriteAnimation_RVAc64070(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12992708 = default(float);
        float __arm64_float_flags_right_12992708 = default(float);
        ulong __arm64_pair_address_12992628 = default(ulong);
        ulong __arm64_pair_address_12992632 = default(ulong);
        ulong __arm64_pair_address_12992772 = default(ulong);
        ulong __arm64_pair_address_12992776 = default(ulong);
        ulong __arm64_pair_address_12993008 = default(ulong);
        ulong __arm64_pair_address_12993012 = default(ulong);
        ulong __arm64_pair_address_12993072 = default(ulong);
        ulong __arm64_pair_address_12993196 = default(ulong);
        ulong __arm64_pair_address_12993200 = default(ulong);
        ulong __arm64_pair_address_12993372 = default(ulong);
        ulong __arm64_pair_address_12993376 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v16 = default(RuntimeVector128);
        RuntimeVector128 v17 = default(RuntimeVector128);
        RuntimeVector128 v18 = default(RuntimeVector128);
        RuntimeVector128 v19 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v20 = default(RuntimeVector128);
        RuntimeVector128 v21 = default(RuntimeVector128);
        RuntimeVector128 v22 = default(RuntimeVector128);
        RuntimeVector128 v23 = default(RuntimeVector128);
        RuntimeVector128 v24 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x60UL)));
        __arm64_pair_address_12992628 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12992628, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12992628) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12992632 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12992632, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12992632) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2EBUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC640A8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2EBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC640A8;
        label_0xC640A8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC640B0UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xD8UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791624UL /* metadata target: Behaviour.get_enabled */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        __arm64_float_flags_left_12992708 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12992708 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)((((__arm64_float_flags_left_12992708 <= __arm64_float_flags_right_12992708) || ((__arm64_float_flags_left_12992708 != __arm64_float_flags_left_12992708) || (__arm64_float_flags_right_12992708 != __arm64_float_flags_right_12992708))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) ^ (unchecked((uint)(x0)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC640FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791624UL /* metadata target: Behaviour.get_enabled */, x0, x1, x2, x3);
        x8 = unchecked((ulong)((~(unchecked((uint)(x0))))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0x1UL)))))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC640FC;
        label_0xC640FC:
        ;
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        __arm64_pair_address_12992772 = unchecked((ulong)((x19) + (0xCCUL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12992772)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12992772) + (0x4UL))))), 0));
        __arm64_pair_address_12992776 = unchecked((ulong)((x19) + (0xD4UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12992776)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12992776) + (0x4UL))))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC64120;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6411CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC64120;
        label_0xC64120:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6414C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6413CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xD8UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x196DDD4UL /* metadata target: CanvasGroup.set_alpha */, x0, x1, x2, x3);
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC6414C;
        label_0xC6414C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        v3 = v11;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC64194;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC64190UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC64194;
        label_0xC64194:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC641B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC641BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC641B0UL);
        }
        goto label_0xC64380;
        label_0xC641B4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            goto label_0xC641BC;
        }
        label_0xC641BC:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1813790UL /* metadata target: Image.set_sprite */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC641E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC63890UL /* metadata target: TouchControlAnimatorBase.IsIllegallyAttachedToSource */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC64200;
        }
        else
        {
            goto label_0xC641E8;
        }
        label_0xC641E8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_12993008 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12993008)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12993008) + (0x8UL))))), 0));
        __arm64_pair_address_12993012 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12993012)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12993012) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x60UL)));
        return x0;
        label_0xC64200:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        RuntimeMemory.WriteF64(sp, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v3.GetUInt64(0)))));
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC64230UL);
        }
        __arm64_pair_address_12993072 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12993072);
#else
        v2 = __ReadVector128(__arm64_pair_address_12993072);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v6 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12993072) + (0x10UL))));
#else
        v6 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12993072) + (0x10UL))));
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x58UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x9CUL))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xDCUL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x50UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v6 = v2;
        v2 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fmul", 0xC64250UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fadd", 0xC64258UL);
        RuntimeCalls.Unsupported("fmul", 0xC6425CUL);
        RuntimeCalls.Unsupported("fadd", 0xC64260UL);
        RuntimeCalls.Unsupported("mov", 0xC64264UL);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179CBA4UL /* metadata target: Transform.set_localPosition */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xB8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xECUL))))), 0));
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3E4UL))))), 0));
        x20 = x0;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178B12CUL /* metadata target: Quaternion.Internal_FromEulerRad */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC642ACUL);
        }
        __arm64_pair_address_12993196 = unchecked((ulong)((x19) + (0x70UL)));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12993196)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12993196) + (0x4UL))))), 0));
        __arm64_pair_address_12993200 = unchecked((ulong)((x19) + (0x68UL)));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12993200)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12993200) + (0x4UL))))), 0));
        x0 = x20;
        x1 = 0x0UL;
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v17 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v18 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v19 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v20 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v21 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v22 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v23 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v24 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v17.GetUInt64(0)))), 0))))), 0));
        v16 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v21.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v22.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v24.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v18.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v20.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v16.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v19.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v23.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D874UL /* metadata target: Transform.set_localRotation */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC64380;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC64340UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x64UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xACUL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xE4UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x5CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_12993372 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12993372)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12993372) + (0x8UL))))), 0));
        __arm64_pair_address_12993376 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12993376)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12993376) + (0x8UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC64368UL);
        RuntimeCalls.Unsupported("fmul", 0xC6436CUL);
        RuntimeCalls.Unsupported("mov", 0xC64370UL);
        x1 = 0x0UL;
        sp = unchecked((ulong)((sp) + (0x60UL)));
        return RuntimeCalls.InvokeDirect(0x179DBE0UL /* metadata target: Transform.set_localScale */);
        label_0xC64380:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControlSpriteAnimatorBase.UpdateSpriteAnimation` — RVA `0xc64384`

- Lift status: **partial**; input span: 700 bytes; span to next metadata RVA: 700 bytes.
- Metadata signature: `protected void UpdateSpriteAnimation(bool skipAnim) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=41 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc643e4; reason: Unknown IR expression at 0xc643e4; reason: Unsupported instruction 'fsub' at 0xc64448; reason: Unsupported instruction 'fmul' at 0xc6444c; reason: Unsupported instruction 'fadd' at 0xc64450; reason: Unsupported instruction 'mov' at 0xc6447c; reason: Unsupported instruction 'mov' at 0xc64480; reason: Unsupported instruction 'mov' at 0xc64484

```csharp
public static ulong TouchControlSpriteAnimatorBase_UpdateSpriteAnimation_RVAc64384(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12993500 = default(ulong);
        ulong __arm64_flags_right_12993500 = default(ulong);
        float __arm64_float_flags_left_12993476 = default(float);
        float __arm64_float_flags_left_12993576 = default(float);
        float __arm64_float_flags_left_12993584 = default(float);
        float __arm64_float_flags_left_12993600 = default(float);
        float __arm64_float_flags_left_12993764 = default(float);
        float __arm64_float_flags_left_12993772 = default(float);
        float __arm64_float_flags_left_12993788 = default(float);
        float __arm64_float_flags_left_12993908 = default(float);
        float __arm64_float_flags_left_12993916 = default(float);
        float __arm64_float_flags_left_12993928 = default(float);
        float __arm64_float_flags_left_12993976 = default(float);
        float __arm64_float_flags_left_12993996 = default(float);
        float __arm64_float_flags_left_12994036 = default(float);
        float __arm64_float_flags_left_12994052 = default(float);
        float __arm64_float_flags_left_12994064 = default(float);
        float __arm64_float_flags_right_12993476 = default(float);
        float __arm64_float_flags_right_12993576 = default(float);
        float __arm64_float_flags_right_12993584 = default(float);
        float __arm64_float_flags_right_12993600 = default(float);
        float __arm64_float_flags_right_12993764 = default(float);
        float __arm64_float_flags_right_12993772 = default(float);
        float __arm64_float_flags_right_12993788 = default(float);
        float __arm64_float_flags_right_12993908 = default(float);
        float __arm64_float_flags_right_12993916 = default(float);
        float __arm64_float_flags_right_12993928 = default(float);
        float __arm64_float_flags_right_12993976 = default(float);
        float __arm64_float_flags_right_12993996 = default(float);
        float __arm64_float_flags_right_12994036 = default(float);
        float __arm64_float_flags_right_12994052 = default(float);
        float __arm64_float_flags_right_12994064 = default(float);
        float __arm64_fp_left_12993596 = default(float);
        float __arm64_fp_left_12993784 = default(float);
        float __arm64_fp_left_12993924 = default(float);
        float __arm64_fp_left_12994032 = default(float);
        float __arm64_fp_left_12994056 = default(float);
        float __arm64_fp_right_12993596 = default(float);
        float __arm64_fp_right_12993784 = default(float);
        float __arm64_fp_right_12993924 = default(float);
        float __arm64_fp_right_12994032 = default(float);
        float __arm64_fp_right_12994056 = default(float);
        ulong __arm64_pair_address_12993416 = default(ulong);
        ulong __arm64_pair_address_12993552 = default(ulong);
        ulong __arm64_pair_address_12993680 = default(ulong);
        ulong __arm64_pair_address_12993684 = default(ulong);
        ulong __arm64_pair_address_12994096 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x40UL)));
        __arm64_pair_address_12993416 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12993416, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12993416) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x90UL))))), 0));
        x19 = x0;
        x0 = 0x0UL;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x0 = RuntimeCalls.InvokeDirect(0xC5834CUL /* metadata target: CFUtils.get_realDeltaTimeClamped */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x90UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xC6463C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x43UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC643F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC643C0UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x44UL))))), 0));
        __arm64_float_flags_left_12993476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12993476 < __arm64_float_flags_right_12993476) || ((__arm64_float_flags_left_12993476 != __arm64_float_flags_left_12993476) || (__arm64_float_flags_right_12993476 != __arm64_float_flags_right_12993476))))
        {
            goto label_0xC643F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x88UL))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        __arm64_flags_left_12993500 = x8;
        __arm64_flags_right_12993500 = 0x0UL;
        x8 = unchecked((ulong)(unchecked((uint)(0x78UL))));
        RuntimeCalls.Unsupported("csel", 0xC643E4UL);
        x8 = (__Unsupported<bool>("Unknown IR expression") ? x8 : x9);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (x8))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC63E00UL /* metadata target: TouchControlSpriteAnimatorBase.BeginSpriteAnim */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        goto label_0xC643F8;
        label_0xC643F8:
        ;
        if ((x8 == 0x0UL))
        {
            goto label_0xC6463C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC643FCUL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x19) + (0xBCUL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x19) + (0xBCUL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x20UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x8) + (0x20UL))));
#endif
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC64418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC64410UL);
        }
        __arm64_pair_address_12993552 = unchecked((ulong)((x8) + (0x48UL)));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12993552)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12993552) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        goto label_0xC64418;
        label_0xC64418:
        ;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x90UL))))), 0));
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        __arm64_float_flags_left_12993576 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993576 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12993584 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993584 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((((__arm64_float_flags_left_12993576 <= __arm64_float_flags_right_12993576) || ((__arm64_float_flags_left_12993576 != __arm64_float_flags_left_12993576) || (__arm64_float_flags_right_12993576 != __arm64_float_flags_right_12993576))) ? (__arm64_float_flags_left_12993584 < __arm64_float_flags_right_12993584) : true) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        __arm64_fp_left_12993596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_fp_right_12993596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12993596 != __arm64_fp_left_12993596) ? __arm64_fp_left_12993596 : ((__arm64_fp_right_12993596 != __arm64_fp_right_12993596) ? __arm64_fp_right_12993596 : (((__arm64_fp_left_12993596 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12993596 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12993596), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12993596), 0))))), 0) : ((__arm64_fp_left_12993596 <= __arm64_fp_right_12993596) ? __arm64_fp_left_12993596 : __arm64_fp_right_12993596))))), 0));
        __arm64_float_flags_left_12993600 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993600 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12993600 >= __arm64_float_flags_right_12993600) || ((__arm64_float_flags_left_12993600 != __arm64_float_flags_left_12993600) || (__arm64_float_flags_right_12993600 != __arm64_float_flags_right_12993600))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC64448UL);
        RuntimeCalls.Unsupported("fmul", 0xC6444CUL);
        RuntimeCalls.Unsupported("fadd", 0xC64450UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(sp, v0);
#else
        __WriteVector128(sp, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xCCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xCCUL))), v0);
#endif
        if ((x0 == 0x0UL))
        {
            goto label_0xC6463C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x358UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x360UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        v4 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(sp);
#else
        v0 = __ReadVector128(sp);
#endif
        x0 = 0x0UL;
        RuntimeCalls.Unsupported("mov", 0xC6447CUL);
        RuntimeCalls.Unsupported("mov", 0xC64480UL);
        RuntimeCalls.Unsupported("mov", 0xC64484UL);
        x0 = RuntimeCalls.InvokeDirect(0xC589F8UL /* metadata target: CFUtils.ScaleColorAlpha */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = 0x0UL;
        __arm64_pair_address_12993680 = unchecked((ulong)((x19) + (0xCCUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12993680, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12993680) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        __arm64_pair_address_12993684 = unchecked((ulong)((x19) + (0xD4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12993684, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12993684) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC64624;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC63890UL /* metadata target: TouchControlAnimatorBase.IsIllegallyAttachedToSource */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC64624;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC6463C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC644B4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x94UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x38UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC644D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC644C8UL);
        }
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x58UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x48UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        goto label_0xC644D4;
        label_0xC644D4:
        ;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x90UL))))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC644D8UL);
        x21 = 0x1BAB000UL;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0xA4UL))))), 0));
        __arm64_float_flags_left_12993764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12993772 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993772 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((((__arm64_float_flags_left_12993764 <= __arm64_float_flags_right_12993764) || ((__arm64_float_flags_left_12993764 != __arm64_float_flags_left_12993764) || (__arm64_float_flags_right_12993764 != __arm64_float_flags_right_12993764))) ? (__arm64_float_flags_left_12993772 < __arm64_float_flags_right_12993772) : true) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        __arm64_fp_left_12993784 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_fp_right_12993784 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12993784 != __arm64_fp_left_12993784) ? __arm64_fp_left_12993784 : ((__arm64_fp_right_12993784 != __arm64_fp_right_12993784) ? __arm64_fp_right_12993784 : (((__arm64_fp_left_12993784 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12993784 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12993784), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12993784), 0))))), 0) : ((__arm64_fp_left_12993784 <= __arm64_fp_right_12993784) ? __arm64_fp_left_12993784 : __arm64_fp_right_12993784))))), 0));
        __arm64_float_flags_left_12993788 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993788 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12993788 >= __arm64_float_flags_right_12993788) || ((__arm64_float_flags_left_12993788 != __arm64_float_flags_left_12993788) || (__arm64_float_flags_right_12993788 != __arm64_float_flags_right_12993788))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC64504UL);
        RuntimeCalls.Unsupported("fadd", 0xC64508UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x9CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x32AUL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC64534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x32AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC6463C;
        }
        else
        {
            goto label_0xC64534;
        }
        label_0xC64534:
        ;
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x138UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x30UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x9 = RuntimeMemory.ReadU64(x9);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0x8UL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC64554UL);
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC64568;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6455CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x50UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x48UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        goto label_0xC64568;
        label_0xC64568:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x90UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        RuntimeCalls.Unsupported("fsub", 0xC64570UL);
        __arm64_float_flags_left_12993908 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993908 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12993916 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993916 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((((__arm64_float_flags_left_12993908 <= __arm64_float_flags_right_12993908) || ((__arm64_float_flags_left_12993908 != __arm64_float_flags_left_12993908) || (__arm64_float_flags_right_12993908 != __arm64_float_flags_right_12993908))) ? (__arm64_float_flags_left_12993916 < __arm64_float_flags_right_12993916) : true) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))), 0));
        __arm64_fp_left_12993924 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_fp_right_12993924 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12993924 != __arm64_fp_left_12993924) ? __arm64_fp_left_12993924 : ((__arm64_fp_right_12993924 != __arm64_fp_right_12993924) ? __arm64_fp_right_12993924 : (((__arm64_fp_left_12993924 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12993924 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12993924), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12993924), 0))))), 0) : ((__arm64_fp_left_12993924 <= __arm64_fp_right_12993924) ? __arm64_fp_left_12993924 : __arm64_fp_right_12993924))))), 0));
        __arm64_float_flags_left_12993928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993928 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12993928 >= __arm64_float_flags_right_12993928) || ((__arm64_float_flags_left_12993928 != __arm64_float_flags_left_12993928) || (__arm64_float_flags_right_12993928 != __arm64_float_flags_right_12993928))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC64590UL);
        RuntimeCalls.Unsupported("fadd", 0xC64594UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xACUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xB4UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x34UL))))), 0));
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC645B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC645A8UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x54UL))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x48UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        goto label_0xC645B4;
        label_0xC645B4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        __arm64_float_flags_left_12993976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
        RuntimeCalls.Unsupported("fccmp", 0xC645CCUL);
        __arm64_float_flags_left_12993996 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12993996 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC645D8UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        RuntimeCalls.Unsupported("fcsel", 0xC645ECUL);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        __arm64_fp_left_12994032 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_fp_right_12994032 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12994032 != __arm64_fp_left_12994032) ? __arm64_fp_left_12994032 : ((__arm64_fp_right_12994032 != __arm64_fp_right_12994032) ? __arm64_fp_right_12994032 : (((__arm64_fp_left_12994032 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12994032 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12994032), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12994032), 0))))), 0) : ((__arm64_fp_left_12994032 <= __arm64_fp_right_12994032) ? __arm64_fp_left_12994032 : __arm64_fp_right_12994032))))), 0));
        __arm64_float_flags_left_12994036 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12994036 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12994036 >= __arm64_float_flags_right_12994036) || ((__arm64_float_flags_left_12994036 != __arm64_float_flags_left_12994036) || (__arm64_float_flags_right_12994036 != __arm64_float_flags_right_12994036))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12994052 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12994052 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_fp_left_12994056 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_fp_right_12994056 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12994056 != __arm64_fp_left_12994056) ? __arm64_fp_left_12994056 : ((__arm64_fp_right_12994056 != __arm64_fp_right_12994056) ? __arm64_fp_right_12994056 : (((__arm64_fp_left_12994056 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12994056 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12994056), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12994056), 0))))), 0) : ((__arm64_fp_left_12994056 <= __arm64_fp_right_12994056) ? __arm64_fp_left_12994056 : __arm64_fp_right_12994056))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12994052 > __arm64_float_flags_right_12994052) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12994064 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12994064 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12994064 >= __arm64_float_flags_right_12994064) || ((__arm64_float_flags_left_12994064 != __arm64_float_flags_left_12994064) || (__arm64_float_flags_right_12994064 != __arm64_float_flags_right_12994064))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xB8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC64624;
        label_0xC64624:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12994096 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12994096)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12994096) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0xC64070UL /* metadata target: TouchControlSpriteAnimatorBase.ApplySpriteAnimation */);
        label_0xC6463C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchControlSpriteAnimatorBase.GetAnimLerpFactor` — RVA `0xc64640`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `private float GetAnimLerpFactor(float duration) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchControlSpriteAnimatorBase_GetAnimLerpFactor_RVAc64640(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x90UL))))), 0));
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        return x0;
        return default(ulong);
    }
```
