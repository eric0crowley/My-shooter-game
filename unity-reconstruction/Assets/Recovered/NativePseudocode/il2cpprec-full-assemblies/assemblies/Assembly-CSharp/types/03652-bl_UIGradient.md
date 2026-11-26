# `bl_UIGradient` — TypeDefIndex 3652

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x28` | `bl_UIGradient.Type` | `_gradientType` |
| `0x2C` | `bl_UIGradient.Blend` | `_blendMode` |
| `0x30` | `bool` | `_modifyVertices` |
| `0x34` | `float` | `_offset` |
| `0x38` | `float` | `_zoom` |
| `0x40` | `Gradient` | `_effectGradient` |

## `bl_UIGradient.get_BlendMode` — RVA `0xce8c44`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bl_UIGradient.Blend get_BlendMode() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint bl_UIGradient_get_BlendMode_RVAce8c44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x2CUL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `bl_UIGradient.set_BlendMode` — RVA `0xce8c4c`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void set_BlendMode(bl_UIGradient.Blend value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong bl_UIGradient_set_BlendMode_RVAce8c4c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x2CUL))), unchecked((uint)(x1)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19967E0UL /* metadata target: BaseMeshEffect.get_graphic */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8C74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCE8C74:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.get_EffectGradient` — RVA `0xce8c78`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Gradient get_EffectGradient() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong bl_UIGradient_get_EffectGradient_RVAce8c78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        return x0;
        return default(ulong);
    }
```

## `bl_UIGradient.set_EffectGradient` — RVA `0xce8c80`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public void set_EffectGradient(Gradient value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong bl_UIGradient_set_EffectGradient_RVAce8c80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19967E0UL /* metadata target: BaseMeshEffect.get_graphic */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8CB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCE8CB4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.get_GradientType` — RVA `0xce8cb8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bl_UIGradient.Type get_GradientType() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint bl_UIGradient_get_GradientType_RVAce8cb8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x28UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `bl_UIGradient.set_GradientType` — RVA `0xce8cc0`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public void set_GradientType(bl_UIGradient.Type value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong bl_UIGradient_set_GradientType_RVAce8cc0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x28UL))), unchecked((uint)(x1)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19967E0UL /* metadata target: BaseMeshEffect.get_graphic */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8CE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCE8CE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.get_ModifyVertices` — RVA `0xce8cec`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool get_ModifyVertices() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint bl_UIGradient_get_ModifyVertices_RVAce8cec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x30UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `bl_UIGradient.set_ModifyVertices` — RVA `0xce8cf4`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public void set_ModifyVertices(bool value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong bl_UIGradient_set_ModifyVertices_RVAce8cf4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x30UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x19967E0UL /* metadata target: BaseMeshEffect.get_graphic */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8D20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCE8D20:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.get_Offset` — RVA `0xce8d24`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_Offset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong bl_UIGradient_get_Offset_RVAce8d24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x34UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `bl_UIGradient.set_Offset` — RVA `0xce8d2c`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public void set_Offset(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong bl_UIGradient_set_Offset_RVAce8d2c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13536572 = default(float);
        float __arm64_float_flags_right_13536572 = default(float);
        float __arm64_fp_left_13536568 = default(float);
        float __arm64_fp_right_13536568 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        __arm64_fp_left_13536568 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_13536568 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_13536568 != __arm64_fp_left_13536568) ? __arm64_fp_left_13536568 : ((__arm64_fp_right_13536568 != __arm64_fp_right_13536568) ? __arm64_fp_right_13536568 : (((__arm64_fp_left_13536568 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_13536568 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_13536568), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_13536568), 0))))), 0) : ((__arm64_fp_left_13536568 <= __arm64_fp_right_13536568) ? __arm64_fp_left_13536568 : __arm64_fp_right_13536568))))), 0));
        __arm64_float_flags_left_13536572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13536572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13536572 >= __arm64_float_flags_right_13536572) || ((__arm64_float_flags_left_13536572 != __arm64_float_flags_left_13536572) || (__arm64_float_flags_right_13536572 != __arm64_float_flags_right_13536572))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        x1 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x34UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x19967E0UL /* metadata target: BaseMeshEffect.get_graphic */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8D68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCE8D68:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.get_Zoom` — RVA `0xce8d6c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_Zoom() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong bl_UIGradient_get_Zoom_RVAce8d6c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x38UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `bl_UIGradient.set_Zoom` — RVA `0xce8d74`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `public void set_Zoom(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong bl_UIGradient_set_Zoom_RVAce8d74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_13536652 = default(float);
        float __arm64_float_flags_right_13536652 = default(float);
        float __arm64_fp_left_13536644 = default(float);
        float __arm64_fp_right_13536644 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41200000UL)), 0)), 0));
        __arm64_fp_left_13536644 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_13536644 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_13536644 != __arm64_fp_left_13536644) ? __arm64_fp_left_13536644 : ((__arm64_fp_right_13536644 != __arm64_fp_right_13536644) ? __arm64_fp_right_13536644 : (((__arm64_fp_left_13536644 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_13536644 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_13536644), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_13536644), 0))))), 0) : ((__arm64_fp_left_13536644 <= __arm64_fp_right_13536644) ? __arm64_fp_left_13536644 : __arm64_fp_right_13536644))))), 0));
        x1 = 0x0UL;
        __arm64_float_flags_left_13536652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13536652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_13536652 >= __arm64_float_flags_right_13536652) || ((__arm64_float_flags_left_13536652 != __arm64_float_flags_left_13536652) || (__arm64_float_flags_right_13536652 != __arm64_float_flags_right_13536652))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x19967E0UL /* metadata target: BaseMeshEffect.get_graphic */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCE8DB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xCE8DB4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.ModifyMesh` — RVA `0xce8db8`

- Lift status: **partial**; input span: 3756 bytes; span to next metadata RVA: 3756 bytes.
- Metadata signature: `public override void ModifyMesh(VertexHelper helper) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=427 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xce8f34; reason: Unknown IR expression at 0xce8f34; reason: Unsupported instruction 'fadd' at 0xce8fec; reason: Unsupported instruction 'fmul' at 0xce8ff4; reason: Unsupported instruction 'fmul' at 0xce9044; reason: Unsupported instruction 'fadd' at 0xce904c; reason: Unsupported instruction 'mov' at 0xce91c4; reason: Unsupported instruction 'fmov' at 0xce981c

```csharp
public static ulong bl_UIGradient_ModifyMesh_RVAce8db8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13537068 = default(uint);
        uint __arm64_flags_left_13537080 = default(uint);
        uint __arm64_flags_left_13537384 = default(uint);
        uint __arm64_flags_left_13537452 = default(uint);
        uint __arm64_flags_left_13537604 = default(uint);
        uint __arm64_flags_left_13537644 = default(uint);
        uint __arm64_flags_left_13537708 = default(uint);
        uint __arm64_flags_left_13538048 = default(uint);
        uint __arm64_flags_left_13538224 = default(uint);
        uint __arm64_flags_left_13538496 = default(uint);
        uint __arm64_flags_left_13538796 = default(uint);
        uint __arm64_flags_left_13539864 = default(uint);
        uint __arm64_flags_left_13540036 = default(uint);
        uint __arm64_flags_left_13540108 = default(uint);
        uint __arm64_flags_left_13540392 = default(uint);
        uint __arm64_flags_result_13537604 = default(uint);
        uint __arm64_flags_right_13537068 = default(uint);
        uint __arm64_flags_right_13537080 = default(uint);
        uint __arm64_flags_right_13537384 = default(uint);
        uint __arm64_flags_right_13537452 = default(uint);
        uint __arm64_flags_right_13537604 = default(uint);
        uint __arm64_flags_right_13537644 = default(uint);
        uint __arm64_flags_right_13537708 = default(uint);
        uint __arm64_flags_right_13538048 = default(uint);
        uint __arm64_flags_right_13538224 = default(uint);
        uint __arm64_flags_right_13538496 = default(uint);
        uint __arm64_flags_right_13538796 = default(uint);
        uint __arm64_flags_right_13539864 = default(uint);
        uint __arm64_flags_right_13540036 = default(uint);
        uint __arm64_flags_right_13540108 = default(uint);
        uint __arm64_flags_right_13540392 = default(uint);
        float __arm64_float_flags_left_13537100 = default(float);
        float __arm64_float_flags_left_13538376 = default(float);
        float __arm64_float_flags_left_13538836 = default(float);
        float __arm64_float_flags_left_13538864 = default(float);
        float __arm64_float_flags_right_13537100 = default(float);
        float __arm64_float_flags_right_13538376 = default(float);
        float __arm64_float_flags_right_13538836 = default(float);
        float __arm64_float_flags_right_13538864 = default(float);
        ulong __arm64_pair_address_13536696 = default(ulong);
        ulong __arm64_pair_address_13536700 = default(ulong);
        ulong __arm64_pair_address_13536704 = default(ulong);
        ulong __arm64_pair_address_13536708 = default(ulong);
        ulong __arm64_pair_address_13536908 = default(ulong);
        ulong __arm64_pair_address_13536912 = default(ulong);
        ulong __arm64_pair_address_13536916 = default(ulong);
        ulong __arm64_pair_address_13536924 = default(ulong);
        ulong __arm64_pair_address_13536928 = default(ulong);
        ulong __arm64_pair_address_13536932 = default(ulong);
        ulong __arm64_pair_address_13536940 = default(ulong);
        ulong __arm64_pair_address_13536944 = default(ulong);
        ulong __arm64_pair_address_13536948 = default(ulong);
        ulong __arm64_pair_address_13536952 = default(ulong);
        ulong __arm64_pair_address_13536960 = default(ulong);
        ulong __arm64_pair_address_13537692 = default(ulong);
        ulong __arm64_pair_address_13537696 = default(ulong);
        ulong __arm64_pair_address_13537700 = default(ulong);
        ulong __arm64_pair_address_13538480 = default(ulong);
        ulong __arm64_pair_address_13538484 = default(ulong);
        ulong __arm64_pair_address_13538488 = default(ulong);
        ulong __arm64_pair_address_13538944 = default(ulong);
        ulong __arm64_pair_address_13538948 = default(ulong);
        ulong __arm64_pair_address_13538956 = default(ulong);
        ulong __arm64_pair_address_13538976 = default(ulong);
        ulong __arm64_pair_address_13539020 = default(ulong);
        ulong __arm64_pair_address_13539032 = default(ulong);
        ulong __arm64_pair_address_13539072 = default(ulong);
        ulong __arm64_pair_address_13539144 = default(ulong);
        ulong __arm64_pair_address_13539376 = default(ulong);
        ulong __arm64_pair_address_13539448 = default(ulong);
        ulong __arm64_pair_address_13539588 = default(ulong);
        ulong __arm64_pair_address_13539732 = default(ulong);
        ulong __arm64_pair_address_13539792 = default(ulong);
        ulong __arm64_pair_address_13539820 = default(ulong);
        ulong __arm64_pair_address_13539848 = default(ulong);
        ulong __arm64_pair_address_13539876 = default(ulong);
        ulong __arm64_pair_address_13539920 = default(ulong);
        ulong __arm64_pair_address_13539924 = default(ulong);
        ulong __arm64_pair_address_13539996 = default(ulong);
        ulong __arm64_pair_address_13540072 = default(ulong);
        ulong __arm64_pair_address_13540092 = default(ulong);
        ulong __arm64_pair_address_13540096 = default(ulong);
        ulong __arm64_pair_address_13540100 = default(ulong);
        ulong __arm64_pair_address_13540428 = default(ulong);
        ulong __arm64_pair_address_13540432 = default(ulong);
        ulong __arm64_pair_address_13540436 = default(ulong);
        ulong __arm64_pair_address_13540440 = default(ulong);
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
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
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
        __arm64_pair_address_13536696 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13536696, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13536696) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_13536696;
        __arm64_pair_address_13536700 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13536700, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13536700) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13536704 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13536704, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13536704) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13536708 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13536708, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13536708) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
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
        sp = unchecked((ulong)((sp) - (0x670UL)));
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x676UL))))))));
        x19 = x1;
        x20 = x0;
        x26 = unchecked((ulong)((sp) + (0x590UL)));
        x24 = unchecked((ulong)((sp) + (0x4B0UL)));
        x25 = unchecked((ulong)((sp) + (0x260UL)));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE8E6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x676UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE8E6C;
        label_0xCE8E6C:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x4A0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x4A8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x498UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x490UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x458UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x450UL))), 0x0UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x26) + (0x5CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x26) + (0x5CUL))), v0);
#endif
        __arm64_pair_address_13536908 = unchecked((ulong)((x26) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536908, v0);
#else
        __WriteVector128(__arm64_pair_address_13536908, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536908) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536908) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13536912 = unchecked((ulong)((x26) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536912, v0);
#else
        __WriteVector128(__arm64_pair_address_13536912, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536912) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536912) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13536916 = x26;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536916, v0);
#else
        __WriteVector128(__arm64_pair_address_13536916, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536916) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536916) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x24) + (0xCCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x24) + (0xCCUL))), v0);
#endif
        __arm64_pair_address_13536924 = unchecked((ulong)((x24) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536924, v0);
#else
        __WriteVector128(__arm64_pair_address_13536924, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536924) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536924) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13536928 = unchecked((ulong)((x24) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536928, v0);
#else
        __WriteVector128(__arm64_pair_address_13536928, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536928) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536928) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13536932 = unchecked((ulong)((x24) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536932, v0);
#else
        __WriteVector128(__arm64_pair_address_13536932, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536932) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536932) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x24) + (0x5CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x24) + (0x5CUL))), v0);
#endif
        __arm64_pair_address_13536940 = unchecked((ulong)((x24) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536940, v0);
#else
        __WriteVector128(__arm64_pair_address_13536940, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536940) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536940) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13536944 = unchecked((ulong)((x24) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536944, v0);
#else
        __WriteVector128(__arm64_pair_address_13536944, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536944) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536944) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13536948 = x24;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536948, v0);
#else
        __WriteVector128(__arm64_pair_address_13536948, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536948) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536948) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13536952 = unchecked((ulong)((x25) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536952, v0);
#else
        __WriteVector128(__arm64_pair_address_13536952, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536952) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536952) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x220UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x220UL))), v0);
#endif
        __arm64_pair_address_13536960 = unchecked((ulong)((x25) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13536960, v0);
#else
        __WriteVector128(__arm64_pair_address_13536960, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13536960) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13536960) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x1E0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x1E0UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1C8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x1C8UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE8EDCUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xCE9C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, x2, x3);
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC80UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC68UL))));
        x21 = x0;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10D0220UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x19966F0UL /* metadata target: VertexHelper.GetUIVertexStream */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCE9C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x28UL))))));
        __arm64_flags_left_13537068 = unchecked((uint)(x8));
        __arm64_flags_right_13537068 = unchecked((uint)0x2UL);
        if ((!((__arm64_flags_left_13537068 >= __arm64_flags_right_13537068))))
        {
            goto label_0xCE930C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE8F34UL);
        }
        RuntimeCalls.Unsupported("b.eq", 0xCE8F34UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCE95F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE8F38UL);
        }
        __arm64_flags_left_13537080 = unchecked((uint)(x8));
        __arm64_flags_right_13537080 = unchecked((uint)0x3UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13537080) - (__arm64_flags_right_13537080))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xCE9C64UL /* metadata target: bl_UIGradient.GetBounds */, x0, x1, x2, x3);
        __arm64_float_flags_left_13537100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13537100 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((__arm64_float_flags_left_13537100 == __arm64_float_flags_right_13537100))
        {
            goto label_0xCE8F68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE8F58UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x38UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xCE8F68;
        label_0xCE8F68:
        ;
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x3E1UL))))))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE8F94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x3E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE8F94;
        label_0xCE8F94:
        ;
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x1E8UL))));
        x27 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x27) + (0x32CUL))))))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x3CUL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x44UL))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE8FDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v2);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x27) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x9)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        goto label_0xCE8FDC;
        label_0xCE8FDC:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x18UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x27 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x27) + (0x3E3UL))))))));
        RuntimeCalls.Unsupported("fadd", 0xCE8FECUL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xCE8FF4UL);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9018;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x27) + (0x3E3UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        goto label_0xCE9018;
        label_0xCE9018:
        ;
        x27 = 0x1A8F000UL;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x48UL))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x50UL))))), 0));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xC78UL))));
        x8 = unchecked((ulong)((sp) + (0x600UL)));
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x608UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x30UL))))))));
        RuntimeCalls.Unsupported("fmul", 0xCE9044UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fadd", 0xCE904CUL);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x80UL))), v1);
#endif
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE918C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x198544CUL /* metadata target: VertexHelper.Clear */, x0, x1, x2, x3);
        __arm64_flags_left_13537384 = unchecked((uint)(x22));
        __arm64_flags_right_13537384 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13537384) - (__arm64_flags_right_13537384))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13537384)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13537384)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13537384) - (__arm64_flags_right_13537384))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13537384)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE90B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCE9074;
        label_0xCE9074:
        ;
        x2 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)((sp) + (0x600UL)));
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)(x23))));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x2D0UL)));
        x1 = unchecked((ulong)((sp) + (0x600UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x2D0UL)));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13537452 = unchecked((uint)(x22));
        __arm64_flags_right_13537452 = unchecked((uint)(x23));
        if ((!((unchecked((uint)((__arm64_flags_left_13537452) - (__arm64_flags_right_13537452))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE9074;
        }
        else
        {
            goto label_0xCE90B4;
        }
        label_0xCE90B4:
        ;
        x2 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x600UL)));
        x1 = unchecked((ulong)((sp) + (0x3B0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x7CUL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x614UL))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x268UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x260UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x25) + (0xCUL))), x8);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x274UL))), unchecked((uint)(x9)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x280UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x278UL))), 0x0UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x288UL))), unchecked((uint)(x0)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x25) + (0x2CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x1 = unchecked((ulong)((sp) + (0x260UL)));
        x0 = x19;
        x2 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x34UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x34UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x44UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x44UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x54UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x54UL))), v0);
#endif
        RuntimeMemory.WritePtr(unchecked((ulong)((x25) + (0x64UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        __arm64_flags_left_13537604 = unchecked((uint)(x22));
        __arm64_flags_right_13537604 = unchecked((uint)0x1UL);
        __arm64_flags_result_13537604 = unchecked((uint)((__arm64_flags_left_13537604) - (__arm64_flags_right_13537604)));
        x21 = unchecked((ulong)(__arm64_flags_result_13537604));
        if (((unchecked((uint)((__arm64_flags_left_13537604) - (__arm64_flags_right_13537604))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13537604) - (__arm64_flags_right_13537604))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13537604)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13537604)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13537604) - (__arm64_flags_right_13537604))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13537604)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xCE9174;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCE9150;
        label_0xCE9150:
        ;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) - (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x23))));
        x3 = unchecked((ulong)(unchecked((uint)(x22))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13537644 = unchecked((uint)(x22));
        __arm64_flags_right_13537644 = unchecked((uint)(x23));
        if ((!((unchecked((uint)((__arm64_flags_left_13537644) - (__arm64_flags_right_13537644))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE9150;
        }
        else
        {
            goto label_0xCE9174;
        }
        label_0xCE9174:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = unchecked((ulong)(unchecked((uint)(x22))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCE918C;
        label_0xCE918C:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = x19;
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x24) + (0xCCUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x24) + (0xCCUL))), v0);
#endif
        __arm64_pair_address_13537692 = unchecked((ulong)((x24) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13537692, v0);
#else
        __WriteVector128(__arm64_pair_address_13537692, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13537692) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13537692) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13537696 = unchecked((ulong)((x24) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13537696, v0);
#else
        __WriteVector128(__arm64_pair_address_13537696, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13537696) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13537696) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13537700 = unchecked((ulong)((x24) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13537700, v0);
#else
        __WriteVector128(__arm64_pair_address_13537700, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13537700) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13537700) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_flags_left_13537708 = unchecked((uint)(x0));
        __arm64_flags_right_13537708 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13537708) - (__arm64_flags_right_13537708))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13537708)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13537708)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13537708) - (__arm64_flags_right_13537708))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13537708)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE91B4UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA60UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeCalls.Unsupported("mov", 0xCE91C4UL);
        x24 = unchecked((ulong)(unchecked((uint)(0x437F0000UL))));
        x25 = 0x1BAB000UL;
        x26 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCE91D4;
        label_0xCE91D4:
        ;
        x1 = unchecked((ulong)((sp) + (0x520UL)));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995BB0UL /* metadata target: VertexHelper.PopulateUIVertex */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x27 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x548UL))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x520UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x524UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x3E0UL))))))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x528UL))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9210;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x3E0UL))), unchecked((byte)(unchecked((uint)(x26)))));
        goto label_0xCE9210;
        label_0xCE9210:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9220;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE921CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCE9220;
        label_0xCE9220:
        ;
        if ((x23 == 0x0UL))
        {
            goto label_0xCE9C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9224UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((sp) + (0x80UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x27))) & (unchecked((uint)(0xFFUL)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x27))) >> (int)(unchecked((int)(unchecked((uint)0x8UL))))))) & (unchecked((uint)0xFFUL))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x27))) >> (int)(unchecked((int)(unchecked((uint)0x10UL))))))) & (unchecked((uint)0xFFUL))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x27))) >> (int)(unchecked((int)(unchecked((uint)(0x18UL)))))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x24))), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x8))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x9))))), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x10))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x11))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x34UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1785F64UL /* metadata target: Gradient.Evaluate */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v4 = v0;
        v5 = v1;
        v6 = v2;
        v7 = v3;
        x0 = x20;
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        x0 = RuntimeCalls.InvokeDirect(0xCEAEACUL /* metadata target: bl_UIGradient.BlendColor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x548UL))), unchecked((uint)(x0)));
        x0 = unchecked((ulong)((sp) + (0x1F0UL)));
        x1 = unchecked((ulong)((sp) + (0x520UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x1F0UL)));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995D10UL /* metadata target: VertexHelper.SetUIVertex */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        x1 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_13538048 = unchecked((uint)(x21));
        __arm64_flags_right_13538048 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13538048) - (__arm64_flags_right_13538048))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13538048)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13538048)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13538048) - (__arm64_flags_right_13538048))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13538048)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE91D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9308UL);
        }
        goto label_0xCE9C30;
        label_0xCE930C:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xCE9C64UL /* metadata target: bl_UIGradient.GetBounds */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x24 = 0x1A8F000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xC98UL))));
        v8 = v0;
        v9 = v1;
        v10 = v2;
        x0 = RuntimeMemory.ReadU64(x24);
        v11 = v3;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9338UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x24);
        goto label_0xCE9340;
        label_0xCE9340:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xCE93A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE935C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9354UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x24);
        goto label_0xCE935C;
        label_0xCE935C:
        ;
        x9 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC60UL))));
        x23 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC88UL))));
        x1 = x23;
        x3 = 0x0UL;
        x22 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xFC261CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x1 = x22;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x8UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCE93A4;
        label_0xCE93A4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x28UL))))));
        v0 = v10;
        v13 = v8;
        __arm64_flags_left_13538224 = unchecked((uint)(x8));
        __arm64_flags_right_13538224 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13538224) - (__arm64_flags_right_13538224))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE9440;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x24);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE93CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE93C4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        goto label_0xCE93CC;
        label_0xCE93CC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        v0 = v11;
        v13 = v9;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xCE9440;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE93F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE93E8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        goto label_0xCE93F0;
        label_0xCE93F0:
        ;
        x9 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC60UL))));
        x23 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC90UL))));
        x1 = x23;
        x3 = 0x0UL;
        x22 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xFC261CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x24);
        x1 = x22;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = v11;
        v13 = v9;
        goto label_0xCE9440;
        label_0xCE9440:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x38UL))))), 0));
        v1 = v9;
        __arm64_float_flags_left_13538376 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13538376 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((__arm64_float_flags_left_13538376 == __arm64_float_flags_right_13538376))
        {
            goto label_0xCE9460;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9454UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        goto label_0xCE9460;
        label_0xCE9460:
        ;
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x30UL))))))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x34UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE94A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        v0 = v8;
        v2 = v10;
        v3 = v11;
        v4 = v12;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xCE9DB4UL /* metadata target: bl_UIGradient.SplitTrianglesAtGradientStops */, x0, x1, x2, x3);
        goto label_0xCE94A0;
        label_0xCE94A0:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = x19;
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x26) + (0x5CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x26) + (0x5CUL))), v0);
#endif
        __arm64_pair_address_13538480 = unchecked((ulong)((x26) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13538480, v0);
#else
        __WriteVector128(__arm64_pair_address_13538480, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13538480) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13538480) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13538484 = unchecked((ulong)((x26) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13538484, v0);
#else
        __WriteVector128(__arm64_pair_address_13538484, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13538484) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13538484) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13538488 = x26;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13538488, v0);
#else
        __WriteVector128(__arm64_pair_address_13538488, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13538488) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13538488) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, x2, x3);
        __arm64_flags_left_13538496 = unchecked((uint)(x0));
        __arm64_flags_right_13538496 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13538496) - (__arm64_flags_right_13538496))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13538496)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13538496)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13538496) - (__arm64_flags_right_13538496))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13538496)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE94C8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        x25 = unchecked((ulong)(unchecked((uint)(0x437F0000UL))));
        goto label_0xCE94DC;
        label_0xCE94DC:
        ;
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995BB0UL /* metadata target: VertexHelper.PopulateUIVertex */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x26 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x5B8UL))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x0 = unchecked((ulong)((sp) + (0x3B0UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xCE9C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x40UL))));
        x0 = unchecked((ulong)((sp) + (0x600UL)));
        x1 = unchecked((ulong)((sp) + (0x3B0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x28UL))));
        x1 = unchecked((ulong)((sp) + (0x600UL)));
        x0 = x24;
        x0 = RuntimeCalls.InvokeIndirect(x27, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCE9C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9538UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x26))) & (unchecked((uint)(0xFFUL)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x26))) >> (int)(unchecked((int)(unchecked((uint)0x8UL))))))) & (unchecked((uint)0xFFUL))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x26))) >> (int)(unchecked((int)(unchecked((uint)0x10UL))))))) & (unchecked((uint)0xFFUL))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x26))) >> (int)(unchecked((int)(unchecked((uint)(0x18UL)))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x25))), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x8))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x9))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x10))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x11))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        x0 = x23;
        x1 = 0x0UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1785F64UL /* metadata target: Gradient.Evaluate */, x0, x1, x2, x3);
        v4 = v0;
        v5 = v1;
        v6 = v2;
        v7 = v3;
        x0 = x20;
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        x0 = RuntimeCalls.InvokeDirect(0xCEAEACUL /* metadata target: bl_UIGradient.BlendColor */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x5B8UL))), unchecked((uint)(x0)));
        x0 = unchecked((ulong)((sp) + (0x340UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x340UL)));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995D10UL /* metadata target: VertexHelper.SetUIVertex */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        x1 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_13538796 = unchecked((uint)(x21));
        __arm64_flags_right_13538796 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13538796) - (__arm64_flags_right_13538796))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13538796)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13538796)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13538796) - (__arm64_flags_right_13538796))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13538796)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE94DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE95F4UL);
        }
        goto label_0xCE9C30;
        label_0xCE95F8:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xCE9C64UL /* metadata target: bl_UIGradient.GetBounds */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v8 = v0;
        v11 = v1;
        v10 = v2;
        v9 = v3;
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_float_flags_left_13538836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13538836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((__arm64_float_flags_left_13538836 == __arm64_float_flags_right_13538836))
        {
            goto label_0xCE9630;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9620UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x38UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xCE9630;
        label_0xCE9630:
        ;
        __arm64_float_flags_left_13538864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13538864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13538864 == __arm64_float_flags_right_13538864))
        {
            goto label_0xCE9648;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9638UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x38UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xCE9648;
        label_0xCE9648:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x30UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE9AEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x44UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x198544CUL /* metadata target: VertexHelper.Clear */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3E1UL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x498UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x490UL))), 0x0UL);
        __arm64_pair_address_13538944 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13538944, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13538944) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        __arm64_pair_address_13538948 = unchecked((ulong)((x25) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13538948, v0);
#else
        __WriteVector128(__arm64_pair_address_13538948, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13538948) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13538948) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x220UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x220UL))), v0);
#endif
        __arm64_pair_address_13538956 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13538956, v2);
#else
        __WriteVector128(__arm64_pair_address_13538956, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13538956) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13538956) + (0x10UL))), v1);
#endif
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE96B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_pair_address_13538976 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13538976);
#else
        v2 = __ReadVector128(__arm64_pair_address_13538976);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13538976) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13538976) + (0x10UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = 0x1BAB000UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x3E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE96B0;
        label_0xCE96B0:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x40UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0));
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1E8UL))));
        x23 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x32CUL))))))));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(x22);
        __arm64_pair_address_13539020 = unchecked((ulong)((sp) + (0x38UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13539020, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13539020) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_13539032 = unchecked((ulong)((x8) + (0x3CUL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13539032)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13539032) + (0x4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x44UL))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9700;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x9)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        goto label_0xCE9700;
        label_0xCE9700:
        ;
        __arm64_pair_address_13539072 = unchecked((ulong)((x8) + (0x18UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13539072)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13539072) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x9 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x3E3UL))))))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9748;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x10 = 0x1BAB000UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x10) + (0x3E3UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        goto label_0xCE9748;
        label_0xCE9748:
        ;
        __arm64_pair_address_13539144 = unchecked((ulong)((x8) + (0x48UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13539144)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13539144) + (0x4UL))))), 0));
        x23 = 0x1A8F000UL;
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x50UL))))), 0));
        x8 = unchecked((ulong)((sp) + (0x600UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC78UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        x2 = RuntimeMemory.ReadU64(x23);
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x608UL))))), 0));
        x2 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x1CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x18UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x28UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x600UL)));
        x1 = unchecked((ulong)((sp) + (0x3B0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x23 = unchecked((ulong)((sp) + (0x600UL)));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x26))))) + (0x7CUL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x614UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x4A0UL))), x8);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x4A8UL))), unchecked((uint)(x9)));
        x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#endif
        x9 = 0x432000UL;
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x3E4UL))))), 0));
        x8 = unchecked((ulong)((sp) + (0x180UL)));
        v8 = (RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)) | RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)).ShiftLeftLogical(unchecked((int)0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#endif
        x26 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x27 = unchecked((ulong)((x23) + (0xCUL)));
        x28 = unchecked((ulong)((x8) + (0xCUL)));
        v9 = (RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)) | RuntimeVector128.Zero.WithUInt32(0, v0.GetUInt32(0)).ShiftLeftLogical(unchecked((int)0x20UL)));
        x10 = unchecked((ulong)((x8) + (0x18UL)));
        x29 = unchecked((ulong)((x8) + (0x3CUL)));
        RuntimeCalls.Unsupported("fmov", 0xCE981CUL);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x0);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x48UL))), x10);
        goto label_0xCE9828;
        label_0xCE9828:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        __arm64_pair_address_13539376 = unchecked((ulong)((x25) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13539376, v0);
#else
        __WriteVector128(__arm64_pair_address_13539376, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13539376) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13539376) + (0x10UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x25) + (0x1E0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x25) + (0x1E0UL))), v0);
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x26))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x3C800000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        x0 = unchecked((ulong)((sp) + (0x9CUL)));
        x1 = unchecked((ulong)((sp) + (0x98UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x458UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x450UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1BAB000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x98UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3E1UL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x9CUL))))), 0));
        __arm64_pair_address_13539448 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13539448, v0);
#else
        __WriteVector128(__arm64_pair_address_13539448, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13539448) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13539448) + (0x10UL))), v1);
#endif
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9894;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x3E1UL))), unchecked((byte)(unchecked((uint)(x9)))));
        goto label_0xCE9894;
        label_0xCE9894:
        ;
        x8 = RuntimeMemory.ReadU64(x22);
        x23 = x22;
        x22 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x32CUL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x3CUL))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x44UL))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE98CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x23;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x32CUL))), unchecked((byte)(unchecked((uint)(x9)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        goto label_0xCE98CC;
        label_0xCE98CC:
        ;
        x9 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x18UL))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x3E3UL))))))));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1E8UL))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9904;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = 0x1BAB000UL;
        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x3E3UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        goto label_0xCE9904;
        label_0xCE9904:
        ;
        __arm64_pair_address_13539588 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_13539588);
#else
        v3 = __ReadVector128(__arm64_pair_address_13539588);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13539588) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13539588) + (0x10UL))));
#endif
        x23 = 0x1A8F000UL;
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeCalls.Unsupported("fmul", 0xCE9914UL);
        RuntimeCalls.Unsupported("fmul", 0xCE9918UL);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x48UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x50UL))))), 0));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC78UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#else
        v4 = __ReadVector128(unchecked((ulong)((sp) + (0x60UL))));
#endif
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xCE9934UL);
        x2 = RuntimeMemory.ReadU64(x23);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#else
        v4 = __ReadVector128(unchecked((ulong)((sp) + (0x50UL))));
#endif
        RuntimeCalls.Unsupported("fmul", 0xCE9944UL);
        x8 = unchecked((ulong)((sp) + (0x600UL)));
        RuntimeCalls.Unsupported("fadd", 0xCE994CUL);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x608UL))))), 0));
        x2 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)((sp) + (0x3B0UL)));
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        RuntimeCalls.Unsupported("fmul", 0xCE996CUL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeCalls.Unsupported("fadd", 0xCE9978UL);
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x600UL)));
        x1 = unchecked((ulong)((sp) + (0x3B0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_pair_address_13539732 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13539732);
#else
        v1 = __ReadVector128(__arm64_pair_address_13539732);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13539732) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13539732) + (0x10UL))));
#endif
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        v0 = v1;
        RuntimeCalls.Unsupported("fadd", 0xCE99A8UL);
        v1 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x3FUL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fmul", 0xCE99B0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(x27);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x180UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x188UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x27) + (0x8UL))))));
        __arm64_pair_address_13539792 = unchecked((ulong)((x25) + (0x1E0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_13539792);
#else
        v1 = __ReadVector128(__arm64_pair_address_13539792);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13539792) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13539792) + (0x10UL))));
#endif
        RuntimeMemory.WriteU64(x28, x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x28) + (0x8UL))), unchecked((uint)(x9)));
        x1 = unchecked((ulong)((sp) + (0x180UL)));
        x2 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x8, v0);
#else
        __WriteVector128(x8, v0);
#endif
        __arm64_pair_address_13539820 = unchecked((ulong)((x25) + (0x1C0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_13539820);
#else
        v0 = __ReadVector128(__arm64_pair_address_13539820);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13539820) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13539820) + (0x10UL))));
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x1A8UL))), unchecked((uint)(x0)));
        x8 = unchecked((ulong)((sp) + (0x110UL)));
        x0 = x19;
        RuntimeMemory.WriteF64(unchecked((ulong)((x8) + (0x9CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1B8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1B4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_13539848 = unchecked((ulong)((x29) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13539848, v2);
#else
        __WriteVector128(__arm64_pair_address_13539848, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13539848) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13539848) + (0x10UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(x29, v0);
#else
        __WriteVector128(x29, v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        x26 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x26))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13539864 = unchecked((uint)(x26));
        __arm64_flags_right_13539864 = unchecked((uint)0x40UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13539864) - (__arm64_flags_right_13539864))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE9828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9A20UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x24UL))))), 0));
        __arm64_pair_address_13539876 = unchecked((ulong)((sp) + (0x18UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13539876)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13539876) + (0x4UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x2CUL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x4A0UL))));
        x9 = 0x433000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x20UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x110UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x28UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x10 = unchecked((ulong)((sp) + (0x110UL)));
        __arm64_pair_address_13539920 = unchecked((ulong)((x25) + (0x200UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_13539920);
#else
        v2 = __ReadVector128(__arm64_pair_address_13539920);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13539920) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13539920) + (0x10UL))));
#endif
        __arm64_pair_address_13539924 = unchecked((ulong)((x25) + (0x220UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v5 = RuntimeMemory.ReadVector128(__arm64_pair_address_13539924);
#else
        v5 = __ReadVector128(__arm64_pair_address_13539924);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_13539924) + (0x10UL))));
#else
        v4 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_13539924) + (0x10UL))));
#endif
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x118UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0x260UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x9) + (0x260UL))));
#endif
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x4A8UL))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x114UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU64(unchecked((ulong)((x10) + (0xCUL))), x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x1 = unchecked((ulong)((sp) + (0x110UL)));
        x0 = x19;
        x2 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x124UL))), unchecked((uint)(x9)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x10) + (0x18UL))), v4);
#else
        __WriteVector128(unchecked((ulong)((x10) + (0x18UL))), v4);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x138UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x10) + (0x3CUL))), v2);
#else
        __WriteVector128(unchecked((ulong)((x10) + (0x3CUL))), v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x10) + (0x4CUL))), v3);
#else
        __WriteVector128(unchecked((ulong)((x10) + (0x4CUL))), v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x10) + (0x2CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x10) + (0x2CUL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x10) + (0x5CUL))), v5);
#else
        __WriteVector128(unchecked((ulong)((x10) + (0x5CUL))), v5);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        __arm64_pair_address_13539996 = unchecked((ulong)((sp) + (0x40UL)));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13539996)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13539996) + (0x4UL))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x38UL))))), 0));
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xCE9AA8;
        label_0xCE9AA8:
        ;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x1UL)))))));
        x3 = unchecked((ulong)(unchecked((uint)(0x40UL))));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13540036 = unchecked((uint)(x21));
        __arm64_flags_right_13540036 = unchecked((uint)0x40UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13540036) - (__arm64_flags_right_13540036))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE9AA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(unchecked((uint)(0x3FUL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x40UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x3CUL))))), 0));
        __arm64_pair_address_13540072 = unchecked((ulong)((sp) + (0x30UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13540072)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13540072) + (0x4UL))))), 0));
        goto label_0xCE9AEC;
        label_0xCE9AEC:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = x19;
        x1 = 0x0UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x24) + (0x5CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x24) + (0x5CUL))), v0);
#endif
        __arm64_pair_address_13540092 = unchecked((ulong)((x24) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13540092, v0);
#else
        __WriteVector128(__arm64_pair_address_13540092, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13540092) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13540092) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13540096 = unchecked((ulong)((x24) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13540096, v0);
#else
        __WriteVector128(__arm64_pair_address_13540096, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13540096) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13540096) + (0x10UL))), v0);
#endif
        __arm64_pair_address_13540100 = x24;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_13540100, v0);
#else
        __WriteVector128(__arm64_pair_address_13540100, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_13540100) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_13540100) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_flags_left_13540108 = unchecked((uint)(x0));
        __arm64_flags_right_13540108 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13540108) - (__arm64_flags_right_13540108))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13540108)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13540108)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13540108) - (__arm64_flags_right_13540108))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13540108)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE9C30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9B14UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x22 = unchecked((ulong)(unchecked((uint)(0x437F0000UL))));
        goto label_0xCE9B30;
        label_0xCE9B30:
        ;
        x1 = unchecked((ulong)((sp) + (0x4B0UL)));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995BB0UL /* metadata target: VertexHelper.PopulateUIVertex */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE9C60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9B4CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4B0UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4B4UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x4D8UL))))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x34UL))))), 0));
        RuntimeCalls.Unsupported("fabd", 0xCE9B5CUL);
        RuntimeCalls.Unsupported("fabd", 0xCE9B60UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)(0x18UL)))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x9))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)0x10UL))))))) & (unchecked((uint)0xFFUL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x9))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)0x8UL))))))) & (unchecked((uint)0xFFUL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0xFFUL)))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x22))), 0)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x9))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((uint)(x8))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x1 = 0x0UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1785F64UL /* metadata target: Gradient.Evaluate */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v4 = v0;
        v5 = v1;
        v6 = v2;
        v7 = v3;
        x0 = x20;
        v0 = v11;
        v1 = v10;
        v2 = v9;
        v3 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xCEAEACUL /* metadata target: bl_UIGradient.BlendColor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x4D8UL))), unchecked((uint)(x0)));
        x0 = unchecked((ulong)((sp) + (0xA0UL)));
        x1 = unchecked((ulong)((sp) + (0x4B0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0xA0UL)));
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995D10UL /* metadata target: VertexHelper.SetUIVertex */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        x1 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_13540392 = unchecked((uint)(x21));
        __arm64_flags_right_13540392 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13540392) - (__arm64_flags_right_13540392))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13540392)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13540392)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13540392) - (__arm64_flags_right_13540392))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13540392)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE9B30;
        }
        else
        {
            goto label_0xCE9C30;
        }
        label_0xCE9C30:
        ;
        sp = unchecked((ulong)((sp) + (0x670UL)));
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
        __arm64_pair_address_13540428 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13540428)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13540428) + (0x8UL))))), 0));
        __arm64_pair_address_13540432 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13540432)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13540432) + (0x8UL))))), 0));
        __arm64_pair_address_13540436 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13540436)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13540436) + (0x8UL))))), 0));
        __arm64_pair_address_13540440 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13540440)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13540440) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13540440) + (0xA0UL)));
        return x0;
        label_0xCE9C60:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `bl_UIGradient.GetBounds` — RVA `0xce9c64`

- Lift status: **partial**; input span: 336 bytes; span to next metadata RVA: 336 bytes.
- Metadata signature: `private Rect GetBounds(List<UIVertex> vertices) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=44 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.gt' at 0xce9d74; reason: Unknown IR expression at 0xce9d74

```csharp
public static ulong bl_UIGradient_GetBounds_RVAce9c64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13540592 = default(uint);
        uint __arm64_flags_left_13540716 = default(uint);
        uint __arm64_flags_right_13540592 = default(uint);
        uint __arm64_flags_right_13540716 = default(uint);
        float __arm64_float_flags_left_13540652 = default(float);
        float __arm64_float_flags_left_13540668 = default(float);
        float __arm64_float_flags_left_13540684 = default(float);
        float __arm64_float_flags_left_13540700 = default(float);
        float __arm64_float_flags_right_13540652 = default(float);
        float __arm64_float_flags_right_13540668 = default(float);
        float __arm64_float_flags_right_13540684 = default(float);
        float __arm64_float_flags_right_13540700 = default(float);
        ulong __arm64_pair_address_13540460 = default(ulong);
        ulong __arm64_pair_address_13540464 = default(ulong);
        ulong __arm64_pair_address_13540764 = default(ulong);
        ulong __arm64_pair_address_13540768 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x70UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13540460 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13540460, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13540460) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13540464 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13540464, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13540464) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x677UL))))))));
        x19 = x1;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9CAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x677UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE9CAC;
        label_0xCE9CAC:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xCE9DB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8F000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC78UL))));
        x8 = sp;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        x8 = sp;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13540592 = unchecked((uint)(x20));
        __arm64_flags_right_13540592 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13540592) - (__arm64_flags_right_13540592))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13540592)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13540592)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13540592) - (__arm64_flags_right_13540592))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13540592)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCE9D7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v10 = v8;
        v9 = v11;
        goto label_0xCE9D00;
        label_0xCE9D00:
        ;
        x2 = RuntimeMemory.ReadU64(x21);
        x8 = sp;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        x8 = sp;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_float_flags_left_13540652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13540652 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13540652 <= __arm64_float_flags_right_13540652) || ((__arm64_float_flags_left_13540652 != __arm64_float_flags_left_13540652) || (__arm64_float_flags_right_13540652 != __arm64_float_flags_right_13540652))))
        {
            goto label_0xCE9D3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v10 = v12;
        goto label_0xCE9D48;
        label_0xCE9D3C:
        ;
        __arm64_float_flags_left_13540668 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13540668 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13540668 >= __arm64_float_flags_right_13540668) || ((__arm64_float_flags_left_13540668 != __arm64_float_flags_left_13540668) || (__arm64_float_flags_right_13540668 != __arm64_float_flags_right_13540668))))
        {
            goto label_0xCE9D48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v8 = v12;
        goto label_0xCE9D48;
        label_0xCE9D48:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        __arm64_float_flags_left_13540684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13540684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13540684 <= __arm64_float_flags_right_13540684) || ((__arm64_float_flags_left_13540684 != __arm64_float_flags_left_13540684) || (__arm64_float_flags_right_13540684 != __arm64_float_flags_right_13540684))))
        {
            goto label_0xCE9D5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v9 = v1;
        goto label_0xCE9D64;
        label_0xCE9D5C:
        ;
        __arm64_float_flags_left_13540700 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13540700 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13540700 < __arm64_float_flags_right_13540700))
        {
            goto label_0xCE9D68;
        }
        else
        {
            goto label_0xCE9D64;
        }
        label_0xCE9D64:
        ;
        v1 = v11;
        goto label_0xCE9D68;
        label_0xCE9D68:
        ;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13540716 = unchecked((uint)(x20));
        __arm64_flags_right_13540716 = unchecked((uint)0x0UL);
        v11 = v1;
        RuntimeCalls.Unsupported("b.gt", 0xCE9D74UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCE9D00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9D78UL);
        }
        goto label_0xCE9D88;
        label_0xCE9D7C:
        ;
        v9 = v11;
        v1 = v11;
        v10 = v8;
        goto label_0xCE9D88;
        label_0xCE9D88:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = v8;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        __arm64_pair_address_13540764 = unchecked((ulong)((sp) + (0x90UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13540764)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13540764) + (0x8UL))))), 0));
        __arm64_pair_address_13540768 = unchecked((ulong)((sp) + (0x80UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13540768)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13540768) + (0x8UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x70UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return x0;
        label_0xCE9DB0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.SplitTrianglesAtGradientStops` — RVA `0xce9db4`

- Lift status: **partial**; input span: 4344 bytes; span to next metadata RVA: 4344 bytes.
- Metadata signature: `private void SplitTrianglesAtGradientStops(List<UIVertex> _vertexList, Rect bounds, float zoomOffset, VertexHelper helper) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=752 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lt' at 0xce9ff0; reason: Unknown IR expression at 0xce9ff0; reason: Unsupported instruction 'b.ne' at 0xcea340; reason: Unknown IR expression at 0xcea340

```csharp
public static ulong bl_UIGradient_SplitTrianglesAtGradientStops_RVAce9db4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13541320 = default(uint);
        uint __arm64_flags_left_13541352 = default(uint);
        uint __arm64_flags_left_13541520 = default(uint);
        ulong __arm64_flags_left_13541624 = default(ulong);
        uint __arm64_flags_left_13541756 = default(uint);
        uint __arm64_flags_left_13541976 = default(uint);
        uint __arm64_flags_left_13542104 = default(uint);
        ulong __arm64_flags_left_13542200 = default(ulong);
        uint __arm64_flags_left_13542228 = default(uint);
        uint __arm64_flags_left_13542496 = default(uint);
        uint __arm64_flags_left_13542832 = default(uint);
        uint __arm64_flags_left_13542960 = default(uint);
        uint __arm64_flags_left_13543228 = default(uint);
        uint __arm64_flags_left_13543444 = default(uint);
        uint __arm64_flags_left_13543516 = default(uint);
        uint __arm64_flags_left_13543596 = default(uint);
        uint __arm64_flags_left_13543668 = default(uint);
        uint __arm64_flags_left_13543932 = default(uint);
        ulong __arm64_flags_left_13544000 = default(ulong);
        ulong __arm64_flags_left_13544060 = default(ulong);
        uint __arm64_flags_left_13544108 = default(uint);
        uint __arm64_flags_left_13544268 = default(uint);
        ulong __arm64_flags_left_13544360 = default(ulong);
        uint __arm64_flags_left_13544512 = default(uint);
        uint __arm64_flags_left_13544520 = default(uint);
        uint __arm64_flags_left_13544816 = default(uint);
        uint __arm64_flags_right_13541320 = default(uint);
        uint __arm64_flags_right_13541352 = default(uint);
        uint __arm64_flags_right_13541520 = default(uint);
        ulong __arm64_flags_right_13541624 = default(ulong);
        uint __arm64_flags_right_13541756 = default(uint);
        uint __arm64_flags_right_13541976 = default(uint);
        uint __arm64_flags_right_13542104 = default(uint);
        ulong __arm64_flags_right_13542200 = default(ulong);
        uint __arm64_flags_right_13542228 = default(uint);
        uint __arm64_flags_right_13542496 = default(uint);
        uint __arm64_flags_right_13542832 = default(uint);
        uint __arm64_flags_right_13542960 = default(uint);
        uint __arm64_flags_right_13543228 = default(uint);
        uint __arm64_flags_right_13543444 = default(uint);
        uint __arm64_flags_right_13543516 = default(uint);
        uint __arm64_flags_right_13543596 = default(uint);
        uint __arm64_flags_right_13543668 = default(uint);
        uint __arm64_flags_right_13543932 = default(uint);
        ulong __arm64_flags_right_13544000 = default(ulong);
        ulong __arm64_flags_right_13544060 = default(ulong);
        uint __arm64_flags_right_13544108 = default(uint);
        uint __arm64_flags_right_13544268 = default(uint);
        ulong __arm64_flags_right_13544360 = default(ulong);
        uint __arm64_flags_right_13544512 = default(uint);
        uint __arm64_flags_right_13544520 = default(uint);
        uint __arm64_flags_right_13544816 = default(uint);
        float __arm64_float_flags_left_13541664 = default(float);
        float __arm64_float_flags_left_13541820 = default(float);
        float __arm64_float_flags_left_13542536 = default(float);
        float __arm64_float_flags_left_13544040 = default(float);
        float __arm64_float_flags_left_13544152 = default(float);
        float __arm64_float_flags_right_13541664 = default(float);
        float __arm64_float_flags_right_13541820 = default(float);
        float __arm64_float_flags_right_13542536 = default(float);
        float __arm64_float_flags_right_13544040 = default(float);
        float __arm64_float_flags_right_13544152 = default(float);
        ulong __arm64_load_address_13544928 = default(ulong);
        ulong __arm64_pair_address_13540792 = default(ulong);
        ulong __arm64_pair_address_13540796 = default(ulong);
        ulong __arm64_pair_address_13544920 = default(ulong);
        ulong __arm64_pair_address_13544924 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
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
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF70UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF70UL)));
        __arm64_pair_address_13540792 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13540792, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13540792) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13540796 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13540796, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13540796) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x950UL)));
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x678UL))))))));
        x24 = x2;
        v9 = v4;
        v8 = v3;
        v10 = v2;
        v11 = v1;
        v12 = v0;
        x20 = x1;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x40UL))), x0);
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE9F30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x678UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE9F30;
        label_0xCE9F30:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x8 = unchecked((ulong)((sp) + (0x6EDUL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0xFFUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0xFFUL))), v0);
#endif
        x8 = unchecked((ulong)((sp) + (0x5DDUL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x7E0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x7E0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x7D0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x7D0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x7C0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x7C0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x7B0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x7B0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x7A0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x7A0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x790UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x790UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x780UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x780UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x770UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x770UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x760UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x760UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x750UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x750UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x740UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x740UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x730UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x730UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x720UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x720UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x710UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x710UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x8) + (0xFFUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x8) + (0xFFUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6D0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6D0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6C0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6C0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6B0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6B0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6A0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6A0UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x690UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x690UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x680UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x680UL))), v0);
#endif
        v0 = v9;
        v1 = v12;
        v2 = v11;
        v3 = v10;
        v4 = v8;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x6F8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x6F0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x700UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xCEAEF8UL /* metadata target: bl_UIGradient.FindStops */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x22 = x0;
        __arm64_flags_left_13541320 = unchecked((uint)(x8));
        __arm64_flags_right_13541320 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13541320) - (__arm64_flags_right_13541320))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13541320)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13541320)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13541320) - (__arm64_flags_right_13541320))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13541320)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEADBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE9FD0UL);
        }
        if ((x24 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x198544CUL /* metadata target: VertexHelper.Clear */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13541352 = unchecked((uint)(x8));
        __arm64_flags_right_13541352 = unchecked((uint)0x1UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.lt", 0xCE9FF0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCEADBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x710UL)));
        x2 = 0x0UL;
        x8 = unchecked((ulong)((x8) + (0x10UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x48UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x38UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x24);
        goto label_0xCEA00C;
        label_0xCEA00C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x958UL))), x2);
        x0 = RuntimeCalls.InvokeDirect(0xCEB290UL /* metadata target: bl_UIGradient.GetPositions */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD40UL))));
        x26 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD10UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x27 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x108F32CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x19 = 0x1A8F000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC80UL))));
        x0 = RuntimeMemory.ReadU64(x19);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = 0x1A8F000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD18UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x23 = x0;
        x2 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0x10D0290UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x28 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10D0290UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        __arm64_flags_left_13541520 = unchecked((uint)(x8));
        __arm64_flags_right_13541520 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13541520) - (__arm64_flags_right_13541520))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13541520)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13541520)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13541520) - (__arm64_flags_right_13541520))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13541520)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEA9F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x29 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x8 = unchecked((ulong)((x26) + (0x24UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x23);
        goto label_0xCEA0A8;
        label_0xCEA0A8:
        ;
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, x2, x3);
        if ((x28 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEA0B8UL);
        }
        if ((x27 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x28) + (0x18UL))))));
        x21 = 0x0UL;
        x24 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x20 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x0UL))), unchecked((uint)(x0)));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x24UL))), unchecked((uint)(x8)));
        goto label_0xCEA0D4;
        label_0xCEA0D4:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE8UL))));
        x0 = x27;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x108FE20UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCEA330;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEA0F0UL);
        }
        if ((x26 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x26) + (0x18UL))))));
        __arm64_flags_left_13541624 = x21;
        __arm64_flags_right_13541624 = x8;
        if ((__arm64_flags_left_13541624 >= __arm64_flags_right_13541624))
        {
            goto label_0xCEADEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x26) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x2UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD38UL))));
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x29))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_float_flags_left_13541664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13541664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13541664 >= __arm64_float_flags_right_13541664) || ((__arm64_float_flags_left_13541664 != __arm64_float_flags_left_13541664) || (__arm64_float_flags_right_13541664 != __arm64_float_flags_right_13541664))))
        {
            goto label_0xCEA330;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(0xAAABUL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC78UL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0xAAAAUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x8 = unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x24))))) * (unchecked((ulong)(unchecked((uint)(x8)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)(0x21UL)))))))));
        x2 = RuntimeMemory.ReadU64(x9);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x1UL))))))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(x8)))))));
        x19 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(x8)))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x958UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(x21)))))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x790UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x26) + (0x18UL))))));
        __arm64_flags_left_13541756 = unchecked((uint)(x19));
        __arm64_flags_right_13541756 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13541756 >= __arm64_flags_right_13541756))
        {
            goto label_0xCEADEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0xAAAAAAAAAAAAAAAAUL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((0xAAABUL) << (int)(unchecked((int)(0x0UL))))))));
        x8 = unchecked((ulong)((unchecked((ulong)((unchecked((ulong)((unchecked((ulong)((unchecked((ulong)((x20) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL))))))))) * (unchecked((ulong)((x8) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL)))))))))))) + (unchecked((ulong)((unchecked((ulong)((unchecked((ulong)((unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x20))))) * (unchecked((ulong)(unchecked((uint)(x8)))))))) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL))))))))) + (unchecked((ulong)((unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x20))))) * (unchecked((ulong)((x8) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL)))))))))))))))) + (unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)((x20) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL))))))))) * (unchecked((ulong)(unchecked((uint)(x8)))))))))))))))))) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL)))))))))))) + (unchecked((ulong)((unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x20))))) * (unchecked((ulong)((x8) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL)))))))))))) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL)))))))))))) + (unchecked((ulong)((unchecked((ulong)((unchecked((ulong)((x20) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL))))))))) * (unchecked((ulong)(unchecked((uint)(x8)))))))) >> (int)(unchecked((int)(unchecked((ulong)(unchecked((uint)0x20UL)))))))))));
        x8 = unchecked((ulong)((x8) >> (int)(unchecked((int)(0x1UL)))));
        x9 = 0xFFFFFFFFFFFFFFF4UL;
        x8 = unchecked((ulong)((unchecked((ulong)((x8) * (x9)))) + (x10)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x2UL)))))))))), 0));
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD38UL))));
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x29))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_float_flags_left_13541820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13541820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13541820 <= __arm64_float_flags_right_13541820) || ((__arm64_float_flags_left_13541820 != __arm64_float_flags_left_13541820) || (__arm64_float_flags_right_13541820 != __arm64_float_flags_right_13541820))))
        {
            goto label_0xCEA230;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD08UL))));
        x0 = x27;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x1090624UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((sp) + (0x8E0UL)));
        x1 = unchecked((ulong)((sp) + (0x790UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD00UL))));
        x0 = unchecked((ulong)((sp) + (0x590UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x23;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x10D1A54UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x2CUL))), unchecked((uint)(x8)));
        goto label_0xCEA330;
        label_0xCEA230:
        ;
        x9 = 0x1A8F000UL;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x27) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xCD0UL))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x9 = RuntimeMemory.ReadU64(x9);
        RuntimeMemory.WriteU32(unchecked((ulong)((x27) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x27) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13541976 = unchecked((uint)(x10));
        __arm64_flags_right_13541976 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13541976 >= __arm64_flags_right_13541976))
        {
            goto label_0xCEA274;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x2UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x27) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x20UL))), unchecked((uint)(x21)));
        goto label_0xCEA28C;
        label_0xCEA274:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x0 = x27;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x108FB08UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCEA28C;
        label_0xCEA28C:
        ;
        x0 = unchecked((ulong)((sp) + (0x610UL)));
        x1 = unchecked((ulong)((sp) + (0x790UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x0 = unchecked((ulong)((sp) + (0x8E0UL)));
        x1 = unchecked((ulong)((sp) + (0x610UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x10UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x23) + (0x1CUL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x23) + (0x18UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13542104 = unchecked((uint)(x9));
        __arm64_flags_right_13542104 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13542104 >= __arm64_flags_right_13542104))
        {
            goto label_0xCEA304;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = unchecked((ulong)((unchecked((ulong)((x9) * (unchecked((ulong)(unchecked((uint)(x11)))))))) + (x8)));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x23) + (0x18UL))), unchecked((uint)(x10)));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCEA330;
        label_0xCEA304:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = unchecked((ulong)((sp) + (0x590UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x23;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x10D0B34UL, x0, x1, x2, x3);
        goto label_0xCEA330;
        label_0xCEA330:
        ;
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13542200 = x21;
        __arm64_flags_right_13542200 = 0x3UL;
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) + (unchecked((uint)(0x1UL)))))));
        RuntimeCalls.Unsupported("b.ne", 0xCEA340UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCEA0D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x27) + (0x18UL))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEA8E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        __arm64_flags_left_13542228 = unchecked((uint)(x8));
        __arm64_flags_right_13542228 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_13542228) - (__arm64_flags_right_13542228))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEA9F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEA35CUL);
        }
        if ((x23 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCF8UL))));
        x0 = x23;
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10D17B4UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x80UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x19 = 0x1A8F000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xCB0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        goto label_0xCEA394;
        label_0xCEA394:
        ;
        x1 = RuntimeMemory.ReadU64(x19);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF12A40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEA3C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x520UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x520UL)));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        goto label_0xCEA394;
        label_0xCEA3C8:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA0UL))));
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF12A3CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x28) + (0x1CUL))))));
        x0 = x27;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x28) + (0x18UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x28) + (0x18UL)))) + (0x8UL))), unchecked((uint)(x8)));
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCF0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1090444UL, x0, x1, x2, x3);
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x590UL))));
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x5A0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        x23 = x24;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x6F0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x6F0UL))), v0);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x700UL))), x8);
        goto label_0xCEA418;
        label_0xCEA418:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCB8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x6F0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0B79CUL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEA60C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEA430UL);
        }
        if ((x26 == 0x0UL))
        {
            goto label_0xCEA900;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x700UL))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x5556UL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x5555UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x26) + (0x18UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) + (unchecked((uint)(0x1UL)))))));
        x9 = unchecked((ulong)(unchecked((long)((unchecked((long)(unchecked((int)(unchecked((uint)(x8))))))) * (unchecked((long)(unchecked((int)(unchecked((uint)(x9)))))))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(0x3FUL)))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(0x20UL)))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x10)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x1UL))))))))))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(x9)))))));
        __arm64_flags_left_13542496 = unchecked((uint)(x20));
        __arm64_flags_right_13542496 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13542496 >= __arm64_flags_right_13542496))
        {
            goto label_0xCEA910;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x26) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD38UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x29))));
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_float_flags_left_13542536 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13542536 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13542536 >= __arm64_float_flags_right_13542536) || ((__arm64_float_flags_left_13542536 != __arm64_float_flags_left_13542536) || (__arm64_float_flags_right_13542536 != __arm64_float_flags_right_13542536))))
        {
            goto label_0xCEA4BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        x10 = unchecked((ulong)(unchecked((uint)(0x5556UL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((int)(unchecked((sbyte)(unchecked((byte)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x5555UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x9 = unchecked((ulong)(unchecked((long)((unchecked((long)(unchecked((int)(unchecked((uint)(x9))))))) * (unchecked((long)(unchecked((int)(unchecked((uint)(x10)))))))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(0x3FUL)))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(0x20UL)))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x10)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x1UL))))))))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(x9)))))));
        x20 = unchecked((ulong)(unchecked((uint)(unchecked((int)(unchecked((sbyte)(unchecked((byte)(unchecked((uint)(x8))))))))))));
        goto label_0xCEA4BC;
        label_0xCEA4BC:
        ;
        x24 = 0x1A8F000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xC78UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x958UL))));
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) + (unchecked((uint)(x25)))))));
        x8 = unchecked((ulong)((sp) + (0x8E0UL)));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x590UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(x25)))))));
        x8 = unchecked((ulong)((sp) + (0x610UL)));
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x8E0UL)));
        x1 = unchecked((ulong)((sp) + (0x610UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD38UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x29))));
        x24 = x23;
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x4B0UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((sp) + (0x440UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x8 = unchecked((ulong)((sp) + (0x610UL)));
        x1 = unchecked((ulong)((sp) + (0x4B0UL)));
        x2 = unchecked((ulong)((sp) + (0x440UL)));
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xCEB414UL /* metadata target: bl_UIGradient.CreateSplitVertex */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x3D0UL)));
        x1 = unchecked((ulong)((sp) + (0x610UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x0 = unchecked((ulong)((sp) + (0x800UL)));
        x1 = unchecked((ulong)((sp) + (0x3D0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x28) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0x10UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x28) + (0x1CUL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCEA908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x28) + (0x18UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13542832 = unchecked((uint)(x9));
        __arm64_flags_right_13542832 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13542832 >= __arm64_flags_right_13542832))
        {
            goto label_0xCEA5DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = unchecked((ulong)((unchecked((ulong)((x9) * (unchecked((ulong)(unchecked((uint)(x11)))))))) + (x8)));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x1 = unchecked((ulong)((sp) + (0x800UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x28) + (0x18UL))), unchecked((uint)(x10)));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCEA418;
        label_0xCEA5DC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = unchecked((ulong)((sp) + (0x870UL)));
        x1 = unchecked((ulong)((sp) + (0x800UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x870UL)));
        x0 = x28;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x10D0B34UL, x0, x1, x2, x3);
        goto label_0xCEA418;
        label_0xCEA60C:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA8UL))));
        x0 = unchecked((ulong)((sp) + (0x6F0UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF0B798UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x28) + (0x18UL))))));
        x21 = 0x1A8F000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xCB0UL))));
        __arm64_flags_left_13542960 = unchecked((uint)(x8));
        __arm64_flags_right_13542960 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13542960) - (__arm64_flags_right_13542960))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCEA798;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = 0x1A8F000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD30UL))));
        x0 = x27;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = RuntimeMemory.ReadU64(x19);
        x0 = RuntimeCalls.InvokeDirect(0x108F818UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x9 = unchecked((ulong)(unchecked((uint)(0x5556UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(0x2UL)))))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x5555UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x9 = unchecked((ulong)(unchecked((long)((unchecked((long)(unchecked((int)(unchecked((uint)(x8))))))) * (unchecked((long)(unchecked((int)(unchecked((uint)(x9)))))))))));
        x2 = RuntimeMemory.ReadU64(x19);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(0x3FUL)))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(0x20UL)))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x10)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x1UL))))))))))));
        x0 = x27;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x19 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(x9)))))));
        x0 = RuntimeCalls.InvokeDirect(0x108F818UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x24 = 0x1A8F000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xC78UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x958UL))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(x25)))))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x360UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) + (unchecked((uint)(x25)))))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = unchecked((ulong)((sp) + (0x2F0UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD38UL))));
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)(x29))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x8 = unchecked((ulong)((sp) + (0x280UL)));
        x1 = unchecked((ulong)((sp) + (0x360UL)));
        x2 = unchecked((ulong)((sp) + (0x2F0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xCEB414UL /* metadata target: bl_UIGradient.CreateSplitVertex */, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x0 = unchecked((ulong)((sp) + (0x8E0UL)));
        x1 = unchecked((ulong)((sp) + (0x280UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x28) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0x10UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x28) + (0x1CUL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x28) + (0x18UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13543228 = unchecked((uint)(x9));
        __arm64_flags_right_13543228 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13543228 >= __arm64_flags_right_13543228))
        {
            goto label_0xCEA768;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = unchecked((ulong)((unchecked((ulong)((x9) * (unchecked((ulong)(unchecked((uint)(x11)))))))) + (x8)));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x28) + (0x18UL))), unchecked((uint)(x10)));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCEA794;
        label_0xCEA768:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = unchecked((ulong)((sp) + (0x590UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x28;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x10D0B34UL, x0, x1, x2, x3);
        goto label_0xCEA794;
        label_0xCEA794:
        ;
        x24 = x23;
        goto label_0xCEA798;
        label_0xCEA798:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCF8UL))));
        x0 = x28;
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10D17B4UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x80UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x28UL))))));
        goto label_0xCEA7C8;
        label_0xCEA7C8:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF12A40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEA7FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        x0 = unchecked((ulong)((sp) + (0x210UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x210UL)));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        goto label_0xCEA7C8;
        label_0xCEA7FC:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA0UL))));
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF12A3CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x24UL))))));
        __arm64_flags_left_13543444 = unchecked((uint)(x8));
        __arm64_flags_right_13543444 = unchecked((uint)0x0UL);
        if (((unchecked((uint)((__arm64_flags_left_13543444) - (__arm64_flags_right_13543444))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543444) - (__arm64_flags_right_13543444))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13543444)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13543444)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543444) - (__arm64_flags_right_13543444))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13543444)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xCEA880;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) - (unchecked((uint)(0x2UL)))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) + (unchecked((uint)(0x1UL)))))));
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = unchecked((ulong)(unchecked((uint)(x19))));
        x3 = unchecked((ulong)(unchecked((uint)(x21))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x25 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) - (unchecked((uint)(0x1UL)))))));
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = unchecked((ulong)(unchecked((uint)(x25))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        __arm64_flags_left_13543516 = unchecked((uint)(x8));
        __arm64_flags_right_13543516 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543516) - (__arm64_flags_right_13543516))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13543516)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13543516)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543516) - (__arm64_flags_right_13543516))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13543516)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEA8DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x2CUL))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) + (unchecked((uint)(0x3UL)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEA8C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x3 = unchecked((ulong)(unchecked((uint)(x19))));
        goto label_0xCEA8D4;
        label_0xCEA880:
        ;
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x2UL)))))));
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x3 = unchecked((ulong)(unchecked((uint)(x21))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        __arm64_flags_left_13543596 = unchecked((uint)(x8));
        __arm64_flags_right_13543596 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543596) - (__arm64_flags_right_13543596))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13543596)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13543596)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543596) - (__arm64_flags_right_13543596))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13543596)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEA8DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) + (unchecked((uint)(0x1UL)))))));
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        goto label_0xCEA8D4;
        label_0xCEA8C8:
        ;
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x3 = unchecked((ulong)(unchecked((uint)(x25))));
        goto label_0xCEA8D4;
        label_0xCEA8D4:
        ;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCEA8DC;
        label_0xCEA8DC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x1CUL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x23) + (0x18UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x23) + (0x18UL)))) + (0x8UL))), unchecked((uint)(x8)));
        goto label_0xCEA8E8;
        label_0xCEA8E8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        x29 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x29))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13543668 = unchecked((uint)(x29));
        __arm64_flags_right_13543668 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543668) - (__arm64_flags_right_13543668))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13543668)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13543668)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543668) - (__arm64_flags_right_13543668))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13543668)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEA0A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEA8FCUL);
        }
        goto label_0xCEA9F4;
        label_0xCEA900:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCEAE00;
        label_0xCEA908:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCEADF8;
        label_0xCEA910:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCEADF8;
        label_0xCEA9F4:
        ;
        if ((x28 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x28) + (0x18UL))))));
        __arm64_flags_left_13543932 = unchecked((uint)(x8));
        __arm64_flags_right_13543932 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543932) - (__arm64_flags_right_13543932))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13543932)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13543932)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13543932) - (__arm64_flags_right_13543932))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13543932)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEAC60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEAA04UL);
        }
        if ((x23 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCEABB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEAA10UL);
        }
        if ((x27 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x0UL;
        x20 = unchecked((ulong)((x26) + (0x20UL)));
        goto label_0xCEAA1C;
        label_0xCEAA1C:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE8UL))));
        x0 = x27;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x108FE20UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCEABA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEAA38UL);
        }
        if ((x26 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x26) + (0x18UL))))));
        __arm64_flags_left_13544000 = x21;
        __arm64_flags_right_13544000 = x8;
        if ((__arm64_flags_left_13544000 >= __arm64_flags_right_13544000))
        {
            goto label_0xCEADEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8F000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x2UL)))))))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD38UL))));
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        x2 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_13544040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13544040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13544040 <= __arm64_float_flags_right_13544040) || ((__arm64_float_flags_left_13544040 != __arm64_float_flags_left_13544040) || (__arm64_float_flags_right_13544040 != __arm64_float_flags_right_13544040))))
        {
            goto label_0xCEABA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC78UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        __arm64_flags_left_13544060 = x21;
        __arm64_flags_right_13544060 = 0x2UL;
        x19 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_13544060) - (__arm64_flags_right_13544060))) == 0x0UL) ? unchecked((uint)0x0UL) : unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)0x1UL)))))));
        x2 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x958UL))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(x21)))))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = unchecked((ulong)((sp) + (0x680UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x26) + (0x18UL))))));
        __arm64_flags_left_13544108 = unchecked((uint)(x19));
        __arm64_flags_right_13544108 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13544108 >= __arm64_flags_right_13544108))
        {
            goto label_0xCEADEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x26) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        x8 = 0x1A8F000UL;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x18UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD38UL))));
        x0 = x22;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(0x1UL)))))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_float_flags_left_13544152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13544152 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13544152 <= __arm64_float_flags_right_13544152) || ((__arm64_float_flags_left_13544152 != __arm64_float_flags_left_13544152) || (__arm64_float_flags_right_13544152 != __arm64_float_flags_right_13544152))))
        {
            goto label_0xCEAB14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD00UL))));
        x0 = unchecked((ulong)((sp) + (0x590UL)));
        x1 = unchecked((ulong)((sp) + (0x680UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x2 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x23;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x10D1A54UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCEABA4;
        label_0xCEAB14:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x0 = unchecked((ulong)((sp) + (0x8E0UL)));
        x1 = unchecked((ulong)((sp) + (0x680UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x19 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x10UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x23) + (0x1CUL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCEADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x23) + (0x18UL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13544268 = unchecked((uint)(x9));
        __arm64_flags_right_13544268 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13544268 >= __arm64_flags_right_13544268))
        {
            goto label_0xCEAB78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = unchecked((ulong)((unchecked((ulong)((x9) * (unchecked((ulong)(unchecked((uint)(x11)))))))) + (x8)));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x23) + (0x18UL))), unchecked((uint)(x10)));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xCEABA4;
        label_0xCEAB78:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x0 = unchecked((ulong)((sp) + (0x590UL)));
        x1 = unchecked((ulong)((sp) + (0x8E0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x23;
        x2 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x10D0B34UL, x0, x1, x2, x3);
        goto label_0xCEABA4;
        label_0xCEABA4:
        ;
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        __arm64_flags_left_13544360 = x21;
        __arm64_flags_right_13544360 = 0x3UL;
        if ((!((unchecked((ulong)((__arm64_flags_left_13544360) - (__arm64_flags_right_13544360))) == 0x0UL))))
        {
            goto label_0xCEAA1C;
        }
        else
        {
            goto label_0xCEABB0;
        }
        label_0xCEABB0:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCF8UL))));
        x0 = x23;
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = RuntimeCalls.InvokeDirect(0x10D17B4UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x80UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x19 = 0x1A8F000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xCB0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        goto label_0xCEABE4;
        label_0xCEABE4:
        ;
        x1 = RuntimeMemory.ReadU64(x19);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF12A40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEAC18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x1A0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)((sp) + (0x1A0UL)));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, x3);
        goto label_0xCEABE4;
        label_0xCEAC18:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA0UL))));
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF12A3CUL, x0, x1, x2, x3);
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        __arm64_flags_left_13544512 = unchecked((uint)(x8));
        __arm64_flags_right_13544512 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13544512) - (__arm64_flags_right_13544512))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13544512)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13544512)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13544512) - (__arm64_flags_right_13544512))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13544512)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEAD28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEAC48UL);
        }
        __arm64_flags_left_13544520 = unchecked((uint)(x8));
        __arm64_flags_right_13544520 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13544520) - (__arm64_flags_right_13544520))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCEAD60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x3UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x1UL)))))));
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x2UL)))))));
        goto label_0xCEAD20;
        label_0xCEAC60:
        ;
        x19 = 0x1A8F000UL;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC78UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x958UL))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x20;
        x2 = RuntimeMemory.ReadU64(x19);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = unchecked((ulong)((sp) + (0x130UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)((sp) + (0x130UL)));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x2 = RuntimeMemory.ReadU64(x19);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = unchecked((ulong)((sp) + (0xC0UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)((sp) + (0xC0UL)));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x2 = RuntimeMemory.ReadU64(x19);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x2UL)))))));
        x8 = unchecked((ulong)((sp) + (0x590UL)));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = unchecked((ulong)((sp) + (0x590UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)((sp) + (0x50UL)));
        x0 = x24;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996560UL /* metadata target: VertexHelper.AddVert */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x24;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1995B18UL /* metadata target: VertexHelper.get_currentVertCount */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x3UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x2UL)))))));
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x1UL)))))));
        goto label_0xCEAD20;
        label_0xCEAD20:
        ;
        x0 = x24;
        goto label_0xCEAD58;
        label_0xCEAD28:
        ;
        x19 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x4UL)))))));
        x25 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x1UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x2UL)))))));
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x3 = unchecked((ulong)(unchecked((uint)(x25))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x3UL)))))));
        x0 = x24;
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x2 = unchecked((ulong)(unchecked((uint)(x25))));
        goto label_0xCEAD58;
        label_0xCEAD58:
        ;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1985698UL /* metadata target: VertexHelper.AddTriangle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCEAD60;
        label_0xCEAD60:
        ;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x958UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0xCUL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        x2 = unchecked((ulong)((x2) + (0x3UL)));
        __arm64_flags_left_13544816 = unchecked((uint)(x2));
        __arm64_flags_right_13544816 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13544816) - (__arm64_flags_right_13544816))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13544816)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13544816)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13544816) - (__arm64_flags_right_13544816))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13544816)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEA00C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEAD78UL);
        }
        goto label_0xCEADBC;
        label_0xCEADBC:
        ;
        sp = unchecked((ulong)((sp) + (0x950UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_13544920 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13544920)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13544920) + (0x8UL))))), 0));
        __arm64_pair_address_13544924 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13544924)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13544924) + (0x8UL))))), 0));
        __arm64_load_address_13544928 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_13544928)), 0));
        sp = unchecked((ulong)((__arm64_load_address_13544928) + (0x90UL)));
        return x0;
        label_0xCEADE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCEADEC;
        label_0xCEADEC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = 0x0UL;
        goto label_0xCEAE80;
        label_0xCEADF8:
        ;
        x21 = 0x0UL;
        goto label_0xCEAE5C;
        label_0xCEAE00:
        ;
        x21 = 0x0UL;
        goto label_0xCEAE38;
        label_0xCEAE38:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF12A3CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCEAE98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = x0;
        goto label_0xCEAE5C;
        label_0xCEAE5C:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x710UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF12A3CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x21 == 0x0UL))
        {
            goto label_0xCEAE98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = x0;
        goto label_0xCEAE80;
        label_0xCEAE80:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x6F0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0B798UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x21 != 0x0UL))
        {
            goto label_0xCEAEA0;
        }
        else
        {
            goto label_0xCEAE98;
        }
        label_0xCEAE98:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xCEAEA0;
        label_0xCEAEA0:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `bl_UIGradient.BlendColor` — RVA `0xceaeac`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `private Color BlendColor(Color colorA, Color colorB) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong bl_UIGradient_BlendColor_RVAceaeac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13545136 = default(uint);
        uint __arm64_flags_left_13545144 = default(uint);
        uint __arm64_flags_right_13545136 = default(uint);
        uint __arm64_flags_right_13545144 = default(uint);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v7 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x2CUL))))));
        __arm64_flags_left_13545136 = unchecked((uint)(x8));
        __arm64_flags_right_13545136 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13545136) - (__arm64_flags_right_13545136))) == unchecked((uint)0x0UL)))
        {
            label_0xCEAED4:
            ;
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
            v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
        }
        else
        {
            __arm64_flags_left_13545144 = unchecked((uint)(x8));
            __arm64_flags_right_13545144 = unchecked((uint)0x1UL);
            if ((!((unchecked((uint)((__arm64_flags_left_13545144) - (__arm64_flags_right_13545144))) == unchecked((uint)0x0UL)))))
            {
            }
            else
            {
                v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
                v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
                v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v6.GetUInt64(0)))), 0))))), 0));
                v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v7.GetUInt64(0)))), 0))))), 0));
            }
        }
        label_0xCEAEE4:
        ;
        return x0;
        return default(ulong);
    }
```

## `bl_UIGradient.FindStops` — RVA `0xceaef8`

- Lift status: **partial**; input span: 920 bytes; span to next metadata RVA: 920 bytes.
- Metadata signature: `private List<float> FindStops(float zoomOffset, Rect bounds) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=122 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xceb020; reason: Unsupported instruction 'b.hs' at 0xceb024; reason: Unknown IR expression at 0xceb024; reason: Unsupported instruction 'cmp' at 0xceb0a8; reason: Unsupported instruction 'b.lt' at 0xceb0ac; reason: Unknown IR expression at 0xceb0ac; reason: Unsupported instruction 'cmp' at 0xceb0e0; reason: Unsupported instruction 'b.hs' at 0xceb0e4

```csharp
public static ulong bl_UIGradient_FindStops_RVAceaef8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13545480 = default(uint);
        uint __arm64_flags_left_13545580 = default(uint);
        uint __arm64_flags_left_13545676 = default(uint);
        uint __arm64_flags_left_13545772 = default(uint);
        uint __arm64_flags_left_13545844 = default(uint);
        uint __arm64_flags_left_13545884 = default(uint);
        uint __arm64_flags_left_13545972 = default(uint);
        uint __arm64_flags_left_13546076 = default(uint);
        uint __arm64_flags_result_13545972 = default(uint);
        uint __arm64_flags_right_13545480 = default(uint);
        uint __arm64_flags_right_13545580 = default(uint);
        uint __arm64_flags_right_13545676 = default(uint);
        uint __arm64_flags_right_13545772 = default(uint);
        uint __arm64_flags_right_13545844 = default(uint);
        uint __arm64_flags_right_13545884 = default(uint);
        uint __arm64_flags_right_13545972 = default(uint);
        uint __arm64_flags_right_13546076 = default(uint);
        float __arm64_float_flags_left_13545516 = default(float);
        float __arm64_float_flags_left_13545524 = default(float);
        float __arm64_float_flags_left_13545708 = default(float);
        float __arm64_float_flags_left_13545716 = default(float);
        float __arm64_float_flags_left_13546040 = default(float);
        float __arm64_float_flags_right_13545516 = default(float);
        float __arm64_float_flags_right_13545524 = default(float);
        float __arm64_float_flags_right_13545708 = default(float);
        float __arm64_float_flags_right_13545716 = default(float);
        float __arm64_float_flags_right_13546040 = default(float);
        ulong __arm64_pair_address_13545208 = default(ulong);
        ulong __arm64_pair_address_13545212 = default(ulong);
        ulong __arm64_pair_address_13545216 = default(ulong);
        ulong __arm64_pair_address_13546104 = default(ulong);
        ulong __arm64_pair_address_13546108 = default(ulong);
        ulong __arm64_pair_address_13546112 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_13545208 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13545208, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13545208) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = __arm64_pair_address_13545208;
        __arm64_pair_address_13545212 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13545212, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13545212) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13545216 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13545216, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13545216) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x22 = 0x1A8F000UL;
        x19 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x67AUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD48UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD50UL))));
        v8 = v4;
        v10 = v3;
        v9 = v2;
        v11 = v1;
        v12 = v0;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCEAFBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x67AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCEAFBC;
        label_0xCEAFBC:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10AF5BCUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEAFD8UL);
        }
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x34UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1786020UL /* metadata target: Gradient.get_colorKeys */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8F000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD58UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        x21 = x0;
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_flags_left_13545480 = unchecked((uint)(x8));
        __arm64_flags_right_13545480 = unchecked((uint)0x1UL);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545480) - (__arm64_flags_right_13545480))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13545480)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13545480)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545480) - (__arm64_flags_right_13545480))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13545480)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEB0B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x24 = unchecked((ulong)((x21) + (0x30UL)));
        goto label_0xCEB020;
        label_0xCEB020:
        ;
        RuntimeCalls.Unsupported("cmp", 0xCEB020UL);
        RuntimeCalls.Unsupported("b.hs", 0xCEB024UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCEB28C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB028UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x24)), 0));
        __arm64_float_flags_left_13545516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13545516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13545516 >= __arm64_float_flags_right_13545516))
        {
            goto label_0xCEB0B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB034UL);
        }
        __arm64_float_flags_left_13545524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13545524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13545524 <= __arm64_float_flags_right_13545524) || ((__arm64_float_flags_left_13545524 != __arm64_float_flags_left_13545524) || (__arm64_float_flags_right_13545524 != __arm64_float_flags_right_13545524))))
        {
            goto label_0xCEB09C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB03CUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x1CUL))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x38UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x22);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_flags_left_13545580 = unchecked((uint)(x10));
        __arm64_flags_right_13545580 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13545580 >= __arm64_flags_right_13545580))
        {
            goto label_0xCEB088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x2UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xCEB09C;
        label_0xCEB088:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10AFE10UL, x0, x1, x2, x3);
        goto label_0xCEB09C;
        label_0xCEB09C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        x24 = unchecked((ulong)((x24) + (0x14UL)));
        RuntimeCalls.Unsupported("cmp", 0xCEB0A8UL);
        RuntimeCalls.Unsupported("b.lt", 0xCEB0ACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCEB020;
        }
        else
        {
            goto label_0xCEB0B0;
        }
        label_0xCEB0B0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17860A0UL /* metadata target: Gradient.get_alphaKeys */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x21 = x0;
        __arm64_flags_left_13545676 = unchecked((uint)(x8));
        __arm64_flags_right_13545676 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545676) - (__arm64_flags_right_13545676))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13545676)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13545676)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545676) - (__arm64_flags_right_13545676))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13545676)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEB170;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x0UL;
        x8 = unchecked((ulong)((x8) & (0xFFFFFFFFUL)));
        x24 = unchecked((ulong)((x21) + (0x24UL)));
        goto label_0xCEB0E0;
        label_0xCEB0E0:
        ;
        RuntimeCalls.Unsupported("cmp", 0xCEB0E0UL);
        RuntimeCalls.Unsupported("b.hs", 0xCEB0E4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCEB28C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB0E8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x24)), 0));
        __arm64_float_flags_left_13545708 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13545708 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_13545708 >= __arm64_float_flags_right_13545708))
        {
            goto label_0xCEB170;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB0F4UL);
        }
        __arm64_float_flags_left_13545716 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13545716 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13545716 <= __arm64_float_flags_right_13545716) || ((__arm64_float_flags_left_13545716 != __arm64_float_flags_left_13545716) || (__arm64_float_flags_right_13545716 != __arm64_float_flags_right_13545716))))
        {
            goto label_0xCEB15C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB0FCUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x1CUL))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x38UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x22);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_flags_left_13545772 = unchecked((uint)(x10));
        __arm64_flags_right_13545772 = unchecked((uint)(x11));
        if ((__arm64_flags_left_13545772 >= __arm64_flags_right_13545772))
        {
            goto label_0xCEB148;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x2UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xCEB15C;
        label_0xCEB148:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10AFE10UL, x0, x1, x2, x3);
        goto label_0xCEB15C;
        label_0xCEB15C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        x24 = unchecked((ulong)((x24) + (0x8UL)));
        RuntimeCalls.Unsupported("cmp", 0xCEB168UL);
        RuntimeCalls.Unsupported("b.lt", 0xCEB16CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xCEB0E0;
        }
        else
        {
            goto label_0xCEB170;
        }
        label_0xCEB170:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x28UL))))));
        __arm64_flags_left_13545844 = unchecked((uint)(x8));
        __arm64_flags_right_13545844 = unchecked((uint)0x1UL);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_13545844) - (__arm64_flags_right_13545844))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_13545844) - (__arm64_flags_right_13545844))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))), 0));
        if ((x19 == 0x0UL))
        {
            goto label_0xCEB288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD68UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10B14ECUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        __arm64_flags_left_13545884 = unchecked((uint)(x8));
        __arm64_flags_right_13545884 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545884) - (__arm64_flags_right_13545884))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13545884)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13545884)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545884) - (__arm64_flags_right_13545884))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13545884)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEB264;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8F000UL;
        x23 = 0x1A8F000UL;
        x24 = 0x1A8C000UL;
        x25 = 0x1A8F000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD38UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD70UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xA60UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xD60UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        goto label_0xCEB1CC;
        label_0xCEB1CC:
        ;
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10AFB6CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_flags_left_13545972 = unchecked((uint)(x20));
        __arm64_flags_right_13545972 = unchecked((uint)0x1UL);
        __arm64_flags_result_13545972 = unchecked((uint)((__arm64_flags_left_13545972) - (__arm64_flags_right_13545972)));
        x21 = unchecked((ulong)(__arm64_flags_result_13545972));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545972) - (__arm64_flags_right_13545972))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13545972)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13545972)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13545972) - (__arm64_flags_right_13545972))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13545972)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEB254;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x10AFB18UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        v9 = v0;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCEB234;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB230UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCEB234;
        label_0xCEB234:
        ;
        RuntimeCalls.Unsupported("fabd", 0xCEB234UL);
        __arm64_float_flags_left_13546040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13546040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_13546040 >= __arm64_float_flags_right_13546040) || ((__arm64_float_flags_left_13546040 != __arm64_float_flags_left_13546040) || (__arm64_float_flags_right_13546040 != __arm64_float_flags_right_13546040))))
        {
            goto label_0xCEB254;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x25);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10B1328UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = unchecked((ulong)(unchecked((uint)(x21))));
        goto label_0xCEB254;
        label_0xCEB254:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13546076 = unchecked((uint)(x20));
        __arm64_flags_right_13546076 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13546076) - (__arm64_flags_right_13546076))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13546076)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13546076)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13546076) - (__arm64_flags_right_13546076))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13546076)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCEB1CC;
        }
        else
        {
            goto label_0xCEB264;
        }
        label_0xCEB264:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_13546104 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13546104)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13546104) + (0x8UL))))), 0));
        __arm64_pair_address_13546108 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13546108)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13546108) + (0x8UL))))), 0));
        __arm64_pair_address_13546112 = sp;
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13546112)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13546112) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13546112) + (0x70UL)));
        return x0;
        label_0xCEB288:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCEB28C;
        label_0xCEB28C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.GetPositions` — RVA `0xceb290`

- Lift status: **exact**; input span: 388 bytes; span to next metadata RVA: 388 bytes.
- Metadata signature: `private float[] GetPositions(List<UIVertex> _vertexList, int index) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=54 (informational only).

```csharp
public static ulong bl_UIGradient_GetPositions_RVAceb290(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13546308 = default(uint);
        uint __arm64_flags_left_13546348 = default(uint);
        uint __arm64_flags_left_13546428 = default(uint);
        uint __arm64_flags_left_13546468 = default(uint);
        uint __arm64_flags_right_13546308 = default(uint);
        uint __arm64_flags_right_13546348 = default(uint);
        uint __arm64_flags_right_13546428 = default(uint);
        uint __arm64_flags_right_13546468 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x23 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x679UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x2C0UL))));
        x21 = unchecked((ulong)(unchecked((uint)(x2))));
        x19 = x1;
        x22 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCEB2E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x679UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCEB2E0;
        label_0xCEB2E0:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xCEB410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x28UL))))));
        x22 = 0x1A8F000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC78UL))));
        x20 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEB37C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCEB410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEB40C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB324UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13546308 = unchecked((uint)(x8));
        __arm64_flags_right_13546308 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13546308 >= __arm64_flags_right_13546308))) || (unchecked((uint)((__arm64_flags_left_13546308) - (__arm64_flags_right_13546308))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCEB40C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB34CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x2UL)))))));
        x0 = x19;
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13546348 = unchecked((uint)(x8));
        __arm64_flags_right_13546348 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13546348 >= __arm64_flags_right_13546348))) || (unchecked((uint)((__arm64_flags_left_13546348) - (__arm64_flags_right_13546348))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCEB40C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB374UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        goto label_0xCEB3F0;
        label_0xCEB37C:
        ;
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCEB410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEB40C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB39CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x20UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13546428 = unchecked((uint)(x8));
        __arm64_flags_right_13546428 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13546428 >= __arm64_flags_right_13546428))) || (unchecked((uint)((__arm64_flags_left_13546428) - (__arm64_flags_right_13546428))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCEB40C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB3C4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x2UL)))))));
        x0 = x19;
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x24UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x2 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0x10D077CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13546468 = unchecked((uint)(x8));
        __arm64_flags_right_13546468 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13546468 >= __arm64_flags_right_13546468))) || (unchecked((uint)((__arm64_flags_left_13546468) - (__arm64_flags_right_13546468))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCEB40C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB3ECUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        goto label_0xCEB3F0;
        label_0xCEB3F0:
        ;
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x28UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        return x0;
        label_0xCEB40C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCEB410;
        label_0xCEB410:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `bl_UIGradient.CreateSplitVertex` — RVA `0xceb414`

- Lift status: **exact**; input span: 340 bytes; span to next metadata RVA: 340 bytes.
- Metadata signature: `private UIVertex CreateSplitVertex(UIVertex vertex1, UIVertex vertex2, float stop) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong bl_UIGradient_CreateSplitVertex_RVAceb414(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_13546520 = default(ulong);
        ulong __arm64_pair_address_13546524 = default(ulong);
        ulong __arm64_pair_address_13546528 = default(ulong);
        ulong __arm64_pair_address_13546532 = default(ulong);
        ulong __arm64_pair_address_13546556 = default(ulong);
        ulong __arm64_pair_address_13546560 = default(ulong);
        ulong __arm64_pair_address_13546564 = default(ulong);
        ulong __arm64_pair_address_13546568 = default(ulong);
        ulong __arm64_pair_address_13546660 = default(ulong);
        ulong __arm64_pair_address_13546668 = default(ulong);
        ulong __arm64_pair_address_13546672 = default(ulong);
        ulong __arm64_pair_address_13546676 = default(ulong);
        ulong __arm64_pair_address_13546680 = default(ulong);
        ulong __arm64_pair_address_13546772 = default(ulong);
        ulong __arm64_pair_address_13546800 = default(ulong);
        ulong __arm64_pair_address_13546832 = default(ulong);
        ulong __arm64_pair_address_13546836 = default(ulong);
        ulong __arm64_pair_address_13546840 = default(ulong);
        ulong __arm64_pair_address_13546844 = default(ulong);
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
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        __arm64_pair_address_13546520 = unchecked((ulong)((sp) + (0x70UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13546520, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13546520) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_13546524 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13546524, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13546524) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13546528 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13546528, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13546528) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13546532 = unchecked((ulong)((sp) + (0xA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13546532, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13546532) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x28UL))))));
        v8 = v0;
        x19 = x8;
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            label_0xCEB4AC:
            ;
            __arm64_pair_address_13546668 = x1;
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546668)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546668) + (0x4UL))))), 0));
            __arm64_pair_address_13546672 = x2;
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546672)), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546672) + (0x4UL))))), 0));
            __arm64_pair_address_13546676 = unchecked((ulong)((x1) + (0x2CUL)));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546676)), 0));
            v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546676) + (0x4UL))))), 0));
            __arm64_pair_address_13546680 = unchecked((ulong)((x2) + (0x2CUL)));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546680)), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546680) + (0x4UL))))), 0));
            v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x1) + (0x8UL))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
            v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            x0 = sp;
            x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
            v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
            v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
            v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
            v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            x0 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
            __arm64_pair_address_13546772 = x19;
            RuntimeMemory.WriteF32(__arm64_pair_address_13546772, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13546772) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0));
        }
        else
        {
            __arm64_pair_address_13546556 = x1;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546556)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546556) + (0x4UL))))), 0));
            __arm64_pair_address_13546560 = x2;
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546560)), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546560) + (0x4UL))))), 0));
            __arm64_pair_address_13546564 = unchecked((ulong)((x1) + (0x2CUL)));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546564)), 0));
            v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546564) + (0x4UL))))), 0));
            __arm64_pair_address_13546568 = unchecked((ulong)((x2) + (0x2CUL)));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13546568)), 0));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13546568) + (0x4UL))))), 0));
            v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x1) + (0x8UL))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
            v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            x0 = sp;
            x2 = unchecked((ulong)(unchecked((uint)(0x6CUL))));
            v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
            v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
            v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
            v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            x0 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xCEB8D4UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
            __arm64_pair_address_13546660 = x19;
            RuntimeMemory.WriteF32(__arm64_pair_address_13546660, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13546660) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        }
        label_0xCEB518:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x14UL))))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xCUL))));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x18UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x18UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x28UL))), unchecked((uint)(x0)));
        __arm64_pair_address_13546800 = unchecked((ulong)((x19) + (0x2CUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_13546800, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_13546800) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x3CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x3CUL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x4CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x4CUL))), v0);
#endif
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xCUL))), x9);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x14UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x5CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x5CUL))), v0);
#endif
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x34UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x34UL)))) + (0x8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        __arm64_pair_address_13546832 = unchecked((ulong)((sp) + (0xA0UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13546832)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13546832) + (0x8UL))))), 0));
        __arm64_pair_address_13546836 = unchecked((ulong)((sp) + (0x90UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13546836)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13546836) + (0x8UL))))), 0));
        __arm64_pair_address_13546840 = unchecked((ulong)((sp) + (0x80UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13546840)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13546840) + (0x8UL))))), 0));
        __arm64_pair_address_13546844 = unchecked((ulong)((sp) + (0x70UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13546844)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13546844) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `bl_UIGradient.ctor` — RVA `0xceb568`

- Lift status: **exact**; input span: 384 bytes; span to next metadata RVA: 384 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=53 (informational only).

```csharp
public static ulong bl_UIGradient_ctor_RVAceb568(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13547140 = default(uint);
        uint __arm64_flags_right_13547140 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x90UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x60UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x20 = 0x1A8F000UL;
        x21 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x67BUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD78UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD80UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCEB5B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x67BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCEB5B8;
        label_0xCEB5B8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x2CUL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x30UL))), unchecked((byte)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x38UL))), unchecked((uint)(x10)));
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1785E64UL /* metadata target: Gradient.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x0;
        x0 = unchecked((ulong)((sp) + (0x48UL)));
        x1 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x58UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0x1785DACUL /* metadata target: GradientColorKey.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCEB6E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB620UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x48UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x48UL))));
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x58UL))))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((sp) + (0x30UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((sp) + (0x30UL))), v0);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x40UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCEB6E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCEB638UL);
        }
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x30UL))));
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x40UL))))));
        x0 = unchecked((ulong)((sp) + (0x18UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x21) + (0x20UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x21) + (0x20UL))), v0);
#endif
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x30UL))), unchecked((uint)(x8)));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x28UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0x1785DACUL /* metadata target: GradientColorKey.ctor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x28UL))))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((sp) + (0x18UL))));
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x10UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(sp, v0);
#else
        __WriteVector128(sp, v0);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        __arm64_flags_left_13547140 = unchecked((uint)(x8));
        __arm64_flags_right_13547140 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13547140 >= __arm64_flags_right_13547140))) || (unchecked((uint)((__arm64_flags_left_13547140) - (__arm64_flags_right_13547140))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCEB6E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x10UL))))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(sp);
#else
        v0 = __ReadVector128(sp);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x44UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x21) + (0x34UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x21) + (0x34UL))), v0);
#endif
        if ((x20 == 0x0UL))
        {
            goto label_0xCEB6E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178605CUL /* metadata target: Gradient.set_colorKeys */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1996C18UL /* metadata target: BaseMeshEffect.ctor */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        return x0;
        label_0xCEB6E0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCEB6E4;
        label_0xCEB6E4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```
