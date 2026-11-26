# `SuperTouchZone` — TypeDefIndex 5031

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x88` | `MultiTouchGestureThresholds` | `customThresh` |
| `0x90` | `int` | `maxFingers` |
| `0x94` | `float` | `touchSmoothing` |
| `0x98` | `bool` | `strictMultiTouch` |
| `0x9C` | `float` | `strictMultiTouchTime` |
| `0xA0` | `bool` | `freezeTwistWhenTooClose` |
| `0xA1` | `bool` | `noPinchAfterDrag` |
| `0xA2` | `bool` | `noPinchAfterTwist` |
| `0xA3` | `bool` | `noTwistAfterDrag` |
| `0xA4` | `bool` | `noTwistAfterPinch` |
| `0xA5` | `bool` | `noDragAfterPinch` |
| `0xA6` | `bool` | `noDragAfterTwist` |
| `0xA7` | `bool` | `startPinchWhenTwisting` |
| `0xA8` | `bool` | `startPinchWhenDragging` |
| `0xA9` | `bool` | `startDragWhenPinching` |
| `0xAA` | `bool` | `startDragWhenTwisting` |
| `0xAB` | `bool` | `startTwistWhenDragging` |
| `0xAC` | `bool` | `startTwistWhenPinching` |
| `0xB0` | `SuperTouchZone.GestureDetectionOrder` | `gestureDetectionOrder` |
| `0xB8` | `SuperTouchZone.MultiFingerTouch[]` | `multiFingerTouch` |
| `0xC0` | `SuperTouchZone.MultiFingerTouchConfig[]` | `multiFingerConfigs` |
| `0xC8` | `SuperTouchZone.FingerState[]` | `fingers` |
| `0xD0` | `SuperTouchZone.FingerState[]` | `fingersOrdered` |
| `0xD8` | `int` | `rawFingersPressedCur` |
| `0xDC` | `int` | `rawFingersPressedPrev` |
| `0xE0` | `bool` | `dontAllowNewFingers` |
| `0xE1` | `bool` | `waitingForMoreFingers` |
| `0xE4` | `float` | `elapsedSinceFirstTouch` |
| `0xE8` | `bool` | `pinchMoved` |
| `0xE9` | `bool` | `pinchJustMoved` |
| `0xEA` | `bool` | `twistMoved` |
| `0xEB` | `bool` | `twistJustMoved` |
| `0xEC` | `float` | `pinchDistQuietInitial` |
| `0xF0` | `float` | `pinchDistInitial` |
| `0xF4` | `float` | `pinchDistCur` |
| `0xF8` | `float` | `pinchDistPrev` |
| `0xFC` | `float` | `twistAngleQuietInitial` |
| `0x100` | `float` | `twistAngleInitial` |
| `0x104` | `float` | `twistAngleCur` |
| `0x108` | `float` | `twistAnglePrev` |
| `0x10C` | `int` | `twistScrollPrev` |
| `0x110` | `int` | `twistScrollCur` |
| `0x114` | `int` | `pinchScrollPrev` |
| `0x118` | `int` | `pinchScrollCur` |
| `0x120` | `EmuTouchBinding` | `separateFingersAsEmuTouchesBinding` |
| `0x128` | `AnalogConfig` | `twistAnalogConfig` |
| `0x130` | `AnalogConfig` | `pinchAnalogConfig` |
| `0x138` | `AxisBinding` | `twistAnalogBinding` |
| `0x140` | `AxisBinding` | `twistDeltaBinding` |
| `0x148` | `DigitalBinding` | `twistRightDigitalBinding` |
| `0x150` | `DigitalBinding` | `twistLeftDigitalBinding` |
| `0x158` | `ScrollDeltaBinding` | `pinchScrollDeltaBinding` |
| `0x160` | `ScrollDeltaBinding` | `twistScrollDeltaBinding` |
| `0x168` | `AxisBinding` | `pinchAnalogBinding` |
| `0x170` | `AxisBinding` | `pinchDeltaBinding` |
| `0x178` | `DigitalBinding` | `pinchDigitalBinding` |
| `0x180` | `DigitalBinding` | `spreadDigitalBinding` |
| `0x188` | `bool` | `emuWithKeys` |
| `0x18C` | `KeyCode` | `emuKeyOneFinger` |
| `0x190` | `KeyCode` | `emuKeyTwoFingers` |
| `0x194` | `KeyCode` | `emuKeyThreeFingers` |
| `0x198` | `KeyCode` | `emuKeySwipeU` |
| `0x19C` | `KeyCode` | `emuKeySwipeR` |
| `0x1A0` | `KeyCode` | `emuKeySwipeD` |
| `0x1A4` | `KeyCode` | `emuKeySwipeL` |
| `0x1A8` | `KeyCode` | `emuKeyTwistR` |
| `0x1AC` | `KeyCode` | `emuKeyTwistL` |
| `0x1B0` | `KeyCode` | `emuKeyPinch` |
| `0x1B4` | `KeyCode` | `emuKeySpread` |
| `0x1B8` | `KeyCode` | `emuMouseTwoFingersKey` |
| `0x1BC` | `KeyCode` | `emuMouseTwistKey` |
| `0x1C0` | `KeyCode` | `emuMousePinchKey` |
| `0x1C4` | `KeyCode` | `emuMouseThreeFingersKey` |
| `0x1C8` | `SuperTouchZone.EmuMouseAxis` | `emuMousePinchAxis` |
| `0x1CC` | `SuperTouchZone.EmuMouseAxis` | `emuMouseTwistAxis` |
| `0x1D0` | `float` | `emuKeySwipeSpeed` |
| `0x1D4` | `float` | `emuKeyPinchSpeed` |
| `0x1D8` | `float` | `emuKeyTwistSpeed` |
| `0x1DC` | `float` | `mouseEmuTwistScreenFactor` |
| `0x1E0` | `int` | `multiFingerCountCur` |
| `0x1E4` | `int` | `multiFingerCountPrev` |
| `0x1E8` | `SuperTouchZone.EmulatedFingerSystem` | `emulatedFingers` |

## `SuperTouchZone.GetScrollDelta` — RVA `0xc44334`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public Vector2 GetScrollDelta(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZone_GetScrollDelta_RVAc44334(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12862340 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC44354;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC44390;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5FB70UL /* metadata target: TouchGestureState.GetScrollDelta */, x0, x1, x2, x3);
        goto label_0xC44388;
        label_0xC44354:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC44374;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC44374;
        label_0xC44374:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12862340 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12862340)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12862340) + (0x4UL))))), 0));
        goto label_0xC44388;
        label_0xC44388:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC44390:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustTapped` — RVA `0xc44394`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public bool JustTapped(int fingerCount, int howManyTimes) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong SuperTouchZone_JustTapped_RVAc44394(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC443BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC443C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC5FB40UL /* metadata target: TouchGestureState.JustTapped */);
        label_0xC443BC:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC443C4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustLongTapped` — RVA `0xc443c8`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool JustLongTapped(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_JustLongTapped_RVAc443c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12862432 = default(uint);
        uint __arm64_flags_right_12862432 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC443E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC443F0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x128UL))))))));
        __arm64_flags_left_12862432 = unchecked((uint)(x8));
        __arm64_flags_right_12862432 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12862432) - (__arm64_flags_right_12862432))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC443E8;
        label_0xC443E8:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC443F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.PressedLong` — RVA `0xc443f4`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool PressedLong(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_PressedLong_RVAc443f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12862476 = default(uint);
        uint __arm64_flags_right_12862476 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC44414;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4441C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x106UL))))))));
        __arm64_flags_left_12862476 = unchecked((uint)(x8));
        __arm64_flags_right_12862476 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12862476) - (__arm64_flags_right_12862476))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC44414;
        label_0xC44414:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC4441C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.PressedNormal` — RVA `0xc44420`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool PressedNormal(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_PressedNormal_RVAc44420(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12862520 = default(uint);
        uint __arm64_flags_right_12862520 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC44440;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC44448;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x104UL))))))));
        __arm64_flags_left_12862520 = unchecked((uint)(x8));
        __arm64_flags_right_12862520 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12862520) - (__arm64_flags_right_12862520))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC44440;
        label_0xC44440:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC44448:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.PressedRaw` — RVA `0xc4444c`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool PressedRaw(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_PressedRaw_RVAc4444c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12862564 = default(uint);
        uint __arm64_flags_right_12862564 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4446C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC44474;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1CUL))))))));
        __arm64_flags_left_12862564 = unchecked((uint)(x8));
        __arm64_flags_right_12862564 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12862564) - (__arm64_flags_right_12862564))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC4446C;
        label_0xC4446C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC44474:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.ctor` — RVA `0xc48e34`

- Lift status: **partial**; input span: 1544 bytes; span to next metadata RVA: 1544 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=232 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lo' at 0xc49080; reason: Unknown IR expression at 0xc49080

```csharp
public static ulong SuperTouchZone_ctor_RVAc48e34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12881932 = default(ulong);
        ulong __arm64_flags_left_12881968 = default(ulong);
        ulong __arm64_flags_left_12882016 = default(ulong);
        ulong __arm64_flags_left_12882040 = default(ulong);
        ulong __arm64_flags_left_12882112 = default(ulong);
        ulong __arm64_flags_left_12882180 = default(ulong);
        ulong __arm64_flags_left_12882288 = default(ulong);
        ulong __arm64_flags_left_12882340 = default(ulong);
        ulong __arm64_flags_result_12882040 = default(ulong);
        ulong __arm64_flags_right_12881932 = default(ulong);
        ulong __arm64_flags_right_12881968 = default(ulong);
        ulong __arm64_flags_right_12882016 = default(ulong);
        ulong __arm64_flags_right_12882040 = default(ulong);
        ulong __arm64_flags_right_12882112 = default(ulong);
        ulong __arm64_flags_right_12882180 = default(ulong);
        ulong __arm64_flags_right_12882288 = default(ulong);
        ulong __arm64_flags_right_12882340 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x239UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xBD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xBE0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC48F04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x990UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x239UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC48F04;
        label_0xC48F04:
        ;
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x288UL))))), 0));
        x8 = 0x3UL;
        x24 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x28 = 0x1A8C000UL;
        x8 = unchecked((ulong)((unchecked((ulong)((x8) & ((~(0xFFFFUL)))))) | (unchecked((ulong)((unchecked((ulong)((0x3F00UL) << (int)(unchecked((int)(0x30UL)))))) << (int)(unchecked((int)(0x0UL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xBF0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC10UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xC00UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x90UL))), x8);
        x8 = 0x432000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x1B8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((x8) + (0x8E0UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((x8) + (0x8E0UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(0x130UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x1C0UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x1CCUL))), unchecked((uint)(x8)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0x1D0UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0x1D0UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0xC4F488UL /* metadata target: TouchControl.ctor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F000000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x9CUL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC6338CUL /* metadata target: MultiTouchGestureThresholds.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x88UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xC8UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xD0UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x29 = 0xFFFFFFFFFFFFFFFDUL;
        x25 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xC48FD0;
        label_0xC48FD0:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4943CUL /* metadata target: SuperTouchZone.FingerState.ctor */, x0, x1, x2, x3);
        if ((x26 == 0x0UL))
        {
            goto label_0xC491D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC48FECUL);
        }
        if ((x22 == 0x0UL))
        {
            goto label_0xC49004;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x22;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49430;
        }
        else
        {
            goto label_0xC49004;
        }
        label_0xC49004:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x26) + (0x18UL))))));
        x27 = unchecked((ulong)((x29) + (0x3UL)));
        __arm64_flags_left_12881932 = x27;
        __arm64_flags_right_12881932 = x8;
        if ((__arm64_flags_left_12881932 >= __arm64_flags_right_12881932))
        {
            goto label_0xC4942C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x26) + (unchecked((ulong)(unchecked((uint)(x25)))))));
        x1 = x22;
        RuntimeMemory.WriteU64(x0, x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xC491D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12881968 = x27;
        __arm64_flags_right_12881968 = x9;
        if ((__arm64_flags_left_12881968 >= __arm64_flags_right_12881968))
        {
            goto label_0xC4942C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = RuntimeMemory.ReadU64(x21);
        if ((x26 == 0x0UL))
        {
            goto label_0xC491D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x25))))))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC4905C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x22;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49430;
        }
        else
        {
            goto label_0xC4905C;
        }
        label_0xC4905C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x26) + (0x18UL))))));
        __arm64_flags_left_12882016 = x27;
        __arm64_flags_right_12882016 = x8;
        if ((__arm64_flags_left_12882016 >= __arm64_flags_right_12882016))
        {
            goto label_0xC4942C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x26) + (unchecked((ulong)(unchecked((uint)(x25)))))));
        x1 = x22;
        RuntimeMemory.WriteU64(x0, x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        __arm64_flags_left_12882040 = x29;
        __arm64_flags_right_12882040 = 0x1UL;
        __arm64_flags_result_12882040 = unchecked((ulong)((__arm64_flags_left_12882040) + (__arm64_flags_right_12882040)));
        x29 = __arm64_flags_result_12882040;
        x25 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x25))) + (unchecked((uint)(0x8UL)))))));
        RuntimeCalls.Unsupported("b.lo", 0xC49080UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC48FD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC08UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xB8UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x24 = RuntimeMemory.ReadU64(x20);
        if ((x24 == 0x0UL))
        {
            goto label_0xC491D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = 0x0UL;
        x25 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xC490BC;
        label_0xC490BC:
        ;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x24) + (0x18UL))))))));
        __arm64_flags_left_12882112 = x27;
        __arm64_flags_right_12882112 = x8;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12882112) - (__arm64_flags_right_12882112))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_12882112)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_12882112)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12882112) - (__arm64_flags_right_12882112))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_12882112)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC49134;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x22 = unchecked((ulong)((x27) + (0x1UL)));
        x1 = unchecked((ulong)(unchecked((uint)(x22))));
        x2 = x19;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC49504UL /* metadata target: SuperTouchZone.MultiFingerTouch.ctor */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC490FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x24);
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49430;
        }
        else
        {
            goto label_0xC490FC;
        }
        label_0xC490FC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x24) + (0x18UL))))));
        x22 = unchecked((ulong)((x22) - (0x1UL)));
        __arm64_flags_left_12882180 = x22;
        __arm64_flags_right_12882180 = x8;
        if ((__arm64_flags_left_12882180 >= __arm64_flags_right_12882180))
        {
            goto label_0xC4942C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x24) + (unchecked((ulong)((x27) << (int)(unchecked((int)(0x3UL))))))));
        x0 = unchecked((ulong)((x24) + (unchecked((ulong)(unchecked((uint)(x25)))))));
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x24 = RuntimeMemory.ReadU64(x20);
        x25 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x25))) + (unchecked((uint)(0x8UL)))))));
        x27 = unchecked((ulong)((x22) + (0x1UL)));
        if ((x24 != 0x0UL))
        {
            goto label_0xC490BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49130UL);
        }
        goto label_0xC491D0;
        label_0xC49134:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBF8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xC0UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x24 = RuntimeMemory.ReadU64(x20);
        if ((x24 == 0x0UL))
        {
            goto label_0xC491D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xC4916C;
        label_0xC4916C:
        ;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x24) + (0x18UL))))))));
        __arm64_flags_left_12882288 = x22;
        __arm64_flags_right_12882288 = x8;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12882288) - (__arm64_flags_right_12882288))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_12882288)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_12882288)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12882288) - (__arm64_flags_right_12882288))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_12882288)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC491D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x28);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC49670UL /* metadata target: SuperTouchZone.MultiFingerTouchConfig.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC491A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x24);
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49430;
        }
        else
        {
            goto label_0xC491A0;
        }
        label_0xC491A0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x24) + (0x18UL))))));
        __arm64_flags_left_12882340 = x22;
        __arm64_flags_right_12882340 = x8;
        if ((__arm64_flags_left_12882340 >= __arm64_flags_right_12882340))
        {
            goto label_0xC4942C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x24) + (unchecked((ulong)((x22) << (int)(unchecked((int)(0x3UL))))))));
        x0 = unchecked((ulong)((x24) + (unchecked((ulong)(unchecked((uint)(x23)))))));
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x24 = RuntimeMemory.ReadU64(x20);
        x22 = unchecked((ulong)((x22) + (0x1UL)));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) + (unchecked((uint)(0x8UL)))))));
        if ((x24 != 0x0UL))
        {
            goto label_0xC4916C;
        }
        else
        {
            goto label_0xC491D0;
        }
        label_0xC491D0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC491D4;
        label_0xC491D4:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBE8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5D500UL /* metadata target: EmuTouchBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x120UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x120UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x990UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x138UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x138UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x140UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x140UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x988UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x150UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x150UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x148UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x148UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x168UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x168UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAC4UL /* metadata target: AxisBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x170UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x170UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x178UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x178UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4EAA8UL /* metadata target: DigitalBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x180UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x180UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB18UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5E460UL /* metadata target: ScrollDeltaBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x158UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x158UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5E460UL /* metadata target: ScrollDeltaBinding.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x160UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x160UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x68UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56BB8UL /* metadata target: AnalogConfig.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x130UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x130UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56BB8UL /* metadata target: AnalogConfig.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x128UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x128UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3DCCUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        v0 = ((RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))).ShiftLeftLogical(unchecked((int)0x20UL))) | (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x8))).ShiftLeftLogical(unchecked((int)0x20UL))).ShiftLeftLogical(unchecked((int)0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xECUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xECUL))), v0);
#endif
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(sp);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4975CUL /* metadata target: SuperTouchZone.InitEmulatedFingers */);
        label_0xC4942C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC49430;
        label_0xC49430:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.InitEmulatedFingers` — RVA `0xc4975c`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `private void InitEmulatedFingers() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong SuperTouchZone_InitEmulatedFingers_RVAc4975c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x23CUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC38UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49790;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC38UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x23CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49790;
        label_0xC49790:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4D108UL /* metadata target: SuperTouchZone.EmulatedFingerSystem.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x1E8UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x1E8UL))), x20);
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `SuperTouchZone.OnDestroyControl` — RVA `0xc497c0`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `protected override void OnDestroyControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong SuperTouchZone_OnDestroyControl_RVAc497c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x298UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A0UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `SuperTouchZone.OnInitControl` — RVA `0xc497d0`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `protected override void OnInitControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong SuperTouchZone_OnInitControl_RVAc497d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12883952 = default(uint);
        uint __arm64_flags_left_12883960 = default(uint);
        uint __arm64_flags_left_12883984 = default(uint);
        uint __arm64_flags_left_12883992 = default(uint);
        uint __arm64_flags_right_12883952 = default(uint);
        uint __arm64_flags_right_12883960 = default(uint);
        uint __arm64_flags_right_12883984 = default(uint);
        uint __arm64_flags_right_12883992 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC49840;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = x0;
        x20 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        goto label_0xC497E8;
        label_0xC497E8:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) - (unchecked((uint)(0x4UL)))))));
        __arm64_flags_left_12883952 = unchecked((uint)(x9));
        __arm64_flags_right_12883952 = unchecked((uint)(x10));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12883952) - (__arm64_flags_right_12883952))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12883952)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12883952)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12883952) - (__arm64_flags_right_12883952))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12883952)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49844;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC497F8UL);
        }
        __arm64_flags_left_12883960 = unchecked((uint)(x9));
        __arm64_flags_right_12883960 = unchecked((uint)(x10));
        if ((__arm64_flags_left_12883960 >= __arm64_flags_right_12883960))
        {
            goto label_0xC4986C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        if ((x10 == 0x0UL))
        {
            goto label_0xC49840;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x18UL))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x20))))))));
        __arm64_flags_left_12883984 = unchecked((uint)(x9));
        __arm64_flags_right_12883984 = unchecked((uint)(x11));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12883984) - (__arm64_flags_right_12883984))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12883984)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12883984)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12883984) - (__arm64_flags_right_12883984))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12883984)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49818UL);
        }
        __arm64_flags_left_12883992 = unchecked((uint)(x9));
        __arm64_flags_right_12883992 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12883992 >= __arm64_flags_right_12883992))
        {
            goto label_0xC4986C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)(x20))))))));
        goto label_0xC4982C;
        label_0xC49828:
        ;
        x1 = 0x0UL;
        goto label_0xC4982C;
        label_0xC4982C:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xC49840;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49830UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC49870UL /* metadata target: SuperTouchZone.MultiFingerTouch.Init */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC497E8;
        }
        else
        {
            goto label_0xC49840;
        }
        label_0xC49840:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC49844;
        label_0xC49844:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x94UL))))), 0));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC49944UL /* metadata target: SuperTouchZone.SetTouchSmoothing */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x298UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC4986C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.SetTouchSmoothing` — RVA `0xc49944`

- Lift status: **exact**; input span: 216 bytes; span to next metadata RVA: 216 bytes.
- Metadata signature: `public void SetTouchSmoothing(float smPow) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong SuperTouchZone_SetTouchSmoothing_RVAc49944(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12884340 = default(uint);
        uint __arm64_flags_left_12884356 = default(uint);
        uint __arm64_flags_left_12884400 = default(uint);
        uint __arm64_flags_left_12884424 = default(uint);
        uint __arm64_flags_left_12884436 = default(uint);
        uint __arm64_flags_left_12884480 = default(uint);
        uint __arm64_flags_right_12884340 = default(uint);
        uint __arm64_flags_right_12884356 = default(uint);
        uint __arm64_flags_right_12884400 = default(uint);
        uint __arm64_flags_right_12884424 = default(uint);
        uint __arm64_flags_right_12884436 = default(uint);
        uint __arm64_flags_right_12884480 = default(uint);
        float __arm64_float_flags_left_12884308 = default(float);
        float __arm64_float_flags_right_12884308 = default(float);
        float __arm64_fp_left_12884304 = default(float);
        float __arm64_fp_right_12884304 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_fp_left_12884304 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12884304 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12884304 != __arm64_fp_left_12884304) ? __arm64_fp_left_12884304 : ((__arm64_fp_right_12884304 != __arm64_fp_right_12884304) ? __arm64_fp_right_12884304 : (((__arm64_fp_left_12884304 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12884304 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12884304), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12884304), 0))))), 0) : ((__arm64_fp_left_12884304 <= __arm64_fp_right_12884304) ? __arm64_fp_left_12884304 : __arm64_fp_right_12884304))))), 0));
        __arm64_float_flags_left_12884308 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12884308 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12884308 >= __arm64_float_flags_right_12884308) || ((__arm64_float_flags_left_12884308 != __arm64_float_flags_left_12884308) || (__arm64_float_flags_right_12884308 != __arm64_float_flags_right_12884308))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x94UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = 0x432000UL;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x3B8UL))))), 0));
        __arm64_flags_left_12884340 = unchecked((uint)(x9));
        __arm64_flags_right_12884340 = unchecked((uint)0x1UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884340) - (__arm64_flags_right_12884340))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12884340)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884340)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884340) - (__arm64_flags_right_12884340))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884340)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC499BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC49984;
        label_0xC49984:
        ;
        __arm64_flags_left_12884356 = unchecked((uint)(x10));
        __arm64_flags_right_12884356 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12884356 >= __arm64_flags_right_12884356))
        {
            goto label_0xC49A18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x20UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x28UL))));
        if ((x12 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC499A0UL);
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((x12) + (0xA4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x30UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12884400 = unchecked((uint)(x10));
        __arm64_flags_right_12884400 = unchecked((uint)(x9));
        RuntimeMemory.WriteF32(unchecked((ulong)((x11) + (0xA4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884400) - (__arm64_flags_right_12884400))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12884400)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884400)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884400) - (__arm64_flags_right_12884400))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884400)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49984;
        }
        else
        {
            goto label_0xC499BC;
        }
        label_0xC499BC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12884424 = unchecked((uint)(x9));
        __arm64_flags_right_12884424 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884424) - (__arm64_flags_right_12884424))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12884424)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884424)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884424) - (__arm64_flags_right_12884424))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884424)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49A0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC499D4;
        label_0xC499D4:
        ;
        __arm64_flags_left_12884436 = unchecked((uint)(x10));
        __arm64_flags_right_12884436 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12884436 >= __arm64_flags_right_12884436))
        {
            goto label_0xC49A18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x20UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x18UL))));
        if ((x12 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC499F0UL);
        }
        RuntimeMemory.WriteF32(unchecked((ulong)((x12) + (0xA4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x20UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC49A14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12884480 = unchecked((uint)(x10));
        __arm64_flags_right_12884480 = unchecked((uint)(x9));
        RuntimeMemory.WriteF32(unchecked((ulong)((x11) + (0xA4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884480) - (__arm64_flags_right_12884480))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12884480)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884480)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884480) - (__arm64_flags_right_12884480))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884480)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC499D4;
        }
        else
        {
            goto label_0xC49A0C;
        }
        label_0xC49A0C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49A14:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC49A18;
        label_0xC49A18:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.ResetControl` — RVA `0xc49a1c`

- Lift status: **exact**; input span: 220 bytes; span to next metadata RVA: 220 bytes.
- Metadata signature: `public override void ResetControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong SuperTouchZone_ResetControl_RVAc49a1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12884552 = default(uint);
        uint __arm64_flags_left_12884560 = default(uint);
        uint __arm64_flags_left_12884616 = default(uint);
        uint __arm64_flags_left_12884624 = default(uint);
        uint __arm64_flags_right_12884552 = default(uint);
        uint __arm64_flags_right_12884560 = default(uint);
        uint __arm64_flags_right_12884616 = default(uint);
        uint __arm64_flags_right_12884624 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC49AB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC49A44;
        label_0xC49A44:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12884552 = unchecked((uint)(x20));
        __arm64_flags_right_12884552 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884552) - (__arm64_flags_right_12884552))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12884552)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884552)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884552) - (__arm64_flags_right_12884552))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884552)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49A78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49A50UL);
        }
        __arm64_flags_left_12884560 = unchecked((uint)(x20));
        __arm64_flags_right_12884560 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12884560 >= __arm64_flags_right_12884560))
        {
            goto label_0xC49AF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49AB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49A64UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC49AF8UL /* metadata target: SuperTouchZone.MultiFingerTouch.Reset */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC49A44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49A74UL);
        }
        goto label_0xC49AB4;
        label_0xC49A78:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC49AB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC49A84;
        label_0xC49A84:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12884616 = unchecked((uint)(x20));
        __arm64_flags_right_12884616 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884616) - (__arm64_flags_right_12884616))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12884616)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884616)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884616) - (__arm64_flags_right_12884616))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884616)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49AB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49A90UL);
        }
        __arm64_flags_left_12884624 = unchecked((uint)(x20));
        __arm64_flags_right_12884624 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12884624 >= __arm64_flags_right_12884624))
        {
            goto label_0xC49AF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49AB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC49AA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC49B48UL /* metadata target: SuperTouchZone.FingerState.Reset */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC49A84;
        }
        else
        {
            goto label_0xC49AB4;
        }
        label_0xC49AB4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC49AB8;
        label_0xC49AB8:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3DCCUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        x8 = unchecked((ulong)((x19) + (0x104UL)));
        v0 = ((RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x9))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x9))).ShiftLeftLogical(unchecked((int)0x20UL))) | (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x9))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)(x9))).ShiftLeftLogical(unchecked((int)0x20UL))).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xFCUL))), 0x0UL);
        x10 = unchecked((ulong)((x19) + (0x10CUL)));
        x11 = unchecked((ulong)((x19) + (0x114UL)));
        RuntimeMemory.WritePtr(x8, 0x0UL);
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xECUL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xECUL))), v0);
#endif
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeMemory.WritePtr(x11, 0x0UL);
        RuntimeMemory.WritePtr(x10, 0x0UL);
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49AF4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetMultiFingerTouch` — RVA `0xc49b80`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `protected SuperTouchZone.MultiFingerTouch GetMultiFingerTouch(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong SuperTouchZone_GetMultiFingerTouch_RVAc49b80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12884868 = default(uint);
        uint __arm64_flags_left_12884888 = default(uint);
        uint __arm64_flags_left_12884904 = default(uint);
        uint __arm64_flags_result_12884868 = default(uint);
        uint __arm64_flags_right_12884868 = default(uint);
        uint __arm64_flags_right_12884888 = default(uint);
        uint __arm64_flags_right_12884904 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        __arm64_flags_left_12884868 = unchecked((uint)(x1));
        __arm64_flags_right_12884868 = unchecked((uint)0x1UL);
        __arm64_flags_result_12884868 = unchecked((uint)((__arm64_flags_left_12884868) - (__arm64_flags_right_12884868)));
        x8 = unchecked((ulong)(__arm64_flags_result_12884868));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884868) - (__arm64_flags_right_12884868))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12884868)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884868)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884868) - (__arm64_flags_right_12884868))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884868)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49BA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC49BC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_12884888 = unchecked((uint)(x10));
        __arm64_flags_right_12884888 = unchecked((uint)(x1));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884888) - (__arm64_flags_right_12884888))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12884888)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12884888)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12884888) - (__arm64_flags_right_12884888))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12884888)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC49BA8;
        }
        else
        {
            goto label_0xC49BA0;
        }
        label_0xC49BA0:
        ;
        x0 = 0x0UL;
        goto label_0xC49BB8;
        label_0xC49BA8:
        ;
        __arm64_flags_left_12884904 = unchecked((uint)(x8));
        __arm64_flags_right_12884904 = unchecked((uint)(x10));
        if ((__arm64_flags_left_12884904 >= __arm64_flags_right_12884904))
        {
            goto label_0xC49BC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x20UL))));
        goto label_0xC49BB8;
        label_0xC49BB8:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49BC0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC49BC4;
        label_0xC49BC4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustPressedRaw` — RVA `0xc49bc8`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool JustPressedRaw(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong SuperTouchZone_JustPressedRaw_RVAc49bc8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49BE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49BF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC61BF0UL /* metadata target: TouchGestureBasicState.JustPressedRaw */);
        label_0xC49BE8:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49BF0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustReleasedRaw` — RVA `0xc49bf4`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool JustReleasedRaw(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong SuperTouchZone_JustReleasedRaw_RVAc49bf4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49C14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49C1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC61C10UL /* metadata target: TouchGestureBasicState.JustReleasedRaw */);
        label_0xC49C14:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49C1C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustPressedNormal` — RVA `0xc49c20`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool JustPressedNormal(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong SuperTouchZone_JustPressedNormal_RVAc49c20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49C40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49C48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC623B4UL /* metadata target: TouchGestureState.JustPressedNormal */);
        label_0xC49C40:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49C48:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustReleasedNormal` — RVA `0xc49c4c`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool JustReleasedNormal(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong SuperTouchZone_JustReleasedNormal_RVAc49c4c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49C6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49C74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC623D4UL /* metadata target: TouchGestureState.JustReleasedNormal */);
        label_0xC49C6C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49C74:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustPressedLong` — RVA `0xc49c78`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool JustPressedLong(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong SuperTouchZone_JustPressedLong_RVAc49c78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49C98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49CA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC623FCUL /* metadata target: TouchGestureState.JustPressedLong */);
        label_0xC49C98:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49CA0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.JustReleasedLong` — RVA `0xc49ca4`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool JustReleasedLong(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong SuperTouchZone_JustReleasedLong_RVAc49ca4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49CC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49CCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC6241CUL /* metadata target: TouchGestureState.JustReleasedLong */);
        label_0xC49CC4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC49CCC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.SwipeActive` — RVA `0xc49cd0`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool SwipeActive(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_SwipeActive_RVAc49cd0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12885224 = default(uint);
        uint __arm64_flags_right_12885224 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49CF0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC49CF8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x120UL))))))));
        __arm64_flags_left_12885224 = unchecked((uint)(x8));
        __arm64_flags_right_12885224 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12885224) - (__arm64_flags_right_12885224))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC49CF0;
        label_0xC49CF0:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC49CF8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.SwipeJustActivated` — RVA `0xc49cfc`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public bool SwipeJustActivated(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_SwipeJustActivated_RVAc49cfc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12885268 = default(uint);
        uint __arm64_flags_right_12885268 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49D1C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC49D24;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x121UL))))))));
        __arm64_flags_left_12885268 = unchecked((uint)(x8));
        __arm64_flags_right_12885268 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12885268) - (__arm64_flags_right_12885268))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC49D1C;
        label_0xC49D1C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC49D24:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.GetCurPos` — RVA `0xc49d28`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public Vector2 GetCurPos(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong SuperTouchZone_GetCurPos_RVAc49d28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49D48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC49D8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (0x34UL)));
        x9 = unchecked((ulong)((x9) + (0x38UL)));
        goto label_0xC49D7C;
        label_0xC49D48:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49D68;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49D68;
        label_0xC49D68:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)((x8) + (0x4UL)));
        goto label_0xC49D7C;
        label_0xC49D7C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x9)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC49D8C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetStartPos` — RVA `0xc49d90`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public Vector2 GetStartPos(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong SuperTouchZone_GetStartPos_RVAc49d90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49DB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC49DF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (0x5CUL)));
        x9 = unchecked((ulong)((x9) + (0x60UL)));
        goto label_0xC49DE4;
        label_0xC49DB0:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49DD0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49DD0;
        label_0xC49DD0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)((x8) + (0x4UL)));
        goto label_0xC49DE4;
        label_0xC49DE4:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x9)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC49DF4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetTapPos` — RVA `0xc49df8`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public Vector2 GetTapPos(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong SuperTouchZone_GetTapPos_RVAc49df8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49E18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC49E5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (0x12CUL)));
        x9 = unchecked((ulong)((x9) + (0x130UL)));
        goto label_0xC49E4C;
        label_0xC49E18:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49E38;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49E38;
        label_0xC49E38:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)((x8) + (0x4UL)));
        goto label_0xC49E4C;
        label_0xC49E4C:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x9)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC49E5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetRawSwipeVector` — RVA `0xc49e60`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public Vector2 GetRawSwipeVector(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZone_GetRawSwipeVector_RVAc49e60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12885680 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49E80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49EBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61C58UL /* metadata target: TouchGestureBasicState.GetSwipeVecRaw */, x0, x1, x2, x3);
        goto label_0xC49EB4;
        label_0xC49E80:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49EA0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49EA0;
        label_0xC49EA0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12885680 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12885680)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12885680) + (0x4UL))))), 0));
        goto label_0xC49EB4;
        label_0xC49EB4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC49EBC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetRawSwipeDelta` — RVA `0xc49ec0`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public Vector2 GetRawSwipeDelta(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZone_GetRawSwipeDelta_RVAc49ec0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12885776 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49EE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49F1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61C80UL /* metadata target: TouchGestureBasicState.GetDeltaVecRaw */, x0, x1, x2, x3);
        goto label_0xC49F14;
        label_0xC49EE0:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49F00;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49F00;
        label_0xC49F00:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12885776 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12885776)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12885776) + (0x4UL))))), 0));
        goto label_0xC49F14;
        label_0xC49F14:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC49F1C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetUnconstrainedSwipeVector` — RVA `0xc49f20`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public Vector2 GetUnconstrainedSwipeVector(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZone_GetUnconstrainedSwipeVector_RVAc49f20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12885872 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49F40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49F7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61C6CUL /* metadata target: TouchGestureBasicState.GetSwipeVecSmooth */, x0, x1, x2, x3);
        goto label_0xC49F74;
        label_0xC49F40:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49F60;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49F60;
        label_0xC49F60:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12885872 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12885872)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12885872) + (0x4UL))))), 0));
        goto label_0xC49F74;
        label_0xC49F74:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC49F7C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetUnconstrainedSwipeDelta` — RVA `0xc49f80`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public Vector2 GetUnconstrainedSwipeDelta(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZone_GetUnconstrainedSwipeDelta_RVAc49f80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12885968 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC49FA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC49FDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61C94UL /* metadata target: TouchGestureBasicState.GetDeltaVecSmooth */, x0, x1, x2, x3);
        goto label_0xC49FD4;
        label_0xC49FA0:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC49FC0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC49FC0;
        label_0xC49FC0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12885968 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12885968)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12885968) + (0x4UL))))), 0));
        goto label_0xC49FD4;
        label_0xC49FD4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC49FDC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetSwipeVector` — RVA `0xc49fe0`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public Vector2 GetSwipeVector(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong SuperTouchZone_GetSwipeVector_RVAc49fe0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC4A044;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (0xD8UL)));
        x9 = unchecked((ulong)((x9) + (0xDCUL)));
        goto label_0xC4A034;
        label_0xC4A000:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A020;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4A020;
        label_0xC4A020:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)((x8) + (0x4UL)));
        goto label_0xC4A034;
        label_0xC4A034:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x9)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4A044:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetSwipeDelta` — RVA `0xc4a048`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public Vector2 GetSwipeDelta(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZone_GetSwipeDelta_RVAc4a048(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12886168 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A068;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A0A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5FB60UL /* metadata target: TouchGestureState.GetConstrainedDeltaVec */, x0, x1, x2, x3);
        goto label_0xC4A09C;
        label_0xC4A068:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A088;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4A088;
        label_0xC4A088:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12886168 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12886168)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12886168) + (0x4UL))))), 0));
        goto label_0xC4A09C;
        label_0xC4A09C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4A0A4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetSwipeDir` — RVA `0xc4a0a8`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public Dir GetSwipeDir(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint SuperTouchZone_GetSwipeDir_RVAc4a0a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A0C8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A0D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A0D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        goto label_0xC4A0C8;
        label_0xC4A0C8:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC4A0D0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.GetScroll` — RVA `0xc4a0d4`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public Vector2 GetScroll(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong SuperTouchZone_GetScroll_RVAc4a0d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A0F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC4A138;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (0xE8UL)));
        x9 = unchecked((ulong)((x9) + (0xECUL)));
        goto label_0xC4A128;
        label_0xC4A0F4:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A114;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4A114;
        label_0xC4A114:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)((x8) + (0x4UL)));
        goto label_0xC4A128;
        label_0xC4A128:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x9)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4A138:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.PinchActive` — RVA `0xc4a13c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool PinchActive() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint SuperTouchZone_PinchActive_RVAc4a13c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xE8UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.PinchJustActivated` — RVA `0xc4a144`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool PinchJustActivated() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint SuperTouchZone_PinchJustActivated_RVAc4a144(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xE9UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.GetPinchScale` — RVA `0xc4a14c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float GetPinchScale() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZone_GetPinchScale_RVAc4a14c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12886348 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12886348 = unchecked((ulong)((x0) + (0xF0UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12886348)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12886348) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.GetPinchScaleDelta` — RVA `0xc4a158`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float GetPinchScaleDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZone_GetPinchScaleDelta_RVAc4a158(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12886360 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12886360 = unchecked((ulong)((x0) + (0xF4UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12886360)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12886360) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.GetPinchDist` — RVA `0xc4a164`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float GetPinchDist() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZone_GetPinchDist_RVAc4a164(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12886372 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12886372 = unchecked((ulong)((x0) + (0xF0UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12886372)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12886372) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.GetPinchDistDelta` — RVA `0xc4a170`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public float GetPinchDistDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZone_GetPinchDistDelta_RVAc4a170(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12886384 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12886384 = unchecked((ulong)((x0) + (0xF4UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12886384)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12886384) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.TwistActive` — RVA `0xc4a17c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool TwistActive() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint SuperTouchZone_TwistActive_RVAc4a17c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xEAUL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.TwistJustActivated` — RVA `0xc4a184`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool TwistJustActivated() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint SuperTouchZone_TwistJustActivated_RVAc4a184(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xEBUL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.GetTwist` — RVA `0xc4a18c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float GetTwist() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong SuperTouchZone_GetTwist_RVAc4a18c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x104UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.GetTwistDelta` — RVA `0xc4a194`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public float GetTwistDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZone_GetTwistDelta_RVAc4a194(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x104UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x108UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.GetTwistScrollDelta` — RVA `0xc4a1a4`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public int GetTwistScrollDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_GetTwistScrollDelta_RVAc4a1a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x110UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10CUL))))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(x9)))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.GetPinchScrollDelta` — RVA `0xc4a1b4`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public int GetPinchScrollDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint SuperTouchZone_GetPinchScrollDelta_RVAc4a1b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x118UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x114UL))))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(x9)))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.GetReleasedDuration` — RVA `0xc4a1c4`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public float GetReleasedDuration(int fingerCount) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong SuperTouchZone_GetReleasedDuration_RVAc4a1c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A1E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A1EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A1D8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x80UL))))), 0));
        goto label_0xC4A1E4;
        label_0xC4A1E0:
        ;
        goto label_0xC4A1E4;
        label_0xC4A1E4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4A1EC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetThresholds` — RVA `0xc4a1f0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public MultiTouchGestureThresholds GetThresholds() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZone_GetThresholds_RVAc4a1f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x88UL))));
        return x0;
        return default(ulong);
    }
```

## `SuperTouchZone.GetAveragedFingerPos` — RVA `0xc4a1f8`

- Lift status: **partial**; input span: 336 bytes; span to next metadata RVA: 336 bytes.
- Metadata signature: `private Vector2 GetAveragedFingerPos(SuperTouchZone.FingerState[] fingers, int count, bool orientedSpace, bool useSmoothPos) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=36 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc4a22c; reason: Unknown IR expression at 0xc4a22c; reason: Unsupported instruction 'b.lt' at 0xc4a260; reason: Unknown IR expression at 0xc4a260; reason: Unsupported instruction 'b.ne' at 0xc4a304; reason: Unknown IR expression at 0xc4a304

```csharp
public static ulong SuperTouchZone_GetAveragedFingerPos_RVAc4a1f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12886552 = default(uint);
        uint __arm64_flags_left_12886560 = default(uint);
        uint __arm64_flags_left_12886608 = default(uint);
        uint __arm64_flags_left_12886668 = default(uint);
        uint __arm64_flags_left_12886688 = default(uint);
        uint __arm64_flags_left_12886704 = default(uint);
        uint __arm64_flags_left_12886776 = default(uint);
        uint __arm64_flags_result_12886688 = default(uint);
        uint __arm64_flags_result_12886704 = default(uint);
        uint __arm64_flags_right_12886552 = default(uint);
        uint __arm64_flags_right_12886560 = default(uint);
        uint __arm64_flags_right_12886608 = default(uint);
        uint __arm64_flags_right_12886668 = default(uint);
        uint __arm64_flags_right_12886688 = default(uint);
        uint __arm64_flags_right_12886704 = default(uint);
        uint __arm64_flags_right_12886776 = default(uint);
        float __arm64_float_flags_left_12886728 = default(float);
        float __arm64_float_flags_left_12886736 = default(float);
        float __arm64_float_flags_left_12886744 = default(float);
        float __arm64_float_flags_left_12886752 = default(float);
        float __arm64_float_flags_right_12886728 = default(float);
        float __arm64_float_flags_right_12886736 = default(float);
        float __arm64_float_flags_right_12886744 = default(float);
        float __arm64_float_flags_right_12886752 = default(float);
        ulong __arm64_pair_address_12886620 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x14 = default(ulong);
        ulong x15 = default(ulong);
        ulong x16 = default(ulong);
        ulong x17 = default(ulong);
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
        if ((x1 == 0x0UL))
        {
            goto label_0xC4A340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x1) + (0x18UL))))));
        x23 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1E0UL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x4))));
        __arm64_flags_left_12886552 = unchecked((uint)(x8));
        __arm64_flags_right_12886552 = unchecked((uint)(x2));
        x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12886552) - (__arm64_flags_right_12886552))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12886552)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12886552)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12886552) - (__arm64_flags_right_12886552))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12886552)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)(x2)))));
        __arm64_flags_left_12886560 = unchecked((uint)(x2));
        __arm64_flags_right_12886560 = unchecked((uint)0x0UL);
        x20 = unchecked((ulong)(unchecked((uint)(x3))));
        x21 = x1;
        RuntimeCalls.Unsupported("csel", 0xC4A22CUL);
        x22 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x0UL) : unchecked((uint)(x8)))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A248;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4A248;
        label_0xC4A248:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        __arm64_flags_left_12886608 = unchecked((uint)(x22));
        __arm64_flags_right_12886608 = unchecked((uint)0x1UL);
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12886620 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12886620)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12886620) + (0x4UL))))), 0));
        RuntimeCalls.Unsupported("b.lt", 0xC4A260UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4A30C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x18UL))))));
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x10 = unchecked((ulong)(unchecked((uint)(0x28UL))));
        x11 = unchecked((ulong)(unchecked((uint)(0x30UL))));
        x12 = unchecked((ulong)(unchecked((uint)(0x34UL))));
        x13 = unchecked((ulong)(unchecked((uint)(0x44UL))));
        x14 = unchecked((ulong)(unchecked((uint)(0x38UL))));
        x15 = unchecked((ulong)(unchecked((uint)(0x48UL))));
        v4 = v0;
        v5 = v1;
        goto label_0xC4A28C;
        label_0xC4A28C:
        ;
        __arm64_flags_left_12886668 = unchecked((uint)(x9));
        __arm64_flags_right_12886668 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_12886668) - (__arm64_flags_right_12886668))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4A344;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x16 = unchecked((ulong)((x21) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x16 = RuntimeMemory.ReadU64(unchecked((ulong)((x16) + (0x20UL))));
        if ((x16 == 0x0UL))
        {
            goto label_0xC4A340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A2A0UL);
        }
        __arm64_flags_left_12886688 = unchecked((uint)(x20));
        __arm64_flags_right_12886688 = unchecked((uint)0x1UL);
        __arm64_flags_result_12886688 = unchecked((uint)((__arm64_flags_left_12886688) & (__arm64_flags_right_12886688)));
        x17 = ((!((__arm64_flags_result_12886688 == unchecked((uint)0x0UL)))) ? x11 : x10);
        x16 = RuntimeMemory.ReadU64(unchecked((ulong)((x16) + (x17))));
        if ((x16 == 0x0UL))
        {
            goto label_0xC4A340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A2B0UL);
        }
        __arm64_flags_left_12886704 = unchecked((uint)(x19));
        __arm64_flags_right_12886704 = unchecked((uint)0x1UL);
        __arm64_flags_result_12886704 = unchecked((uint)((__arm64_flags_left_12886704) & (__arm64_flags_right_12886704)));
        x17 = ((!((__arm64_flags_result_12886704 == unchecked((uint)0x0UL)))) ? x13 : x12);
        x0 = ((!((__arm64_flags_result_12886704 == unchecked((uint)0x0UL)))) ? x15 : x14);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x16) + (x0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x16) + (x17))))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4A2EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A2C8UL);
        }
        __arm64_float_flags_left_12886728 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12886728 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12886728 < __arm64_float_flags_right_12886728) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12886736 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12886736 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12886736 < __arm64_float_flags_right_12886736) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12886744 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12886744 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12886744 > __arm64_float_flags_right_12886744) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12886752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12886752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12886752 > __arm64_float_flags_right_12886752) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        goto label_0xC4A2F4;
        label_0xC4A2EC:
        ;
        v1 = v2;
        v0 = v3;
        goto label_0xC4A2F4;
        label_0xC4A2F4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12886776 = unchecked((uint)(x22));
        __arm64_flags_right_12886776 = unchecked((uint)(x8));
        v4 = v3;
        v5 = v2;
        RuntimeCalls.Unsupported("b.ne", 0xC4A304UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4A28C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A308UL);
        }
        goto label_0xC4A314;
        label_0xC4A30C:
        ;
        v2 = v1;
        v3 = v0;
        goto label_0xC4A314;
        label_0xC4A314:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4A340:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC4A344;
        label_0xC4A344:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.StartMultiFingerTouch` — RVA `0xc4a348`

- Lift status: **partial**; input span: 344 bytes; span to next metadata RVA: 344 bytes.
- Metadata signature: `private void StartMultiFingerTouch(int fingerNum, SuperTouchZone.FingerState[] fingers, Vector2 startScreenPos, Vector2 startOrientedPos, bool quietMode) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=41 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ge' at 0xc4a418; reason: Unknown IR expression at 0xc4a418

```csharp
public static ulong SuperTouchZone_StartMultiFingerTouch_RVAc4a348(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12886928 = default(uint);
        uint __arm64_flags_left_12886936 = default(uint);
        uint __arm64_flags_left_12886968 = default(uint);
        uint __arm64_flags_left_12887024 = default(uint);
        uint __arm64_flags_left_12887092 = default(uint);
        uint __arm64_flags_left_12887112 = default(uint);
        uint __arm64_flags_right_12886928 = default(uint);
        uint __arm64_flags_right_12886936 = default(uint);
        uint __arm64_flags_right_12886968 = default(uint);
        uint __arm64_flags_right_12887024 = default(uint);
        uint __arm64_flags_right_12887092 = default(uint);
        uint __arm64_flags_right_12887112 = default(uint);
        ulong __arm64_pair_address_12886856 = default(ulong);
        ulong __arm64_pair_address_12886860 = default(ulong);
        ulong __arm64_pair_address_12887184 = default(ulong);
        ulong __arm64_pair_address_12887188 = default(ulong);
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
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12886856 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12886856, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12886856) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12886856;
        __arm64_pair_address_12886860 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12886860, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12886860) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A47C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        v8 = v3;
        v9 = v2;
        v10 = v1;
        v11 = v0;
        x19 = x2;
        x20 = x0;
        x21 = unchecked((ulong)(unchecked((uint)(x1))));
        x24 = 0x0UL;
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x3))) & (unchecked((uint)(0x1UL)))))));
        goto label_0xC4A38C;
        label_0xC4A38C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12886928 = unchecked((uint)(x24));
        __arm64_flags_right_12886928 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12886928) - (__arm64_flags_right_12886928))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12886928)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12886928)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12886928) - (__arm64_flags_right_12886928))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12886928)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4A480;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A398UL);
        }
        __arm64_flags_left_12886936 = unchecked((uint)(x24));
        __arm64_flags_right_12886936 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12886936 >= __arm64_flags_right_12886936))
        {
            goto label_0xC4A49C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x24) << (int)(unchecked((int)(0x3UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x23 == 0x0UL))
        {
            goto label_0xC4A47C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A47C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12886968 = unchecked((uint)(x8));
        __arm64_flags_right_12886968 = unchecked((uint)(x21));
        if ((!((unchecked((uint)((__arm64_flags_left_12886968) - (__arm64_flags_right_12886968))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC4A418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A3C0UL);
        }
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0xE4UL))))), 0));
        x0 = x23;
        x1 = x19;
        v0 = v11;
        v1 = v10;
        v2 = v9;
        v3 = v8;
        x2 = unchecked((ulong)(unchecked((uint)(x22))));
        x0 = RuntimeCalls.InvokeDirect(0xC4A4BCUL /* metadata target: SuperTouchZone.MultiFingerTouch.Start */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A47C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12887024 = unchecked((uint)(x8));
        __arm64_flags_right_12887024 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12887024) - (__arm64_flags_right_12887024))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC4A470;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4A680UL /* metadata target: SuperTouchZone.GetTwoFingerDist */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0xECUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4A744UL /* metadata target: SuperTouchZone.GetTwoFingerAngle */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0xFCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC4A470;
        label_0xC4A418:
        ;
        RuntimeCalls.Unsupported("b.ge", 0xC4A418UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4A42C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xC4A8C0UL /* metadata target: SuperTouchZone.MultiFingerTouch.End */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4A434;
        label_0xC4A42C:
        ;
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xC4A944UL /* metadata target: SuperTouchZone.MultiFingerTouch.EndAndReport */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4A434;
        label_0xC4A434:
        ;
        __arm64_flags_left_12887092 = unchecked((uint)(x21));
        __arm64_flags_right_12887092 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12887092) - (__arm64_flags_right_12887092))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12887092)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12887092)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12887092) - (__arm64_flags_right_12887092))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12887092)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4A470;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A47C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12887112 = unchecked((uint)(x8));
        __arm64_flags_right_12887112 = unchecked((uint)(x21));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12887112) - (__arm64_flags_right_12887112))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12887112)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12887112)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12887112) - (__arm64_flags_right_12887112))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12887112)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4A470;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A47C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC624ECUL /* metadata target: TouchGestureState.CancelTap */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A47C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC624ECUL /* metadata target: TouchGestureState.CancelTap */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4A470;
        label_0xC4A470:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        x24 = unchecked((ulong)((x24) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4A38C;
        }
        else
        {
            goto label_0xC4A47C;
        }
        label_0xC4A47C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4A480;
        label_0xC4A480:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_12887184 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12887184)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12887184) + (0x8UL))))), 0));
        __arm64_pair_address_12887188 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12887188)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12887188) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12887188) + (0x60UL)));
        return x0;
        label_0xC4A49C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetTwoFingerDist` — RVA `0xc4a680`

- Lift status: **partial**; input span: 196 bytes; span to next metadata RVA: 196 bytes.
- Metadata signature: `private float GetTwoFingerDist() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=21 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fsub' at 0xc4a700; reason: Unsupported instruction 'fmul' at 0xc4a71c; reason: Unsupported instruction 'faddp' at 0xc4a720

```csharp
public static ulong SuperTouchZone_GetTwoFingerDist_RVAc4a680(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fp_left_12887848 = default(float);
        float __arm64_fp_right_12887848 = default(float);
        ulong __arm64_pair_address_12887680 = default(ulong);
        ulong __arm64_pair_address_12887864 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12887680 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12887680, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12887680) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12887680;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A72C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4BB0CUL /* metadata target: SuperTouchZone.MultiFingerTouch.GetFinger */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A72C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4BB0CUL /* metadata target: SuperTouchZone.MultiFingerTouch.GetFinger */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A72C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC4A740;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = 0x1BAB000UL;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x44UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x243UL))))))));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x9) + (0x44UL))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A6F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4A6F8;
        label_0xC4A6F8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        RuntimeCalls.Unsupported("fsub", 0xC4A700UL);
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A714;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A710UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4A714;
        label_0xC4A714:
        ;
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        RuntimeCalls.Unsupported("fmul", 0xC4A71CUL);
        RuntimeCalls.Unsupported("faddp", 0xC4A720UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))))), 0));
        __arm64_fp_left_12887848 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_fp_right_12887848 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12887848 != __arm64_fp_left_12887848) ? __arm64_fp_left_12887848 : ((__arm64_fp_right_12887848 != __arm64_fp_right_12887848) ? __arm64_fp_right_12887848 : (((__arm64_fp_left_12887848 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12887848 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12887848), 0)) & (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12887848), 0))))), 0) : ((__arm64_fp_left_12887848 >= __arm64_fp_right_12887848) ? __arm64_fp_left_12887848 : __arm64_fp_right_12887848))))), 0));
        goto label_0xC4A72C;
        label_0xC4A72C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        v0 = v8;
        __arm64_pair_address_12887864 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12887864)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12887864) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12887864) + (0x30UL)));
        return x0;
        label_0xC4A740:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetTwoFingerAngle` — RVA `0xc4a744`

- Lift status: **partial**; input span: 380 bytes; span to next metadata RVA: 380 bytes.
- Metadata signature: `private float GetTwoFingerAngle(float defaultAngle) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=36 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintm' at 0xc4a870

```csharp
public static ulong SuperTouchZone_GetTwoFingerAngle_RVAc4a744(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12887996 = default(float);
        float __arm64_float_flags_left_12888072 = default(float);
        float __arm64_float_flags_left_12888200 = default(float);
        float __arm64_float_flags_left_12888216 = default(float);
        float __arm64_float_flags_right_12887996 = default(float);
        float __arm64_float_flags_right_12888072 = default(float);
        float __arm64_float_flags_right_12888200 = default(float);
        float __arm64_float_flags_right_12888216 = default(float);
        float __arm64_fp_left_12888196 = default(float);
        float __arm64_fp_right_12888196 = default(float);
        ulong __arm64_pair_address_12887876 = default(ulong);
        ulong __arm64_pair_address_12887880 = default(ulong);
        ulong __arm64_pair_address_12887960 = default(ulong);
        ulong __arm64_pair_address_12887964 = default(ulong);
        ulong __arm64_pair_address_12888140 = default(ulong);
        ulong __arm64_pair_address_12888240 = default(ulong);
        ulong __arm64_pair_address_12888244 = default(ulong);
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
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12887876 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12887876, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12887876) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12887876;
        __arm64_pair_address_12887880 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12887880, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12887880) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A8A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4BB0CUL /* metadata target: SuperTouchZone.MultiFingerTouch.GetFinger */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A8A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4BB0CUL /* metadata target: SuperTouchZone.MultiFingerTouch.GetFinger */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4A8A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4A8BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC4A8BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A798UL);
        }
        __arm64_pair_address_12887960 = unchecked((ulong)((x8) + (0x44UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12887960)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12887960) + (0x4UL))))), 0));
        __arm64_pair_address_12887964 = unchecked((ulong)((x9) + (0x44UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12887964)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12887964) + (0x4UL))))), 0));
        x8 = 0x432000UL;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12887996 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12887996 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12887996 <= __arm64_float_flags_right_12887996))
        {
            goto label_0xC4A8A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A7E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4A7E4;
        label_0xC4A7E4:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A7FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A7F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4A7FC;
        label_0xC4A7FC:
        ;
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_12888072 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12888072 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12888072 <= __arm64_float_flags_right_12888072) || ((__arm64_float_flags_left_12888072 != __arm64_float_flags_left_12888072) || (__arm64_float_flags_right_12888072 != __arm64_float_flags_right_12888072))))
        {
            goto label_0xC4A81C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A810UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC4A850;
        label_0xC4A81C:
        ;
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4A83C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4A83C;
        label_0xC4A83C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12888140 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12888140)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12888140) + (0x4UL))))), 0));
        goto label_0xC4A850;
        label_0xC4A850:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5929CUL /* metadata target: CFUtils.VecToAngle */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x43B40000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFC3B40000UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        RuntimeCalls.Unsupported("frintm", 0xC4A870UL);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x43340000UL))));
        __arm64_fp_left_12888196 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12888196 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12888196 != __arm64_fp_left_12888196) ? __arm64_fp_left_12888196 : ((__arm64_fp_right_12888196 != __arm64_fp_right_12888196) ? __arm64_fp_right_12888196 : (((__arm64_fp_left_12888196 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12888196 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12888196), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12888196), 0))))), 0) : ((__arm64_fp_left_12888196 <= __arm64_fp_right_12888196) ? __arm64_fp_left_12888196 : __arm64_fp_right_12888196))))), 0));
        __arm64_float_flags_left_12888200 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12888200 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12888200 >= __arm64_float_flags_right_12888200) || ((__arm64_float_flags_left_12888200 != __arm64_float_flags_left_12888200) || (__arm64_float_flags_right_12888200 != __arm64_float_flags_right_12888200))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12888216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12888216 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12888216 > __arm64_float_flags_right_12888216) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        goto label_0xC4A8A4;
        label_0xC4A8A4:
        ;
        v0 = v8;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_12888240 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12888240)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12888240) + (0x8UL))))), 0));
        __arm64_pair_address_12888244 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12888244)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12888244) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12888244) + (0x40UL)));
        return x0;
        label_0xC4A8BC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.CancelTapsOnMultiFingersOtherThan` — RVA `0xc4a9a0`

- Lift status: **exact**; input span: 152 bytes; span to next metadata RVA: 152 bytes.
- Metadata signature: `private void CancelTapsOnMultiFingersOtherThan(int howManyFingers) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static ulong SuperTouchZone_CancelTapsOnMultiFingersOtherThan_RVAc4a9a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12888516 = default(uint);
        uint __arm64_flags_left_12888524 = default(uint);
        uint __arm64_flags_left_12888556 = default(uint);
        uint __arm64_flags_right_12888516 = default(uint);
        uint __arm64_flags_right_12888524 = default(uint);
        uint __arm64_flags_right_12888556 = default(uint);
        ulong sp = default(ulong);
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
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AA20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = x0;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x21 = 0x0UL;
        goto label_0xC4A9C0;
        label_0xC4A9C0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12888516 = unchecked((uint)(x21));
        __arm64_flags_right_12888516 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12888516) - (__arm64_flags_right_12888516))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12888516)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12888516)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12888516) - (__arm64_flags_right_12888516))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12888516)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4AA24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4A9CCUL);
        }
        __arm64_flags_left_12888524 = unchecked((uint)(x21));
        __arm64_flags_right_12888524 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12888524 >= __arm64_flags_right_12888524))
        {
            goto label_0xC4AA34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC4AA20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC4AA20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_12888556 = unchecked((uint)(x9));
        __arm64_flags_right_12888556 = unchecked((uint)(x20));
        if ((unchecked((uint)((__arm64_flags_left_12888556) - (__arm64_flags_right_12888556))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AA18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AA20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC624ECUL /* metadata target: TouchGestureState.CancelTap */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AA20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC624ECUL /* metadata target: TouchGestureState.CancelTap */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        goto label_0xC4AA18;
        label_0xC4AA18:
        ;
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4A9C0;
        }
        else
        {
            goto label_0xC4AA20;
        }
        label_0xC4AA20:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC4AA24;
        label_0xC4AA24:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4AA34:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.OnUpdateControl` — RVA `0xc4aa38`

- Lift status: **partial**; input span: 1572 bytes; span to next metadata RVA: 1572 bytes.
- Metadata signature: `protected override void OnUpdateControl() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=193 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc4ac00; reason: Unknown IR expression at 0xc4ac00; reason: Unsupported instruction 'b.pl' at 0xc4af1c; reason: Unknown IR expression at 0xc4af1c

```csharp
public static ulong SuperTouchZone_OnUpdateControl_RVAc4aa38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12888748 = default(uint);
        uint __arm64_flags_left_12888756 = default(uint);
        uint __arm64_flags_left_12888836 = default(uint);
        uint __arm64_flags_left_12888968 = default(uint);
        uint __arm64_flags_left_12889060 = default(uint);
        uint __arm64_flags_left_12889072 = default(uint);
        uint __arm64_flags_left_12889104 = default(uint);
        uint __arm64_flags_left_12889152 = default(uint);
        uint __arm64_flags_left_12889204 = default(uint);
        uint __arm64_flags_left_12889232 = default(uint);
        uint __arm64_flags_left_12889356 = default(uint);
        uint __arm64_flags_left_12889364 = default(uint);
        uint __arm64_flags_left_12889400 = default(uint);
        uint __arm64_flags_left_12889524 = default(uint);
        uint __arm64_flags_left_12889532 = default(uint);
        uint __arm64_flags_left_12889608 = default(uint);
        uint __arm64_flags_left_12889616 = default(uint);
        uint __arm64_flags_right_12888748 = default(uint);
        uint __arm64_flags_right_12888756 = default(uint);
        uint __arm64_flags_right_12888836 = default(uint);
        uint __arm64_flags_right_12888968 = default(uint);
        uint __arm64_flags_right_12889060 = default(uint);
        uint __arm64_flags_right_12889072 = default(uint);
        uint __arm64_flags_right_12889104 = default(uint);
        uint __arm64_flags_right_12889152 = default(uint);
        uint __arm64_flags_right_12889204 = default(uint);
        uint __arm64_flags_right_12889232 = default(uint);
        uint __arm64_flags_right_12889356 = default(uint);
        uint __arm64_flags_right_12889364 = default(uint);
        uint __arm64_flags_right_12889400 = default(uint);
        uint __arm64_flags_right_12889524 = default(uint);
        uint __arm64_flags_right_12889532 = default(uint);
        uint __arm64_flags_right_12889608 = default(uint);
        uint __arm64_flags_right_12889616 = default(uint);
        float __arm64_float_flags_left_12889272 = default(float);
        float __arm64_float_flags_left_12889864 = default(float);
        float __arm64_float_flags_left_12890048 = default(float);
        float __arm64_float_flags_left_12890092 = default(float);
        float __arm64_float_flags_right_12889272 = default(float);
        float __arm64_float_flags_right_12889864 = default(float);
        float __arm64_float_flags_right_12890048 = default(float);
        float __arm64_float_flags_right_12890092 = default(float);
        ulong __arm64_load_address_12890148 = default(ulong);
        ulong __arm64_load_address_12890180 = default(ulong);
        ulong __arm64_pair_address_12888636 = default(ulong);
        ulong __arm64_pair_address_12888640 = default(ulong);
        ulong __arm64_pair_address_12889408 = default(ulong);
        ulong __arm64_pair_address_12889412 = default(ulong);
        ulong __arm64_pair_address_12889760 = default(ulong);
        ulong __arm64_pair_address_12889820 = default(ulong);
        ulong __arm64_pair_address_12889852 = default(ulong);
        ulong __arm64_pair_address_12890128 = default(ulong);
        ulong __arm64_pair_address_12890132 = default(ulong);
        ulong __arm64_pair_address_12890172 = default(ulong);
        ulong __arm64_pair_address_12890176 = default(ulong);
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
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        __arm64_pair_address_12888636 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12888636, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12888636) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12888640 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12888640, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12888640) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x23AUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4AA78;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x23AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4AA78;
        label_0xC4AA78:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4DBACUL /* metadata target: SuperTouchZone.EmulatedFingerSystem.Update */, x0, x1, x2, x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0xD8UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x19) + (0xD8UL)))) + (0x8UL))), unchecked((uint)(x9)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x23 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4AAA8;
        label_0xC4AAA8:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12888748 = unchecked((uint)(x23));
        __arm64_flags_right_12888748 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12888748) - (__arm64_flags_right_12888748))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12888748)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12888748)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12888748) - (__arm64_flags_right_12888748))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12888748)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4AB4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AAB4UL);
        }
        __arm64_flags_left_12888756 = unchecked((uint)(x23));
        __arm64_flags_right_12888756 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12888756 >= __arm64_flags_right_12888756))
        {
            goto label_0xC4B04C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4B078UL /* metadata target: SuperTouchZone.FingerState.Update */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AB30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x24 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x24);
        x25 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0xD8UL))))))));
        x0 = x20;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4B050;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x24) + (0x18UL))))));
        __arm64_flags_left_12888836 = unchecked((uint)(x25));
        __arm64_flags_right_12888836 = unchecked((uint)(x8));
        if ((__arm64_flags_left_12888836 >= __arm64_flags_right_12888836))
        {
            goto label_0xC4B04C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x24) + (unchecked((ulong)((x25) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xD8UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            goto label_0xC4AB30;
        }
        label_0xC4AB30:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61C10UL /* metadata target: TouchGestureBasicState.JustReleasedRaw */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) | (unchecked((uint)(x0)))))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4AAA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AB48UL);
        }
        goto label_0xC4AE34;
        label_0xC4AB4C:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4A1F8UL /* metadata target: SuperTouchZone.GetAveragedFingerPos */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x4 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v8 = v0;
        v9 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC4A1F8UL /* metadata target: SuperTouchZone.GetAveragedFingerPos */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        v10 = v0;
        v11 = v1;
        __arm64_flags_left_12888968 = unchecked((uint)(x1));
        __arm64_flags_right_12888968 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12888968) - (__arm64_flags_right_12888968))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12888968)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12888968)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12888968) - (__arm64_flags_right_12888968))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12888968)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4ABCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4ABA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4ABA0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4ABA4;
        label_0xC4ABA4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ABC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BCB8UL /* metadata target: InputRig.WakeTouchControlsUp */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4ABC8;
        label_0xC4ABC8:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        goto label_0xC4ABCC;
        label_0xC4ABCC:
        ;
        if ((unchecked((uint)(x1)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4ABD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4ABD0UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xE0UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC4ABD8;
        label_0xC4ABD8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x98UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AC3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x90UL))))));
        __arm64_flags_left_12889060 = unchecked((uint)(x8));
        __arm64_flags_right_12889060 = unchecked((uint)0x1UL);
        if (((unchecked((uint)((__arm64_flags_left_12889060) - (__arm64_flags_right_12889060))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889060) - (__arm64_flags_right_12889060))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12889060)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12889060)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889060) - (__arm64_flags_right_12889060))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12889060)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC4AC3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        __arm64_flags_left_12889072 = unchecked((uint)(x1));
        __arm64_flags_right_12889072 = unchecked((uint)(x8));
        x9 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12889072) - (__arm64_flags_right_12889072))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & ((~(unchecked((uint)(x21)))))))));
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4AC90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AC00UL);
        }
        RuntimeCalls.Unsupported("cset", 0xC4AC00UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & ((~(unchecked((uint)(x21)))))))));
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4ACCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        __arm64_flags_left_12889104 = unchecked((uint)(x1));
        __arm64_flags_right_12889104 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_12889104) - (__arm64_flags_right_12889104))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889104) - (__arm64_flags_right_12889104))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12889104)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12889104)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889104) - (__arm64_flags_right_12889104))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12889104)) < unchecked((int)0x0UL)))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xE0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4ACF8;
        label_0xC4AC3C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xDCUL))))));
        __arm64_flags_left_12889152 = unchecked((uint)(x1));
        __arm64_flags_right_12889152 = unchecked((uint)(x8));
        if ((unchecked((uint)((__arm64_flags_left_12889152) - (__arm64_flags_right_12889152))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ACFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        x0 = x19;
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC4A348UL /* metadata target: SuperTouchZone.StartMultiFingerTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x19) + (0xD8UL)))) + (0x4UL))))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xE0UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        __arm64_flags_left_12889204 = unchecked((uint)(x1));
        __arm64_flags_right_12889204 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889204) - (__arm64_flags_right_12889204))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12889204)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12889204)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889204) - (__arm64_flags_right_12889204))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12889204)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4ACFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4ACFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AC88UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC4B0B0UL /* metadata target: SuperTouchZone.MultiFingerTouch.DisableTapUntilRelease */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4ACFC;
        label_0xC4AC90:
        ;
        __arm64_flags_left_12889232 = unchecked((uint)(x1));
        __arm64_flags_right_12889232 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889232) - (__arm64_flags_right_12889232))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12889232)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12889232)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889232) - (__arm64_flags_right_12889232))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12889232)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4ACFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE1UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ACFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4ACA0UL);
        }
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xE4UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x9CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        __arm64_float_flags_left_12889272 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12889272 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12889272 <= __arm64_float_flags_right_12889272) || ((__arm64_float_flags_left_12889272 != __arm64_float_flags_left_12889272) || (__arm64_float_flags_right_12889272 != __arm64_float_flags_right_12889272))))
        {
            goto label_0xC4ACFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0xE0UL))), unchecked((ushort)(unchecked((uint)(x8)))));
        goto label_0xC4ACFC;
        label_0xC4ACCC:
        ;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4ACDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xE1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC4ACDC;
        label_0xC4ACDC:
        ;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        v0 = v8;
        v1 = v9;
        v2 = v10;
        v3 = v11;
        goto label_0xC4ACF8;
        label_0xC4ACF8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC4A348UL /* metadata target: SuperTouchZone.StartMultiFingerTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4ACFC;
        label_0xC4ACFC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x0UL;
        goto label_0xC4AD08;
        label_0xC4AD08:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12889356 = unchecked((uint)(x21));
        __arm64_flags_right_12889356 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889356) - (__arm64_flags_right_12889356))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12889356)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12889356)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889356) - (__arm64_flags_right_12889356))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12889356)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4AD88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AD14UL);
        }
        __arm64_flags_left_12889364 = unchecked((uint)(x21));
        __arm64_flags_right_12889364 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12889364 >= __arm64_flags_right_12889364))
        {
            goto label_0xC4B04C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xD8UL))))));
        __arm64_flags_left_12889400 = unchecked((uint)(x9));
        __arm64_flags_right_12889400 = unchecked((uint)(x8));
        if ((!((unchecked((uint)((__arm64_flags_left_12889400) - (__arm64_flags_right_12889400))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC4AD48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AD40UL);
        }
        __arm64_pair_address_12889408 = unchecked((ulong)((x20) + (0x4CUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12889408, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12889408) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        __arm64_pair_address_12889412 = unchecked((ulong)((x20) + (0x54UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12889412, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12889412) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
        goto label_0xC4AD48;
        label_0xC4AD48:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4B0ECUL /* metadata target: SuperTouchZone.MultiFingerTouch.Update */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61BF0UL /* metadata target: TouchGestureBasicState.JustPressedRaw */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AD78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4A9A0UL /* metadata target: SuperTouchZone.CancelTapsOnMultiFingersOtherThan */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4AD78;
        label_0xC4AD78:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4AD08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AD84UL);
        }
        goto label_0xC4AE34;
        label_0xC4AD88:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4B7ECUL /* metadata target: SuperTouchZone.UpdateTwistAndPinch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ADF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC4ADB0;
        label_0xC4ADB0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12889524 = unchecked((uint)(x20));
        __arm64_flags_right_12889524 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889524) - (__arm64_flags_right_12889524))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12889524)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12889524)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889524) - (__arm64_flags_right_12889524))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12889524)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4ADF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4ADBCUL);
        }
        __arm64_flags_left_12889532 = unchecked((uint)(x20));
        __arm64_flags_right_12889532 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12889532 >= __arm64_flags_right_12889532))
        {
            goto label_0xC4B04C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x2 = unchecked((ulong)((x8) + (0x24UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3E94CUL /* metadata target: InputRig.SyncEmuTouch */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4ADB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4ADF4UL);
        }
        goto label_0xC4AE34;
        label_0xC4ADF8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC4AE04;
        label_0xC4AE04:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12889608 = unchecked((uint)(x20));
        __arm64_flags_right_12889608 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889608) - (__arm64_flags_right_12889608))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12889608)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12889608)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12889608) - (__arm64_flags_right_12889608))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12889608)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4AE38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AE10UL);
        }
        __arm64_flags_left_12889616 = unchecked((uint)(x20));
        __arm64_flags_right_12889616 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12889616 >= __arm64_flags_right_12889616))
        {
            goto label_0xC4B04C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AE24UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC4BAC8UL /* metadata target: SuperTouchZone.MultiFingerTouch.SyncToRig */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4AE04;
        }
        else
        {
            goto label_0xC4AE34;
        }
        label_0xC4AE34:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC4AE38;
        label_0xC4AE38:
        ;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x88UL))));
        if ((x21 == 0x0UL))
        {
            goto label_0xC4B02C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x158UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x118UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x114UL))))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x3 = 0x0UL;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(x9)))))));
        x0 = RuntimeCalls.InvokeDirect(0xC5E7E8UL /* metadata target: ScrollDeltaBinding.SyncScrollDelta */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x160UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x110UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10CUL))))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x3 = 0x0UL;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(x9)))))));
        x0 = RuntimeCalls.InvokeDirect(0xC5E7E8UL /* metadata target: ScrollDeltaBinding.SyncScrollDelta */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE8UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AF3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x168UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AECC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AEA0UL);
        }
        __arm64_pair_address_12889760 = unchecked((ulong)((x19) + (0xF0UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12889760)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12889760) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x94UL))))), 0));
        x1 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC574F8UL /* metadata target: AnalogConfig.GetAnalogVal */, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4AECC;
        label_0xC4AECC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x170UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AEFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AEDCUL);
        }
        __arm64_pair_address_12889820 = unchecked((ulong)((x19) + (0xF4UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12889820)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12889820) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x98UL))))), 0));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4AEFC;
        label_0xC4AEFC:
        ;
        __arm64_pair_address_12889852 = unchecked((ulong)((x19) + (0xF0UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12889852)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12889852) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x9CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12889864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12889864 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12889864 <= __arm64_float_flags_right_12889864) || ((__arm64_float_flags_left_12889864 != __arm64_float_flags_left_12889864) || (__arm64_float_flags_right_12889864 != __arm64_float_flags_right_12889864))))
        {
            goto label_0xC4AF1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x180UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC4AF28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AF18UL);
        }
        goto label_0xC4AE34;
        label_0xC4AF1C:
        ;
        RuntimeCalls.Unsupported("b.pl", 0xC4AF1CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4AF3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x178UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            goto label_0xC4AF28;
        }
        label_0xC4AF28:
        ;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4AF3C;
        label_0xC4AF3C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xEAUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4B02C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AF84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AF5CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x78UL))))), 0));
        x1 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC574F8UL /* metadata target: AnalogConfig.GetAnalogVal */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4AF84;
        label_0xC4AF84:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4AFB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4AF94UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x108UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x7CUL))))), 0));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4AFB8;
        label_0xC4AFB8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x80UL))))), 0));
        __arm64_float_flags_left_12890048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12890048 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12890048 <= __arm64_float_flags_right_12890048) || ((__arm64_float_flags_left_12890048 != __arm64_float_flags_left_12890048) || (__arm64_float_flags_right_12890048 != __arm64_float_flags_right_12890048))))
        {
            goto label_0xC4AFEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x21) + (0x80UL))))), 0));
        goto label_0xC4AFEC;
        label_0xC4AFEC:
        ;
        __arm64_float_flags_left_12890092 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12890092 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12890092 >= __arm64_float_flags_right_12890092) || ((__arm64_float_flags_left_12890092 != __arm64_float_flags_left_12890092) || (__arm64_float_flags_right_12890092 != __arm64_float_flags_right_12890092))))
        {
            goto label_0xC4B02C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x150UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4AE34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_12890128 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12890128)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12890128) + (0x8UL))))), 0));
        __arm64_pair_address_12890132 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12890132)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12890132) + (0x8UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        __arm64_load_address_12890148 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12890148)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12890148) + (0x70UL)));
        return RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */);
        label_0xC4B02C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        __arm64_pair_address_12890172 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12890172)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12890172) + (0x8UL))))), 0));
        __arm64_pair_address_12890176 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12890176)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12890176) + (0x8UL))))), 0));
        __arm64_load_address_12890180 = sp;
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12890180)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12890180) + (0x70UL)));
        return x0;
        label_0xC4B04C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4B050;
        label_0xC4B050:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `SuperTouchZone.UpdateEmulatedFingers` — RVA `0xc4b05c`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `private void UpdateEmulatedFingers() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong SuperTouchZone_UpdateEmulatedFingers_RVAc4b05c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4B074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4DBACUL /* metadata target: SuperTouchZone.EmulatedFingerSystem.Update */);
        label_0xC4B074:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.UpdateTwistAndPinch` — RVA `0xc4b7ec`

- Lift status: **partial**; input span: 732 bytes; span to next metadata RVA: 732 bytes.
- Metadata signature: `private void UpdateTwistAndPinch(bool lastUpdateMode) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=69 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fabd' at 0xc4b8b0; reason: Unsupported instruction 'cset' at 0xc4ba0c; reason: Unknown IR expression at 0xc4ba0c; reason: Unsupported instruction 'cset' at 0xc4ba40; reason: Unknown IR expression at 0xc4ba40

```csharp
public static ulong SuperTouchZone_UpdateTwistAndPinch_RVAc4b7ec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12892532 = default(uint);
        uint __arm64_flags_left_12892576 = default(uint);
        uint __arm64_flags_left_12892584 = default(uint);
        uint __arm64_flags_left_12892620 = default(uint);
        uint __arm64_flags_left_12892628 = default(uint);
        uint __arm64_flags_left_12892668 = default(uint);
        uint __arm64_flags_left_12892676 = default(uint);
        uint __arm64_flags_left_12892720 = default(uint);
        uint __arm64_flags_left_12892728 = default(uint);
        uint __arm64_flags_left_12892748 = default(uint);
        uint __arm64_flags_right_12892532 = default(uint);
        uint __arm64_flags_right_12892576 = default(uint);
        uint __arm64_flags_right_12892584 = default(uint);
        uint __arm64_flags_right_12892620 = default(uint);
        uint __arm64_flags_right_12892628 = default(uint);
        uint __arm64_flags_right_12892668 = default(uint);
        uint __arm64_flags_right_12892676 = default(uint);
        uint __arm64_flags_right_12892720 = default(uint);
        uint __arm64_flags_right_12892728 = default(uint);
        uint __arm64_flags_right_12892748 = default(uint);
        float __arm64_float_flags_left_12892340 = default(float);
        float __arm64_float_flags_left_12892436 = default(float);
        float __arm64_float_flags_left_12892452 = default(float);
        float __arm64_float_flags_right_12892340 = default(float);
        float __arm64_float_flags_right_12892436 = default(float);
        float __arm64_float_flags_right_12892452 = default(float);
        ulong __arm64_pair_address_12892260 = default(ulong);
        ulong __arm64_pair_address_12892472 = default(ulong);
        ulong __arm64_pair_address_12892512 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4BAB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B800UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xF4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x104UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x110UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x118UL))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x88UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x19 = x0;
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xE9UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0xF8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x108UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x10CUL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x114UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0xEBUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BAB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61BF0UL /* metadata target: TouchGestureBasicState.JustPressedRaw */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4B87C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B854UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xECUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xFCUL))))), 0));
        x8 = unchecked((ulong)((x19) + (0x104UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_12892260 = unchecked((ulong)((x19) + (0xF0UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12892260, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12892260) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xF8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x100UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x8) + (0x8UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x8) + (0x8UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(x8, 0x0UL);
        goto label_0xC4BAB0;
        label_0xC4B87C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1CUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4B8F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x121UL))))))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4A680UL /* metadata target: SuperTouchZone.GetTwoFingerDist */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE8UL))))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xF4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4B8C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B8A4UL);
        }
        if ((x24 == 0x0UL))
        {
            goto label_0xC4BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B8A8UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xF0UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x90UL))))), 0));
        RuntimeCalls.Unsupported("fabd", 0xC4B8B0UL);
        __arm64_float_flags_left_12892340 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12892340 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12892340 <= __arm64_float_flags_right_12892340) || ((__arm64_float_flags_left_12892340 != __arm64_float_flags_left_12892340) || (__arm64_float_flags_right_12892340 != __arm64_float_flags_right_12892340))))
        {
            goto label_0xC4B8C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC4B8C8;
        label_0xC4B8C4:
        ;
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4B8C8;
        label_0xC4B8C8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4A744UL /* metadata target: SuperTouchZone.GetTwoFingerAngle */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x100UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xEAUL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x104UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4B908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B8E8UL);
        }
        if ((x24 != 0x0UL))
        {
            goto label_0xC4B934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B8ECUL);
        }
        goto label_0xC4BAC4;
        label_0xC4B8F0:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xF4UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xE8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xF0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x100UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        goto label_0xC4BAB0;
        label_0xC4B908:
        ;
        if ((x24 == 0x0UL))
        {
            goto label_0xC4BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B90CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xF4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0xA4UL))))), 0));
        __arm64_float_flags_left_12892436 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12892436 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12892436 <= __arm64_float_flags_right_12892436) || ((__arm64_float_flags_left_12892436 != __arm64_float_flags_left_12892436) || (__arm64_float_flags_right_12892436 != __arm64_float_flags_right_12892436))))
        {
            goto label_0xC4B934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B91CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x74UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12892452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12892452 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12892452 <= __arm64_float_flags_right_12892452) || ((__arm64_float_flags_left_12892452 != __arm64_float_flags_left_12892452) || (__arm64_float_flags_right_12892452 != __arm64_float_flags_right_12892452))))
        {
            goto label_0xC4B934;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC4B938;
        label_0xC4B934:
        ;
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4B938;
        label_0xC4B938:
        ;
        __arm64_pair_address_12892472 = unchecked((ulong)((x19) + (0xF0UL)));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12892472)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12892472) + (0x4UL))))), 0));
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x118UL))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0xA0UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x24) + (0x6CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58578UL /* metadata target: CFUtils.GetScrollValue */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x118UL))), unchecked((uint)(x0)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x104UL))))), 0));
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x110UL))))));
        __arm64_pair_address_12892512 = unchecked((ulong)((x24) + (0x84UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12892512)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12892512) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58578UL /* metadata target: CFUtils.GetScrollValue */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x19) + (0xB0UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x110UL))), unchecked((uint)(x0)));
        __arm64_flags_left_12892532 = unchecked((uint)(x8));
        __arm64_flags_right_12892532 = unchecked((uint)0x5UL);
        if (((__arm64_flags_left_12892532 >= __arm64_flags_right_12892532) && (!((unchecked((uint)((__arm64_flags_left_12892532) - (__arm64_flags_right_12892532))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC4B98C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x452000UL;
        x9 = unchecked((ulong)((x9) + (0x108UL)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (x8))))));
        goto label_0xC4B990;
        label_0xC4B98C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4B990;
        label_0xC4B990:
        ;
        x9 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x10 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4B998;
        label_0xC4B998:
        ;
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) >> (int)(unchecked((int)(unchecked((uint)(x9)))))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) & (unchecked((uint)(0x7UL)))))));
        __arm64_flags_left_12892576 = unchecked((uint)(x11));
        __arm64_flags_right_12892576 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12892576) - (__arm64_flags_right_12892576))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4B9E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B9A8UL);
        }
        __arm64_flags_left_12892584 = unchecked((uint)(x11));
        __arm64_flags_right_12892584 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12892584) - (__arm64_flags_right_12892584))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4B9B0UL);
        }
        if ((unchecked((uint)(x11)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xEAUL))))))));
        x12 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)(0x1UL)))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) | (unchecked((uint)(x12)))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA6UL))))))));
        x12 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA2UL))))))));
        __arm64_flags_left_12892620 = unchecked((uint)(x11));
        __arm64_flags_right_12892620 = unchecked((uint)0x0UL);
        x11 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12892620) - (__arm64_flags_right_12892620))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12892628 = unchecked((uint)(x12));
        __arm64_flags_right_12892628 = unchecked((uint)0x0UL);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) | (unchecked((uint)(x11)))))));
        goto label_0xC4BA0C;
        label_0xC4B9E0:
        ;
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC4BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x11) + (0x120UL))))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) | (unchecked((uint)(x22)))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA3UL))))))));
        x12 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA1UL))))))));
        __arm64_flags_left_12892668 = unchecked((uint)(x11));
        __arm64_flags_right_12892668 = unchecked((uint)0x0UL);
        x11 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12892668) - (__arm64_flags_right_12892668))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12892676 = unchecked((uint)(x12));
        __arm64_flags_right_12892676 = unchecked((uint)0x0UL);
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)(x11)))))));
        goto label_0xC4BA0C;
        label_0xC4BA0C:
        ;
        RuntimeCalls.Unsupported("cset", 0xC4BA0CUL);
        x11 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)(x11)))))));
        goto label_0xC4BA48;
        label_0xC4BA18:
        ;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xE8UL))))))));
        x12 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)(0x1UL)))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) | (unchecked((uint)(x12)))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA5UL))))))));
        x12 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA4UL))))))));
        __arm64_flags_left_12892720 = unchecked((uint)(x11));
        __arm64_flags_right_12892720 = unchecked((uint)0x0UL);
        x11 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12892720) - (__arm64_flags_right_12892720))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12892728 = unchecked((uint)(x12));
        __arm64_flags_right_12892728 = unchecked((uint)0x0UL);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) | (unchecked((uint)(x11)))))));
        RuntimeCalls.Unsupported("cset", 0xC4BA40UL);
        x11 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)(x11)))))));
        goto label_0xC4BA48;
        label_0xC4BA48:
        ;
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x3UL)))))));
        __arm64_flags_left_12892748 = unchecked((uint)(x9));
        __arm64_flags_right_12892748 = unchecked((uint)0x9UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12892748) - (__arm64_flags_right_12892748))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC4B998;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4BA54UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC624C8UL /* metadata target: TouchGestureState.BlockSwipe */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BAC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC624C8UL /* metadata target: TouchGestureState.BlockSwipe */, x0, x1, x2, x3);
        goto label_0xC4BA88;
        label_0xC4BA7C:
        ;
        if ((unchecked((uint)(x22)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4BB44UL /* metadata target: SuperTouchZone.OnTwoFingerDragStart */, x0, x1, x2, x3);
        goto label_0xC4BA88;
        label_0xC4BA88:
        ;
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BA94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4BBC0UL /* metadata target: SuperTouchZone.OnPinchStart */, x0, x1, x2, x3);
        goto label_0xC4BA94;
        label_0xC4BA94:
        ;
        if ((unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BAB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4BC04UL /* metadata target: SuperTouchZone.OnTwistStart */);
        label_0xC4BAB0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4BAC4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.UpdateTwistAndPinch` — RVA `0xc4bb3c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private void UpdateTwistAndPinch() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SuperTouchZone_UpdateTwistAndPinch_RVAc4bb3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return RuntimeCalls.InvokeDirect(0xC4B7ECUL /* metadata target: SuperTouchZone.UpdateTwistAndPinch */);
        return default(ulong);
    }
```

## `SuperTouchZone.OnTwoFingerDragStart` — RVA `0xc4bb44`

- Lift status: **exact**; input span: 124 bytes; span to next metadata RVA: 124 bytes.
- Metadata signature: `private void OnTwoFingerDragStart() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong SuperTouchZone_OnTwoFingerDragStart_RVAc4bb44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC49B80UL /* metadata target: SuperTouchZone.GetMultiFingerTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BB70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BBBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BB7C;
        }
        else
        {
            goto label_0xC4BB70;
        }
        label_0xC4BB70:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4BB7C:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC62498UL /* metadata target: TouchGestureState.ForceSwipe */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BBBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC62498UL /* metadata target: TouchGestureState.ForceSwipe */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xABUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BBA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4BC04UL /* metadata target: SuperTouchZone.OnTwistStart */, x0, x1, x2, x3);
        goto label_0xC4BBA4;
        label_0xC4BBA4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA8UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BB70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4BBC0UL /* metadata target: SuperTouchZone.OnPinchStart */);
        label_0xC4BBBC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.OnPinchStart` — RVA `0xc4bbc0`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `private void OnPinchStart() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong SuperTouchZone_OnPinchStart_RVAc4bbc0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xE8UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BBD4;
        }
        else
        {
            goto label_0xC4BBCC;
        }
        label_0xC4BBCC:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4BBD4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xA9UL))))))));
        x19 = x0;
        x9 = unchecked((ulong)(unchecked((uint)(0x101UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0xE8UL))), unchecked((ushort)(unchecked((uint)(x9)))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BBF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4BB44UL /* metadata target: SuperTouchZone.OnTwoFingerDragStart */, x0, x1, x2, x3);
        goto label_0xC4BBF0;
        label_0xC4BBF0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xACUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BBCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4BC04UL /* metadata target: SuperTouchZone.OnTwistStart */);
        return default(ulong);
    }
```

## `SuperTouchZone.OnTwistStart` — RVA `0xc4bc04`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `private void OnTwistStart() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong SuperTouchZone_OnTwistStart_RVAc4bc04(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xEAUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BC18;
        }
        else
        {
            goto label_0xC4BC10;
        }
        label_0xC4BC10:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4BC18:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xAAUL))))))));
        x19 = x0;
        x9 = unchecked((ulong)(unchecked((uint)(0x101UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0xEAUL))), unchecked((ushort)(unchecked((uint)(x9)))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BC34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4BB44UL /* metadata target: SuperTouchZone.OnTwoFingerDragStart */, x0, x1, x2, x3);
        goto label_0xC4BC34;
        label_0xC4BC34:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA7UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BC10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4BBC0UL /* metadata target: SuperTouchZone.OnPinchStart */);
        return default(ulong);
    }
```

## `SuperTouchZone.GetFirstUnusedFinger` — RVA `0xc4bc48`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `private SuperTouchZone.FingerState GetFirstUnusedFinger(TouchObject newTouchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong SuperTouchZone_GetFirstUnusedFinger_RVAc4bc48(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12893292 = default(uint);
        uint __arm64_flags_left_12893300 = default(uint);
        uint __arm64_flags_left_12893312 = default(uint);
        uint __arm64_flags_left_12893344 = default(uint);
        uint __arm64_flags_right_12893292 = default(uint);
        uint __arm64_flags_right_12893300 = default(uint);
        uint __arm64_flags_right_12893312 = default(uint);
        uint __arm64_flags_right_12893344 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x98UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BC5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xE0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4BCA8;
        }
        else
        {
            goto label_0xC4BC5C;
        }
        label_0xC4BC5C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4BCB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x90UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12893292 = unchecked((uint)(x10));
        __arm64_flags_right_12893292 = unchecked((uint)(x9));
        x10 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893292) - (__arm64_flags_right_12893292))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12893292)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12893292)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893292) - (__arm64_flags_right_12893292))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12893292)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x10)) : unchecked((uint)(x9)))));
        __arm64_flags_left_12893300 = unchecked((uint)(x10));
        __arm64_flags_right_12893300 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893300) - (__arm64_flags_right_12893300))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12893300)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12893300)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893300) - (__arm64_flags_right_12893300))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12893300)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4BCA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4BC80;
        label_0xC4BC80:
        ;
        __arm64_flags_left_12893312 = unchecked((uint)(x9));
        __arm64_flags_right_12893312 = unchecked((uint)(x11));
        if ((unchecked((uint)((__arm64_flags_left_12893312) - (__arm64_flags_right_12893312))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BCB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x12) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BCB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x12 == 0x0UL))
        {
            goto label_0xC4BCAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12893344 = unchecked((uint)(x10));
        __arm64_flags_right_12893344 = unchecked((uint)(x11));
        if ((!((unchecked((uint)((__arm64_flags_left_12893344) - (__arm64_flags_right_12893344))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC4BC80;
        }
        else
        {
            goto label_0xC4BCA8;
        }
        label_0xC4BCA8:
        ;
        x0 = 0x0UL;
        goto label_0xC4BCAC;
        label_0xC4BCAC:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4BCB4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC4BCB8;
        label_0xC4BCB8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.GetFingerByTouch` — RVA `0xc4bcbc`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `private SuperTouchZone.FingerState GetFingerByTouch(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong SuperTouchZone_GetFingerByTouch_RVAc4bcbc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12893392 = default(uint);
        uint __arm64_flags_left_12893404 = default(uint);
        ulong __arm64_flags_left_12893428 = default(ulong);
        uint __arm64_flags_left_12893440 = default(uint);
        uint __arm64_flags_right_12893392 = default(uint);
        uint __arm64_flags_right_12893404 = default(uint);
        ulong __arm64_flags_right_12893428 = default(ulong);
        uint __arm64_flags_right_12893440 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        if ((x1 == 0x0UL))
        {
            goto label_0xC4BD08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4BD18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12893392 = unchecked((uint)(x9));
        __arm64_flags_right_12893392 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893392) - (__arm64_flags_right_12893392))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12893392)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12893392)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893392) - (__arm64_flags_right_12893392))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12893392)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4BD08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4BCDC;
        label_0xC4BCDC:
        ;
        __arm64_flags_left_12893404 = unchecked((uint)(x10));
        __arm64_flags_right_12893404 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12893404 >= __arm64_flags_right_12893404))
        {
            goto label_0xC4BD14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BD18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        __arm64_flags_left_12893428 = x1;
        __arm64_flags_right_12893428 = x11;
        if ((unchecked((ulong)((__arm64_flags_left_12893428) - (__arm64_flags_right_12893428))) == 0x0UL))
        {
            goto label_0xC4BD0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12893440 = unchecked((uint)(x10));
        __arm64_flags_right_12893440 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893440) - (__arm64_flags_right_12893440))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12893440)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12893440)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12893440) - (__arm64_flags_right_12893440))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12893440)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4BCDC;
        }
        else
        {
            goto label_0xC4BD08;
        }
        label_0xC4BD08:
        ;
        x0 = 0x0UL;
        goto label_0xC4BD0C;
        label_0xC4BD0C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4BD14:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC4BD18;
        label_0xC4BD18:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.CanBeActivatedByOtherControl` — RVA `0xc4bd1c`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public override bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint SuperTouchZone_CanBeActivatedByOtherControl_RVAc4bd1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12893496 = default(ulong);
        ulong __arm64_flags_right_12893496 = default(ulong);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x3 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4F7F8UL /* metadata target: TouchControl.CanBeActivatedByOtherControl */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC4BD44:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        else
        {
            x0 = x19;
            x0 = RuntimeCalls.InvokeDirect(0xC4BC48UL /* metadata target: SuperTouchZone.GetFirstUnusedFinger */, x0, x1, x2, x3);
            __arm64_flags_left_12893496 = x0;
            __arm64_flags_right_12893496 = 0x0UL;
            x0 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12893496) - (__arm64_flags_right_12893496))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        label_0xC4BD48:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.CanBeTouchedDirectly` — RVA `0xc4bd50`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public override bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint SuperTouchZone_CanBeTouchedDirectly_RVAc4bd50(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12893548 = default(ulong);
        ulong __arm64_flags_right_12893548 = default(ulong);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4F7D8UL /* metadata target: TouchControl.CanBeTouchedDirectly */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC4BD78:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        else
        {
            x0 = x19;
            x0 = RuntimeCalls.InvokeDirect(0xC4BC48UL /* metadata target: SuperTouchZone.GetFirstUnusedFinger */, x0, x1, x2, x3);
            __arm64_flags_left_12893548 = x0;
            __arm64_flags_right_12893548 = 0x0UL;
            x0 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12893548) - (__arm64_flags_right_12893548))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        label_0xC4BD7C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.CanBeSwipedOverFromNothing` — RVA `0xc4bd84`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public override bool CanBeSwipedOverFromNothing(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint SuperTouchZone_CanBeSwipedOverFromNothing_RVAc4bd84(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12893600 = default(ulong);
        ulong __arm64_flags_right_12893600 = default(ulong);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4F770UL /* metadata target: TouchControl.CanBeSwipedOverFromNothingDefault */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC4BDAC:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        else
        {
            x0 = x19;
            x0 = RuntimeCalls.InvokeDirect(0xC4BC48UL /* metadata target: SuperTouchZone.GetFirstUnusedFinger */, x0, x1, x2, x3);
            __arm64_flags_left_12893600 = x0;
            __arm64_flags_right_12893600 = 0x0UL;
            x0 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12893600) - (__arm64_flags_right_12893600))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        label_0xC4BDB0:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.CanBeSwipedOverFromRestrictedList` — RVA `0xc4bdb8`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public override bool CanBeSwipedOverFromRestrictedList(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint SuperTouchZone_CanBeSwipedOverFromRestrictedList_RVAc4bdb8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12893652 = default(ulong);
        ulong __arm64_flags_right_12893652 = default(ulong);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x2 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4F790UL /* metadata target: TouchControl.CanBeSwipedOverFromRestrictedListDefault */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC4BDE0:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        else
        {
            x0 = x19;
            x0 = RuntimeCalls.InvokeDirect(0xC4BC48UL /* metadata target: SuperTouchZone.GetFirstUnusedFinger */, x0, x1, x2, x3);
            __arm64_flags_left_12893652 = x0;
            __arm64_flags_right_12893652 = 0x0UL;
            x0 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12893652) - (__arm64_flags_right_12893652))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        label_0xC4BDE4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.CanSwipeOverOthers` — RVA `0xc4bdec`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public override bool CanSwipeOverOthers(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static uint SuperTouchZone_CanSwipeOverOthers_RVAc4bdec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x28UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BE2C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = x0;
        x19 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xC4BCBCUL /* metadata target: SuperTouchZone.GetFingerByTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BE2C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x3 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x20UL))))));
        x0 = x20;
        x1 = x19;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x4 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F7A0UL /* metadata target: TouchControl.CanSwipeOverOthersDefault */)));
        label_0xC4BE2C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `SuperTouchZone.OnTouchStart` — RVA `0xc4be3c`

- Lift status: **exact**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public override bool OnTouchStart(TouchObject touch, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static uint SuperTouchZone_OnTouchStart_RVAc4be3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BEC0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)(x3))));
        x23 = x2;
        x19 = x0;
        x20 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xC4BC48UL /* metadata target: SuperTouchZone.GetFirstUnusedFinger */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BEC4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4BED4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x23;
        x3 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC4D4D0UL /* metadata target: SuperTouchZone.EmulatedFingerSystem.OnSystemTouchStart */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4BEB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x22;
        x1 = x20;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC4BED8UL /* metadata target: SuperTouchZone.FingerState.OnTouchStart */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4BEC0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4BEA4UL)));
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC4BED4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4D6E4UL /* metadata target: TouchObject.AddControl */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4BEB8;
        label_0xC4BEB8:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC4BEC4;
        label_0xC4BEC0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4BEC4;
        label_0xC4BEC4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4BED4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(uint);
    }
```

## `SuperTouchZone.OnTouchEnd` — RVA `0xc4bff0`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `public override bool OnTouchEnd(TouchObject touch, TouchControl.TouchEndType touchEndType) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=21 (informational only).

```csharp
public static uint SuperTouchZone_OnTouchEnd_RVAc4bff0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12894292 = default(uint);
        uint __arm64_flags_left_12894304 = default(uint);
        uint __arm64_flags_right_12894292 = default(uint);
        uint __arm64_flags_right_12894304 = default(uint);
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C02C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C090;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x3 = 0x0UL;
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x21 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xC4D920UL /* metadata target: SuperTouchZone.EmulatedFingerSystem.OnSystemTouchEnd */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C044;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC4C030;
        label_0xC4C02C:
        ;
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4C030;
        label_0xC4C030:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x22))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4C044:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C090;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x23 = 0x0UL;
        goto label_0xC4C050;
        label_0xC4C050:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12894292 = unchecked((uint)(x23));
        __arm64_flags_right_12894292 = unchecked((uint)(x9));
        x22 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894292) - (__arm64_flags_right_12894292))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12894292)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12894292)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894292) - (__arm64_flags_right_12894292))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12894292)) < unchecked((int)0x0UL))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894292) - (__arm64_flags_right_12894292))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12894292)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12894292)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894292) - (__arm64_flags_right_12894292))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12894292)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C030;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C060UL)));
        }
        __arm64_flags_left_12894304 = unchecked((uint)(x23));
        __arm64_flags_right_12894304 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12894304 >= __arm64_flags_right_12894304))
        {
            goto label_0xC4C094;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C090;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x21;
        x2 = unchecked((ulong)(unchecked((uint)(x19))));
        x0 = RuntimeCalls.InvokeDirect(0xC4C098UL /* metadata target: SuperTouchZone.FingerState.OnTouchEnd */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C030;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC8UL))));
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4C050;
        }
        else
        {
            goto label_0xC4C090;
        }
        label_0xC4C090:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4C094;
        label_0xC4C094:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `SuperTouchZone.OnTouchMove` — RVA `0xc4c150`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `public override bool OnTouchMove(TouchObject touch) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static uint SuperTouchZone_OnTouchMove_RVAc4c150(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12894640 = default(uint);
        uint __arm64_flags_left_12894652 = default(uint);
        uint __arm64_flags_right_12894640 = default(uint);
        uint __arm64_flags_right_12894652 = default(uint);
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C188;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C1E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = 0x0UL;
        x20 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xC4D97CUL /* metadata target: SuperTouchZone.EmulatedFingerSystem.OnSystemTouchMove */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C1A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC4C18C;
        label_0xC4C188:
        ;
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4C18C;
        label_0xC4C18C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC4C1A0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C1E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x0UL;
        goto label_0xC4C1AC;
        label_0xC4C1AC:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12894640 = unchecked((uint)(x22));
        __arm64_flags_right_12894640 = unchecked((uint)(x9));
        x21 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894640) - (__arm64_flags_right_12894640))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12894640)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12894640)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894640) - (__arm64_flags_right_12894640))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12894640)) < unchecked((int)0x0UL))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894640) - (__arm64_flags_right_12894640))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12894640)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12894640)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894640) - (__arm64_flags_right_12894640))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12894640)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C18C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C1BCUL)));
        }
        __arm64_flags_left_12894652 = unchecked((uint)(x22));
        __arm64_flags_right_12894652 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12894652 >= __arm64_flags_right_12894652))
        {
            goto label_0xC4C1EC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x22) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C1E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4C1F0UL /* metadata target: SuperTouchZone.FingerState.OnTouchMove */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C18C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x22 = unchecked((ulong)((x22) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4C1AC;
        }
        else
        {
            goto label_0xC4C1E8;
        }
        label_0xC4C1E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC4C1EC;
        label_0xC4C1EC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.OnTouchPressureChange` — RVA `0xc4c28c`

- Lift status: **partial**; input span: 120 bytes; span to next metadata RVA: 120 bytes.
- Metadata signature: `public override bool OnTouchPressureChange(TouchObject touch) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=13 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc4c2f4; reason: Unknown IR expression at 0xc4c2f4

```csharp
public static uint SuperTouchZone_OnTouchPressureChange_RVAc4c28c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12894896 = default(uint);
        uint __arm64_flags_left_12894904 = default(uint);
        uint __arm64_flags_left_12894952 = default(uint);
        uint __arm64_flags_right_12894896 = default(uint);
        uint __arm64_flags_right_12894904 = default(uint);
        uint __arm64_flags_right_12894952 = default(uint);
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
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C2E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = x0;
        x20 = x1;
        x21 = 0x0UL;
        goto label_0xC4C2AC;
        label_0xC4C2AC:
        ;
        x22 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12894896 = unchecked((uint)(x21));
        __arm64_flags_right_12894896 = unchecked((uint)(x22));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894896) - (__arm64_flags_right_12894896))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12894896)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12894896)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12894896) - (__arm64_flags_right_12894896))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12894896)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C2E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C2B8UL)));
        }
        __arm64_flags_left_12894904 = unchecked((uint)(x21));
        __arm64_flags_right_12894904 = unchecked((uint)(x22));
        if ((__arm64_flags_left_12894904 >= __arm64_flags_right_12894904))
        {
            goto label_0xC4C300;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C2E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4C304UL /* metadata target: SuperTouchZone.FingerState.OnTouchPressureChange */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C2E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4C2AC;
        }
        else
        {
            goto label_0xC4C2E4;
        }
        label_0xC4C2E4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC4C2E8;
        label_0xC4C2E8:
        ;
        __arm64_flags_left_12894952 = unchecked((uint)(x21));
        __arm64_flags_right_12894952 = unchecked((uint)(x22));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeCalls.Unsupported("cset", 0xC4C2F4UL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC4C300:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.ReleaseAllTouches` — RVA `0xc4c374`

- Lift status: **exact**; input span: 248 bytes; span to next metadata RVA: 248 bytes.
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static ulong SuperTouchZone_ReleaseAllTouches_RVAc4c374(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12895128 = default(uint);
        uint __arm64_flags_left_12895136 = default(uint);
        uint __arm64_flags_left_12895200 = default(uint);
        uint __arm64_flags_left_12895208 = default(uint);
        uint __arm64_flags_left_12895244 = default(uint);
        uint __arm64_flags_right_12895128 = default(uint);
        uint __arm64_flags_right_12895136 = default(uint);
        uint __arm64_flags_right_12895200 = default(uint);
        uint __arm64_flags_right_12895208 = default(uint);
        uint __arm64_flags_right_12895244 = default(uint);
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C458;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        x19 = x0;
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC4C394;
        label_0xC4C394:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12895128 = unchecked((uint)(x20));
        __arm64_flags_right_12895128 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895128) - (__arm64_flags_right_12895128))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12895128)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12895128)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895128) - (__arm64_flags_right_12895128))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12895128)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C3CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4C3A0UL);
        }
        __arm64_flags_left_12895136 = unchecked((uint)(x20));
        __arm64_flags_right_12895136 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12895136 >= __arm64_flags_right_12895136))
        {
            goto label_0xC4C468;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC4C46CUL /* metadata target: SuperTouchZone.FingerState.ReleaseTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4C394;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4C3C8UL);
        }
        goto label_0xC4C464;
        label_0xC4C3CC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        goto label_0xC4C3D8;
        label_0xC4C3D8:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) - (unchecked((uint)(0x4UL)))))));
        __arm64_flags_left_12895200 = unchecked((uint)(x21));
        __arm64_flags_right_12895200 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895200) - (__arm64_flags_right_12895200))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12895200)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12895200)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895200) - (__arm64_flags_right_12895200))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12895200)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C440;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4C3E8UL);
        }
        __arm64_flags_left_12895208 = unchecked((uint)(x21));
        __arm64_flags_right_12895208 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12895208 >= __arm64_flags_right_12895208))
        {
            goto label_0xC4C468;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x20))))))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC4A8C0UL /* metadata target: SuperTouchZone.MultiFingerTouch.End */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12895244 = unchecked((uint)(x21));
        __arm64_flags_right_12895244 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12895244 >= __arm64_flags_right_12895244))
        {
            goto label_0xC4C468;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)(x20))))))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4D3BCUL /* metadata target: TouchObject.End */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4C3D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4C43CUL);
        }
        goto label_0xC4C464;
        label_0xC4C440:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4D23CUL /* metadata target: SuperTouchZone.EmulatedFingerSystem.EndMouseAndTouches */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xD8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC4C458;
        label_0xC4C458:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4C464:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4C468;
        label_0xC4C468:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.OnIsBoundToAxis` — RVA `0xc4c500`

- Lift status: **exact**; input span: 444 bytes; span to next metadata RVA: 444 bytes.
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=63 (informational only).

```csharp
public static uint SuperTouchZone_OnIsBoundToAxis_RVAc4c500(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12895516 = default(uint);
        uint __arm64_flags_left_12895544 = default(uint);
        uint __arm64_flags_left_12895600 = default(uint);
        uint __arm64_flags_left_12895608 = default(uint);
        uint __arm64_flags_right_12895516 = default(uint);
        uint __arm64_flags_right_12895544 = default(uint);
        uint __arm64_flags_right_12895600 = default(uint);
        uint __arm64_flags_right_12895608 = default(uint);
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x90UL))))));
        x19 = x2;
        x21 = x0;
        x20 = x1;
        __arm64_flags_left_12895516 = unchecked((uint)(x8));
        __arm64_flags_right_12895516 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895516) - (__arm64_flags_right_12895516))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12895516)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12895516)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895516) - (__arm64_flags_right_12895516))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12895516)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C580;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC4C52C;
        label_0xC4C52C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12895544 = unchecked((uint)(x22));
        __arm64_flags_right_12895544 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12895544 >= __arm64_flags_right_12895544))
        {
            goto label_0xC4C6B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x22) << (int)(unchecked((int)(0x3UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x90UL))))));
        x22 = unchecked((ulong)((x22) + (0x1UL)));
        __arm64_flags_left_12895600 = unchecked((uint)(x8));
        __arm64_flags_right_12895600 = unchecked((uint)0x3UL);
        x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895600) - (__arm64_flags_right_12895600))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12895600)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12895600)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895600) - (__arm64_flags_right_12895600))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12895600)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)(x23)))));
        __arm64_flags_left_12895608 = unchecked((uint)(x22));
        __arm64_flags_right_12895608 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895608) - (__arm64_flags_right_12895608))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12895608)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12895608)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895608) - (__arm64_flags_right_12895608))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12895608)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C52C;
        }
        else
        {
            goto label_0xC4C580;
        }
        label_0xC4C580:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x138UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x140UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x150UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x148UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x168UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x170UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x178UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x180UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C67C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x158UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C690;
        }
        else
        {
            goto label_0xC4C67C;
        }
        label_0xC4C67C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4C690:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x160UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C6B4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */)));
        label_0xC4C6B4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC4C6B8;
        label_0xC4C6B8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.OnIsBoundToKey` — RVA `0xc4c6bc`

- Lift status: **exact**; input span: 416 bytes; span to next metadata RVA: 416 bytes.
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=59 (informational only).

```csharp
public static uint SuperTouchZone_OnIsBoundToKey_RVAc4c6bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12895960 = default(uint);
        uint __arm64_flags_left_12895988 = default(uint);
        uint __arm64_flags_left_12896044 = default(uint);
        uint __arm64_flags_left_12896052 = default(uint);
        uint __arm64_flags_right_12895960 = default(uint);
        uint __arm64_flags_right_12895988 = default(uint);
        uint __arm64_flags_right_12896044 = default(uint);
        uint __arm64_flags_right_12896052 = default(uint);
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x90UL))))));
        x19 = x2;
        x21 = x0;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        __arm64_flags_left_12895960 = unchecked((uint)(x8));
        __arm64_flags_right_12895960 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895960) - (__arm64_flags_right_12895960))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12895960)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12895960)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12895960) - (__arm64_flags_right_12895960))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12895960)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C73C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC4C6E8;
        label_0xC4C6E8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12895988 = unchecked((uint)(x22));
        __arm64_flags_right_12895988 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12895988 >= __arm64_flags_right_12895988))
        {
            goto label_0xC4C858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x22) << (int)(unchecked((int)(0x3UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x90UL))))));
        x22 = unchecked((ulong)((x22) + (0x1UL)));
        __arm64_flags_left_12896044 = unchecked((uint)(x8));
        __arm64_flags_right_12896044 = unchecked((uint)0x3UL);
        x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896044) - (__arm64_flags_right_12896044))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896044)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896044)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896044) - (__arm64_flags_right_12896044))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896044)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)(x23)))));
        __arm64_flags_left_12896052 = unchecked((uint)(x22));
        __arm64_flags_right_12896052 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896052) - (__arm64_flags_right_12896052))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896052)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896052)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896052) - (__arm64_flags_right_12896052))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896052)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C6E8;
        }
        else
        {
            goto label_0xC4C73C;
        }
        label_0xC4C73C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x138UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x140UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x150UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x148UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x168UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x178UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x180UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C81C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x158UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C830;
        }
        else
        {
            goto label_0xC4C81C;
        }
        label_0xC4C81C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4C830:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x160UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C854;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */)));
        label_0xC4C854:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4C858;
        label_0xC4C858:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.IsUsingKeyForEmulation` — RVA `0xc4c85c`

- Lift status: **exact**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `public override bool IsUsingKeyForEmulation(KeyCode key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static uint SuperTouchZone_IsUsingKeyForEmulation_RVAc4c85c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12896360 = default(uint);
        uint __arm64_flags_left_12896372 = default(uint);
        uint __arm64_flags_left_12896384 = default(uint);
        uint __arm64_flags_left_12896396 = default(uint);
        uint __arm64_flags_left_12896408 = default(uint);
        uint __arm64_flags_left_12896420 = default(uint);
        uint __arm64_flags_left_12896432 = default(uint);
        uint __arm64_flags_left_12896444 = default(uint);
        uint __arm64_flags_left_12896456 = default(uint);
        uint __arm64_flags_left_12896468 = default(uint);
        uint __arm64_flags_left_12896480 = default(uint);
        uint __arm64_flags_left_12896492 = default(uint);
        uint __arm64_flags_left_12896504 = default(uint);
        uint __arm64_flags_left_12896516 = default(uint);
        uint __arm64_flags_left_12896544 = default(uint);
        uint __arm64_flags_right_12896360 = default(uint);
        uint __arm64_flags_right_12896372 = default(uint);
        uint __arm64_flags_right_12896384 = default(uint);
        uint __arm64_flags_right_12896396 = default(uint);
        uint __arm64_flags_right_12896408 = default(uint);
        uint __arm64_flags_right_12896420 = default(uint);
        uint __arm64_flags_right_12896432 = default(uint);
        uint __arm64_flags_right_12896444 = default(uint);
        uint __arm64_flags_right_12896456 = default(uint);
        uint __arm64_flags_right_12896468 = default(uint);
        uint __arm64_flags_right_12896480 = default(uint);
        uint __arm64_flags_right_12896492 = default(uint);
        uint __arm64_flags_right_12896504 = default(uint);
        uint __arm64_flags_right_12896516 = default(uint);
        uint __arm64_flags_right_12896544 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x188UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC4C914:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18CUL))))));
            __arm64_flags_left_12896360 = unchecked((uint)(x8));
            __arm64_flags_right_12896360 = unchecked((uint)(x1));
            if ((unchecked((uint)((__arm64_flags_left_12896360) - (__arm64_flags_right_12896360))) == unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x190UL))))));
                __arm64_flags_left_12896372 = unchecked((uint)(x8));
                __arm64_flags_right_12896372 = unchecked((uint)(x1));
                if ((unchecked((uint)((__arm64_flags_left_12896372) - (__arm64_flags_right_12896372))) == unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x194UL))))));
                    __arm64_flags_left_12896384 = unchecked((uint)(x8));
                    __arm64_flags_right_12896384 = unchecked((uint)(x1));
                    if ((unchecked((uint)((__arm64_flags_left_12896384) - (__arm64_flags_right_12896384))) == unchecked((uint)0x0UL)))
                    {
                    }
                    else
                    {
                        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1B0UL))))));
                        __arm64_flags_left_12896396 = unchecked((uint)(x8));
                        __arm64_flags_right_12896396 = unchecked((uint)(x1));
                        if ((unchecked((uint)((__arm64_flags_left_12896396) - (__arm64_flags_right_12896396))) == unchecked((uint)0x0UL)))
                        {
                        }
                        else
                        {
                            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1B4UL))))));
                            __arm64_flags_left_12896408 = unchecked((uint)(x8));
                            __arm64_flags_right_12896408 = unchecked((uint)(x1));
                            if ((unchecked((uint)((__arm64_flags_left_12896408) - (__arm64_flags_right_12896408))) == unchecked((uint)0x0UL)))
                            {
                            }
                            else
                            {
                                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1ACUL))))));
                                __arm64_flags_left_12896420 = unchecked((uint)(x8));
                                __arm64_flags_right_12896420 = unchecked((uint)(x1));
                                if ((unchecked((uint)((__arm64_flags_left_12896420) - (__arm64_flags_right_12896420))) == unchecked((uint)0x0UL)))
                                {
                                }
                                else
                                {
                                    x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1A8UL))))));
                                    __arm64_flags_left_12896432 = unchecked((uint)(x8));
                                    __arm64_flags_right_12896432 = unchecked((uint)(x1));
                                    if ((unchecked((uint)((__arm64_flags_left_12896432) - (__arm64_flags_right_12896432))) == unchecked((uint)0x0UL)))
                                    {
                                    }
                                    else
                                    {
                                        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x198UL))))));
                                        __arm64_flags_left_12896444 = unchecked((uint)(x8));
                                        __arm64_flags_right_12896444 = unchecked((uint)(x1));
                                        if ((unchecked((uint)((__arm64_flags_left_12896444) - (__arm64_flags_right_12896444))) == unchecked((uint)0x0UL)))
                                        {
                                        }
                                        else
                                        {
                                            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x19CUL))))));
                                            __arm64_flags_left_12896456 = unchecked((uint)(x8));
                                            __arm64_flags_right_12896456 = unchecked((uint)(x1));
                                            if ((unchecked((uint)((__arm64_flags_left_12896456) - (__arm64_flags_right_12896456))) == unchecked((uint)0x0UL)))
                                            {
                                            }
                                            else
                                            {
                                                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1A0UL))))));
                                                __arm64_flags_left_12896468 = unchecked((uint)(x8));
                                                __arm64_flags_right_12896468 = unchecked((uint)(x1));
                                                if ((unchecked((uint)((__arm64_flags_left_12896468) - (__arm64_flags_right_12896468))) == unchecked((uint)0x0UL)))
                                                {
                                                }
                                                else
                                                {
                                                    x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1A4UL))))));
                                                    __arm64_flags_left_12896480 = unchecked((uint)(x8));
                                                    __arm64_flags_right_12896480 = unchecked((uint)(x1));
                                                    if ((unchecked((uint)((__arm64_flags_left_12896480) - (__arm64_flags_right_12896480))) == unchecked((uint)0x0UL)))
                                                    {
                                                    }
                                                    else
                                                    {
                                                        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1B8UL))))));
                                                        __arm64_flags_left_12896492 = unchecked((uint)(x8));
                                                        __arm64_flags_right_12896492 = unchecked((uint)(x1));
                                                        if ((unchecked((uint)((__arm64_flags_left_12896492) - (__arm64_flags_right_12896492))) == unchecked((uint)0x0UL)))
                                                        {
                                                        }
                                                        else
                                                        {
                                                            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1C4UL))))));
                                                            __arm64_flags_left_12896504 = unchecked((uint)(x8));
                                                            __arm64_flags_right_12896504 = unchecked((uint)(x1));
                                                            if ((unchecked((uint)((__arm64_flags_left_12896504) - (__arm64_flags_right_12896504))) == unchecked((uint)0x0UL)))
                                                            {
                                                            }
                                                            else
                                                            {
                                                                x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1C0UL))))));
                                                                __arm64_flags_left_12896516 = unchecked((uint)(x8));
                                                                __arm64_flags_right_12896516 = unchecked((uint)(x1));
                                                                if ((!((unchecked((uint)((__arm64_flags_left_12896516) - (__arm64_flags_right_12896516))) == unchecked((uint)0x0UL)))))
                                                                {
                                                                    label_0xC4C91C:
                                                                    ;
                                                                    x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x1BCUL))))));
                                                                    __arm64_flags_left_12896544 = unchecked((uint)(x8));
                                                                    __arm64_flags_right_12896544 = unchecked((uint)(x1));
                                                                    x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12896544) - (__arm64_flags_right_12896544))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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
                        }
                    }
                }
            }
            label_0xC4C90C:
            ;
            x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `SuperTouchZone.OnIsEmulatingTouches` — RVA `0xc4c92c`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `protected override bool OnIsEmulatingTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static uint SuperTouchZone_OnIsEmulatingTouches_RVAc4c92c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12896600 = default(uint);
        uint __arm64_flags_left_12896628 = default(uint);
        uint __arm64_flags_left_12896676 = default(uint);
        uint __arm64_flags_left_12896684 = default(uint);
        uint __arm64_flags_right_12896600 = default(uint);
        uint __arm64_flags_right_12896628 = default(uint);
        uint __arm64_flags_right_12896676 = default(uint);
        uint __arm64_flags_right_12896684 = default(uint);
        ulong sp = default(ulong);
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
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C9CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE40UL /* metadata target: InputBindingBase.IsEmulatingTouches */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4C954;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC4C9BC;
        label_0xC4C954:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x90UL))))));
        __arm64_flags_left_12896600 = unchecked((uint)(x8));
        __arm64_flags_right_12896600 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896600) - (__arm64_flags_right_12896600))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896600)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896600)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896600) - (__arm64_flags_right_12896600))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896600)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C9B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC4C968;
        label_0xC4C968:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C9CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12896628 = unchecked((uint)(x20));
        __arm64_flags_right_12896628 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12896628 >= __arm64_flags_right_12896628))
        {
            goto label_0xC4C9D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4C9CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4C9CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE40UL /* metadata target: InputBindingBase.IsEmulatingTouches */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4C9BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x90UL))))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        __arm64_flags_left_12896676 = unchecked((uint)(x8));
        __arm64_flags_right_12896676 = unchecked((uint)0x3UL);
        x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896676) - (__arm64_flags_right_12896676))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896676)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896676)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896676) - (__arm64_flags_right_12896676))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896676)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)(x21)))));
        __arm64_flags_left_12896684 = unchecked((uint)(x20));
        __arm64_flags_right_12896684 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896684) - (__arm64_flags_right_12896684))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896684)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896684)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896684) - (__arm64_flags_right_12896684))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896684)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C968;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4C9B4UL)));
        }
        goto label_0xC4C9BC;
        label_0xC4C9B8:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4C9BC;
        label_0xC4C9BC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4C9CC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC4C9D0;
        label_0xC4C9D0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.OnIsEmulatingMousePosition` — RVA `0xc4c9d4`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `protected override bool OnIsEmulatingMousePosition() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static uint SuperTouchZone_OnIsEmulatingMousePosition_RVAc4c9d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12896736 = default(uint);
        uint __arm64_flags_left_12896768 = default(uint);
        uint __arm64_flags_left_12896816 = default(uint);
        uint __arm64_flags_left_12896824 = default(uint);
        uint __arm64_flags_right_12896736 = default(uint);
        uint __arm64_flags_right_12896768 = default(uint);
        uint __arm64_flags_right_12896816 = default(uint);
        uint __arm64_flags_right_12896824 = default(uint);
        ulong sp = default(ulong);
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
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x90UL))))));
        __arm64_flags_left_12896736 = unchecked((uint)(x8));
        __arm64_flags_right_12896736 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896736) - (__arm64_flags_right_12896736))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896736)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896736)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896736) - (__arm64_flags_right_12896736))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896736)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4CA44;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = x0;
        x20 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC4C9F4;
        label_0xC4C9F4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4CA58;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12896768 = unchecked((uint)(x20));
        __arm64_flags_right_12896768 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12896768 >= __arm64_flags_right_12896768))
        {
            goto label_0xC4CA5C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4CA58;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4CA58;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE4CUL /* metadata target: InputBindingBase.IsEmulatingMousePosition */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4CA48;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x90UL))))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        __arm64_flags_left_12896816 = unchecked((uint)(x8));
        __arm64_flags_right_12896816 = unchecked((uint)0x3UL);
        x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896816) - (__arm64_flags_right_12896816))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896816)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896816)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896816) - (__arm64_flags_right_12896816))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896816)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)(x21)))));
        __arm64_flags_left_12896824 = unchecked((uint)(x20));
        __arm64_flags_right_12896824 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896824) - (__arm64_flags_right_12896824))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12896824)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12896824)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12896824) - (__arm64_flags_right_12896824))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12896824)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4C9F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4CA40UL)));
        }
        goto label_0xC4CA48;
        label_0xC4CA44:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4CA48;
        label_0xC4CA48:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4CA58:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC4CA5C;
        label_0xC4CA5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `SuperTouchZone.OnGetSubBindingDescriptions` — RVA `0xc4ca60`

- Lift status: **partial**; input span: 808 bytes; span to next metadata RVA: 808 bytes.
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=147 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc4cb58; reason: Unsupported instruction 'b.ge' at 0xc4cb5c; reason: Unknown IR expression at 0xc4cb5c

```csharp
public static ulong SuperTouchZone_OnGetSubBindingDescriptions_RVAc4ca60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12897136 = default(ulong);
        ulong __arm64_flags_left_12897144 = default(ulong);
        uint __arm64_flags_left_12897296 = default(uint);
        ulong __arm64_flags_right_12897136 = default(ulong);
        ulong __arm64_flags_right_12897144 = default(ulong);
        uint __arm64_flags_right_12897296 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        sp = unchecked((ulong)((sp) - (0x70UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x23BUL))))))));
        x19 = x3;
        x21 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4CB14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x23BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4CB14;
        label_0xC4CB14:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4CD80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = 0x1A8C000UL;
        x24 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x29 = 0x1A8C000UL;
        x28 = 0x1A8C000UL;
        x27 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xC40UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xC88UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC70UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0xC80UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xC50UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xC68UL))));
        x25 = 0x0UL;
        goto label_0xC4CB54;
        label_0xC4CB54:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        RuntimeCalls.Unsupported("cmp", 0xC4CB58UL);
        RuntimeCalls.Unsupported("b.ge", 0xC4CB5CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4CBE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4CB60UL);
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xC4CD80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CUL))))))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4CB78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x20) + (0x90UL))))))));
        __arm64_flags_left_12897136 = x25;
        __arm64_flags_right_12897136 = x10;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12897136) - (__arm64_flags_right_12897136))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_12897136)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_12897136)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12897136) - (__arm64_flags_right_12897136))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_12897136)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC4CBD8;
        }
        else
        {
            goto label_0xC4CB78;
        }
        label_0xC4CB78:
        ;
        __arm64_flags_left_12897144 = x25;
        __arm64_flags_right_12897144 = x9;
        if ((__arm64_flags_left_12897144 >= __arm64_flags_right_12897144))
        {
            goto label_0xC4CD84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x25) << (int)(unchecked((int)(0x3UL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4CD80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x25 = unchecked((ulong)((x25) + (0x1UL)));
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x25)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x26);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x2 = x0;
        x0 = x21;
        x1 = x22;
        x3 = x19;
        x4 = x20;
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC0UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4CB54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4CBD4UL);
        }
        goto label_0xC4CD80;
        label_0xC4CBD8:
        ;
        x25 = unchecked((ulong)((x25) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC4CB54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4CBE0UL);
        }
        goto label_0xC4CD80;
        label_0xC4CBE4:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC4CD80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x120UL))));
        x2 = RuntimeMemory.ReadU64(x24);
        x0 = x21;
        x3 = x19;
        x4 = x20;
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4CC18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x90UL))))));
        __arm64_flags_left_12897296 = unchecked((uint)(x8));
        __arm64_flags_right_12897296 = unchecked((uint)0x2UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12897296) - (__arm64_flags_right_12897296))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12897296)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12897296)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12897296) - (__arm64_flags_right_12897296))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12897296)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4CD60;
        }
        else
        {
            goto label_0xC4CC18;
        }
        label_0xC4CC18:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x168UL))));
        x3 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x4 = x19;
        x5 = x20;
        x6 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x170UL))));
        x3 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = x21;
        x4 = x19;
        x5 = x20;
        x6 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x178UL))));
        x2 = RuntimeMemory.ReadU64(x29);
        x0 = x21;
        x3 = x19;
        x4 = x20;
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x180UL))));
        x2 = RuntimeMemory.ReadU64(x28);
        x0 = x21;
        x3 = x19;
        x4 = x20;
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x138UL))));
        x3 = RuntimeMemory.ReadU64(x27);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x4 = x19;
        x5 = x20;
        x6 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x140UL))));
        x3 = RuntimeMemory.ReadU64(x27);
        x2 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = x21;
        x4 = x19;
        x5 = x20;
        x6 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = 0x1A8C000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x150UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC58UL))));
        x0 = x21;
        x3 = x19;
        x4 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x148UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC48UL))));
        x0 = x21;
        x3 = x19;
        x4 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x158UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC60UL))));
        x0 = x21;
        x3 = x19;
        x4 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x160UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC78UL))));
        x0 = x21;
        x3 = x19;
        x4 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x5 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        goto label_0xC4CD60;
        label_0xC4CD60:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x70UL)));
        return x0;
        label_0xC4CD80:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC4CD84;
        label_0xC4CD84:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.DrawMarkerGUI` — RVA `0xc4cd88`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void DrawMarkerGUI() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong SuperTouchZone_DrawMarkerGUI_RVAc4cd88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4CDA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4E280UL /* metadata target: SuperTouchZone.EmulatedFingerSystem.DrawMarkers */);
        label_0xC4CDA0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SuperTouchZone.ReleaseEmulatedFingers` — RVA `0xc4cda4`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `private void ReleaseEmulatedFingers(bool cancel) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong SuperTouchZone_ReleaseEmulatedFingers_RVAc4cda4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4CDC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4D354UL /* metadata target: SuperTouchZone.EmulatedFingerSystem.EndTouches */);
        label_0xC4CDC0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```
