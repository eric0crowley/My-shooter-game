# `TouchGestureThresholds` — TypeDefIndex 5098

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `float` | `tapMoveThreshCm` |
| `0x14` | `float` | `tapPosThreshCm` |
| `0x18` | `float` | `dragThreshCm` |
| `0x1C` | `float` | `scrollThreshCm` |
| `0x20` | `float` | `scrollMagnetFactor` |
| `0x24` | `float` | `swipeSegLenCm` |
| `0x28` | `float` | `swipeJoystickRadCm` |
| `0x2C` | `float` | `tapMaxDur` |
| `0x30` | `float` | `multiTapMaxTimeGap` |
| `0x34` | `float` | `longPressMinTime` |
| `0x38` | `float` | `longTapMaxDuration` |
| `0x3C` | `float` | `_tapMoveThreshPx` |
| `0x40` | `float` | `_tapPosThreshPx` |
| `0x44` | `float` | `_dragThreshPx` |
| `0x48` | `float` | `_swipeSegLenPx` |
| `0x4C` | `float` | `_swipeJoystickRadPx` |
| `0x50` | `float` | `_scrollThreshPx` |
| `0x54` | `float` | `storedDpi` |

## `TouchGestureThresholds.Recalc` — RVA `0xc6269c`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `public void Recalc(float dpi) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong TouchGestureThresholds_Recalc_RVAc6269c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12986028 = default(float);
        float __arm64_float_flags_left_12986040 = default(float);
        float __arm64_float_flags_right_12986028 = default(float);
        float __arm64_float_flags_right_12986040 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x54UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x42C00000UL))));
        __arm64_float_flags_left_12986028 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986028 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12986028 > __arm64_float_flags_right_12986028) || ((__arm64_float_flags_left_12986028 != __arm64_float_flags_left_12986028) || (__arm64_float_flags_right_12986028 != __arm64_float_flags_right_12986028))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12986040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986040 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986040 != __arm64_float_flags_right_12986040) || ((__arm64_float_flags_left_12986040 != __arm64_float_flags_left_12986040) || (__arm64_float_flags_right_12986040 != __arm64_float_flags_right_12986040))))
        {
            goto label_0xC626C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC626C0UL);
        }
        return x0;
        label_0xC626C4:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = 0x432000UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x54UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x35CUL))))), 0));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_tapMoveThreshPxSq` — RVA `0xc630a0`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_tapMoveThreshPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_tapMoveThreshPxSq_RVAc630a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x3CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_dragThreshPxSq` — RVA `0xc63118`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_dragThreshPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_dragThreshPxSq_RVAc63118(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x44UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_swipeSegLenPxSq` — RVA `0xc63124`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_swipeSegLenPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_swipeSegLenPxSq_RVAc63124(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x48UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_tapPosThreshPxSq` — RVA `0xc631d4`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_tapPosThreshPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_tapPosThreshPxSq_RVAc631d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x40UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_tapMoveThreshPx` — RVA `0xc63224`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_tapMoveThreshPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_tapMoveThreshPx_RVAc63224(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x3CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_tapPosThreshPx` — RVA `0xc6322c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_tapPosThreshPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_tapPosThreshPx_RVAc6322c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x40UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_dragThreshPx` — RVA `0xc63234`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_dragThreshPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_dragThreshPx_RVAc63234(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x44UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_swipeSegLenPx` — RVA `0xc6323c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_swipeSegLenPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_swipeSegLenPx_RVAc6323c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x48UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_swipeJoystickRadPx` — RVA `0xc63244`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_swipeJoystickRadPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_swipeJoystickRadPx_RVAc63244(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x4CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_swipeJoystickRadPxSq` — RVA `0xc6324c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_swipeJoystickRadPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_swipeJoystickRadPxSq_RVAc6324c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x4CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_scrollThreshPx` — RVA `0xc63258`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_scrollThreshPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_scrollThreshPx_RVAc63258(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x50UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.get_scrollThreshPxSq` — RVA `0xc63260`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_scrollThreshPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureThresholds_get_scrollThreshPxSq_RVAc63260(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x50UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.ctor` — RVA `0xc6326c`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong TouchGestureThresholds_ctor_RVAc6326c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12989096 = default(ulong);
        ulong __arm64_pair_address_12989100 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        x9 = 0x433000UL;
        x10 = 0x432000UL;
        x11 = 0x433000UL;
        x12 = 0x433000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xB00UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xB00UL))));
#endif
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x10) + (0x1B8UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((x9) + (0xE0UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((x9) + (0xE0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((x11) + (0x1C0UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((x11) + (0x1C0UL))));
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(unchecked((ulong)((x12) + (0x30UL))));
#else
        v4 = __ReadVector128(unchecked((ulong)((x12) + (0x30UL))));
#endif
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x50UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        __arm64_pair_address_12989096 = unchecked((ulong)((x19) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12989096, v2);
#else
        __WriteVector128(__arm64_pair_address_12989096, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12989096) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12989096) + (0x10UL))), v3);
#endif
        __arm64_pair_address_12989100 = unchecked((ulong)((x19) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12989100, v4);
#else
        __WriteVector128(__arm64_pair_address_12989100, v4);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12989100) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12989100) + (0x10UL))), v0);
#endif
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureThresholds.OnRecalc` — RVA `0xc632b8`

- Lift status: **partial**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `protected virtual void OnRecalc(float dpcm) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmul' at 0xc632c4; reason: Unsupported instruction 'fmul' at 0xc632cc; reason: Unsupported instruction 'fmax' at 0xc632d8; reason: Unsupported instruction 'fmax' at 0xc632dc

```csharp
public static ulong TouchGestureThresholds_OnRecalc_RVAc632b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fp_left_12989156 = default(float);
        float __arm64_fp_left_12989160 = default(float);
        float __arm64_fp_right_12989156 = default(float);
        float __arm64_fp_right_12989160 = default(float);
        ulong __arm64_pair_address_12989116 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x0) + (0x10UL))))), 0));
        __arm64_pair_address_12989116 = unchecked((ulong)((x0) + (0x18UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12989116)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12989116) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x0) + (0x24UL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC632C4UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC632CCUL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v4 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x40UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x40UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeCalls.Unsupported("fmax", 0xC632D8UL);
        RuntimeCalls.Unsupported("fmax", 0xC632DCUL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        __arm64_fp_left_12989156 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_fp_right_12989156 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12989156 != __arm64_fp_left_12989156) ? __arm64_fp_left_12989156 : ((__arm64_fp_right_12989156 != __arm64_fp_right_12989156) ? __arm64_fp_right_12989156 : (((__arm64_fp_left_12989156 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12989156 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12989156), 0)) & (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12989156), 0))))), 0) : ((__arm64_fp_left_12989156 >= __arm64_fp_right_12989156) ? __arm64_fp_left_12989156 : __arm64_fp_right_12989156))))), 0));
        __arm64_fp_left_12989160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12989160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12989160 != __arm64_fp_left_12989160) ? __arm64_fp_left_12989160 : ((__arm64_fp_right_12989160 != __arm64_fp_right_12989160) ? __arm64_fp_right_12989160 : (((__arm64_fp_left_12989160 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12989160 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12989160), 0)) & (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12989160), 0))))), 0) : ((__arm64_fp_left_12989160 >= __arm64_fp_right_12989160) ? __arm64_fp_left_12989160 : __arm64_fp_right_12989160))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x3CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x44UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x48UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v3.GetUInt64(0)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x50UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```
