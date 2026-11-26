# `MultiTouchGestureThresholds` — TypeDefIndex 5099

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x58` | `float` | `pinchDistThreshCm` |
| `0x5C` | `float` | `pinchAnalogRangeCm` |
| `0x60` | `float` | `pinchDeltaRangeCm` |
| `0x64` | `float` | `pinchDigitalThreshCm` |
| `0x68` | `float` | `pinchScrollStepCm` |
| `0x6C` | `float` | `pinchScrollMagnet` |
| `0x70` | `float` | `twistMinDistCm` |
| `0x74` | `float` | `twistAngleThresh` |
| `0x78` | `float` | `twistAnalogRange` |
| `0x7C` | `float` | `twistDeltaRange` |
| `0x80` | `float` | `twistDigitalThresh` |
| `0x84` | `float` | `twistScrollStep` |
| `0x88` | `float` | `twistScrollMagnet` |
| `0x8C` | `float` | `multiFingerTapMaxFingerDistCm` |
| `0x90` | `float` | `_pinchDistThreshPx` |
| `0x94` | `float` | `_pinchAnalogRangePx` |
| `0x98` | `float` | `_pinchDeltaRangePx` |
| `0x9C` | `float` | `_pinchDigitalThreshPx` |
| `0xA0` | `float` | `_pinchScrollStepPx` |
| `0xA4` | `float` | `_twistMinDistPx` |
| `0xA8` | `float` | `_multiFingerTapMaxFingerDistPx` |

## `MultiTouchGestureThresholds.get_pinchDistThreshPx` — RVA `0xc63300`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_pinchDistThreshPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchDistThreshPx_RVAc63300(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x90UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchDistThreshPxSq` — RVA `0xc63308`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_pinchDistThreshPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchDistThreshPxSq_RVAc63308(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x90UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchAnalogRangePx` — RVA `0xc63314`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_pinchAnalogRangePx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchAnalogRangePx_RVAc63314(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x94UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchAnalogRangePxSq` — RVA `0xc6331c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_pinchAnalogRangePxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchAnalogRangePxSq_RVAc6331c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x94UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchDeltaRangePx` — RVA `0xc63328`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_pinchDeltaRangePx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchDeltaRangePx_RVAc63328(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x98UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchDeltaRangePxSq` — RVA `0xc63330`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_pinchDeltaRangePxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchDeltaRangePxSq_RVAc63330(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x98UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchDigitalThreshPx` — RVA `0xc6333c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_pinchDigitalThreshPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchDigitalThreshPx_RVAc6333c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x9CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchDigitalThreshPxSq` — RVA `0xc63344`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_pinchDigitalThreshPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchDigitalThreshPxSq_RVAc63344(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x9CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchScrollStepPx` — RVA `0xc63350`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_pinchScrollStepPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchScrollStepPx_RVAc63350(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xA0UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_pinchScrollStepPxSq` — RVA `0xc63358`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_pinchScrollStepPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_pinchScrollStepPxSq_RVAc63358(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xA0UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_twistMinDistPx` — RVA `0xc63364`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_twistMinDistPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_twistMinDistPx_RVAc63364(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xA4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_twistMinDistPxSq` — RVA `0xc6336c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_twistMinDistPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_twistMinDistPxSq_RVAc6336c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xA4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_multiFingerTapMaxFingerDistPx` — RVA `0xc63378`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_multiFingerTapMaxFingerDistPx() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_multiFingerTapMaxFingerDistPx_RVAc63378(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xA8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.get_multiFingerTapMaxFingerDistPxSq` — RVA `0xc63380`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float get_multiFingerTapMaxFingerDistPxSq() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_get_multiFingerTapMaxFingerDistPxSq_RVAc63380(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xA8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.ctor` — RVA `0xc6338c`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong MultiTouchGestureThresholds_ctor_RVAc6338c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC6326CUL /* metadata target: TouchGestureThresholds.ctor */, x0, x1, x2, x3);
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0xE80UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0xE80UL))));
#endif
        x8 = 0x433000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x1A0UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x8) + (0x1A0UL))));
#endif
        x8 = 0x431000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x70UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x70UL))), v0);
#endif
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xFA8UL))))), 0));
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x58UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x58UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x820UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x8) + (0x820UL))));
#endif
        x8 = 0x433000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x80UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x80UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x3F000000UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x8CUL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x8CUL))), v1);
#endif
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x68UL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x9CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x9CUL))), v0);
#endif
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `MultiTouchGestureThresholds.OnRecalc` — RVA `0xc633e4`

- Lift status: **partial**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `protected override void OnRecalc(float dpcm) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmul' at 0xc63410; reason: Unsupported instruction 'fmax' at 0xc63420

```csharp
public static ulong MultiTouchGestureThresholds_OnRecalc_RVAc633e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fp_left_12989480 = default(float);
        float __arm64_fp_left_12989484 = default(float);
        float __arm64_fp_left_12989488 = default(float);
        float __arm64_fp_right_12989480 = default(float);
        float __arm64_fp_right_12989484 = default(float);
        float __arm64_fp_right_12989488 = default(float);
        ulong __arm64_pair_address_12989496 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x20UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(sp, v0);
#else
        __WriteVector128(sp, v0);
#endif
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC632B8UL /* metadata target: TouchGestureThresholds.OnRecalc */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x70UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((x19) + (0x58UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((x19) + (0x58UL))));
#endif
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x68UL))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(sp);
#else
        v4 = __ReadVector128(sp);
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC63410UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v4 = ((RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x40UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x40UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL))) | (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x40UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x40UL)) << (int)(unchecked((int)(unchecked((uint)0x18UL))))))).ShiftLeftLogical(unchecked((int)0x20UL))).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeCalls.Unsupported("fmax", 0xC63420UL);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        __arm64_fp_left_12989480 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12989480 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12989480 != __arm64_fp_left_12989480) ? __arm64_fp_left_12989480 : ((__arm64_fp_right_12989480 != __arm64_fp_right_12989480) ? __arm64_fp_right_12989480 : (((__arm64_fp_left_12989480 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12989480 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12989480), 0)) & (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12989480), 0))))), 0) : ((__arm64_fp_left_12989480 >= __arm64_fp_right_12989480) ? __arm64_fp_left_12989480 : __arm64_fp_right_12989480))))), 0));
        __arm64_fp_left_12989484 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_fp_right_12989484 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12989484 != __arm64_fp_left_12989484) ? __arm64_fp_left_12989484 : ((__arm64_fp_right_12989484 != __arm64_fp_right_12989484) ? __arm64_fp_right_12989484 : (((__arm64_fp_left_12989484 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12989484 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12989484), 0)) & (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12989484), 0))))), 0) : ((__arm64_fp_left_12989484 >= __arm64_fp_right_12989484) ? __arm64_fp_left_12989484 : __arm64_fp_right_12989484))))), 0));
        __arm64_fp_left_12989488 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_fp_right_12989488 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12989488 != __arm64_fp_left_12989488) ? __arm64_fp_left_12989488 : ((__arm64_fp_right_12989488 != __arm64_fp_right_12989488) ? __arm64_fp_right_12989488 : (((__arm64_fp_left_12989488 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12989488 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12989488), 0)) & (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12989488), 0))))), 0) : ((__arm64_fp_left_12989488 >= __arm64_fp_right_12989488) ? __arm64_fp_left_12989488 : __arm64_fp_right_12989488))))), 0));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x90UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x90UL))), v1);
#endif
        __arm64_pair_address_12989496 = unchecked((ulong)((x19) + (0xA4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12989496, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12989496) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xA0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x20UL)));
        return x0;
        return default(ulong);
    }
```
