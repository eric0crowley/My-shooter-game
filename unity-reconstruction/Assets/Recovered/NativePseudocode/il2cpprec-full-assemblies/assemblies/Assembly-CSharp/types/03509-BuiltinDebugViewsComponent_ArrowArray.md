# `BuiltinDebugViewsComponent.ArrowArray` — TypeDefIndex 3509

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `Mesh` | `<mesh>k__BackingField` |
| `0x18` | `int` | `<columnCount>k__BackingField` |
| `0x1C` | `int` | `<rowCount>k__BackingField` |

## `BuiltinDebugViewsComponent.ArrowArray.ctor` — RVA `0xccffb4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_ArrowArray_ctor_RVAccffb4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.ArrowArray.Release` — RVA `0xccffbc`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void Release() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_ArrowArray_Release_RVAccffbc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
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

## `BuiltinDebugViewsComponent.ArrowArray.BuildMesh` — RVA `0xccffe4`

- Lift status: **partial**; input span: 1080 bytes; span to next metadata RVA: 1080 bytes.
- Metadata signature: `public void BuildMesh(int columns, int rows) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=141 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xcd00c8; reason: Unknown IR expression at 0xcd00c8; reason: Unsupported instruction 'b.ls' at 0xcd00e0; reason: Unknown IR expression at 0xcd00e0; reason: Unsupported instruction 'b.eq' at 0xcd00f0; reason: Unknown IR expression at 0xcd00f0; reason: Unsupported instruction 'b.ls' at 0xcd0108; reason: Unknown IR expression at 0xcd0108

```csharp
public static ulong BuiltinDebugViewsComponent_ArrowArray_BuildMesh_RVAccffe4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13435068 = default(uint);
        uint __arm64_flags_left_13435092 = default(uint);
        uint __arm64_flags_left_13435108 = default(uint);
        uint __arm64_flags_left_13435132 = default(uint);
        uint __arm64_flags_left_13435148 = default(uint);
        uint __arm64_flags_left_13435280 = default(uint);
        uint __arm64_flags_left_13435332 = default(uint);
        ulong __arm64_flags_left_13435384 = default(ulong);
        uint __arm64_flags_left_13435436 = default(uint);
        uint __arm64_flags_left_13435524 = default(uint);
        ulong __arm64_flags_left_13435584 = default(ulong);
        uint __arm64_flags_left_13435600 = default(uint);
        uint __arm64_flags_left_13435616 = default(uint);
        uint __arm64_flags_left_13435656 = default(uint);
        ulong __arm64_flags_left_13435688 = default(ulong);
        ulong __arm64_flags_left_13435704 = default(ulong);
        uint __arm64_flags_right_13435068 = default(uint);
        uint __arm64_flags_right_13435092 = default(uint);
        uint __arm64_flags_right_13435108 = default(uint);
        uint __arm64_flags_right_13435132 = default(uint);
        uint __arm64_flags_right_13435148 = default(uint);
        uint __arm64_flags_right_13435280 = default(uint);
        uint __arm64_flags_right_13435332 = default(uint);
        ulong __arm64_flags_right_13435384 = default(ulong);
        uint __arm64_flags_right_13435436 = default(uint);
        uint __arm64_flags_right_13435524 = default(uint);
        ulong __arm64_flags_right_13435584 = default(ulong);
        uint __arm64_flags_right_13435600 = default(uint);
        uint __arm64_flags_right_13435616 = default(uint);
        uint __arm64_flags_right_13435656 = default(uint);
        ulong __arm64_flags_right_13435688 = default(ulong);
        ulong __arm64_flags_right_13435704 = default(ulong);
        ulong __arm64_pair_address_13434860 = default(ulong);
        ulong __arm64_pair_address_13434864 = default(ulong);
        ulong __arm64_pair_address_13435400 = default(ulong);
        ulong __arm64_pair_address_13435456 = default(ulong);
        ulong __arm64_pair_address_13435544 = default(ulong);
        ulong __arm64_pair_address_13435904 = default(ulong);
        ulong __arm64_pair_address_13435908 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
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
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13434860 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13434860, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13434860) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13434864 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13434864, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13434864) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
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
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x18UL))), unchecked((uint)(x2)));
        x19 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x5B1UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB90UL))));
        x21 = unchecked((ulong)(unchecked((uint)(x1))));
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCD00A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x5B1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCD00A0;
        label_0xCD00A0:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x24 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD00BCUL);
        }
        __arm64_flags_left_13435068 = unchecked((uint)(x8));
        __arm64_flags_right_13435068 = unchecked((uint)0x1UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x24) + (0x20UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x24) + (0x28UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.eq", 0xCD00C8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0x78UL))))), 0));
        __arm64_flags_left_13435092 = unchecked((uint)(x8));
        __arm64_flags_right_13435092 = unchecked((uint)0x2UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x24) + (0x34UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x24) + (0x2CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeCalls.Unsupported("b.ls", 0xCD00E0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD00E4UL);
        }
        __arm64_flags_left_13435108 = unchecked((uint)(x8));
        __arm64_flags_right_13435108 = unchecked((uint)0x3UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x24) + (0x38UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x24) + (0x40UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.eq", 0xCD00F0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x431000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0xE60UL))))), 0));
        __arm64_flags_left_13435132 = unchecked((uint)(x8));
        __arm64_flags_right_13435132 = unchecked((uint)0x4UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x24) + (0x4CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x24) + (0x44UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeCalls.Unsupported("b.ls", 0xCD0108UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD010CUL);
        }
        __arm64_flags_left_13435148 = unchecked((uint)(x8));
        __arm64_flags_right_13435148 = unchecked((uint)0x5UL);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x22);
        RuntimeMemory.WriteF64(unchecked((ulong)((x24) + (0x50UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x24) + (0x58UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.eq", 0xCD011CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE10UL))));
        x19 = 0x1A8E000UL;
        x20 = 0x1A8E000UL;
        x23 = 0x1A8E000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE08UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE18UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE00UL))));
        RuntimeCalls.Unsupported("fmov", 0xCD0140UL);
        x25 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x18UL))))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x24) + (0x5CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x24) + (0x64UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) * (unchecked((uint)(x25)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x1UL))))))))))));
        x26 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x1UL)))))))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x19);
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10DC484UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(x26))));
        x23 = x0;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x4UL))), unchecked((uint)(x26)));
        x0 = RuntimeCalls.InvokeDirect(0x10D9EB8UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_flags_left_13435280 = unchecked((uint)(x25));
        __arm64_flags_right_13435280 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13435280) - (__arm64_flags_right_13435280))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13435280)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13435280)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13435280) - (__arm64_flags_right_13435280))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13435280)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCD02EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD0198UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x27 = 0x1A8E000UL;
        x28 = 0x1A8E000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xDF0UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xDF8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x18UL))))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x21))))))), 0));
        x26 = unchecked((ulong)((x24) + (0x28UL)));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        x20 = unchecked((ulong)(unchecked((uint)(0xCUL))));
        goto label_0xCD01C4;
        label_0xCD01C4:
        ;
        __arm64_flags_left_13435332 = unchecked((uint)(x21));
        __arm64_flags_right_13435332 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13435332) - (__arm64_flags_right_13435332))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13435332)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13435332)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13435332) - (__arm64_flags_right_13435332))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13435332)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCD02D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x1CUL))))));
        x25 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        goto label_0xCD01E0;
        label_0xCD01E0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x25))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        x19 = 0x0UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        x29 = x26;
        goto label_0xCD01F4;
        label_0xCD01F4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x24) + (0x18UL))))));
        __arm64_flags_left_13435384 = x19;
        __arm64_flags_right_13435384 = x8;
        if ((__arm64_flags_left_13435384 >= __arm64_flags_right_13435384))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD0200UL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x1CUL))))));
        __arm64_pair_address_13435400 = unchecked((ulong)((x29) + (0xFFFFFFFFFFFFFFF8UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13435400)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13435400) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x29)), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        x8 = RuntimeMemory.ReadU64(x27);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x9 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x22) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13435436 = unchecked((uint)(x10));
        __arm64_flags_right_13435436 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13435436 >= __arm64_flags_right_13435436))
        {
            goto label_0xCD024C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x9 = unchecked((ulong)((unchecked((ulong)((x10) * (unchecked((ulong)(unchecked((uint)(x20)))))))) + (x9)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x18UL))), unchecked((uint)(x8)));
        __arm64_pair_address_13435456 = unchecked((ulong)((x9) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13435456, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13435456) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x9) + (0x28UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        goto label_0xCD0260;
        label_0xCD024C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x20UL))));
        x0 = x22;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10DCCA0UL, x0, x1, x2, x3);
        goto label_0xCD0260;
        label_0xCD0260:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x28);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x23) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x23) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13435524 = unchecked((uint)(x10));
        __arm64_flags_right_13435524 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13435524 >= __arm64_flags_right_13435524))
        {
            goto label_0xCD02A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x23) + (0x18UL))), unchecked((uint)(x9)));
        __arm64_pair_address_13435544 = unchecked((ulong)((x8) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13435544, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13435544) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        goto label_0xCD02BC;
        label_0xCD02A0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x0 = x23;
        v0 = v9;
        v1 = v8;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10DA6A8UL, x0, x1, x2, x3);
        goto label_0xCD02BC;
        label_0xCD02BC:
        ;
        x19 = unchecked((ulong)((x19) + (0x1UL)));
        __arm64_flags_left_13435584 = x19;
        __arm64_flags_right_13435584 = 0x6UL;
        x29 = unchecked((ulong)((x29) + (0xCUL)));
        RuntimeCalls.Unsupported("b.ne", 0xCD02C8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD01F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x25 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x25))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13435600 = unchecked((uint)(x25));
        __arm64_flags_right_13435600 = unchecked((uint)(x21));
        if ((!((unchecked((uint)((__arm64_flags_left_13435600) - (__arm64_flags_right_13435600))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCD01E0;
        }
        else
        {
            goto label_0xCD02D8;
        }
        label_0xCD02D8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x18UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x4UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13435616 = unchecked((uint)(x9));
        __arm64_flags_right_13435616 = unchecked((uint)(x8));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x1CUL))), unchecked((uint)(x9)));
        RuntimeCalls.Unsupported("b.ne", 0xCD02E8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD01C4;
        }
        else
        {
            goto label_0xCD02EC;
        }
        label_0xCD02EC:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDE8UL))));
        x20 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x4UL))))));
        x0 = RuntimeMemory.ReadU64(x8);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_flags_left_13435656 = unchecked((uint)(x20));
        __arm64_flags_right_13435656 = unchecked((uint)0x1UL);
        x24 = x0;
        RuntimeCalls.Unsupported("b.lt", 0xCD0310UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCD0340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD0314UL);
        }
        if ((x24 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x24) + (0x18UL))))));
        x8 = 0x0UL;
        x10 = unchecked((ulong)(unchecked((uint)(x20))));
        x11 = unchecked((ulong)((x24) + (0x20UL)));
        goto label_0xCD0328;
        label_0xCD0328:
        ;
        __arm64_flags_left_13435688 = x8;
        __arm64_flags_right_13435688 = x9;
        if ((__arm64_flags_left_13435688 >= __arm64_flags_right_13435688))
        {
            goto label_0xCD0418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCD0330UL);
        }
        RuntimeMemory.WriteU32(unchecked((ulong)((x11) + (x8))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)((x8) + (0x1UL)));
        __arm64_flags_left_13435704 = x10;
        __arm64_flags_right_13435704 = x8;
        if ((!((unchecked((ulong)((__arm64_flags_left_13435704) - (__arm64_flags_right_13435704))) == 0x0UL))))
        {
            goto label_0xCD0328;
        }
        else
        {
            goto label_0xCD0340;
        }
        label_0xCD0340:
        ;
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE20UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = 0x0UL;
        x26 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x177C0DCUL /* metadata target: Mesh.ctor */, x0, x1, x2, x3);
        if ((x26 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x34UL))));
        x0 = x26;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1798C88UL /* metadata target: Object.set_hideFlags */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x25 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x25) + (0x10UL))), x26);
        x0 = x25;
        x1 = x26;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x22;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177CDA4UL /* metadata target: Mesh.SetVertices */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = x23;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177D17CUL /* metadata target: Mesh.SetUVs */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x1 = x24;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177DB84UL /* metadata target: Mesh.SetIndices */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(x25);
        if ((x0 == 0x0UL))
        {
            goto label_0xCD0414;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x177DF68UL /* metadata target: Mesh.UploadMeshData */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x18UL))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x19) + (0x18UL)))) + (0x0UL))), unchecked((uint)(x21)));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x19) + (0x18UL)))) + (0x4UL))), unchecked((uint)(x8)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_13435904 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13435904)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13435904) + (0x8UL))))), 0));
        __arm64_pair_address_13435908 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13435908)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13435908) + (0x8UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x10UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xA0UL)));
        return x0;
        label_0xCD0414:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCD0418;
        label_0xCD0418:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.ArrowArray.get_mesh` — RVA `0xcd0634`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Mesh get_mesh() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_ArrowArray_get_mesh_RVAcd0634(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        return x0;
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.ArrowArray.set_mesh` — RVA `0xcd063c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private void set_mesh(Mesh value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_ArrowArray_set_mesh_RVAcd063c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.ArrowArray.get_columnCount` — RVA `0xcd0644`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public int get_columnCount() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint BuiltinDebugViewsComponent_ArrowArray_get_columnCount_RVAcd0644(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `BuiltinDebugViewsComponent.ArrowArray.set_columnCount` — RVA `0xcd064c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private void set_columnCount(int value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_ArrowArray_set_columnCount_RVAcd064c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x1)));
        return x0;
        return default(ulong);
    }
```

## `BuiltinDebugViewsComponent.ArrowArray.get_rowCount` — RVA `0xcd0654`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public int get_rowCount() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint BuiltinDebugViewsComponent_ArrowArray_get_rowCount_RVAcd0654(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `BuiltinDebugViewsComponent.ArrowArray.set_rowCount` — RVA `0xcd065c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private void set_rowCount(int value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong BuiltinDebugViewsComponent_ArrowArray_set_rowCount_RVAcd065c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x1)));
        return x0;
        return default(ulong);
    }
```
