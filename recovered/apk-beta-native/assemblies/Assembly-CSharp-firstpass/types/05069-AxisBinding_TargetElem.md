# `AxisBinding.TargetElem` — TypeDefIndex 5069

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `bool` | `separateAxes` |
| `0x18` | `string` | `singleAxis` |
| `0x20` | `bool` | `reverseSingleAxis` |
| `0x28` | `string` | `positiveAxis` |
| `0x30` | `string` | `negativeAxis` |
| `0x38` | `bool` | `positiveAxisAsPositive` |
| `0x39` | `bool` | `negativeAxisAsPositive` |
| `0x3C` | `int` | `singleAxisId` |
| `0x40` | `int` | `positiveAxisId` |
| `0x44` | `int` | `negativeAxisId` |

## `AxisBinding.TargetElem.SetSingleAxis` — RVA `0xc5b50c`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public void SetSingleAxis(string name, bool flip) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong AxisBinding_TargetElem_SetSingleAxis_RVAc5b50c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x1);
        x0 = x19;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8UL))), unchecked((byte)(unchecked((uint)(x20)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `AxisBinding.TargetElem.CopyFrom` — RVA `0xc5b690`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `public void CopyFrom(AxisBinding.TargetElem elem) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong AxisBinding_TargetElem_CopyFrom_RVAc5b690(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            label_0xC5B6FC:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x10UL))))))));
            x19 = x1;
            x20 = x0;
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
            x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x18UL))));
            RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x20UL))))))));
            x0 = x20;
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
            x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
            RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x38UL))))))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x38UL))), unchecked((byte)(unchecked((uint)(x8)))));
            x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
            RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x30UL))), x1);
            x0 = x20;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x39UL))))))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x9UL))), unchecked((byte)(unchecked((uint)(x8)))));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            return x0;
        }
        return default(ulong);
    }
```

## `AxisBinding.TargetElem.ctor` — RVA `0xc5b770`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong AxisBinding_TargetElem_ctor_RVAc5b770(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2B5UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x230UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2B5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC5B7A4:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x20UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x1);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x101UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x10UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x8UL))), unchecked((ushort)(unchecked((uint)(x8)))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `AxisBinding.TargetElem.SyncFloat` — RVA `0xc5b8fc`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public void SyncFloat(float val, InputRig.InputSource source, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static ulong AxisBinding_TargetElem_SyncFloat_RVAc5b8fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12957988 = default(uint);
        uint __arm64_flags_left_12958020 = default(uint);
        uint __arm64_flags_left_12958052 = default(uint);
        uint __arm64_flags_right_12957988 = default(uint);
        uint __arm64_flags_right_12958020 = default(uint);
        uint __arm64_flags_right_12958052 = default(uint);
        float __arm64_float_flags_left_12957964 = default(float);
        float __arm64_float_flags_right_12957964 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        x3 = unchecked((ulong)(unchecked((uint)(x1))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5B934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5B90CUL);
        }
        __arm64_float_flags_left_12957964 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12957964 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12957964 >= __arm64_float_flags_right_12957964))
        {
            goto label_0xC5B954;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5B914UL);
        }
        if ((x2 == 0x0UL))
        {
            goto label_0xC5B984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x39UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_flags_left_12957988 = unchecked((uint)(x8));
        __arm64_flags_right_12957988 = unchecked((uint)0x0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12957988) - (__arm64_flags_right_12957988))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        x8 = unchecked((ulong)((x0) + (0x44UL)));
        goto label_0xC5B970;
        label_0xC5B934:
        ;
        if ((x2 == 0x0UL))
        {
            goto label_0xC5B984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_flags_left_12958020 = unchecked((uint)(x8));
        __arm64_flags_right_12958020 = unchecked((uint)0x0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12958020) - (__arm64_flags_right_12958020))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        x8 = unchecked((ulong)((x0) + (0x3CUL)));
        goto label_0xC5B970;
        label_0xC5B954:
        ;
        if ((x2 == 0x0UL))
        {
            goto label_0xC5B984;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x38UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_flags_left_12958052 = unchecked((uint)(x8));
        __arm64_flags_right_12958052 = unchecked((uint)0x0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12958052) - (__arm64_flags_right_12958052))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x8 = unchecked((ulong)((x0) + (0x40UL)));
        goto label_0xC5B970;
        label_0xC5B970:
        ;
        x0 = x2;
        x2 = x8;
        x4 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC3DB4CUL /* metadata target: InputRig.SetAxis */);
        label_0xC5B984:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `AxisBinding.TargetElem.SyncScroll` — RVA `0xc5ba68`

- Lift status: **partial**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public void SyncScroll(int val, InputRig rig) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=10 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cneg' at 0xc5ba94; reason: Unknown IR expression at 0xc5ba94

```csharp
public static ulong AxisBinding_TargetElem_SyncScroll_RVAc5ba68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12958348 = default(uint);
        uint __arm64_flags_right_12958348 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5BA7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC5BA7C:
        ;
        if ((x2 == 0x0UL))
        {
            goto label_0xC5BAAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x4 = 0x0UL;
        __arm64_flags_left_12958348 = unchecked((uint)(x9));
        __arm64_flags_right_12958348 = unchecked((uint)0x0UL);
        x9 = unchecked((ulong)((x0) + (0x3CUL)));
        RuntimeCalls.Unsupported("cneg", 0xC5BA94UL);
        x3 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((-(unchecked((uint)(x1)))))) : unchecked((uint)(x1)))));
        x0 = x2;
        x1 = x8;
        x2 = x9;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC3DBECUL /* metadata target: InputRig.SetAxisScroll */);
        label_0xC5BAAC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `AxisBinding.TargetElem.IsBoundToAxis` — RVA `0xc5bb60`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public bool IsBoundToAxis(string axisName) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static uint AxisBinding_TargetElem_IsBoundToAxis_RVAc5bb60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        x20 = x0;
        x19 = x1;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5BB9C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5BBA4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC5BB9C:
        ;
        x8 = unchecked((ulong)((x20) + (0x18UL)));
        goto label_0xC5BBA8;
        label_0xC5BBA4:
        ;
        x8 = unchecked((ulong)((x20) + (0x30UL)));
        goto label_0xC5BBA8;
        label_0xC5BBA8:
        ;
        x0 = RuntimeMemory.ReadU64(x8);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */)));
        return default(uint);
    }
```

## `AxisBinding.TargetElem.GetAxis` — RVA `0xc5bd20`

- Lift status: **partial**; input span: 256 bytes; span to next metadata RVA: 256 bytes.
- Metadata signature: `public float GetAxis(InputRig rig) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=35 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fcsel' at 0xc5bdc8; reason: Unknown IR expression at 0xc5bdc8

```csharp
public static ulong AxisBinding_TargetElem_GetAxis_RVAc5bd20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12959160 = default(uint);
        uint __arm64_flags_left_12959188 = default(uint);
        uint __arm64_flags_right_12959160 = default(uint);
        uint __arm64_flags_right_12959188 = default(uint);
        ulong __arm64_load_address_12959212 = default(ulong);
        ulong __arm64_load_address_12959252 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2B6UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5BD60;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2B6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5BD60;
        label_0xC5BD60:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5BD70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5BD6CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5BD70;
        label_0xC5BD70:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5BDE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5BDF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5BD90UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC5BE1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x21 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x38UL))))))));
        x2 = unchecked((ulong)((x20) + (0x40UL)));
        x0 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC36050UL /* metadata target: InputRig.GetAxis */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        x22 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x39UL))))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_flags_left_12959160 = unchecked((uint)(x21));
        __arm64_flags_right_12959160 = unchecked((uint)0x0UL);
        x2 = unchecked((ulong)((x20) + (0x44UL)));
        x0 = x19;
        x3 = 0x0UL;
        RuntimeCalls.Unsupported("fcsel", 0xC5BDC8UL);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC36050UL /* metadata target: InputRig.GetAxis */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_flags_left_12959188 = unchecked((uint)(x22));
        __arm64_flags_right_12959188 = unchecked((uint)0x0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12959188) - (__arm64_flags_right_12959188))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC5BDE0;
        label_0xC5BDE0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_12959212 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12959212)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12959212) + (0x30UL)));
        return x0;
        label_0xC5BDF4:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC5BE1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        x2 = unchecked((ulong)((x20) + (0x3CUL)));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x3 = 0x0UL;
        __arm64_load_address_12959252 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12959252)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12959252) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC36050UL /* metadata target: InputRig.GetAxis */);
        label_0xC5BE1C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `AxisBinding.TargetElem.SetSeparateAxis` — RVA `0xc5be20`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void SetSeparateAxis(string name, bool positiveSide, bool asPositive) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong AxisBinding_TargetElem_SetSeparateAxis_RVAc5be20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x3))) & (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x10UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC5BE50:
            ;
            RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x1);
            x0 = x19;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9UL))), unchecked((byte)(unchecked((uint)(x20)))));
        }
        else
        {
            RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x1);
            x0 = x19;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x10UL))), unchecked((byte)(unchecked((uint)(x20)))));
        }
        label_0xC5BE60:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```
