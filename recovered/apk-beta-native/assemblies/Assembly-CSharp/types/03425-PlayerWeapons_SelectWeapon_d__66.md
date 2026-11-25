# `PlayerWeapons.<SelectWeapon>d__66` — TypeDefIndex 3425

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `PlayerWeapons` | `<>4__this` |
| `0x28` | `int` | `index` |
| `0x2C` | `bool` | `isOffhandThrow` |
| `0x2D` | `bool` | `endOffhandThrow` |

## `PlayerWeapons.<SelectWeapon>d__66.ctor` — RVA `0xcb3c9c`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong PlayerWeapons_SelectWeapon_d__66_ctor_RVAcb3c9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x10UL))), unchecked((uint)(x19)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `PlayerWeapons.<SelectWeapon>d__66.Dispose` — RVA `0xcb3eac`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong PlayerWeapons_SelectWeapon_d__66_Dispose_RVAcb3eac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `PlayerWeapons.<SelectWeapon>d__66.MoveNext` — RVA `0xcb3eb0`

- Lift status: **partial**; input span: 2476 bytes; span to next metadata RVA: 2476 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=310 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'ldr' at 0xcb4358

```csharp
public static uint PlayerWeapons_SelectWeapon_d__66_MoveNext_RVAcb3eb0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13320072 = default(uint);
        uint __arm64_flags_left_13320160 = default(uint);
        uint __arm64_flags_left_13320236 = default(uint);
        uint __arm64_flags_left_13320632 = default(uint);
        uint __arm64_flags_left_13321040 = default(uint);
        uint __arm64_flags_left_13321208 = default(uint);
        uint __arm64_flags_left_13321216 = default(uint);
        uint __arm64_flags_left_13321260 = default(uint);
        uint __arm64_flags_left_13321280 = default(uint);
        uint __arm64_flags_left_13321340 = default(uint);
        uint __arm64_flags_left_13321380 = default(uint);
        uint __arm64_flags_left_13321440 = default(uint);
        uint __arm64_flags_left_13321500 = default(uint);
        uint __arm64_flags_left_13321540 = default(uint);
        uint __arm64_flags_left_13321592 = default(uint);
        uint __arm64_flags_left_13321688 = default(uint);
        uint __arm64_flags_left_13321724 = default(uint);
        uint __arm64_flags_left_13321776 = default(uint);
        uint __arm64_flags_left_13321956 = default(uint);
        uint __arm64_flags_left_13322096 = default(uint);
        uint __arm64_flags_left_13322140 = default(uint);
        uint __arm64_flags_right_13320072 = default(uint);
        uint __arm64_flags_right_13320160 = default(uint);
        uint __arm64_flags_right_13320236 = default(uint);
        uint __arm64_flags_right_13320632 = default(uint);
        uint __arm64_flags_right_13321040 = default(uint);
        uint __arm64_flags_right_13321208 = default(uint);
        uint __arm64_flags_right_13321216 = default(uint);
        uint __arm64_flags_right_13321260 = default(uint);
        uint __arm64_flags_right_13321280 = default(uint);
        uint __arm64_flags_right_13321340 = default(uint);
        uint __arm64_flags_right_13321380 = default(uint);
        uint __arm64_flags_right_13321440 = default(uint);
        uint __arm64_flags_right_13321500 = default(uint);
        uint __arm64_flags_right_13321540 = default(uint);
        uint __arm64_flags_right_13321592 = default(uint);
        uint __arm64_flags_right_13321688 = default(uint);
        uint __arm64_flags_right_13321724 = default(uint);
        uint __arm64_flags_right_13321776 = default(uint);
        uint __arm64_flags_right_13321956 = default(uint);
        uint __arm64_flags_right_13322096 = default(uint);
        uint __arm64_flags_right_13322140 = default(uint);
        float __arm64_float_flags_left_13320752 = default(float);
        float __arm64_float_flags_left_13320992 = default(float);
        float __arm64_float_flags_left_13321864 = default(float);
        float __arm64_float_flags_right_13320752 = default(float);
        float __arm64_float_flags_right_13320992 = default(float);
        float __arm64_float_flags_right_13321864 = default(float);
        ulong __arm64_load_address_13322284 = default(ulong);
        ulong __arm64_pair_address_13319860 = default(ulong);
        ulong __arm64_pair_address_13319864 = default(ulong);
        ulong __arm64_pair_address_13319868 = default(ulong);
        ulong __arm64_pair_address_13322272 = default(ulong);
        ulong __arm64_pair_address_13322276 = default(ulong);
        ulong __arm64_pair_address_13322280 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v14 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF60UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF60UL)));
        __arm64_pair_address_13319860 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13319860, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13319860) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13319864 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13319864, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13319864) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13319868 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13319868, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13319868) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x4DBUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB3F80;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x178UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x538UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x158UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x660UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x668UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x648UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x498UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x670UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x678UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x4DBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCB3F80;
        label_0xCB3F80:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        __arm64_flags_left_13320072 = unchecked((uint)(x8));
        __arm64_flags_right_13320072 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13320072) - (__arm64_flags_right_13320072))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB43A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB3F90UL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB4804;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        x0 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = x23;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xC0UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x21) + (0x1CUL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13320160 = unchecked((uint)(x9));
        __arm64_flags_right_13320160 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13320160 >= __arm64_flags_right_13320160))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x538UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x20 = x23;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xB0UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x38UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x88UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0x28UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13320236 = unchecked((uint)(x9));
        __arm64_flags_right_13320236 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13320236 >= __arm64_flags_right_13320236))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x1A8E000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x158UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB47FC;
        }
        else
        {
            goto label_0xCB405C;
        }
        label_0xCB405C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB406C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB4804;
        }
        else
        {
            goto label_0xCB406C;
        }
        label_0xCB406C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x88UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1A0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB4804;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x17CUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB4804;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x28UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB40B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB40B0UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x120UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xCB40B4;
        label_0xCB40B4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB40BCUL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x2D0UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x72DUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB41A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xD8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x740UL))));
        x0 = RuntimeMemory.ReadU64(x24);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB40EC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB40E8UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCB40EC;
        label_0xCB40EC:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB4118;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x740UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17799D0UL /* metadata target: Renderer.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCB4118;
        label_0xCB4118:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(x24);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x748UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB4134;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4130UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCB4134;
        label_0xCB4134:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB4160;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x748UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCB4160;
        label_0xCB4160:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(x24);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x750UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB417C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4178UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCB417C;
        label_0xCB417C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798274UL /* metadata target: Object.op_Implicit */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB41A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x750UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCB41A8;
        label_0xCB41A8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x134UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x130UL))))));
        __arm64_flags_left_13320632 = unchecked((uint)(x8));
        __arm64_flags_right_13320632 = unchecked((uint)(x9));
        if ((unchecked((uint)((__arm64_flags_left_13320632) - (__arm64_flags_right_13320632))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB41F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x129UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB41F8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB41F4UL)));
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x3B8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xCB41F8;
        label_0xCB41F8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4200UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x129UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x498UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x17960E0UL /* metadata target: MonoBehaviour.StopCoroutine */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, x1, x2, x3);
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x23) + (0x120UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179AD58UL /* metadata target: Time.get_timeSinceLevelLoad */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_13320752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13320752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13320752 <= __arm64_float_flags_right_13320752) || ((__arm64_float_flags_left_13320752 != __arm64_float_flags_left_13320752) || (__arm64_float_flags_right_13320752 != __arm64_float_flags_right_13320752))))
        {
            goto label_0xCB42B0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x17EUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB4280;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x129UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB4280;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x158UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x140UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x158UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4264UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x158UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */, x0, x1, x2, x3);
        goto label_0xCB4280;
        label_0xCB4280:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4288UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767EB4UL /* metadata target: Animator.set_speed */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x660UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        goto label_0xCB42B0;
        label_0xCB42B0:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D14UL /* metadata target: GameObject.get_activeSelf */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB4314;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x88UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2B0UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB42E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2DFUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB4834;
        }
        else
        {
            goto label_0xCB42E8;
        }
        label_0xCB42E8:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x668UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x3A6UL))), unchecked((byte)(unchecked((uint)(x9)))));
        goto label_0xCB4314;
        label_0xCB4314:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD58UL /* metadata target: Time.get_timeSinceLevelLoad */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        __arm64_float_flags_left_13320992 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13320992 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13320992 <= __arm64_float_flags_right_13320992) || ((__arm64_float_flags_left_13320992 != __arm64_float_flags_left_13320992) || (__arm64_float_flags_right_13320992 != __arm64_float_flags_right_13320992))))
        {
            goto label_0xCB43AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x98UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x345UL))))))));
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2CUL))))))));
        x11 = 0x432000UL;
        x11 = unchecked((ulong)((x11) + (0x168UL)));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) ^ (unchecked((uint)(0x1UL)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) | (unchecked((uint)(x10)))))));
        __arm64_flags_left_13321040 = unchecked((uint)(x9));
        __arm64_flags_right_13321040 = unchecked((uint)0x0UL);
        x9 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_13321040) - (__arm64_flags_right_13321040))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("ldr", 0xCB4358UL);
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x238UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4F4UL))))), 0));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1799B00UL /* metadata target: WaitForSeconds.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x0)));
        goto label_0xCB4808;
        label_0xCB43A0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x23 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            goto label_0xCB43AC;
        }
        label_0xCB43AC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x25 = 0x1A8E000UL;
        x26 = 0x1A8E000UL;
        x9 = 0x432000UL;
        x29 = 0x1A8E000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x538UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x158UL))));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x46CUL))))), 0));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0x668UL))));
        x20 = unchecked((ulong)((x23) + (0xB8UL)));
        x21 = unchecked((ulong)((x23) + (0x98UL)));
        x24 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x27 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF000000UL)), 0)), 0));
        goto label_0xCB43F0;
        label_0xCB43F0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x28 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) - (unchecked((uint)(0x4UL)))))));
        __arm64_flags_left_13321208 = unchecked((uint)(x28));
        __arm64_flags_right_13321208 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13321208) - (__arm64_flags_right_13321208))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13321208)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13321208)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13321208) - (__arm64_flags_right_13321208))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13321208)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCB4804;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4400UL)));
        }
        __arm64_flags_left_13321216 = unchecked((uint)(x28));
        __arm64_flags_right_13321216 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321216 >= __arm64_flags_right_13321216))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(x20, x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x28UL))))));
        __arm64_flags_left_13321260 = unchecked((uint)(x28));
        __arm64_flags_right_13321260 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_13321260) - (__arm64_flags_right_13321260))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCB46D8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321280 = unchecked((uint)(x28));
        __arm64_flags_right_13321280 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321280 >= __arm64_flags_right_13321280))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA0UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4460UL)));
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0xA0UL))), x0);
        x1 = x0;
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321340 = unchecked((uint)(x28));
        __arm64_flags_right_13321340 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321340 >= __arm64_flags_right_13321340))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x98UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321380 = unchecked((uint)(x28));
        __arm64_flags_right_13321380 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321380 >= __arm64_flags_right_13321380))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x26);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB44C4UL)));
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x58UL))), x0);
        x1 = x0;
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321440 = unchecked((uint)(x28));
        __arm64_flags_right_13321440 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321440 >= __arm64_flags_right_13321440))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x26);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4500UL)));
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x78UL))), x0);
        x1 = x0;
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321500 = unchecked((uint)(x28));
        __arm64_flags_right_13321500 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321500 >= __arm64_flags_right_13321500))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321540 = unchecked((uint)(x28));
        __arm64_flags_right_13321540 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321540 >= __arm64_flags_right_13321540))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x26);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0x98UL))), x0);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321592 = unchecked((uint)(x28));
        __arm64_flags_right_13321592 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321592 >= __arm64_flags_right_13321592))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x2DUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB45B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x3D8UL))), unchecked((byte)(unchecked((uint)(x27)))));
        x0 = RuntimeCalls.InvokeDirect(0x179AD30UL /* metadata target: Time.get_time */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x23) + (0x120UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xCB45B8;
        label_0xCB45B8:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB45C0UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xCB485CUL /* metadata target: WeaponBehavior.InitializeWeapon */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x28UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x23) + (0xDCUL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321688 = unchecked((uint)(x28));
        __arm64_flags_right_13321688 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321688 >= __arm64_flags_right_13321688))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321724 = unchecked((uint)(x28));
        __arm64_flags_right_13321724 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321724 >= __arm64_flags_right_13321724))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179CB18UL /* metadata target: Transform.get_localPosition */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321776 = unchecked((uint)(x28));
        __arm64_flags_right_13321776 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321776 >= __arm64_flags_right_13321776))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179CB18UL /* metadata target: Transform.get_localPosition */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4664UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179CBA4UL /* metadata target: Transform.set_localPosition */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AD58UL /* metadata target: Time.get_timeSinceLevelLoad */, x0, x1, x2, x3);
        __arm64_float_flags_left_13321864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13321864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13321864 <= __arm64_float_flags_right_13321864) || ((__arm64_float_flags_left_13321864 != __arm64_float_flags_left_13321864) || (__arm64_float_flags_right_13321864 != __arm64_float_flags_right_13321864))))
        {
            goto label_0xCB47BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4698UL)));
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x238UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x88UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2B0UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCB46B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x2DFUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB47E8;
        }
        else
        {
            goto label_0xCB46B4;
        }
        label_0xCB46B4:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x29);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB46D0UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x3A6UL))), unchecked((byte)(unchecked((uint)(x27)))));
        goto label_0xCB47D8;
        label_0xCB46D8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13321956 = unchecked((uint)(x28));
        __arm64_flags_right_13321956 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13321956 >= __arm64_flags_right_13321956))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794C14UL /* metadata target: GameObject.get_transform */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x100UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = x0;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D14UL /* metadata target: GameObject.get_activeSelf */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB4764;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x29);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB4760UL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x3A6UL))), unchecked((byte)(unchecked((uint)(x27)))));
        goto label_0xCB4764;
        label_0xCB4764:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13322096 = unchecked((uint)(x28));
        __arm64_flags_right_13322096 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13322096 >= __arm64_flags_right_13322096))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x26);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB478CUL)));
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x3A7UL))), unchecked((byte)(unchecked((uint)(x27)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13322140 = unchecked((uint)(x28));
        __arm64_flags_right_13322140 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13322140 >= __arm64_flags_right_13322140))
        {
            goto label_0xCB4858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x24))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCB47D8;
        label_0xCB47BC:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x648UL))));
        goto label_0xCB47CC;
        label_0xCB47CC:
        ;
        x1 = RuntimeMemory.ReadU64(x8);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        goto label_0xCB47D8;
        label_0xCB47D8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xCB43F0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCB47E4UL)));
        }
        goto label_0xCB4854;
        label_0xCB47E8:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x670UL))));
        goto label_0xCB47CC;
        label_0xCB47FC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x28UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCB405C;
        }
        else
        {
            goto label_0xCB4804;
        }
        label_0xCB4804:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCB4808;
        label_0xCB4808:
        ;
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
        __arm64_pair_address_13322272 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13322272)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13322272) + (0x8UL))))), 0));
        __arm64_pair_address_13322276 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13322276)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13322276) + (0x8UL))))), 0));
        __arm64_pair_address_13322280 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13322280)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13322280) + (0x8UL))))), 0));
        __arm64_load_address_13322284 = sp;
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13322284)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13322284) + (0xA0UL)));
        return unchecked((uint)(x0));
        label_0xCB4834:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xCB4854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x678UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1767884UL /* metadata target: Animator.SetTrigger */, x0, x1, x2, x3);
        goto label_0xCB4314;
        label_0xCB4854:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCB4858;
        label_0xCB4858:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `PlayerWeapons.<SelectWeapon>d__66.get_Current` — RVA `0xcb501c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong PlayerWeapons_SelectWeapon_d__66_get_Current_RVAcb501c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `PlayerWeapons.<SelectWeapon>d__66.Reset` — RVA `0xcb5024`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong PlayerWeapons_SelectWeapon_d__66_Reset_RVAcb5024(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1549CD0UL /* metadata target: NotSupportedException.ctor */, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x698UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `PlayerWeapons.<SelectWeapon>d__66.get_Current` — RVA `0xcb505c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong PlayerWeapons_SelectWeapon_d__66_get_Current_RVAcb505c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
