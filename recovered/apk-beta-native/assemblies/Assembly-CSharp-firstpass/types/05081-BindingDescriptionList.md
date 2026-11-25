# `BindingDescriptionList` — TypeDefIndex 5081

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x28` | `BindingDescription.BindingType` | `typeMask` |
| `0x2C` | `bool` | `addUnusedBindings` |
| `0x30` | `int` | `axisInputSourceMask` |
| `0x38` | `BindingDescriptionList.NameFormatter` | `menuNameFormatter` |

## `BindingDescriptionList.ctor` — RVA `0xc5d660`

- Lift status: **exact**; input span: 180 bytes; span to next metadata RVA: 180 bytes.
- Metadata signature: `public void .ctor(BindingDescription.BindingType typeMask, bool addUnusedBindings, int axisInputSourceMask, BindingDescriptionList.NameFormatter menuNameFormatter) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).

```csharp
public static ulong BindingDescriptionList_ctor_RVAc5d660(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x25 = 0x1BAB000UL;
        x24 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x2D1UL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x18UL))));
        x20 = x4;
        x19 = unchecked((ulong)(unchecked((uint)(x3))));
        x23 = unchecked((ulong)(unchecked((uint)(x2))));
        x22 = unchecked((ulong)(unchecked((uint)(x1))));
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x2D1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC5D6B8:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x24 = 0x1A8D000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x20UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xC5D6D0:
        ;
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0x1043A40UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x38UL))), x20);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)(0x1UL)))))));
        x0 = x21;
        x1 = x20;
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF0UL))), unchecked((uint)(x22)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x19)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `BindingDescriptionList.Setup` — RVA `0xc5d714`

- Lift status: **exact**; input span: 60 bytes; span to next metadata RVA: 60 bytes.
- Metadata signature: `public void Setup(BindingDescription.BindingType typeMask, bool addUnusedBindings, int axisInputSourceMask, BindingDescriptionList.NameFormatter menuNameFormatter) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong BindingDescriptionList_Setup_RVAc5d714(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x38UL))), x4);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF0UL))), unchecked((uint)(x1)));
        x0 = x20;
        x1 = x4;
        x19 = unchecked((ulong)(unchecked((uint)(x3))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x19)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `BindingDescriptionList.Add` — RVA `0xc5d750`

- Lift status: **exact**; input span: 848 bytes; span to next metadata RVA: 848 bytes.
- Metadata signature: `public void Add(InputBindingBase binding, string name, string menuPath, Object undoObject) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=125 (informational only).

```csharp
public static ulong BindingDescriptionList_Add_RVAc5d750(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_inverted_12966108 = default(uint);
        uint __arm64_flags_left_12965896 = default(uint);
        ulong __arm64_flags_left_12965916 = default(ulong);
        uint __arm64_flags_left_12965940 = default(uint);
        ulong __arm64_flags_left_12965960 = default(ulong);
        uint __arm64_flags_left_12965984 = default(uint);
        ulong __arm64_flags_left_12966004 = default(ulong);
        uint __arm64_flags_left_12966028 = default(uint);
        ulong __arm64_flags_left_12966048 = default(ulong);
        uint __arm64_flags_left_12966108 = default(uint);
        uint __arm64_flags_left_12966304 = default(uint);
        uint __arm64_flags_result_12966108 = default(uint);
        uint __arm64_flags_right_12965896 = default(uint);
        ulong __arm64_flags_right_12965916 = default(ulong);
        uint __arm64_flags_right_12965940 = default(uint);
        ulong __arm64_flags_right_12965960 = default(ulong);
        uint __arm64_flags_right_12965984 = default(uint);
        ulong __arm64_flags_right_12966004 = default(ulong);
        uint __arm64_flags_right_12966028 = default(uint);
        ulong __arm64_flags_right_12966048 = default(ulong);
        uint __arm64_flags_right_12966108 = default(uint);
        uint __arm64_flags_right_12966304 = default(uint);
        ulong __arm64_pair_address_12965860 = default(ulong);
        ulong __arm64_pair_address_12966144 = default(ulong);
        ulong __arm64_pair_address_12966248 = default(ulong);
        ulong __arm64_pair_address_12966264 = default(ulong);
        ulong __arm64_pair_address_12966320 = default(ulong);
        ulong __arm64_pair_address_12966352 = default(ulong);
        ulong __arm64_pair_address_12966372 = default(ulong);
        ulong __arm64_pair_address_12966400 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
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
        sp = unchecked((ulong)((sp) - (0x130UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))), x19);
        x24 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x2D2UL))))))));
        x19 = x4;
        x22 = x3;
        x23 = x2;
        x20 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5D7DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x990UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x7C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x2D2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5D7DC;
        label_0xC5D7DC:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x40UL))), 0x0UL);
        __arm64_pair_address_12965860 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12965860, v0);
#else
        __WriteVector128(__arm64_pair_address_12965860, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12965860) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12965860) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#endif
        if ((x20 == 0x0UL))
        {
            goto label_0xC5D8A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x990UL))));
        x8 = RuntimeMemory.ReadU64(x20);
        x10 = RuntimeMemory.ReadU64(x9);
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x130UL))))))));
        __arm64_flags_left_12965896 = unchecked((uint)(x9));
        __arm64_flags_right_12965896 = unchecked((uint)(x11));
        if ((!((__arm64_flags_left_12965896 >= __arm64_flags_right_12965896))))
        {
            goto label_0xC5D824;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x11 = unchecked((ulong)((x12) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12965916 = x11;
        __arm64_flags_right_12965916 = x10;
        if ((unchecked((ulong)((__arm64_flags_left_12965916) - (__arm64_flags_right_12965916))) == 0x0UL))
        {
            goto label_0xC5DA6C;
        }
        else
        {
            goto label_0xC5D824;
        }
        label_0xC5D824:
        ;
        x10 = 0x1A8C000UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0x988UL))));
        x10 = RuntimeMemory.ReadU64(x10);
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x130UL))))))));
        __arm64_flags_left_12965940 = unchecked((uint)(x9));
        __arm64_flags_right_12965940 = unchecked((uint)(x11));
        if ((!((__arm64_flags_left_12965940 >= __arm64_flags_right_12965940))))
        {
            goto label_0xC5D850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x11 = unchecked((ulong)((x12) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12965960 = x11;
        __arm64_flags_right_12965960 = x10;
        if ((unchecked((ulong)((__arm64_flags_left_12965960) - (__arm64_flags_right_12965960))) == 0x0UL))
        {
            goto label_0xC5DA78;
        }
        else
        {
            goto label_0xC5D850;
        }
        label_0xC5D850:
        ;
        x10 = 0x1A8C000UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0xBE8UL))));
        x10 = RuntimeMemory.ReadU64(x10);
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x130UL))))))));
        __arm64_flags_left_12965984 = unchecked((uint)(x9));
        __arm64_flags_right_12965984 = unchecked((uint)(x11));
        if ((!((__arm64_flags_left_12965984 >= __arm64_flags_right_12965984))))
        {
            goto label_0xC5D87C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x11 = unchecked((ulong)((x12) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12966004 = x11;
        __arm64_flags_right_12966004 = x10;
        if ((unchecked((ulong)((__arm64_flags_left_12966004) - (__arm64_flags_right_12966004))) == 0x0UL))
        {
            goto label_0xC5DA84;
        }
        else
        {
            goto label_0xC5D87C;
        }
        label_0xC5D87C:
        ;
        x10 = 0x1A8D000UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0x30UL))));
        x10 = RuntimeMemory.ReadU64(x10);
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x130UL))))))));
        __arm64_flags_left_12966028 = unchecked((uint)(x9));
        __arm64_flags_right_12966028 = unchecked((uint)(x11));
        if ((!((__arm64_flags_left_12966028 >= __arm64_flags_right_12966028))))
        {
            goto label_0xC5D8A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xFFFFFFFFFFFFFFF8UL))));
        __arm64_flags_left_12966048 = x8;
        __arm64_flags_right_12966048 = x10;
        if ((unchecked((ulong)((__arm64_flags_left_12966048) - (__arm64_flags_right_12966048))) == 0x0UL))
        {
            goto label_0xC5DA90;
        }
        else
        {
            goto label_0xC5D8A8;
        }
        label_0xC5D8A8:
        ;
        x28 = unchecked((ulong)(unchecked((uint)(0x7FUL))));
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5D8B0;
        label_0xC5D8B0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        x24 = x23;
        if ((x8 == 0x0UL))
        {
            goto label_0xC5D8D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x20;
        x2 = x23;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x24 = x0;
        goto label_0xC5D8D8;
        label_0xC5D8D8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x28UL))))));
        __arm64_flags_left_12966108 = unchecked((uint)(x28));
        __arm64_flags_right_12966108 = unchecked((uint)(x8));
        __arm64_flags_inverted_12966108 = (~(__arm64_flags_right_12966108));
        __arm64_flags_result_12966108 = unchecked((uint)((__arm64_flags_left_12966108) & (__arm64_flags_inverted_12966108)));
        x8 = unchecked((ulong)(((!((__arm64_flags_result_12966108 == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x25))) | (unchecked((uint)(x8)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5DA10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x29 = unchecked((ulong)((sp) + (0x10UL)));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = unchecked((ulong)((x29) | (0x8UL)));
        x1 = x23;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x40UL))), 0x0UL);
        __arm64_pair_address_12966144 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966144, v0);
#else
        __WriteVector128(__arm64_pair_address_12966144, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966144) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966144) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#endif
        x25 = unchecked((ulong)((x29) + (0x20UL)));
        x26 = unchecked((ulong)((x29) + (0x30UL)));
        x27 = unchecked((ulong)((x29) + (0x10UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x10UL))), unchecked((uint)(x28)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x27;
        x1 = x24;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x29) + (0x18UL)));
        x1 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x26;
        x1 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x25;
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x9 = 0x1A8D000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x28UL))));
        __arm64_pair_address_12966248 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12966248);
#else
        v0 = __ReadVector128(__arm64_pair_address_12966248);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12966248) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12966248) + (0x10UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x10 = RuntimeMemory.ReadU64(x9);
        __arm64_pair_address_12966264 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966264, v0);
#else
        __WriteVector128(__arm64_pair_address_12966264, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966264) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966264) + (0x10UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x70UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x70UL))), v2);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x8);
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x1CUL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5DA9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x21) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12966304 = unchecked((uint)(x9));
        __arm64_flags_right_12966304 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12966304 >= __arm64_flags_right_12966304))
        {
            goto label_0xC5D9E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x18UL))), unchecked((uint)(x10)));
        __arm64_pair_address_12966320 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12966320);
#else
        v2 = __ReadVector128(__arm64_pair_address_12966320);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12966320) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12966320) + (0x10UL))));
#endif
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#endif
        x11 = unchecked((ulong)(unchecked((uint)(0x38UL))));
        x8 = unchecked((ulong)((unchecked((ulong)((x9) * (unchecked((ulong)(unchecked((uint)(x11)))))))) + (x8)));
        x0 = unchecked((ulong)((x8) + (0x28UL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x50UL))), x10);
        __arm64_pair_address_12966352 = unchecked((ulong)((x8) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966352, v2);
#else
        __WriteVector128(__arm64_pair_address_12966352, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966352) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966352) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC5DA10;
        label_0xC5D9E0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0x20UL))));
        __arm64_pair_address_12966372 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12966372);
#else
        v0 = __ReadVector128(__arm64_pair_address_12966372);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12966372) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12966372) + (0x10UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x70UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x70UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x1 = unchecked((ulong)((sp) + (0x90UL)));
        x0 = x21;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        __arm64_pair_address_12966400 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966400, v0);
#else
        __WriteVector128(__arm64_pair_address_12966400, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966400) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966400) + (0x10UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xB0UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0xB0UL))), v2);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xC0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x1044334UL, x0, x1, x2, x3);
        goto label_0xC5DA10;
        label_0xC5DA10:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x7C8UL))));
        x0 = x22;
        x1 = x24;
        x3 = 0x0UL;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC5DA9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x3 = x0;
        x0 = x20;
        x1 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1C8UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1C8UL)))) + (0x8UL))));
        x2 = x19;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x120UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x130UL)));
        return x0;
        label_0xC5DA6C:
        ;
        x25 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x28 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        goto label_0xC5D8B0;
        label_0xC5DA78:
        ;
        x25 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x28 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC5D8B0;
        label_0xC5DA84:
        ;
        x25 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x28 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xC5D8B0;
        label_0xC5DA90:
        ;
        x25 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x28 = unchecked((ulong)(unchecked((uint)(0x40UL))));
        goto label_0xC5D8B0;
        label_0xC5DA9C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `BindingDescriptionList.Add` — RVA `0xc5daac`

- Lift status: **exact**; input span: 496 bytes; span to next metadata RVA: 496 bytes.
- Metadata signature: `public void Add(AxisBinding binding, InputRig.InputSource sourceType, string name, string menuPath, Object undoObject) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=66 (informational only).

```csharp
public static ulong BindingDescriptionList_Add_RVAc5daac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12966920 = default(uint);
        uint __arm64_flags_right_12966920 = default(uint);
        ulong __arm64_pair_address_12966664 = default(ulong);
        ulong __arm64_pair_address_12966756 = default(ulong);
        ulong __arm64_pair_address_12966864 = default(ulong);
        ulong __arm64_pair_address_12966880 = default(ulong);
        ulong __arm64_pair_address_12966936 = default(ulong);
        ulong __arm64_pair_address_12966968 = default(ulong);
        ulong __arm64_pair_address_12966988 = default(ulong);
        ulong __arm64_pair_address_12967016 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        sp = unchecked((ulong)((sp) - (0x130UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))), x19);
        x25 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x2D3UL))))))));
        x21 = x5;
        x22 = x4;
        x23 = x3;
        x24 = unchecked((ulong)(unchecked((uint)(x2))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5DB00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x2D3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5DB00;
        label_0xC5DB00:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x40UL))), 0x0UL);
        __arm64_pair_address_12966664 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966664, v0);
#else
        __WriteVector128(__arm64_pair_address_12966664, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966664) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966664) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#endif
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x28UL))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x30UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)(x24)))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5DC78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x25 = x23;
        if ((x8 == 0x0UL))
        {
            goto label_0xC5DB4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x20;
        x2 = x23;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x25 = x0;
        goto label_0xC5DB4C;
        label_0xC5DB4C:
        ;
        x29 = unchecked((ulong)((sp) + (0x10UL)));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = unchecked((ulong)((x29) | (0x8UL)));
        x1 = x23;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x40UL))), 0x0UL);
        __arm64_pair_address_12966756 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966756, v0);
#else
        __WriteVector128(__arm64_pair_address_12966756, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966756) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966756) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x10UL))), v0);
#endif
        x26 = unchecked((ulong)((x29) + (0x20UL)));
        x27 = unchecked((ulong)((x29) + (0x30UL)));
        x28 = unchecked((ulong)((x29) + (0x10UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x10UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x38UL))), unchecked((uint)(x24)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x28;
        x1 = x25;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x29) + (0x18UL)));
        x1 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x28UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x27;
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x26;
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x9 = 0x1A8D000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x28UL))));
        __arm64_pair_address_12966864 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12966864);
#else
        v0 = __ReadVector128(__arm64_pair_address_12966864);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12966864) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12966864) + (0x10UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x10 = RuntimeMemory.ReadU64(x9);
        __arm64_pair_address_12966880 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966880, v0);
#else
        __WriteVector128(__arm64_pair_address_12966880, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966880) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966880) + (0x10UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x70UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x70UL))), v2);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), x8);
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x1CUL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5DC98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12966920 = unchecked((uint)(x9));
        __arm64_flags_right_12966920 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12966920 >= __arm64_flags_right_12966920))
        {
            goto label_0xC5DC48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x18UL))), unchecked((uint)(x10)));
        __arm64_pair_address_12966936 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12966936);
#else
        v2 = __ReadVector128(__arm64_pair_address_12966936);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12966936) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12966936) + (0x10UL))));
#endif
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#endif
        x11 = unchecked((ulong)(unchecked((uint)(0x38UL))));
        x8 = unchecked((ulong)((unchecked((ulong)((x9) * (unchecked((ulong)(unchecked((uint)(x11)))))))) + (x8)));
        x0 = unchecked((ulong)((x8) + (0x28UL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x50UL))), x10);
        __arm64_pair_address_12966968 = unchecked((ulong)((x8) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12966968, v2);
#else
        __WriteVector128(__arm64_pair_address_12966968, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12966968) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12966968) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0x20UL))), v1);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC5DC78;
        label_0xC5DC48:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0x20UL))));
        __arm64_pair_address_12966988 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12966988);
#else
        v0 = __ReadVector128(__arm64_pair_address_12966988);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12966988) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12966988) + (0x10UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x70UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x70UL))));
#endif
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x1 = unchecked((ulong)((sp) + (0x90UL)));
        x0 = x19;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        __arm64_pair_address_12967016 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12967016, v0);
#else
        __WriteVector128(__arm64_pair_address_12967016, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12967016) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12967016) + (0x10UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0xB0UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0xB0UL))), v2);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xC0UL))), x9);
        x0 = RuntimeCalls.InvokeDirect(0x1044334UL, x0, x1, x2, x3);
        goto label_0xC5DC78;
        label_0xC5DC78:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x120UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x120UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x130UL)));
        return x0;
        label_0xC5DC98:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
