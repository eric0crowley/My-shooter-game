# `TouchGestureState` — TypeDefIndex 5097

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0xCC` | `float` | `elapsedSinceLastTapCandidate` |
| `0xD0` | `Vector2` | `segmentOrigin` |
| `0xD8` | `Vector2` | `constrainedVecCur` |
| `0xE0` | `Vector2` | `constrainedVecPrev` |
| `0xE8` | `Vector2` | `scrollVecCur` |
| `0xF0` | `Vector2` | `scrollVecPrev` |
| `0xF8` | `TouchGestureConfig.DirConstraint` | `swipeConstraint` |
| `0xFC` | `TouchGestureConfig.DirConstraint` | `swipeDirConstraint` |
| `0x100` | `TouchGestureConfig.DirConstraint` | `scrollConstraint` |
| `0x104` | `bool` | `cleanPressCur` |
| `0x105` | `bool` | `cleanPressPrev` |
| `0x106` | `bool` | `holdPressCur` |
| `0x107` | `bool` | `holdPressPrev` |
| `0x108` | `Vector2` | `lastDirOrigin` |
| `0x110` | `TouchGestureThresholds` | `thresh` |
| `0x118` | `TouchGestureConfig` | `config` |
| `0x120` | `bool` | `moved` |
| `0x121` | `bool` | `justMoved` |
| `0x122` | `bool` | `nonStaticFlag` |
| `0x123` | `bool` | `cancelTapFlag` |
| `0x124` | `bool` | `disableTapUntilReleaseFlag` |
| `0x125` | `bool` | `flushTapsFlag` |
| `0x126` | `bool` | `holdDelayedEvents` |
| `0x127` | `bool` | `justTapped` |
| `0x128` | `bool` | `justLongTapped` |
| `0x12C` | `Vector2` | `tapPos` |
| `0x134` | `int` | `tapCount` |
| `0x138` | `DirectionState` | `swipeDirState` |
| `0x140` | `DirectionState` | `swipeDirState4` |
| `0x148` | `DirectionState` | `swipeDirState8` |
| `0x150` | `bool` | `blockDrag` |
| `0x154` | `Vector2` | `tapFirstPos` |
| `0x15C` | `int` | `tapCandidateCount` |
| `0x160` | `int` | `lastReportedTapCount` |
| `0x164` | `bool` | `tapCandidateReleased` |

## `TouchGestureState.JustTapped` — RVA `0xc5fb40`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool JustTapped(int howManyTimes) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchGestureState_JustTapped_RVAc5fb40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12974924 = default(uint);
        uint __arm64_flags_right_12974924 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x127UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC5FB58:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x134UL))))));
            __arm64_flags_left_12974924 = unchecked((uint)(x8));
            __arm64_flags_right_12974924 = unchecked((uint)(x1));
            x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12974924) - (__arm64_flags_right_12974924))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `TouchGestureState.GetConstrainedDeltaVec` — RVA `0xc5fb60`

- Lift status: **partial**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public Vector2 GetConstrainedDeltaVec() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fsub' at 0xc5fb64; reason: Unsupported instruction 'mov' at 0xc5fb68

```csharp
public static ulong TouchGestureState_GetConstrainedDeltaVec_RVAc5fb60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12974944 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12974944 = unchecked((ulong)((x0) + (0xD8UL)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12974944)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12974944) + (0x8UL))))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC5FB64UL);
        RuntimeCalls.Unsupported("mov", 0xC5FB68UL);
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.GetScrollDelta` — RVA `0xc5fb70`

- Lift status: **partial**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public Vector2 GetScrollDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fsub' at 0xc5fb74; reason: Unsupported instruction 'mov' at 0xc5fb78

```csharp
public static ulong TouchGestureState_GetScrollDelta_RVAc5fb70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12974960 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12974960 = unchecked((ulong)((x0) + (0xE8UL)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12974960)), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12974960) + (0x8UL))))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC5FB74UL);
        RuntimeCalls.Unsupported("mov", 0xC5FB78UL);
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.BasicConstructor` — RVA `0xc62190`

- Lift status: **exact**; input span: 232 bytes; span to next metadata RVA: 232 bytes.
- Metadata signature: `private void BasicConstructor(TouchGestureThresholds thresholds, TouchGestureConfig config) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong TouchGestureState_BasicConstructor_RVAc62190(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x23 = 0x1BAB000UL;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x2E0UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x140UL))));
        x21 = x2;
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC621D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x140UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x2E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC621D0;
        label_0xC621D0:
        ;
        x0 = unchecked((ulong)((x19) + (0x118UL)));
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x118UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x110UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x110UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5AE6CUL /* metadata target: DirectionState.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x138UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x138UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5AE6CUL /* metadata target: DirectionState.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x140UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x140UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5AE6CUL /* metadata target: DirectionState.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x148UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x148UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `TouchGestureState.ctor` — RVA `0xc62278`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public void .ctor(TouchGestureThresholds thresholds, TouchGestureConfig config) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong TouchGestureState_ctor_RVAc62278(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = x1;
        x1 = 0x0UL;
        x19 = x2;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x1 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = x21;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC62190UL /* metadata target: TouchGestureState.BasicConstructor */);
        return default(ulong);
    }
```

## `TouchGestureState.ctor` — RVA `0xc622ac`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchGestureState_ctor_RVAc622ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC62190UL /* metadata target: TouchGestureState.BasicConstructor */);
        return default(ulong);
    }
```

## `TouchGestureState.SetThresholds` — RVA `0xc622d0`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void SetThresholds(TouchGestureThresholds thresh) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchGestureState_SetThresholds_RVAc622d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)((x0) + (0x110UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x110UL))), x1);
        x0 = x8;
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchGestureState.SetConfig` — RVA `0xc622e0`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void SetConfig(TouchGestureConfig config) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchGestureState_SetConfig_RVAc622e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)((x0) + (0x118UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x118UL))), x1);
        x0 = x8;
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchGestureState.Reset` — RVA `0xc622f0`

- Lift status: **exact**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public override void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong TouchGestureState_Reset_RVAc622f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC61AE8UL /* metadata target: TouchGestureBasicState.Reset */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x100UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xF8UL))), 0x0UL);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62328;
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
        goto label_0xC62328;
        label_0xC62328:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
        x9 = unchecked((ulong)((x19) + (0x127UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xD8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x134UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x15CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x24UL)))) + (0x0UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((x19) + (0x24UL)))) + (0x8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x164UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU16(x9, unchecked((ushort)(unchecked((uint)0x0UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x104UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x120UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x124UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC623A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AE88UL /* metadata target: DirectionState.Reset */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC623A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AE88UL /* metadata target: DirectionState.Reset */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC623A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5AE88UL /* metadata target: DirectionState.Reset */);
        label_0xC623A8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchGestureState.PressedNormal` — RVA `0xc623ac`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool PressedNormal() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchGestureState_PressedNormal_RVAc623ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x104UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchGestureState.JustPressedNormal` — RVA `0xc623b4`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool JustPressedNormal() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchGestureState_JustPressedNormal_RVAc623b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12985280 = default(uint);
        uint __arm64_flags_right_12985280 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x104UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC623CC:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x105UL))))))));
            __arm64_flags_left_12985280 = unchecked((uint)(x8));
            __arm64_flags_right_12985280 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12985280) - (__arm64_flags_right_12985280))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `TouchGestureState.JustReleasedNormal` — RVA `0xc623d4`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool JustReleasedNormal() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchGestureState_JustReleasedNormal_RVAc623d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12985320 = default(uint);
        uint __arm64_flags_right_12985320 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x104UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC623E4:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x105UL))))))));
            __arm64_flags_left_12985320 = unchecked((uint)(x8));
            __arm64_flags_right_12985320 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12985320) - (__arm64_flags_right_12985320))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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

## `TouchGestureState.PressedLong` — RVA `0xc623f4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool PressedLong() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchGestureState_PressedLong_RVAc623f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x106UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchGestureState.JustPressedLong` — RVA `0xc623fc`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool JustPressedLong() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchGestureState_JustPressedLong_RVAc623fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12985352 = default(uint);
        uint __arm64_flags_right_12985352 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x106UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC62414:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x107UL))))))));
            __arm64_flags_left_12985352 = unchecked((uint)(x8));
            __arm64_flags_right_12985352 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12985352) - (__arm64_flags_right_12985352))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `TouchGestureState.JustReleasedLong` — RVA `0xc6241c`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool JustReleasedLong() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchGestureState_JustReleasedLong_RVAc6241c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12985392 = default(uint);
        uint __arm64_flags_right_12985392 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x106UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC6242C:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x107UL))))))));
            __arm64_flags_left_12985392 = unchecked((uint)(x8));
            __arm64_flags_right_12985392 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12985392) - (__arm64_flags_right_12985392))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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

## `TouchGestureState.GetTapPos` — RVA `0xc6243c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public Vector2 GetTapPos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureState_GetTapPos_RVAc6243c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x12CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x130UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.JustLongTapped` — RVA `0xc62448`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool JustLongTapped() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchGestureState_JustLongTapped_RVAc62448(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x128UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchGestureState.GetSwipeDirState` — RVA `0xc62450`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public DirectionState GetSwipeDirState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureState_GetSwipeDirState_RVAc62450(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.GetSwipeDirState4` — RVA `0xc62458`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public DirectionState GetSwipeDirState4() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureState_GetSwipeDirState4_RVAc62458(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x140UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.GetSwipeDirState8` — RVA `0xc62460`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public DirectionState GetSwipeDirState8() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureState_GetSwipeDirState8_RVAc62460(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x148UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.GetSegmentOrigin` — RVA `0xc62468`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Vector2 GetSegmentOrigin() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureState_GetSegmentOrigin_RVAc62468(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12985448 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12985448 = unchecked((ulong)((x0) + (0xD0UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12985448)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12985448) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.JustSwiped` — RVA `0xc62470`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool JustSwiped() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchGestureState_JustSwiped_RVAc62470(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x121UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchGestureState.Swiped` — RVA `0xc62478`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool Swiped() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchGestureState_Swiped_RVAc62478(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchGestureState.GetConstrainedSwipeVec` — RVA `0xc62480`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Vector2 GetConstrainedSwipeVec() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureState_GetConstrainedSwipeVec_RVAc62480(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12985472 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12985472 = unchecked((ulong)((x0) + (0xD8UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12985472)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12985472) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.GetScroll` — RVA `0xc62488`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Vector2 GetScroll() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureState_GetScroll_RVAc62488(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12985480 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        __arm64_pair_address_12985480 = unchecked((ulong)((x0) + (0xE8UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12985480)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12985480) + (0x4UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.GetReleasedDurationRaw` — RVA `0xc62490`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float GetReleasedDurationRaw() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchGestureState_GetReleasedDurationRaw_RVAc62490(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x80UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.ForceSwipe` — RVA `0xc62498`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void ForceSwipe() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchGestureState_ForceSwipe_RVAc62498(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC624A4:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(0x101UL))));
            RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x120UL))), unchecked((ushort)(unchecked((uint)(x8)))));
            return x0;
        }
        else
        {
            return x0;
        }
        return default(ulong);
    }
```

## `TouchGestureState.OnSwipeStart` — RVA `0xc624b0`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `private void OnSwipeStart() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchGestureState_OnSwipeStart_RVAc624b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC624BC:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(0x101UL))));
            RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x120UL))), unchecked((ushort)(unchecked((uint)(x8)))));
            return x0;
        }
        else
        {
            return x0;
        }
        return default(ulong);
    }
```

## `TouchGestureState.BlockSwipe` — RVA `0xc624c8`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void BlockSwipe() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchGestureState_BlockSwipe_RVAc624c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x120UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x150UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x120UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        }
        label_0xC624DC:
        ;
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.HoldDelayedEvents` — RVA `0xc624e0`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void HoldDelayedEvents(bool holdThemForNow) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureState_HoldDelayedEvents_RVAc624e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x126UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.CancelTap` — RVA `0xc624ec`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public void CancelTap() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchGestureState_CancelTap_RVAc624ec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x123UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC624FC:
        ;
        x8 = unchecked((ulong)((x0) + (0x15CUL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x8, 0x0UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.ResetTapState` — RVA `0xc62510`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `private void ResetTapState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureState_ResetTapState_RVAc62510(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)((x0) + (0x15CUL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x8, 0x0UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.DisableTapUntilRelease` — RVA `0xc62524`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void DisableTapUntilRelease() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchGestureState_DisableTapUntilRelease_RVAc62524(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = unchecked((ulong)((x0) + (0x15CUL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x124UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WritePtr(x9, 0x0UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.FlushRegisteredTaps` — RVA `0xc62540`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void FlushRegisteredTaps() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureState_FlushRegisteredTaps_RVAc62540(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x125UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.MarkAsNonStatic` — RVA `0xc6254c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void MarkAsNonStatic() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchGestureState_MarkAsNonStatic_RVAc6254c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x122UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.Update` — RVA `0xc62558`

- Lift status: **exact**; input span: 324 bytes; span to next metadata RVA: 324 bytes.
- Metadata signature: `public override void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=37 (informational only).

```csharp
public static ulong TouchGestureState_Update_RVAc62558(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12985792 = default(float);
        float __arm64_float_flags_left_12985804 = default(float);
        float __arm64_float_flags_right_12985792 = default(float);
        float __arm64_float_flags_right_12985804 = default(float);
        ulong __arm64_load_address_12986000 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2E1UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x490UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC62588:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x20 == 0x0UL))
        {
        }
        else
        {
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x490UL))));
            x0 = RuntimeMemory.ReadU64(x8);
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            }
            label_0xC625A8:
            ;
            x0 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xC3896CUL /* metadata target: CFScreen.get_dpi */, x0, x1, x2, x3);
            x8 = 0x432000UL;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x54UL))))), 0));
            x8 = unchecked((ulong)(unchecked((uint)(0x42C00000UL))));
            __arm64_float_flags_left_12985792 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12985792 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12985792 > __arm64_float_flags_right_12985792) || ((__arm64_float_flags_left_12985792 != __arm64_float_flags_left_12985792) || (__arm64_float_flags_right_12985792 != __arm64_float_flags_right_12985792))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
            __arm64_float_flags_left_12985804 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12985804 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            if ((__arm64_float_flags_left_12985804 == __arm64_float_flags_right_12985804))
            {
            }
            else
            {
                x8 = RuntimeMemory.ReadU64(x20);
                x9 = 0x432000UL;
                RuntimeMemory.WriteF32(unchecked((ulong)((x20) + (0x54UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x35CUL))))), 0));
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
                x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
                x0 = x20;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
            }
        }
        label_0xC625F4:
        ;
        x8 = unchecked((ulong)((x19) + (0x127UL)));
        RuntimeMemory.WriteU16(x8, unchecked((ushort)(unchecked((uint)0x0UL))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x104UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x106UL))))))));
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x121UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x105UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x107UL))), unchecked((byte)(unchecked((uint)(x9)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xF0UL))), x10);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xE0UL))), x11);
        if ((x0 == 0x0UL))
        {
        }
        else
        {
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0xC5AEF8UL /* metadata target: DirectionState.BeginFrame */, x0, x1, x2, x3);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
            if ((x0 == 0x0UL))
            {
            }
            else
            {
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0xC5AEF8UL /* metadata target: DirectionState.BeginFrame */, x0, x1, x2, x3);
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
                if ((x0 == 0x0UL))
                {
                }
                else
                {
                    x1 = 0x0UL;
                    x0 = RuntimeCalls.InvokeDirect(0xC5AEF8UL /* metadata target: DirectionState.BeginFrame */, x0, x1, x2, x3);
                    x0 = x19;
                    x0 = RuntimeCalls.InvokeDirect(0xC61D34UL /* metadata target: TouchGestureBasicState.InternalUpdate */, x0, x1, x2, x3);
                    x0 = x19;
                    x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
                    x0 = RuntimeCalls.InvokeDirect(0xC626E0UL /* metadata target: TouchGestureState.CheckTap */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                    x0 = x19;
                    x0 = RuntimeCalls.InvokeDirect(0xC61EB8UL /* metadata target: TouchGestureBasicState.InternalPostUpdate */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                    x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x164UL))))))));
                    if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
                    {
                    }
                    else
                    {
                        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0xCCUL))))), 0));
                        x0 = 0x0UL;
                        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
                        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xCCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
                    }
                    label_0xC62688:
                    ;
                    x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                    x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
                    x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
                    __arm64_load_address_12986000 = sp;
                    v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12986000)), 0));
                    sp = unchecked((ulong)((__arm64_load_address_12986000) + (0x20UL)));
                    return x0;
                }
            }
        }
        label_0xC62698:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `TouchGestureState.CheckTap` — RVA `0xc626e0`

- Lift status: **partial**; input span: 816 bytes; span to next metadata RVA: 816 bytes.
- Metadata signature: `private void CheckTap(bool lastUpdate) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=58 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fsub' at 0xc6287c; reason: Unsupported instruction 'fmul' at 0xc62880; reason: Unsupported instruction 'faddp' at 0xc62884; reason: Unsupported instruction 'b.ge' at 0xc62a08; reason: Unknown IR expression at 0xc62a08

```csharp
public static ulong TouchGestureState_CheckTap_RVAc626e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12986100 = default(uint);
        uint __arm64_flags_left_12986128 = default(uint);
        uint __arm64_flags_left_12986140 = default(uint);
        uint __arm64_flags_left_12986200 = default(uint);
        uint __arm64_flags_left_12986272 = default(uint);
        uint __arm64_flags_left_12986368 = default(uint);
        uint __arm64_flags_left_12986380 = default(uint);
        uint __arm64_flags_left_12986472 = default(uint);
        uint __arm64_flags_left_12986528 = default(uint);
        uint __arm64_flags_left_12986744 = default(uint);
        uint __arm64_flags_left_12986756 = default(uint);
        uint __arm64_flags_left_12986804 = default(uint);
        uint __arm64_flags_left_12986812 = default(uint);
        uint __arm64_flags_left_12986832 = default(uint);
        uint __arm64_flags_left_12986880 = default(uint);
        uint __arm64_flags_right_12986100 = default(uint);
        uint __arm64_flags_right_12986128 = default(uint);
        uint __arm64_flags_right_12986140 = default(uint);
        uint __arm64_flags_right_12986200 = default(uint);
        uint __arm64_flags_right_12986272 = default(uint);
        uint __arm64_flags_right_12986368 = default(uint);
        uint __arm64_flags_right_12986380 = default(uint);
        uint __arm64_flags_right_12986472 = default(uint);
        uint __arm64_flags_right_12986528 = default(uint);
        uint __arm64_flags_right_12986744 = default(uint);
        uint __arm64_flags_right_12986756 = default(uint);
        uint __arm64_flags_right_12986804 = default(uint);
        uint __arm64_flags_right_12986812 = default(uint);
        uint __arm64_flags_right_12986832 = default(uint);
        uint __arm64_flags_right_12986880 = default(uint);
        float __arm64_float_flags_left_12986224 = default(float);
        float __arm64_float_flags_left_12986252 = default(float);
        float __arm64_float_flags_left_12986352 = default(float);
        float __arm64_float_flags_left_12986508 = default(float);
        float __arm64_float_flags_left_12986604 = default(float);
        float __arm64_float_flags_left_12986628 = default(float);
        float __arm64_float_flags_left_12986648 = default(float);
        float __arm64_float_flags_left_12986676 = default(float);
        float __arm64_float_flags_left_12986704 = default(float);
        float __arm64_float_flags_right_12986224 = default(float);
        float __arm64_float_flags_right_12986252 = default(float);
        float __arm64_float_flags_right_12986352 = default(float);
        float __arm64_float_flags_right_12986508 = default(float);
        float __arm64_float_flags_right_12986604 = default(float);
        float __arm64_float_flags_right_12986628 = default(float);
        float __arm64_float_flags_right_12986648 = default(float);
        float __arm64_float_flags_right_12986676 = default(float);
        float __arm64_float_flags_right_12986704 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
        if ((x10 == 0x0UL))
        {
            goto label_0xC627D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x118UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC627D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x10UL))))));
        __arm64_flags_left_12986100 = unchecked((uint)(x8));
        __arm64_flags_right_12986100 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986100) - (__arm64_flags_right_12986100))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986100)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986100)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986100) - (__arm64_flags_right_12986100))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986100)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC627D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x125UL))))))));
        x8 = unchecked((ulong)((x0) + (0x12CUL)));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62748;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x15CUL))))));
        x11 = unchecked((ulong)((x0) + (0x15CUL)));
        __arm64_flags_left_12986128 = unchecked((uint)(x12));
        __arm64_flags_right_12986128 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986128) - (__arm64_flags_right_12986128))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986128)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986128)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986128) - (__arm64_flags_right_12986128))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986128)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC62738;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
        __arm64_flags_left_12986140 = unchecked((uint)(x12));
        __arm64_flags_right_12986140 = unchecked((uint)(x13));
        if (((unchecked((uint)((__arm64_flags_left_12986140) - (__arm64_flags_right_12986140))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986140) - (__arm64_flags_right_12986140))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986140)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986140)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986140) - (__arm64_flags_right_12986140))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986140)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC62738;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x13)))));
        x13 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        RuntimeMemory.WriteU64(x8, x13);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x12)));
        goto label_0xC62738;
        label_0xC62738:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x11, 0x0UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x125UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC62748;
        label_0xC62748:
        ;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC627D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x15CUL))))));
        x11 = unchecked((ulong)((x0) + (0x15CUL)));
        __arm64_flags_left_12986200 = unchecked((uint)(x12));
        __arm64_flags_right_12986200 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986200) - (__arm64_flags_right_12986200))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986200)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986200)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986200) - (__arm64_flags_right_12986200))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986200)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC627CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x126UL))))))));
        if ((unchecked((uint)(x13)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62778;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62768UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x24UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x2CUL))))), 0));
        __arm64_float_flags_left_12986224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986224 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12986224 > __arm64_float_flags_right_12986224))
        {
            goto label_0xC62794;
        }
        else
        {
            goto label_0xC62778;
        }
        label_0xC62778:
        ;
        x13 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x122UL))))))));
        if ((unchecked((uint)(x13)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62794;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62780UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x3CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x8CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12986252 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986252 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986252 <= __arm64_float_flags_right_12986252) || ((__arm64_float_flags_left_12986252 != __arm64_float_flags_left_12986252) || (__arm64_float_flags_right_12986252 != __arm64_float_flags_right_12986252))))
        {
            goto label_0xC627CC;
        }
        else
        {
            goto label_0xC62794;
        }
        label_0xC62794:
        ;
        x13 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x14UL))))))));
        if ((unchecked((uint)(x13)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC627BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
        __arm64_flags_left_12986272 = unchecked((uint)(x12));
        __arm64_flags_right_12986272 = unchecked((uint)(x13));
        if (((unchecked((uint)((__arm64_flags_left_12986272) - (__arm64_flags_right_12986272))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986272) - (__arm64_flags_right_12986272))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986272)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986272)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986272) - (__arm64_flags_right_12986272))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986272)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC627BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x13)))));
        x13 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        RuntimeMemory.WriteU64(x8, x13);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x12)));
        goto label_0xC627BC;
        label_0xC627BC:
        ;
        x12 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x11, 0x0UL);
        goto label_0xC627CC;
        label_0xC627CC:
        ;
        x13 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1DUL))))))));
        if ((unchecked((uint)(x13)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62868;
        }
        else
        {
            goto label_0xC627D4;
        }
        label_0xC627D4:
        ;
        return x0;
        label_0xC627D8:
        ;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x164UL))))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62834;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x126UL))))))));
        if ((unchecked((uint)(x11)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62834;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC627E8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0xCCUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x30UL))))), 0));
        __arm64_float_flags_left_12986352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986352 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986352 <= __arm64_float_flags_right_12986352) || ((__arm64_float_flags_left_12986352 != __arm64_float_flags_left_12986352) || (__arm64_float_flags_right_12986352 != __arm64_float_flags_right_12986352))))
        {
            goto label_0xC62834;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x15CUL))))));
        x11 = unchecked((ulong)((x0) + (0x15CUL)));
        __arm64_flags_left_12986368 = unchecked((uint)(x12));
        __arm64_flags_right_12986368 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986368) - (__arm64_flags_right_12986368))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986368)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986368)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986368) - (__arm64_flags_right_12986368))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986368)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC62828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
        __arm64_flags_left_12986380 = unchecked((uint)(x12));
        __arm64_flags_right_12986380 = unchecked((uint)(x13));
        if (((unchecked((uint)((__arm64_flags_left_12986380) - (__arm64_flags_right_12986380))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986380) - (__arm64_flags_right_12986380))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986380)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986380)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986380) - (__arm64_flags_right_12986380))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986380)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC62828;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x13)))));
        x13 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        RuntimeMemory.WriteU64(x8, x13);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x12)));
        goto label_0xC62828;
        label_0xC62828:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x11, 0x0UL);
        goto label_0xC62834;
        label_0xC62834:
        ;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1DUL))))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC627D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x123UL))))))));
        if ((unchecked((uint)(x11)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6284C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x124UL))))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC628DC;
        }
        else
        {
            goto label_0xC6284C;
        }
        label_0xC6284C:
        ;
        x8 = unchecked((ulong)((x0) + (0x15CUL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x8, 0x0UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC6285C;
        label_0xC6285C:
        ;
        x8 = unchecked((ulong)((x0) + (0x123UL)));
        RuntimeMemory.WriteU16(x8, unchecked((ushort)(unchecked((uint)0x0UL))));
        return x0;
        label_0xC62868:
        ;
        __arm64_flags_left_12986472 = unchecked((uint)(x12));
        __arm64_flags_right_12986472 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986472) - (__arm64_flags_right_12986472))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986472)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986472)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986472) - (__arm64_flags_right_12986472))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986472)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC628CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62870UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x0) + (0x34UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x28UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x40UL))))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC6287CUL);
        RuntimeCalls.Unsupported("fmul", 0xC62880UL);
        RuntimeCalls.Unsupported("faddp", 0xC62884UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12986508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986508 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986508 <= __arm64_float_flags_right_12986508) || ((__arm64_float_flags_left_12986508 != __arm64_float_flags_left_12986508) || (__arm64_float_flags_right_12986508 != __arm64_float_flags_right_12986508))))
        {
            goto label_0xC627D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x14UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC628BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
        __arm64_flags_left_12986528 = unchecked((uint)(x12));
        __arm64_flags_right_12986528 = unchecked((uint)(x9));
        if (((unchecked((uint)((__arm64_flags_left_12986528) - (__arm64_flags_right_12986528))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986528) - (__arm64_flags_right_12986528))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986528)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986528)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986528) - (__arm64_flags_right_12986528))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986528)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC628BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        RuntimeMemory.WriteU64(x8, x9);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x12)));
        goto label_0xC628BC;
        label_0xC628BC:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x11))))) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)(unchecked((uint)(x11)))), 0x0UL);
        goto label_0xC628D0;
        label_0xC628CC:
        ;
        if ((unchecked((uint)(x12)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC627D4;
        }
        else
        {
            goto label_0xC628D0;
        }
        label_0xC628D0:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5CUL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x28UL))), x9);
        return x0;
        label_0xC628DC:
        ;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x16UL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x80UL))))), 0));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC628E8UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x34UL))))), 0));
        __arm64_float_flags_left_12986604 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986604 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986604 <= __arm64_float_flags_right_12986604) || ((__arm64_float_flags_left_12986604 != __arm64_float_flags_left_12986604) || (__arm64_float_flags_right_12986604 != __arm64_float_flags_right_12986604))))
        {
            goto label_0xC62930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x122UL))))))));
        if ((unchecked((uint)(x11)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC628FCUL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x38UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12986628 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986628 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986628 > __arm64_float_flags_right_12986628) || ((__arm64_float_flags_left_12986628 != __arm64_float_flags_left_12986628) || (__arm64_float_flags_right_12986628 != __arm64_float_flags_right_12986628))))
        {
            goto label_0xC62930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6290CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x3CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x84UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12986648 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986648 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986648 > __arm64_float_flags_right_12986648) || ((__arm64_float_flags_left_12986648 != __arm64_float_flags_left_12986648) || (__arm64_float_flags_right_12986648 != __arm64_float_flags_right_12986648))))
        {
            goto label_0xC62930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x68UL))));
        x12 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x128UL))), unchecked((byte)(unchecked((uint)(x12)))));
        RuntimeMemory.WriteU64(x8, x11);
        goto label_0xC62930;
        label_0xC62930:
        ;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x2CUL))))), 0));
        __arm64_float_flags_left_12986676 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986676 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12986676 > __arm64_float_flags_right_12986676) || ((__arm64_float_flags_left_12986676 != __arm64_float_flags_left_12986676) || (__arm64_float_flags_right_12986676 != __arm64_float_flags_right_12986676))))
        {
            goto label_0xC62958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x122UL))))))));
        if ((unchecked((uint)(x11)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62944UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x3CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x84UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12986704 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12986704 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12986704 <= __arm64_float_flags_right_12986704))
        {
            goto label_0xC629A4;
        }
        else
        {
            goto label_0xC62958;
        }
        label_0xC62958:
        ;
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x14UL))))))));
        x9 = unchecked((ulong)((x0) + (0x15CUL)));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62974;
        }
        else
        {
            goto label_0xC62964;
        }
        label_0xC62964:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x9, 0x0UL);
        goto label_0xC6285C;
        label_0xC62974:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(x9)));
        __arm64_flags_left_12986744 = unchecked((uint)(x10));
        __arm64_flags_right_12986744 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986744) - (__arm64_flags_right_12986744))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986744)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986744)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986744) - (__arm64_flags_right_12986744))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986744)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC62964;
        }
        else
        {
            goto label_0xC62980;
        }
        label_0xC62980:
        ;
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
        __arm64_flags_left_12986756 = unchecked((uint)(x10));
        __arm64_flags_right_12986756 = unchecked((uint)(x11));
        if (((unchecked((uint)((__arm64_flags_left_12986756) - (__arm64_flags_right_12986756))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986756) - (__arm64_flags_right_12986756))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986756)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986756)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986756) - (__arm64_flags_right_12986756))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986756)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC62964;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x11)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        RuntimeMemory.WriteU64(x8, x11);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x10)));
        goto label_0xC62964;
        label_0xC629A4:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x15CUL))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x15CUL))), unchecked((uint)(x10)));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x10UL))))));
        __arm64_flags_left_12986804 = unchecked((uint)(x10));
        __arm64_flags_right_12986804 = unchecked((uint)(x11));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986804) - (__arm64_flags_right_12986804))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12986804)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986804)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986804) - (__arm64_flags_right_12986804))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986804)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC62A00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC629BCUL);
        }
        __arm64_flags_left_12986812 = unchecked((uint)(x10));
        __arm64_flags_right_12986812 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986812) - (__arm64_flags_right_12986812))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986812)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986812)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986812) - (__arm64_flags_right_12986812))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986812)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC629F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x14UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC629F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
        __arm64_flags_left_12986832 = unchecked((uint)(x10));
        __arm64_flags_right_12986832 = unchecked((uint)(x9));
        if (((unchecked((uint)((__arm64_flags_left_12986832) - (__arm64_flags_right_12986832))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986832) - (__arm64_flags_right_12986832))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12986832)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12986832)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12986832) - (__arm64_flags_right_12986832))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12986832)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC629F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x160UL))), unchecked((uint)(x10)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        RuntimeMemory.WriteU64(x8, x9);
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x10)));
        goto label_0xC629F0;
        label_0xC629F0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x164UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC6285C;
        label_0xC62A00:
        ;
        __arm64_flags_left_12986880 = unchecked((uint)(x10));
        __arm64_flags_right_12986880 = unchecked((uint)0x1UL);
        x9 = unchecked((ulong)((x0) + (0x15CUL)));
        RuntimeCalls.Unsupported("b.ge", 0xC62A08UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC62980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62A0CUL);
        }
        goto label_0xC62964;
        return default(ulong);
    }
```

## `TouchGestureState.OnRelease` — RVA `0xc62a10`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `protected override void OnRelease(Vector2 pos, bool cancel) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong TouchGestureState_OnRelease_RVAc62a10(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62A34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62A24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x123UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC62A24;
        label_0xC62A24:
        ;
        x8 = unchecked((ulong)((x0) + (0x15CUL)));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x8, 0x0UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC62A34;
        label_0xC62A34:
        ;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return RuntimeCalls.InvokeDirect(0xC620D0UL /* metadata target: TouchGestureBasicState.OnRelease */);
        return default(ulong);
    }
```

## `TouchGestureState.OnPress` — RVA `0xc62a3c`

- Lift status: **exact**; input span: 212 bytes; span to next metadata RVA: 212 bytes.
- Metadata signature: `protected override void OnPress(Vector2 startPos, Vector2 pos, float delay, bool startedByMouse, bool isPressureSensitive, float pressure) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong TouchGestureState_OnPress_RVAc62a3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)(0x1UL)))))));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC62040UL /* metadata target: TouchGestureBasicState.OnPress */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x150UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x120UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x122UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62A80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC62A80;
        label_0xC62A80:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x9)), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x44UL))));
        v0 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xD8UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xD8UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(x8)), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xD0UL))), x9);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x100UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        v0 = v0;
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((x19) + (0xE8UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((x19) + (0xE8UL))), v0);
#endif
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xF8UL))), 0x0UL);
        if ((x8 == 0x0UL))
        {
            goto label_0xC62AD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x2CUL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x100UL))), unchecked((uint)(x9)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0x24UL))))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xF8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        goto label_0xC62AD4;
        label_0xC62AD4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC62B0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AE88UL /* metadata target: DirectionState.Reset */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC62B0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AE88UL /* metadata target: DirectionState.Reset */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC62B0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5AE88UL /* metadata target: DirectionState.Reset */);
        label_0xC62B0C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `TouchGestureState.CheckMovement` — RVA `0xc62b10`

- Lift status: **partial**; input span: 1424 bytes; span to next metadata RVA: 1424 bytes.
- Metadata signature: `protected override void CheckMovement(bool itsFinalUpdate) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=127 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fabd' at 0xc62b38; reason: Unsupported instruction 'fcmgt' at 0xc62b3c; reason: Unsupported instruction 'bif' at 0xc62b40; reason: Unsupported instruction 'fsub' at 0xc62b48; reason: Unsupported instruction 'fmul' at 0xc62b4c; reason: Unsupported instruction 'faddp' at 0xc62b50; reason: Unsupported instruction 'fsub' at 0xc62d20; reason: Unsupported instruction 'mov' at 0xc62d24

```csharp
public static ulong TouchGestureState_CheckMovement_RVAc62b10(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_fcvtz_source_12987616 = default(float);
        uint __arm64_flags_left_12987452 = default(uint);
        uint __arm64_flags_left_12987532 = default(uint);
        uint __arm64_flags_left_12987540 = default(uint);
        uint __arm64_flags_left_12987588 = default(uint);
        uint __arm64_flags_left_12987696 = default(uint);
        uint __arm64_flags_left_12987784 = default(uint);
        uint __arm64_flags_left_12987792 = default(uint);
        uint __arm64_flags_left_12987964 = default(uint);
        uint __arm64_flags_left_12988044 = default(uint);
        uint __arm64_flags_left_12988052 = default(uint);
        uint __arm64_flags_left_12988460 = default(uint);
        uint __arm64_flags_result_12987588 = default(uint);
        uint __arm64_flags_right_12987452 = default(uint);
        uint __arm64_flags_right_12987532 = default(uint);
        uint __arm64_flags_right_12987540 = default(uint);
        uint __arm64_flags_right_12987588 = default(uint);
        uint __arm64_flags_right_12987696 = default(uint);
        uint __arm64_flags_right_12987784 = default(uint);
        uint __arm64_flags_right_12987792 = default(uint);
        uint __arm64_flags_right_12987964 = default(uint);
        uint __arm64_flags_right_12988044 = default(uint);
        uint __arm64_flags_right_12988052 = default(uint);
        uint __arm64_flags_right_12988460 = default(uint);
        float __arm64_float_flags_left_12987220 = default(float);
        float __arm64_float_flags_left_12987292 = default(float);
        float __arm64_float_flags_left_12987368 = default(float);
        float __arm64_float_flags_left_12987476 = default(float);
        float __arm64_float_flags_left_12987504 = default(float);
        float __arm64_float_flags_left_12987512 = default(float);
        float __arm64_float_flags_left_12987620 = default(float);
        float __arm64_float_flags_left_12987724 = default(float);
        float __arm64_float_flags_left_12987756 = default(float);
        float __arm64_float_flags_left_12987764 = default(float);
        float __arm64_float_flags_left_12987924 = default(float);
        float __arm64_float_flags_left_12987988 = default(float);
        float __arm64_float_flags_left_12988016 = default(float);
        float __arm64_float_flags_left_12988024 = default(float);
        float __arm64_float_flags_left_12988156 = default(float);
        float __arm64_float_flags_left_12988232 = default(float);
        float __arm64_float_flags_left_12988548 = default(float);
        float __arm64_float_flags_right_12987220 = default(float);
        float __arm64_float_flags_right_12987292 = default(float);
        float __arm64_float_flags_right_12987368 = default(float);
        float __arm64_float_flags_right_12987476 = default(float);
        float __arm64_float_flags_right_12987504 = default(float);
        float __arm64_float_flags_right_12987512 = default(float);
        float __arm64_float_flags_right_12987620 = default(float);
        float __arm64_float_flags_right_12987724 = default(float);
        float __arm64_float_flags_right_12987756 = default(float);
        float __arm64_float_flags_right_12987764 = default(float);
        float __arm64_float_flags_right_12987924 = default(float);
        float __arm64_float_flags_right_12987988 = default(float);
        float __arm64_float_flags_right_12988016 = default(float);
        float __arm64_float_flags_right_12988024 = default(float);
        float __arm64_float_flags_right_12988156 = default(float);
        float __arm64_float_flags_right_12988232 = default(float);
        float __arm64_float_flags_right_12988548 = default(float);
        ulong __arm64_load_address_12988528 = default(ulong);
        ulong __arm64_pair_address_12987156 = default(ulong);
        ulong __arm64_pair_address_12987428 = default(ulong);
        ulong __arm64_pair_address_12987432 = default(ulong);
        ulong __arm64_pair_address_12987872 = default(ulong);
        ulong __arm64_pair_address_12987876 = default(ulong);
        ulong __arm64_pair_address_12987940 = default(ulong);
        ulong __arm64_pair_address_12987944 = default(ulong);
        ulong __arm64_pair_address_12988124 = default(ulong);
        ulong __arm64_pair_address_12988300 = default(ulong);
        ulong __arm64_pair_address_12988524 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
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
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)));
        __arm64_pair_address_12987156 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12987156, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12987156) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x0) + (0x34UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x0) + (0x5CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x0) + (0x94UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
        RuntimeCalls.Unsupported("fabd", 0xC62B38UL);
        RuntimeCalls.Unsupported("fcmgt", 0xC62B3CUL);
        RuntimeCalls.Unsupported("bif", 0xC62B40UL);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x8CUL))))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC62B48UL);
        RuntimeCalls.Unsupported("fmul", 0xC62B4CUL);
        RuntimeCalls.Unsupported("faddp", 0xC62B50UL);
        __arm64_float_flags_left_12987220 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987220 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12987220 > __arm64_float_flags_right_12987220) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x8CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x94UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v2.GetUInt64(0)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC6305C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x118UL))));
        x19 = x0;
        if ((x9 == 0x0UL))
        {
            goto label_0xC6305C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1CUL))))))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62BC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x106UL))))))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62BD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x17UL))))))));
        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62BA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x122UL))))))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62BB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62B94UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12987292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987292 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12987292 > __arm64_float_flags_right_12987292))
        {
            goto label_0xC62BB4;
        }
        else
        {
            goto label_0xC62BA4;
        }
        label_0xC62BA4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x18UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62BFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62BFC;
        }
        else
        {
            goto label_0xC62BB4;
        }
        label_0xC62BB4:
        ;
        x9 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x106UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC62C00;
        label_0xC62BC4:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x104UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x106UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC62C24;
        label_0xC62BD0:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x15UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62BF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x122UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62BF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62BE0UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12987368 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987368 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987368 <= __arm64_float_flags_right_12987368) || ((__arm64_float_flags_left_12987368 != __arm64_float_flags_left_12987368) || (__arm64_float_flags_right_12987368 != __arm64_float_flags_right_12987368))))
        {
            goto label_0xC63078;
        }
        else
        {
            goto label_0xC62BF0;
        }
        label_0xC62BF0:
        ;
        x9 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC62BF4;
        label_0xC62BF4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC62C00;
        label_0xC62BFC:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC62C00;
        label_0xC62C00:
        ;
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x104UL))))))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62C24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62C08UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62C24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62C0CUL);
        }
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62C24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC630ACUL /* metadata target: TouchGestureState.IsPotentialTap */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62C24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x104UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC62C24;
        label_0xC62C24:
        ;
        __arm64_pair_address_12987428 = unchecked((ulong)((x19) + (0x34UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12987428)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12987428) + (0x4UL))))), 0));
        __arm64_pair_address_12987432 = unchecked((ulong)((x19) + (0x5CUL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12987432)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12987432) + (0x4UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x100UL))))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62CA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62C3CUL);
        }
        __arm64_flags_left_12987452 = unchecked((uint)(x8));
        __arm64_flags_right_12987452 = unchecked((uint)0x3UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12987452) - (__arm64_flags_right_12987452))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC62C8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62C4CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x50UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12987476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987476 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987476 <= __arm64_float_flags_right_12987476) || ((__arm64_float_flags_left_12987476 != __arm64_float_flags_left_12987476) || (__arm64_float_flags_right_12987476 != __arm64_float_flags_right_12987476))))
        {
            goto label_0xC62C68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x100UL))), unchecked((uint)(x8)));
        goto label_0xC62C6C;
        label_0xC62C68:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC62C6C;
        label_0xC62C6C:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12987504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987504 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987504 <= __arm64_float_flags_right_12987504) || ((__arm64_float_flags_left_12987504 != __arm64_float_flags_left_12987504) || (__arm64_float_flags_right_12987504 != __arm64_float_flags_right_12987504))))
        {
            goto label_0xC62C8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62C78UL);
        }
        __arm64_float_flags_left_12987512 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987512 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987512 <= __arm64_float_flags_right_12987512) || ((__arm64_float_flags_left_12987512 != __arm64_float_flags_left_12987512) || (__arm64_float_flags_right_12987512 != __arm64_float_flags_right_12987512))))
        {
            goto label_0xC62C8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x100UL))), unchecked((uint)(x8)));
        goto label_0xC62C9C;
        label_0xC62C8C:
        ;
        __arm64_flags_left_12987532 = unchecked((uint)(x8));
        __arm64_flags_right_12987532 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12987532) - (__arm64_flags_right_12987532))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62CA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62C94UL);
        }
        __arm64_flags_left_12987540 = unchecked((uint)(x8));
        __arm64_flags_right_12987540 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12987540) - (__arm64_flags_right_12987540))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC62CA8;
        }
        else
        {
            goto label_0xC62C9C;
        }
        label_0xC62C9C:
        ;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC62CA8;
        label_0xC62CA4:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC62CA8;
        label_0xC62CA8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x20 = unchecked((ulong)(unchecked((uint)(0xECUL))));
        x22 = unchecked((ulong)(unchecked((uint)(0xE8UL))));
        x23 = unchecked((ulong)(unchecked((uint)(0x7F800000UL))));
        x24 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        goto label_0xC62CC4;
        label_0xC62CC4:
        ;
        __arm64_flags_left_12987588 = unchecked((uint)(x21));
        __arm64_flags_right_12987588 = unchecked((uint)0x1UL);
        __arm64_flags_result_12987588 = unchecked((uint)((__arm64_flags_left_12987588) & (__arm64_flags_right_12987588)));
        x9 = ((!((__arm64_flags_result_12987588 == unchecked((uint)0x0UL)))) ? x22 : x20);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (x9))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x50UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x20UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x23))), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((__arm64_flags_result_12987588 == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))), 0));
        __arm64_fcvtz_source_12987616 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_12987616 != __arm64_fcvtz_source_12987616) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_12987616 >= global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x4F000000UL)), 0)) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_12987616 < global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xCF000000UL)), 0)) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_12987616)))))))));
        __arm64_float_flags_left_12987620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987620 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        x0 = unchecked((ulong)(((__arm64_float_flags_left_12987620 == __arm64_float_flags_right_12987620) ? unchecked((uint)(x24)) : unchecked((uint)(x8)))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58578UL /* metadata target: CFUtils.GetScrollValue */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62D10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xE8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 != 0x0UL))
        {
            goto label_0xC62CC4;
        }
        else
        {
            goto label_0xC62D0C;
        }
        label_0xC62D0C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC62D10;
        label_0xC62D10:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x44UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x5CUL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xF8UL))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xECUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeCalls.Unsupported("fsub", 0xC62D20UL);
        RuntimeCalls.Unsupported("mov", 0xC62D24UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0xD8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62DE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62D30UL);
        }
        __arm64_flags_left_12987696 = unchecked((uint)(x8));
        __arm64_flags_right_12987696 = unchecked((uint)0x3UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12987696) - (__arm64_flags_right_12987696))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC62D88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62D40UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x94UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x44UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12987724 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987724 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987724 <= __arm64_float_flags_right_12987724) || ((__arm64_float_flags_left_12987724 != __arm64_float_flags_left_12987724) || (__arm64_float_flags_right_12987724 != __arm64_float_flags_right_12987724))))
        {
            goto label_0xC62D60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xF8UL))), unchecked((uint)(x8)));
        goto label_0xC62D64;
        label_0xC62D60:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC62D64;
        label_0xC62D64:
        ;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x98UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12987756 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987756 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987756 <= __arm64_float_flags_right_12987756) || ((__arm64_float_flags_left_12987756 != __arm64_float_flags_left_12987756) || (__arm64_float_flags_right_12987756 != __arm64_float_flags_right_12987756))))
        {
            goto label_0xC62D88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62D74UL);
        }
        __arm64_float_flags_left_12987764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987764 <= __arm64_float_flags_right_12987764) || ((__arm64_float_flags_left_12987764 != __arm64_float_flags_left_12987764) || (__arm64_float_flags_right_12987764 != __arm64_float_flags_right_12987764))))
        {
            goto label_0xC62D88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xF8UL))), unchecked((uint)(x8)));
        goto label_0xC62DA4;
        label_0xC62D88:
        ;
        __arm64_flags_left_12987784 = unchecked((uint)(x8));
        __arm64_flags_right_12987784 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12987784) - (__arm64_flags_right_12987784))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62DA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62D90UL);
        }
        __arm64_flags_left_12987792 = unchecked((uint)(x8));
        __arm64_flags_right_12987792 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12987792) - (__arm64_flags_right_12987792))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC62DB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62D98UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xDCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC62DE8;
        label_0xC62DA4:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xD8UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC62DE8;
        label_0xC62DB0:
        ;
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62DD0;
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
        goto label_0xC62DD0;
        label_0xC62DD0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12987872 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12987872)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12987872) + (0x4UL))))), 0));
        __arm64_pair_address_12987876 = unchecked((ulong)((x19) + (0xD8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12987876, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12987876) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        goto label_0xC62DE8;
        label_0xC62DE8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x120UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62E24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x150UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62E24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62E00UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x44UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12987924 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987924 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987924 <= __arm64_float_flags_right_12987924) || ((__arm64_float_flags_left_12987924 != __arm64_float_flags_left_12987924) || (__arm64_float_flags_right_12987924 != __arm64_float_flags_right_12987924))))
        {
            goto label_0xC62E24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x101UL))));
        RuntimeMemory.WriteU16(unchecked((ulong)((x19) + (0x120UL))), unchecked((ushort)(unchecked((uint)(x8)))));
        goto label_0xC62E24;
        label_0xC62E24:
        ;
        __arm64_pair_address_12987940 = unchecked((ulong)((x19) + (0x44UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12987940)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12987940) + (0x4UL))))), 0));
        __arm64_pair_address_12987944 = unchecked((ulong)((x19) + (0xD0UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12987944)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12987944) + (0x4UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0xFCUL))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62EE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62E3CUL);
        }
        __arm64_flags_left_12987964 = unchecked((uint)(x8));
        __arm64_flags_right_12987964 = unchecked((uint)0x3UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12987964) - (__arm64_flags_right_12987964))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC62E8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62E4CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x48UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12987988 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12987988 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12987988 <= __arm64_float_flags_right_12987988) || ((__arm64_float_flags_left_12987988 != __arm64_float_flags_left_12987988) || (__arm64_float_flags_right_12987988 != __arm64_float_flags_right_12987988))))
        {
            goto label_0xC62E68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFCUL))), unchecked((uint)(x8)));
        goto label_0xC62E6C;
        label_0xC62E68:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        goto label_0xC62E6C;
        label_0xC62E6C:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12988016 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12988016 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12988016 <= __arm64_float_flags_right_12988016) || ((__arm64_float_flags_left_12988016 != __arm64_float_flags_left_12988016) || (__arm64_float_flags_right_12988016 != __arm64_float_flags_right_12988016))))
        {
            goto label_0xC62E8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62E78UL);
        }
        __arm64_float_flags_left_12988024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12988024 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12988024 <= __arm64_float_flags_right_12988024) || ((__arm64_float_flags_left_12988024 != __arm64_float_flags_left_12988024) || (__arm64_float_flags_right_12988024 != __arm64_float_flags_right_12988024))))
        {
            goto label_0xC62E8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFCUL))), unchecked((uint)(x8)));
        goto label_0xC62E9C;
        label_0xC62E8C:
        ;
        __arm64_flags_left_12988044 = unchecked((uint)(x8));
        __arm64_flags_right_12988044 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12988044) - (__arm64_flags_right_12988044))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC62EA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62E94UL);
        }
        __arm64_flags_left_12988052 = unchecked((uint)(x8));
        __arm64_flags_right_12988052 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12988052) - (__arm64_flags_right_12988052))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC62EAC;
        }
        else
        {
            goto label_0xC62E9C;
        }
        label_0xC62E9C:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC62EE0;
        label_0xC62EA4:
        ;
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        goto label_0xC62EE0;
        label_0xC62EAC:
        ;
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62ECC;
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
        goto label_0xC62ECC;
        label_0xC62ECC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12988124 = x8;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12988124)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12988124) + (0x4UL))))), 0));
        goto label_0xC62EE0;
        label_0xC62EE0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62EE8UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x48UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12988156 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12988156 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12988156 <= __arm64_float_flags_right_12988156) || ((__arm64_float_flags_left_12988156 != __arm64_float_flags_left_12988156) || (__arm64_float_flags_right_12988156 != __arm64_float_flags_right_12988156))))
        {
            goto label_0xC6305C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC62F24;
        label_0xC62F24:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62F3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62F38UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC62F3C;
        label_0xC62F3C:
        ;
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_12988232 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12988232 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12988232 <= __arm64_float_flags_right_12988232) || ((__arm64_float_flags_left_12988232 != __arm64_float_flags_left_12988232) || (__arm64_float_flags_right_12988232 != __arm64_float_flags_right_12988232))))
        {
            goto label_0xC62F5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC62F50UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC62F90;
        label_0xC62F5C:
        ;
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC62F7C;
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
        goto label_0xC62F7C;
        label_0xC62F7C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12988300 = x8;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12988300)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12988300) + (0x4UL))))), 0));
        goto label_0xC62F90;
        label_0xC62F90:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x432000UL;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x10UL))))));
        v0 = v8;
        v1 = v9;
        v2 = v10;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC59AACUL /* metadata target: CFUtils.VecToDir */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AF0CUL /* metadata target: DirectionState.SetDir */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x148UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x10UL))))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v0 = v8;
        v1 = v9;
        v2 = v10;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC59AACUL /* metadata target: CFUtils.VecToDir */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AF0CUL /* metadata target: DirectionState.SetDir */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x1CUL))))));
        x10 = unchecked((ulong)((x19) + (0x140UL)));
        x11 = unchecked((ulong)((x19) + (0x148UL)));
        __arm64_flags_left_12988460 = unchecked((uint)(x9));
        __arm64_flags_right_12988460 = unchecked((uint)0x1UL);
        x9 = ((unchecked((uint)((__arm64_flags_left_12988460) - (__arm64_flags_right_12988460))) == unchecked((uint)0x0UL)) ? x11 : x10);
        x9 = RuntimeMemory.ReadU64(x9);
        if ((x9 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC62D0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x10UL))))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AF0CUL /* metadata target: DirectionState.SetDir */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x44UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xD0UL))), x8);
        goto label_0xC6305C;
        label_0xC6305C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_12988524 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12988524)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12988524) + (0x8UL))))), 0));
        __arm64_load_address_12988528 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12988528)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12988528) + (0x50UL)));
        return x0;
        label_0xC63078:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x24UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x34UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        __arm64_float_flags_left_12988548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12988548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12988548 <= __arm64_float_flags_right_12988548) || ((__arm64_float_flags_left_12988548 != __arm64_float_flags_left_12988548) || (__arm64_float_flags_right_12988548 != __arm64_float_flags_right_12988548))))
        {
            goto label_0xC63098;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x106UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC62BF4;
        label_0xC63098:
        ;
        x9 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC62C00;
        return default(ulong);
    }
```

## `TouchGestureState.IsPotentialTap` — RVA `0xc630ac`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public bool IsPotentialTap() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static uint TouchGestureState_IsPotentialTap_RVAc630ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12988640 = default(uint);
        uint __arm64_flags_right_12988640 = default(uint);
        float __arm64_float_flags_left_12988664 = default(float);
        float __arm64_float_flags_left_12988684 = default(float);
        float __arm64_float_flags_right_12988664 = default(float);
        float __arm64_float_flags_right_12988684 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x118UL))));
            if ((x9 == 0x0UL))
            {
            }
            else
            {
                x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
                if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x123UL))))))));
                    if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
                    {
                    }
                    else
                    {
                        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x124UL))))))));
                        if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
                        {
                            label_0xC630DC:
                            ;
                            x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x10UL))))));
                            __arm64_flags_left_12988640 = unchecked((uint)(x9));
                            __arm64_flags_right_12988640 = unchecked((uint)0x1UL);
                            if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988640) - (__arm64_flags_right_12988640))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12988640)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12988640)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988640) - (__arm64_flags_right_12988640))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12988640)) < unchecked((int)0x0UL))))))
                            {
                            }
                            else
                            {
                                x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x122UL))))))));
                                if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
                                {
                                }
                                else
                                {
                                    v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x24UL))))), 0));
                                    v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2CUL))))), 0));
                                    __arm64_float_flags_left_12988664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                                    __arm64_float_flags_right_12988664 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                                    if (((__arm64_float_flags_left_12988664 >= __arm64_float_flags_right_12988664) || ((__arm64_float_flags_left_12988664 != __arm64_float_flags_left_12988664) || (__arm64_float_flags_right_12988664 != __arm64_float_flags_right_12988664))))
                                    {
                                    }
                                    else
                                    {
                                        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3CUL))))), 0));
                                        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x8CUL))))), 0));
                                        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                                        __arm64_float_flags_left_12988684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                                        __arm64_float_flags_right_12988684 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                                        x0 = unchecked((ulong)(((__arm64_float_flags_left_12988684 < __arm64_float_flags_right_12988684) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                                        return unchecked((uint)(x0));
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        label_0xC630D4:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchGestureState.IsPotentialLongPress` — RVA `0xc63130`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public bool IsPotentialLongPress() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static uint TouchGestureState_IsPotentialLongPress_RVAc63130(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12988776 = default(float);
        float __arm64_float_flags_left_12988796 = default(float);
        float __arm64_float_flags_right_12988776 = default(float);
        float __arm64_float_flags_right_12988796 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
        }
        else
        {
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x118UL))));
            if ((x9 == 0x0UL))
            {
            }
            else
            {
                x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
                if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
                {
                }
                else
                {
                    x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x122UL))))))));
                    if ((unchecked((uint)(x10)) == unchecked((uint)0x0UL)))
                    {
                        label_0xC63158:
                        ;
                        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x15UL))))))));
                        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
                        {
                        }
                        else
                        {
                            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x24UL))))), 0));
                            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x34UL))))), 0));
                            __arm64_float_flags_left_12988776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                            __arm64_float_flags_right_12988776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                            if (((__arm64_float_flags_left_12988776 >= __arm64_float_flags_right_12988776) || ((__arm64_float_flags_left_12988776 != __arm64_float_flags_left_12988776) || (__arm64_float_flags_right_12988776 != __arm64_float_flags_right_12988776))))
                            {
                            }
                            else
                            {
                                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3CUL))))), 0));
                                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x8CUL))))), 0));
                                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
                                __arm64_float_flags_left_12988796 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                                __arm64_float_flags_right_12988796 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                                x0 = unchecked((ulong)(((__arm64_float_flags_left_12988796 < __arm64_float_flags_right_12988796) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                                return unchecked((uint)(x0));
                            }
                        }
                    }
                }
            }
        }
        label_0xC63150:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchGestureState.ReportTap` — RVA `0xc63188`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `private void ReportTap(bool reset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchGestureState_ReportTap_RVAc63188(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12988812 = default(uint);
        uint __arm64_flags_left_12988824 = default(uint);
        uint __arm64_flags_right_12988812 = default(uint);
        uint __arm64_flags_right_12988824 = default(uint);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x15CUL))))));
        __arm64_flags_left_12988812 = unchecked((uint)(x8));
        __arm64_flags_right_12988812 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988812) - (__arm64_flags_right_12988812))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12988812)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12988812)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988812) - (__arm64_flags_right_12988812))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12988812)) < unchecked((int)0x0UL))))))
        {
        }
        else
        {
            x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
            __arm64_flags_left_12988824 = unchecked((uint)(x8));
            __arm64_flags_right_12988824 = unchecked((uint)(x9));
            if (((unchecked((uint)((__arm64_flags_left_12988824) - (__arm64_flags_right_12988824))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988824) - (__arm64_flags_right_12988824))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12988824)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12988824)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988824) - (__arm64_flags_right_12988824))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12988824)) < unchecked((int)0x0UL)))))))
            {
            }
            else
            {
                x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x9 = unchecked((ulong)((x0) + (0x12CUL)));
                RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x160UL))), unchecked((uint)(x8)));
                RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x10)))));
                x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x28UL))));
                RuntimeMemory.WriteU64(x9, x10);
                RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x8)));
            }
        }
        label_0xC631BC:
        ;
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = unchecked((ulong)((x0) + (0x15CUL)));
            RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
            RuntimeMemory.WritePtr(x8, 0x0UL);
        }
        label_0xC631D0:
        ;
        return x0;
        return default(ulong);
    }
```

## `TouchGestureState.ReportTap` — RVA `0xc631e0`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `private void ReportTap() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchGestureState_ReportTap_RVAc631e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12988904 = default(uint);
        uint __arm64_flags_left_12988916 = default(uint);
        uint __arm64_flags_right_12988904 = default(uint);
        uint __arm64_flags_right_12988916 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x15CUL))))));
        x8 = unchecked((ulong)((x0) + (0x15CUL)));
        __arm64_flags_left_12988904 = unchecked((uint)(x9));
        __arm64_flags_right_12988904 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988904) - (__arm64_flags_right_12988904))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12988904)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12988904)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988904) - (__arm64_flags_right_12988904))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12988904)) < unchecked((int)0x0UL))))))
        {
        }
        else
        {
            x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x160UL))))));
            __arm64_flags_left_12988916 = unchecked((uint)(x9));
            __arm64_flags_right_12988916 = unchecked((uint)(x10));
            if (((unchecked((uint)((__arm64_flags_left_12988916) - (__arm64_flags_right_12988916))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988916) - (__arm64_flags_right_12988916))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12988916)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12988916)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12988916) - (__arm64_flags_right_12988916))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12988916)) < unchecked((int)0x0UL)))))))
            {
            }
            else
            {
                x11 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                x10 = unchecked((ulong)((x0) + (0x12CUL)));
                RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x127UL))), unchecked((byte)(unchecked((uint)(x11)))));
                x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0x28UL))));
                RuntimeMemory.WriteU64(x10, x11);
                RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x134UL))), unchecked((uint)(x9)));
            }
        }
        label_0xC63214:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0xCCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x8, 0x0UL);
        return x0;
        return default(ulong);
    }
```
