# `InputRig.AxisConfig` — TypeDefIndex 4996

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x18` | `InputRig.AxisType` | `axisType` |
| `0x1C` | `InputRig.DeltaTransformMode` | `deltaMode` |
| `0x20` | `bool` | `snap` |
| `0x24` | `float` | `scale` |
| `0x28` | `bool` | `affectSourceKeys` |
| `0x2C` | `KeyCode` | `affectedKeyPositive` |
| `0x30` | `KeyCode` | `affectedKeyNegative` |
| `0x34` | `KeyCode` | `keyboardPositive` |
| `0x38` | `KeyCode` | `keyboardPositiveAlt0` |
| `0x3C` | `KeyCode` | `keyboardPositiveAlt1` |
| `0x40` | `KeyCode` | `keyboardPositiveAlt2` |
| `0x44` | `KeyCode` | `keyboardNegative` |
| `0x48` | `KeyCode` | `keyboardNegativeAlt0` |
| `0x4C` | `KeyCode` | `keyboardNegativeAlt1` |
| `0x50` | `KeyCode` | `keyboardNegativeAlt2` |
| `0x54` | `float` | `analogToDigitalThresh` |
| `0x58` | `float` | `rawSmoothingTime` |
| `0x5C` | `float` | `smoothingTime` |
| `0x60` | `float` | `digitalToAnalogAccelTime` |
| `0x64` | `float` | `digitalToAnalogDecelTime` |
| `0x68` | `bool` | `digitalToScrollAutoRepeat` |
| `0x6C` | `float` | `digitalToScrollRepeatInterval` |
| `0x70` | `float` | `digitalToScrollDelay` |
| `0x74` | `float` | `scrollToAnalogSmoothingTime` |
| `0x78` | `float` | `scrollToAnalogStepDuration` |
| `0x7C` | `float` | `scrollToDeltaSmoothingTime` |
| `0x80` | `float` | `valRaw` |
| `0x84` | `float` | `val` |
| `0x88` | `int` | `scrollPrev` |
| `0x8C` | `int` | `scrollCur` |
| `0x90` | `bool` | `digiCur` |
| `0x91` | `bool` | `digiPrev` |
| `0x92` | `bool` | `muteUntilRelease` |
| `0x94` | `float` | `digitalToAnalogVal` |
| `0x98` | `bool` | `analogToDigitalNegCur` |
| `0x99` | `bool` | `analogToDigitalPosCur` |
| `0x9C` | `float` | `valSmoothVel` |
| `0xA0` | `float` | `valRawSmoothVel` |
| `0xA4` | `float` | `scrollToAnalogTimeRemaining` |
| `0xA8` | `float` | `scrollToAnalogValue` |
| `0xAC` | `int` | `scrollToDigitalClicksRemaining` |
| `0xB0` | `bool` | `scrollToDigitalClickOn` |
| `0xB4` | `float` | `deltaAccumTarget` |
| `0xB8` | `float` | `deltaAccumSmoothCur` |
| `0xBC` | `float` | `deltaAccumSmoothPrev` |
| `0xC0` | `float` | `deltaAccumRawCur` |
| `0xC4` | `float` | `deltaAccumRawPrev` |
| `0xC8` | `float` | `scrollElapsedSinceChange` |
| `0xCC` | `bool` | `digiToScrollPositivePrev` |
| `0xCD` | `bool` | `digiToScrollNegativePrev` |
| `0xCE` | `bool` | `digiToScrollDelayPhase` |
| `0xCF` | `bool` | `<frDigitalPos>k__BackingField` |
| `0xD0` | `bool` | `<frDigitalNeg>k__BackingField` |
| `0xD4` | `float` | `<frAnalogPos>k__BackingField` |
| `0xD8` | `float` | `<frAnalogNeg>k__BackingField` |
| `0xDC` | `float` | `<frMouseDeltaPos>k__BackingField` |
| `0xE0` | `float` | `<frMouseDeltaNeg>k__BackingField` |
| `0xE4` | `float` | `<frTouchDeltaPos>k__BackingField` |
| `0xE8` | `float` | `<frTouchDeltaNeg>k__BackingField` |
| `0xEC` | `float` | `<frNormalizedDeltaPos>k__BackingField` |
| `0xF0` | `float` | `<frNormalizedDeltaNeg>k__BackingField` |
| `0xF4` | `int` | `<frScrollDelta>k__BackingField` |

## `InputRig.AxisConfig.get_frDigitalPos` — RVA `0xc40bdc`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool get_frDigitalPos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_AxisConfig_get_frDigitalPos_RVAc40bdc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xCFUL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.set_frDigitalPos` — RVA `0xc40be4`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `protected void set_frDigitalPos(bool value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frDigitalPos_RVAc40be4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xCFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frDigitalNeg` — RVA `0xc40bf0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool get_frDigitalNeg() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_AxisConfig_get_frDigitalNeg_RVAc40bf0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xD0UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.set_frDigitalNeg` — RVA `0xc40bf8`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `protected void set_frDigitalNeg(bool value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frDigitalNeg_RVAc40bf8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xD0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frAnalogPos` — RVA `0xc40c04`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frAnalogPos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frAnalogPos_RVAc40c04(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xD4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frAnalogPos` — RVA `0xc40c0c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frAnalogPos(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frAnalogPos_RVAc40c0c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xD4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frAnalogNeg` — RVA `0xc40c14`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frAnalogNeg() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frAnalogNeg_RVAc40c14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xD8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frAnalogNeg` — RVA `0xc40c1c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frAnalogNeg(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frAnalogNeg_RVAc40c1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xD8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frMouseDeltaPos` — RVA `0xc40c24`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frMouseDeltaPos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frMouseDeltaPos_RVAc40c24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xDCUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frMouseDeltaPos` — RVA `0xc40c2c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frMouseDeltaPos(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frMouseDeltaPos_RVAc40c2c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xDCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frMouseDeltaNeg` — RVA `0xc40c34`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frMouseDeltaNeg() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frMouseDeltaNeg_RVAc40c34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xE0UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frMouseDeltaNeg` — RVA `0xc40c3c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frMouseDeltaNeg(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frMouseDeltaNeg_RVAc40c3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xE0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frTouchDeltaPos` — RVA `0xc40c44`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frTouchDeltaPos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frTouchDeltaPos_RVAc40c44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xE4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frTouchDeltaPos` — RVA `0xc40c4c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frTouchDeltaPos(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frTouchDeltaPos_RVAc40c4c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xE4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frTouchDeltaNeg` — RVA `0xc40c54`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frTouchDeltaNeg() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frTouchDeltaNeg_RVAc40c54(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xE8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frTouchDeltaNeg` — RVA `0xc40c5c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frTouchDeltaNeg(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frTouchDeltaNeg_RVAc40c5c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xE8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frNormalizedDeltaPos` — RVA `0xc40c64`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frNormalizedDeltaPos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frNormalizedDeltaPos_RVAc40c64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xECUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frNormalizedDeltaPos` — RVA `0xc40c6c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frNormalizedDeltaPos(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frNormalizedDeltaPos_RVAc40c6c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xECUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frNormalizedDeltaNeg` — RVA `0xc40c74`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float get_frNormalizedDeltaNeg() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_get_frNormalizedDeltaNeg_RVAc40c74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xF0UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.set_frNormalizedDeltaNeg` — RVA `0xc40c7c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frNormalizedDeltaNeg(float value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frNormalizedDeltaNeg_RVAc40c7c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xF0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.get_frScrollDelta` — RVA `0xc40c84`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public int get_frScrollDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_AxisConfig_get_frScrollDelta_RVAc40c84(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xF4UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.set_frScrollDelta` — RVA `0xc40c8c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_frScrollDelta(int value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong InputRig_AxisConfig_set_frScrollDelta_RVAc40c8c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xF4UL))), unchecked((uint)(x1)));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.ctor` — RVA `0xc40c94`

- Lift status: **exact**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong InputRig_AxisConfig_ctor_RVAc40c94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1F9UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA50UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC40CC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA50UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1F9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC40CC8;
        label_0xC40CC8:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xD80UL))))), 0));
        x8 = 0x433000UL;
        x9 = unchecked((ulong)(unchecked((uint)(0x3E800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x64UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x18UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x70UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x70UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x24UL))), unchecked((uint)(x8)));
        x8 = 0x432000UL;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x54UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x54UL))), v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x8D0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x8D0UL))));
#endif
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = RuntimeMemory.ReadU64(x19);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x28UL))), unchecked((byte)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x68UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x9 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3DCCUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x34UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x44UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x7CUL))), unchecked((uint)(x9)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x6CUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x6CUL))), v0);
#endif
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `InputRig.AxisConfig.CreateDigital` — RVA `0xc40d50`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public static InputRig.AxisConfig CreateDigital(string name, KeyCode key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong InputRig_AxisConfig_CreateDigital_RVAc40d50(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1FAUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA58UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA58UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1FAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC40D8C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC40C94UL /* metadata target: InputRig.AxisConfig.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            label_0xC40DD4:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x0 = x21;
            RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
            x1 = x20;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
            RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x34UL))), unchecked((uint)(x19)));
            RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x18UL))), unchecked((uint)(x8)));
            RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x44UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
            x0 = x21;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            return x0;
        }
        return default(ulong);
    }
```

## `InputRig.AxisConfig.CreateScrollWheel` — RVA `0xc40dd8`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public static InputRig.AxisConfig CreateScrollWheel(string name, KeyCode keyPositive, KeyCode keyNegative) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong InputRig_AxisConfig_CreateScrollWheel_RVAc40dd8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1FBUL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA58UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA58UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1FBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC40E18:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC40C94UL /* metadata target: InputRig.AxisConfig.ctor */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            label_0xC40E60:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x0 = x22;
            RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x21);
            x1 = x21;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x3UL))));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x34UL))), unchecked((uint)(x20)));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x18UL))), unchecked((uint)(x8)));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x44UL))), unchecked((uint)(x19)));
            x0 = x22;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            return x0;
        }
        return default(ulong);
    }
```

## `InputRig.AxisConfig.CreateAnalog` — RVA `0xc40e64`

- Lift status: **exact**; input span: 132 bytes; span to next metadata RVA: 132 bytes.
- Metadata signature: `public static InputRig.AxisConfig CreateAnalog(string name, KeyCode keyPositive) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong InputRig_AxisConfig_CreateAnalog_RVAc40e64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1FCUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA58UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA58UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1FCUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC40EA0:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC40C94UL /* metadata target: InputRig.AxisConfig.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            label_0xC40EE4:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x0 = x21;
            RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
            x1 = x20;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x18UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
            RuntimeMemory.WriteU32(unchecked((ulong)((x21) + (0x34UL))), unchecked((uint)(x19)));
            RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x44UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
            x0 = x21;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            return x0;
        }
        return default(ulong);
    }
```

## `InputRig.AxisConfig.CreateSignedAnalog` — RVA `0xc40ee8`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public static InputRig.AxisConfig CreateSignedAnalog(string name, KeyCode keyPositive, KeyCode keyNegative) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong InputRig_AxisConfig_CreateSignedAnalog_RVAc40ee8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1FDUL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA58UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA58UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1FDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC40F28:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC40C94UL /* metadata target: InputRig.AxisConfig.ctor */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            label_0xC40F70:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x0 = x22;
            RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x21);
            x1 = x21;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x34UL))), unchecked((uint)(x20)));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x18UL))), unchecked((uint)(x8)));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x44UL))), unchecked((uint)(x19)));
            x0 = x22;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            return x0;
        }
        return default(ulong);
    }
```

## `InputRig.AxisConfig.CreateDelta` — RVA `0xc40f74`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public static InputRig.AxisConfig CreateDelta(string name, KeyCode keyPositive, KeyCode keyNegative) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong InputRig_AxisConfig_CreateDelta_RVAc40f74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1FEUL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xA58UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA58UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1FEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC40FB4:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC40C94UL /* metadata target: InputRig.AxisConfig.ctor */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            label_0xC40FFC:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x0 = x22;
            RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x21);
            x1 = x21;
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x4UL))));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x34UL))), unchecked((uint)(x20)));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x18UL))), unchecked((uint)(x8)));
            RuntimeMemory.WriteU32(unchecked((ulong)((x22) + (0x44UL))), unchecked((uint)(x19)));
            x0 = x22;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            return x0;
        }
        return default(ulong);
    }
```

## `InputRig.AxisConfig.Reset` — RVA `0xc41000`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_AxisConfig_Reset_RVAc41000(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        v0 = RuntimeVector128.Zero.WithUInt64(0, 0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0x10000UL))));
        v1 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xD0UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xB4UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xC4UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xBCUL))), 0x0UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x9CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xCCUL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0xD4UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0xD4UL))), v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x0) + (0xE4UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((x0) + (0xE4UL))), v1);
#endif
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.MuteUntilRelease` — RVA `0xc41034`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void MuteUntilRelease() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_AxisConfig_MuteUntilRelease_RVAc41034(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x92UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.IsMuted` — RVA `0xc41040`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsMuted() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_AxisConfig_IsMuted_RVAc41040(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x92UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.ApplyKeyboardInput` — RVA `0xc41048`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `public void ApplyKeyboardInput() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static uint InputRig_AxisConfig_ApplyKeyboardInput_RVAc41048(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x34UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC41090;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x38UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC41090;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x3CUL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC41090;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x40UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41098;
        }
        else
        {
            goto label_0xC41090;
        }
        label_0xC41090:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xCFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC41098;
        label_0xC41098:
        ;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x44UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC410D8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x48UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC410D8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x4CUL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC410D8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BF54UL /* metadata target: InputRig.GetSourceKeyState */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC410E0;
        }
        else
        {
            goto label_0xC410D8;
        }
        label_0xC410D8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xD0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC410E0;
        label_0xC410E0:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.SetSignedDigital` — RVA `0xc410e8`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void SetSignedDigital(bool vpositive) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_AxisConfig_SetSignedDigital_RVAc410e8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC410F8:
            ;
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xD0UL))), unchecked((byte)(unchecked((uint)(x8)))));
            return x0;
        }
        else
        {
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xCFUL))), unchecked((byte)(unchecked((uint)(x8)))));
            return x0;
        }
        return default(ulong);
    }
```

## `InputRig.AxisConfig.Update` — RVA `0xc41100`

- Lift status: **partial**; input span: 2028 bytes; span to next metadata RVA: 2028 bytes.
- Metadata signature: `public override void Update(InputRig rig) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=390 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc41160; reason: Unknown IR expression at 0xc41160; reason: Unsupported instruction 'csel' at 0xc41174; reason: Unknown IR expression at 0xc41174; reason: Unsupported instruction 'cset' at 0xc411b4; reason: Unknown IR expression at 0xc411b4

```csharp
public static ulong InputRig_AxisConfig_Update_RVAc41100(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12849508 = default(uint);
        uint __arm64_flags_left_12849592 = default(uint);
        uint __arm64_flags_left_12849696 = default(uint);
        uint __arm64_flags_left_12851156 = default(uint);
        uint __arm64_flags_result_12849508 = default(uint);
        uint __arm64_flags_right_12849508 = default(uint);
        uint __arm64_flags_right_12849592 = default(uint);
        uint __arm64_flags_right_12849696 = default(uint);
        uint __arm64_flags_right_12851156 = default(uint);
        float __arm64_float_flags_left_12849484 = default(float);
        float __arm64_float_flags_left_12849492 = default(float);
        float __arm64_float_flags_left_12849572 = default(float);
        float __arm64_float_flags_left_12849580 = default(float);
        float __arm64_float_flags_left_12849688 = default(float);
        float __arm64_float_flags_right_12849484 = default(float);
        float __arm64_float_flags_right_12849492 = default(float);
        float __arm64_float_flags_right_12849572 = default(float);
        float __arm64_float_flags_right_12849580 = default(float);
        float __arm64_float_flags_right_12849688 = default(float);
        float __arm64_fp_left_12849684 = default(float);
        float __arm64_fp_right_12849684 = default(float);
        ulong __arm64_load_address_12849456 = default(ulong);
        ulong __arm64_pair_address_12849408 = default(ulong);
        ulong __arm64_pair_address_12849412 = default(ulong);
        ulong __arm64_pair_address_12849652 = default(ulong);
        ulong __arm64_pair_address_12850172 = default(ulong);
        ulong __arm64_pair_address_12850316 = default(ulong);
        ulong __arm64_pair_address_12850336 = default(ulong);
        ulong __arm64_pair_address_12851396 = default(ulong);
        ulong __arm64_pair_address_12851416 = default(ulong);
        ulong __arm64_pair_address_12851420 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
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
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12849408 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12849408, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12849408) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12849408;
        __arm64_pair_address_12849412 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12849412, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12849412) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x8CUL))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x90UL))))))));
        x22 = x0;
        x20 = x1;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x88UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x91UL))), unchecked((byte)(unchecked((uint)(x9)))));
        __arm64_load_address_12849456 = unchecked((ulong)((x22) + (0xD4UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_load_address_12849456)), 0));
        x22 = __arm64_load_address_12849456;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xD8UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x54UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xD0UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xCFUL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)))), 0));
        __arm64_float_flags_left_12849484 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12849484 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        x11 = unchecked((ulong)(((__arm64_float_flags_left_12849484 < __arm64_float_flags_right_12849484) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_float_flags_left_12849492 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12849492 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) | (unchecked((uint)(x8)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x98UL))), unchecked((byte)(unchecked((uint)(x11)))));
        RuntimeCalls.Unsupported("cset", 0xC41160UL);
        x11 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12849508 = unchecked((uint)(x10));
        __arm64_flags_right_12849508 = unchecked((uint)0xFFUL);
        __arm64_flags_result_12849508 = unchecked((uint)((__arm64_flags_left_12849508) & (__arm64_flags_right_12849508)));
        x10 = unchecked((ulong)(unchecked((uint)(0x60UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x99UL))), unchecked((byte)(unchecked((uint)(x11)))));
        x11 = unchecked((ulong)(unchecked((uint)(0x64UL))));
        RuntimeCalls.Unsupported("csel", 0xC41174UL);
        x10 = (__Unsupported<bool>("Unknown IR expression") ? x11 : x10);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (x10))))), 0));
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x94UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) - (unchecked((uint)(x8)))))));
        x19 = x0;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC411C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x3B8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12849572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12849572 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12849572 <= __arm64_float_flags_right_12849572) || ((__arm64_float_flags_left_12849572 != __arm64_float_flags_left_12849572) || (__arm64_float_flags_right_12849572 != __arm64_float_flags_right_12849572))))
        {
            goto label_0xC411C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC411ACUL);
        }
        __arm64_float_flags_left_12849580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12849580 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x8 = unchecked((ulong)((~(unchecked((uint)(x8))))));
        RuntimeCalls.Unsupported("cset", 0xC411B4UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12849592 = unchecked((uint)(x9));
        __arm64_flags_right_12849592 = unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)0x1FUL))))));
        if ((unchecked((uint)((__arm64_flags_left_12849592) - (__arm64_flags_right_12849592))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC411C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC411C0UL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x94UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC411C8;
        label_0xC411C8:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4E0UL))))), 0));
        v3 = v0;
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC574ACUL /* metadata target: CFUtils.MoveTowards */, x0, x1, x2, x3);
        v1 = v0;
        __arm64_pair_address_12849652 = unchecked((ulong)((x19) + (0xD4UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12849652)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12849652) + (0x4UL))))), 0));
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x94UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC58484UL /* metadata target: CFUtils.ApplyDeltaInput */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        __arm64_fp_left_12849684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12849684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12849684 != __arm64_fp_left_12849684) ? __arm64_fp_left_12849684 : ((__arm64_fp_right_12849684 != __arm64_fp_right_12849684) ? __arm64_fp_right_12849684 : (((__arm64_fp_left_12849684 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12849684 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12849684), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12849684), 0))))), 0) : ((__arm64_fp_left_12849684 <= __arm64_fp_right_12849684) ? __arm64_fp_left_12849684 : __arm64_fp_right_12849684))))), 0));
        __arm64_float_flags_left_12849688 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12849688 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12849688 >= __arm64_float_flags_right_12849688) || ((__arm64_float_flags_left_12849688 != __arm64_float_flags_left_12849688) || (__arm64_float_flags_right_12849688 != __arm64_float_flags_right_12849688))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_flags_left_12849696 = unchecked((uint)(x8));
        __arm64_flags_right_12849696 = unchecked((uint)0x4UL);
        if (((__arm64_flags_left_12849696 >= __arm64_flags_right_12849696) && (!((unchecked((uint)((__arm64_flags_left_12849696) - (__arm64_flags_right_12849696))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC41788;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x9 = unchecked((ulong)((x9) + (0xB2UL)));
        x10 = 0xC41240UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC413F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        __arm64_pair_address_12850172 = unchecked((ulong)((x19) + (0xB4UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12850172)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12850172) + (0x4UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC0UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x5CUL))))), 0));
        x0 = 0x0UL;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xBCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xB4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        x21 = unchecked((ulong)((x19) + (0x9CUL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v3 = v0;
        v0 = v8;
        v1 = v9;
        x0 = x21;
        v2 = v10;
        v4 = v11;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC589B8UL /* metadata target: CFUtils.SmoothDamp */, x0, x1, x2, x3);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC0UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xB4UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x58UL))))), 0));
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xB8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x21 = unchecked((ulong)((x19) + (0xA0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, x1, x2, x3);
        v3 = v0;
        v0 = v8;
        v1 = v9;
        x0 = x21;
        v2 = v10;
        v4 = v11;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC589B8UL /* metadata target: CFUtils.SmoothDamp */, x0, x1, x2, x3);
        __arm64_pair_address_12850316 = unchecked((ulong)((x19) + (0xB8UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12850316)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12850316) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xC4UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xC0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12850336 = unchecked((ulong)((x19) + (0x80UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12850336, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12850336) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        goto label_0xC41788;
        label_0xC41788:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x92UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC417E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xD0UL))))))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, 0x0UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x9CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x90UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x94UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC417D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xCFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC417D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x98UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC417D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x99UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC417D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xF4UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC417D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC417CCUL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x92UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC417D0;
        label_0xC417D0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x18UL))))));
        __arm64_flags_left_12851156 = unchecked((uint)(x8));
        __arm64_flags_right_12851156 = unchecked((uint)0x4UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12851156) - (__arm64_flags_right_12851156))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC417E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC417DCUL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x92UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC417E0;
        label_0xC417E0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x98UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC417F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xD0UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4184C;
        }
        else
        {
            goto label_0xC417F0;
        }
        label_0xC417F0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x28UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41804;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC417F8UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC413F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0x30UL)));
        goto label_0xC4183C;
        label_0xC41804:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC413F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x44UL))))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x48UL))))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x4CUL))))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((x19) + (0x50UL)));
        goto label_0xC4183C;
        label_0xC4183C:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4184C;
        label_0xC4184C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x99UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4185C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xCFUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC418B8;
        }
        else
        {
            goto label_0xC4185C;
        }
        label_0xC4185C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x28UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41870;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC41864UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC413F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0x2CUL)));
        goto label_0xC418A8;
        label_0xC41870:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC413F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x34UL))))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x38UL))))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x3CUL))))));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)((x19) + (0x40UL)));
        goto label_0xC418A8;
        label_0xC418A8:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(x8)));
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3DD94UL /* metadata target: InputRig.SetKeyCode */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC418B8;
        label_0xC418B8:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xCFUL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x20UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_12851396 = x22;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12851396, v0);
#else
        __WriteVector128(__arm64_pair_address_12851396, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12851396) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12851396) + (0x10UL))), v0);
#endif
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_12851416 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12851416)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12851416) + (0x8UL))))), 0));
        __arm64_pair_address_12851420 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12851420)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12851420) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12851420) + (0x60UL)));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.Set` — RVA `0xc418ec`

- Lift status: **exact**; input span: 512 bytes; span to next metadata RVA: 512 bytes.
- Metadata signature: `public void Set(float v, InputRig.InputSource source) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=120 (informational only).

```csharp
public static ulong InputRig_AxisConfig_Set_RVAc418ec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12851448 = default(uint);
        uint __arm64_flags_right_12851448 = default(uint);
        ulong __arm64_pair_address_12851436 = default(ulong);
        ulong __arm64_pair_address_12851940 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12851436 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12851436, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12851436) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12851436;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        __arm64_flags_left_12851448 = unchecked((uint)(x1));
        __arm64_flags_right_12851448 = unchecked((uint)0x5UL);
        if (((__arm64_flags_left_12851448 >= __arm64_flags_right_12851448) && (!((unchecked((uint)((__arm64_flags_left_12851448) - (__arm64_flags_right_12851448))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC41ADC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = unchecked((ulong)((x9) + (0xB7UL)));
        x10 = 0xC41924UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        v8 = v0;
        x19 = x0;
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC41ADC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_12851940 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12851940)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12851940) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.SetAnalog` — RVA `0xc41aec`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void SetAnalog(float v) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong InputRig_AxisConfig_SetAnalog_RVAc41aec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12852016 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xD4UL))))), 0));
        x19 = x0;
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC584F4UL /* metadata target: CFUtils.ApplyPositveDeltaInput */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xD8UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xD4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC58508UL /* metadata target: CFUtils.ApplyNegativeDeltaInput */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xD8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12852016 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12852016)), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.SetMouseDelta` — RVA `0xc41b38`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void SetMouseDelta(float mouseDelta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong InputRig_AxisConfig_SetMouseDelta_RVAc41b38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12852092 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xDCUL))))), 0));
        x19 = x0;
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC584F4UL /* metadata target: CFUtils.ApplyPositveDeltaInput */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xE0UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xDCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC58508UL /* metadata target: CFUtils.ApplyNegativeDeltaInput */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12852092 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12852092)), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.SetTouchDelta` — RVA `0xc41b84`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void SetTouchDelta(float touchDelta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong InputRig_AxisConfig_SetTouchDelta_RVAc41b84(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12852168 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xE4UL))))), 0));
        x19 = x0;
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC584F4UL /* metadata target: CFUtils.ApplyPositveDeltaInput */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xE8UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC58508UL /* metadata target: CFUtils.ApplyNegativeDeltaInput */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12852168 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12852168)), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.SetNormalizedDelta` — RVA `0xc41bd0`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public void SetNormalizedDelta(float normalizedDelta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong InputRig_AxisConfig_SetNormalizedDelta_RVAc41bd0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12852244 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xECUL))))), 0));
        x19 = x0;
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC584F4UL /* metadata target: CFUtils.ApplyPositveDeltaInput */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xF0UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xECUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = 0x0UL;
        v0 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC58508UL /* metadata target: CFUtils.ApplyNegativeDeltaInput */, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xF0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12852244 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12852244)), 0));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.SetScrollDelta` — RVA `0xc41c1c`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public void SetScrollDelta(int scrollDelta) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint InputRig_AxisConfig_SetScrollDelta_RVAc41c1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xF4UL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC584C4UL /* metadata target: CFUtils.ApplyDeltaInputInt */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xF4UL))), unchecked((uint)(x0)));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.SetDigital` — RVA `0xc41c3c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void SetDigital() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong InputRig_AxisConfig_SetDigital_RVAc41c3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xCFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.GetAnalog` — RVA `0xc41c48`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public float GetAnalog() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong InputRig_AxisConfig_GetAnalog_RVAc41c48(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852304 = default(uint);
        uint __arm64_flags_right_12852304 = default(uint);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x84UL))))), 0));
        __arm64_flags_left_12852304 = unchecked((uint)(x8));
        __arm64_flags_right_12852304 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_12852304) - (__arm64_flags_right_12852304))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x24UL))))), 0));
        }
        label_0xC41C60:
        ;
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.GetAnalogRaw` — RVA `0xc41c64`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public float GetAnalogRaw() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong InputRig_AxisConfig_GetAnalogRaw_RVAc41c64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852332 = default(uint);
        uint __arm64_flags_right_12852332 = default(uint);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x80UL))))), 0));
        __arm64_flags_left_12852332 = unchecked((uint)(x8));
        __arm64_flags_right_12852332 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_12852332) - (__arm64_flags_right_12852332))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x24UL))))), 0));
        }
        label_0xC41C7C:
        ;
        return x0;
        return default(ulong);
    }
```

## `InputRig.AxisConfig.IsControlledByInput` — RVA `0xc41c80`

- Lift status: **exact**; input span: 176 bytes; span to next metadata RVA: 176 bytes.
- Metadata signature: `public bool IsControlledByInput() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint InputRig_AxisConfig_IsControlledByInput_RVAc41c80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852516 = default(uint);
        uint __arm64_flags_right_12852516 = default(uint);
        float __arm64_float_flags_left_12852384 = default(float);
        float __arm64_float_flags_left_12852400 = default(float);
        float __arm64_float_flags_left_12852416 = default(float);
        float __arm64_float_flags_left_12852432 = default(float);
        float __arm64_float_flags_left_12852448 = default(float);
        float __arm64_float_flags_left_12852464 = default(float);
        float __arm64_float_flags_left_12852480 = default(float);
        float __arm64_float_flags_left_12852496 = default(float);
        float __arm64_float_flags_right_12852384 = default(float);
        float __arm64_float_flags_right_12852400 = default(float);
        float __arm64_float_flags_right_12852416 = default(float);
        float __arm64_float_flags_right_12852432 = default(float);
        float __arm64_float_flags_right_12852448 = default(float);
        float __arm64_float_flags_right_12852464 = default(float);
        float __arm64_float_flags_right_12852480 = default(float);
        float __arm64_float_flags_right_12852496 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xD0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xCFUL))))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xD8UL))))), 0));
                x8 = 0x432000UL;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                __arm64_float_flags_left_12852384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12852384 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                if ((__arm64_float_flags_left_12852384 > __arm64_float_flags_right_12852384))
                {
                }
                else
                {
                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xD4UL))))), 0));
                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                    __arm64_float_flags_left_12852400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                    __arm64_float_flags_right_12852400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                    if ((__arm64_float_flags_left_12852400 > __arm64_float_flags_right_12852400))
                    {
                    }
                    else
                    {
                        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xE0UL))))), 0));
                        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                        __arm64_float_flags_left_12852416 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                        __arm64_float_flags_right_12852416 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                        if ((__arm64_float_flags_left_12852416 > __arm64_float_flags_right_12852416))
                        {
                        }
                        else
                        {
                            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xDCUL))))), 0));
                            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                            __arm64_float_flags_left_12852432 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                            __arm64_float_flags_right_12852432 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                            if ((__arm64_float_flags_left_12852432 > __arm64_float_flags_right_12852432))
                            {
                            }
                            else
                            {
                                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xF0UL))))), 0));
                                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                                __arm64_float_flags_left_12852448 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                                __arm64_float_flags_right_12852448 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                                if ((__arm64_float_flags_left_12852448 > __arm64_float_flags_right_12852448))
                                {
                                }
                                else
                                {
                                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xECUL))))), 0));
                                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                                    __arm64_float_flags_left_12852464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                                    __arm64_float_flags_right_12852464 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                                    if ((__arm64_float_flags_left_12852464 > __arm64_float_flags_right_12852464))
                                    {
                                    }
                                    else
                                    {
                                        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xE8UL))))), 0));
                                        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                                        __arm64_float_flags_left_12852480 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                                        __arm64_float_flags_right_12852480 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                                        if ((__arm64_float_flags_left_12852480 > __arm64_float_flags_right_12852480))
                                        {
                                        }
                                        else
                                        {
                                            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xE4UL))))), 0));
                                            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
                                            __arm64_float_flags_left_12852496 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                                            __arm64_float_flags_right_12852496 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                                            if (((__arm64_float_flags_left_12852496 <= __arm64_float_flags_right_12852496) || ((__arm64_float_flags_left_12852496 != __arm64_float_flags_left_12852496) || (__arm64_float_flags_right_12852496 != __arm64_float_flags_right_12852496))))
                                            {
                                                label_0xC41D20:
                                                ;
                                                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0xF4UL))))));
                                                __arm64_flags_left_12852516 = unchecked((uint)(x8));
                                                __arm64_flags_right_12852516 = unchecked((uint)0x0UL);
                                                x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12852516) - (__arm64_flags_right_12852516))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                                                return unchecked((uint)(x0));
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        label_0xC41D18:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.GetButton` — RVA `0xc41d30`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool GetButton() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint InputRig_AxisConfig_GetButton_RVAc41d30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x90UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.GetButtonDown` — RVA `0xc41d38`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool GetButtonDown() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint InputRig_AxisConfig_GetButtonDown_RVAc41d38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852556 = default(uint);
        uint __arm64_flags_right_12852556 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x91UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC41D48:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x90UL))))))));
            __arm64_flags_left_12852556 = unchecked((uint)(x8));
            __arm64_flags_right_12852556 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12852556) - (__arm64_flags_right_12852556))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `InputRig.AxisConfig.GetButtonUp` — RVA `0xc41d58`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool GetButtonUp() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint InputRig_AxisConfig_GetButtonUp_RVAc41d58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852580 = default(uint);
        uint __arm64_flags_right_12852580 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x91UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC41D70:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x90UL))))))));
            __arm64_flags_left_12852580 = unchecked((uint)(x8));
            __arm64_flags_right_12852580 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12852580) - (__arm64_flags_right_12852580))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `InputRig.AxisConfig.GetSupportedInputSourceMask` — RVA `0xc41d78`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public int GetSupportedInputSourceMask() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint InputRig_AxisConfig_GetSupportedInputSourceMask_RVAc41d78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852604 = default(uint);
        uint __arm64_flags_right_12852604 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        __arm64_flags_left_12852604 = unchecked((uint)(x8));
        __arm64_flags_right_12852604 = unchecked((uint)0x4UL);
        if (((__arm64_flags_left_12852604 >= __arm64_flags_right_12852604) && (!((unchecked((uint)((__arm64_flags_left_12852604) - (__arm64_flags_right_12852604))) == unchecked((uint)0x0UL))))))
        {
            label_0xC41D94:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x9 = 0x452000UL;
            x9 = unchecked((ulong)((x9) + (0xF4UL)));
            x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (x8))))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `InputRig.AxisConfig.DoesSupportInputSource` — RVA `0xc41d9c`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool DoesSupportInputSource(InputRig.InputSource source) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static uint InputRig_AxisConfig_DoesSupportInputSource_RVAc41d9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852640 = default(uint);
        uint __arm64_flags_right_12852640 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        __arm64_flags_left_12852640 = unchecked((uint)(x8));
        __arm64_flags_right_12852640 = unchecked((uint)0x4UL);
        if (((__arm64_flags_left_12852640 >= __arm64_flags_right_12852640) && (!((unchecked((uint)((__arm64_flags_left_12852640) - (__arm64_flags_right_12852640))) == unchecked((uint)0x0UL))))))
        {
            label_0xC41DB8:
            ;
            x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        else
        {
            x9 = 0x452000UL;
            x9 = unchecked((ulong)((x9) + (0xF4UL)));
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (x8))))));
        }
        label_0xC41DBC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)(x1)))))))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0x1UL)))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `InputRig.AxisConfig.IsSignedAxis` — RVA `0xc41dc8`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `private bool IsSignedAxis() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static uint InputRig_AxisConfig_IsSignedAxis_RVAc41dc8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852688 = default(uint);
        uint __arm64_flags_right_12852688 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12852688 = unchecked((uint)(x8));
        __arm64_flags_right_12852688 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_12852688 >= __arm64_flags_right_12852688) && (!((unchecked((uint)((__arm64_flags_left_12852688) - (__arm64_flags_right_12852688))) == unchecked((uint)0x0UL))))))
        {
            label_0xC41DEC:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0xFUL)))))));
            x9 = unchecked((ulong)(unchecked((uint)(0xDUL))));
            x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)(x8)))))))));
            x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0x1UL)))))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `InputRig.AxisConfig.DoesAffectKeyCode` — RVA `0xc41df4`

- Lift status: **exact**; input span: 204 bytes; span to next metadata RVA: 204 bytes.
- Metadata signature: `public bool DoesAffectKeyCode(KeyCode key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=21 (informational only).

```csharp
public static uint InputRig_AxisConfig_DoesAffectKeyCode_RVAc41df4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12852736 = default(uint);
        uint __arm64_flags_left_12852748 = default(uint);
        uint __arm64_flags_left_12852760 = default(uint);
        uint __arm64_flags_left_12852772 = default(uint);
        uint __arm64_flags_left_12852784 = default(uint);
        uint __arm64_flags_left_12852804 = default(uint);
        uint __arm64_flags_left_12852816 = default(uint);
        uint __arm64_flags_left_12852828 = default(uint);
        uint __arm64_flags_left_12852840 = default(uint);
        uint __arm64_flags_left_12852860 = default(uint);
        uint __arm64_flags_left_12852872 = default(uint);
        uint __arm64_flags_left_12852892 = default(uint);
        uint __arm64_flags_left_12852904 = default(uint);
        uint __arm64_flags_result_12852804 = default(uint);
        uint __arm64_flags_result_12852892 = default(uint);
        uint __arm64_flags_right_12852736 = default(uint);
        uint __arm64_flags_right_12852748 = default(uint);
        uint __arm64_flags_right_12852760 = default(uint);
        uint __arm64_flags_right_12852772 = default(uint);
        uint __arm64_flags_right_12852784 = default(uint);
        uint __arm64_flags_right_12852804 = default(uint);
        uint __arm64_flags_right_12852816 = default(uint);
        uint __arm64_flags_right_12852828 = default(uint);
        uint __arm64_flags_right_12852840 = default(uint);
        uint __arm64_flags_right_12852860 = default(uint);
        uint __arm64_flags_right_12852872 = default(uint);
        uint __arm64_flags_right_12852892 = default(uint);
        uint __arm64_flags_right_12852904 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x28UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41E78;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x34UL))))));
        __arm64_flags_left_12852736 = unchecked((uint)(x8));
        __arm64_flags_right_12852736 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852736) - (__arm64_flags_right_12852736))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x38UL))))));
        __arm64_flags_left_12852748 = unchecked((uint)(x8));
        __arm64_flags_right_12852748 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852748) - (__arm64_flags_right_12852748))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x3CUL))))));
        __arm64_flags_left_12852760 = unchecked((uint)(x8));
        __arm64_flags_right_12852760 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852760) - (__arm64_flags_right_12852760))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x40UL))))));
        __arm64_flags_left_12852772 = unchecked((uint)(x8));
        __arm64_flags_right_12852772 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852772) - (__arm64_flags_right_12852772))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12852784 = unchecked((uint)(x8));
        __arm64_flags_right_12852784 = unchecked((uint)0x4UL);
        if (((__arm64_flags_left_12852784 >= __arm64_flags_right_12852784) && (!((unchecked((uint)((__arm64_flags_left_12852784) - (__arm64_flags_right_12852784))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC41EB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1AUL))));
        __arm64_flags_left_12852804 = unchecked((uint)(x8));
        __arm64_flags_right_12852804 = unchecked((uint)(x9));
        __arm64_flags_result_12852804 = unchecked((uint)((__arm64_flags_left_12852804) & (__arm64_flags_right_12852804)));
        if ((__arm64_flags_result_12852804 == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x44UL))))));
        __arm64_flags_left_12852816 = unchecked((uint)(x8));
        __arm64_flags_right_12852816 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852816) - (__arm64_flags_right_12852816))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x48UL))))));
        __arm64_flags_left_12852828 = unchecked((uint)(x8));
        __arm64_flags_right_12852828 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852828) - (__arm64_flags_right_12852828))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x4CUL))))));
        __arm64_flags_left_12852840 = unchecked((uint)(x8));
        __arm64_flags_right_12852840 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852840) - (__arm64_flags_right_12852840))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        goto label_0xC41EA8;
        label_0xC41E78:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x2CUL))))));
        __arm64_flags_left_12852860 = unchecked((uint)(x8));
        __arm64_flags_right_12852860 = unchecked((uint)(x1));
        if ((unchecked((uint)((__arm64_flags_left_12852860) - (__arm64_flags_right_12852860))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12852872 = unchecked((uint)(x8));
        __arm64_flags_right_12852872 = unchecked((uint)0x4UL);
        if (((__arm64_flags_left_12852872 >= __arm64_flags_right_12852872) && (!((unchecked((uint)((__arm64_flags_left_12852872) - (__arm64_flags_right_12852872))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC41EB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1AUL))));
        __arm64_flags_left_12852892 = unchecked((uint)(x8));
        __arm64_flags_right_12852892 = unchecked((uint)(x9));
        __arm64_flags_result_12852892 = unchecked((uint)((__arm64_flags_left_12852892) & (__arm64_flags_right_12852892)));
        if ((__arm64_flags_result_12852892 == unchecked((uint)0x0UL)))
        {
            goto label_0xC41EB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x30UL))))));
        goto label_0xC41EA8;
        label_0xC41EA8:
        ;
        __arm64_flags_left_12852904 = unchecked((uint)(x8));
        __arm64_flags_right_12852904 = unchecked((uint)(x1));
        if ((!((unchecked((uint)((__arm64_flags_left_12852904) - (__arm64_flags_right_12852904))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC41EB8;
        }
        else
        {
            goto label_0xC41EB0;
        }
        label_0xC41EB0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        label_0xC41EB8:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```
