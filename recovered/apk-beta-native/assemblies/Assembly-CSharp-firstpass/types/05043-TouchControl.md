# `TouchControl` — TypeDefIndex 5043

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x22` | `bool` | `ignoreFingerRadius` |
| `0x23` | `bool` | `cantBeControlledDirectly` |
| `0x24` | `bool` | `shareTouch` |
| `0x25` | `bool` | `dontAcceptSharedTouches` |
| `0x26` | `bool` | `canBeSwipedOver` |
| `0x27` | `bool` | `restictSwipeOverTargets` |
| `0x28` | `TouchControl.SwipeOverOthersMode` | `swipeOverOthersMode` |
| `0x2C` | `TouchControl.SwipeOffMode` | `swipeOffMode` |
| `0x30` | `List<TouchControl>` | `swipeOverTargetList` |
| `0x38` | `TouchControl.Shape` | `shape` |
| `0x40` | `List<TouchControlAnimatorBase>` | `animatorList` |
| `0x48` | `DisablingConditionSet` | `disablingConditions` |
| `0x50` | `int` | `hidingFlagsCur` |
| `0x58` | `InputRig` | `_rig` |
| `0x60` | `Canvas` | `_canvas` |
| `0x68` | `TouchControlPanel` | `_panel` |
| `0x70` | `bool` | `isHidden` |
| `0x71` | `bool` | `baseAlphaAnimOn` |
| `0x74` | `float` | `baseAlphaStart` |
| `0x78` | `float` | `baseAlphaEnd` |
| `0x7C` | `float` | `baseAlphaCur` |
| `0x80` | `float` | `baseAlphaAnimDur` |
| `0x84` | `float` | `baseAlphaAnimElapsed` |

## `TouchControl.GetCamera` — RVA `0xc4da28`

- Lift status: **exact**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `public Camera GetCamera() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong TouchControl_GetCamera_RVAc4da28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x252UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4DA5C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x252UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4DA5C;
        label_0xC4DA5C:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4DA70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4DA6CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4DA70;
        label_0xC4DA70:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4DAB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4DAC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x196FF1CUL /* metadata target: Canvas.get_renderMode */, x0, x1, x2, x3);
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4DAB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4DAC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x19705F4UL /* metadata target: Canvas.get_worldCamera */);
        label_0xC4DAB0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4DAC0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.GetScreenSpaceCenter` — RVA `0xc4e150`

- Lift status: **exact**; input span: 184 bytes; span to next metadata RVA: 184 bytes.
- Metadata signature: `public Vector2 GetScreenSpaceCenter(Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static ulong TouchControl_GetScreenSpaceCenter_RVAc4e150(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12902736 = default(ulong);
        ulong __arm64_pair_address_12902908 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12902736 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12902736, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12902736) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12902736;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x25AUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4E190;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x25AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4E190;
        label_0xC4E190:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC51604UL /* metadata target: TouchControl.GetWorldSpaceCenter */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        v8 = v0;
        v9 = v1;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4E1B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4E1ACUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4E1B0;
        label_0xC4E1B0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4E1E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4E1C4UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC4E204;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        v0 = v8;
        v1 = v9;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F6B8UL /* metadata target: Camera.WorldToScreenPoint */, x0, x1, x2, x3);
        v8 = v0;
        v9 = v1;
        goto label_0xC4E1E8;
        label_0xC4E1E8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        __arm64_pair_address_12902908 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12902908)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12902908) + (0x8UL))))), 0));
        return x0;
        label_0xC4E204:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.IsActive` — RVA `0xc4ef30`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsActive() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_IsActive_RVAc4ef30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12906292 = default(uint);
        uint __arm64_flags_result_12906292 = default(uint);
        uint __arm64_flags_right_12906292 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12906292 = unchecked((uint)(x8));
        __arm64_flags_right_12906292 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12906292 = unchecked((uint)((__arm64_flags_left_12906292) & (__arm64_flags_right_12906292)));
        x0 = unchecked((ulong)(((__arm64_flags_result_12906292 == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.get_rig` — RVA `0xc4f458`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public InputRig get_rig() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchControl_get_rig_RVAc4f458(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.set_rig` — RVA `0xc4f460`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_rig(InputRig value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_set_rig_RVAc4f460(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x1);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchControl.get_canvas` — RVA `0xc4f468`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public Canvas get_canvas() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchControl_get_canvas_RVAc4f468(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.set_canvas` — RVA `0xc4f470`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_canvas(Canvas value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_set_canvas_RVAc4f470(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x60UL))), x1);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchControl.get_panel` — RVA `0xc4f478`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public TouchControlPanel get_panel() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchControl_get_panel_RVAc4f478(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x68UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.set_panel` — RVA `0xc4f480`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void set_panel(TouchControlPanel value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_set_panel_RVAc4f480(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x68UL))), x1);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchControl.ctor` — RVA `0xc4f488`

- Lift status: **exact**; input span: 292 bytes; span to next metadata RVA: 292 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=47 (informational only).

```csharp
public static ulong TouchControl_ctor_RVAc4f488(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x20 = 0x1A8C000UL;
        x24 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x24BUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA90UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xD20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD28UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x4B0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x4B8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA90UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x24BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4F514;
        label_0xC4F514:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)0x2UL)) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)0x2UL)).ShiftLeftLogical(unchecked((int)0x20UL)));
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x28UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4F5B4UL /* metadata target: DisablingConditionSet.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2BD4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2BD4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x30UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `TouchControl.GetSubBindingDescriptions` — RVA `0xc4f664`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void GetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_GetSubBindingDescriptions_RVAc4f664(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x5 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x248UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x250UL))));
        return RuntimeCalls.InvokeIndirect(x5);
        return default(ulong);
    }
```

## `TouchControl.IsBoundToAxis` — RVA `0xc4f674`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_IsBoundToAxis_RVAc4f674(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x258UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x260UL))));
        return RuntimeCalls.InvokeIndirect(x4);
        return default(ulong);
    }
```

## `TouchControl.IsBoundToKey` — RVA `0xc4f684`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsBoundToKey(KeyCode key, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_IsBoundToKey_RVAc4f684(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x268UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x270UL))));
        return RuntimeCalls.InvokeIndirect(x4);
        return default(ulong);
    }
```

## `TouchControl.IsEmulatingTouches` — RVA `0xc4f694`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsEmulatingTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_IsEmulatingTouches_RVAc4f694(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x278UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x280UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `TouchControl.IsEmulatingMousePosition` — RVA `0xc4f6a4`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsEmulatingMousePosition() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_IsEmulatingMousePosition_RVAc4f6a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x288UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x290UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `TouchControl.IsUsingKeyForEmulation` — RVA `0xc4f6b4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public virtual bool IsUsingKeyForEmulation(KeyCode key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_IsUsingKeyForEmulation_RVAc4f6b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.OnGetSubBindingDescriptions` — RVA `0xc4f6bc`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `protected virtual void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_OnGetSubBindingDescriptions_RVAc4f6bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `TouchControl.OnIsBoundToAxis` — RVA `0xc4f6c0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected virtual bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_OnIsBoundToAxis_RVAc4f6c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.OnIsBoundToKey` — RVA `0xc4f6c8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected virtual bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_OnIsBoundToKey_RVAc4f6c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.OnIsEmulatingTouches` — RVA `0xc4f6d0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected virtual bool OnIsEmulatingTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_OnIsEmulatingTouches_RVAc4f6d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.OnIsEmulatingMousePosition` — RVA `0xc4f6d8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected virtual bool OnIsEmulatingMousePosition() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_OnIsEmulatingMousePosition_RVAc4f6d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.CheckSwipeOff` — RVA `0xc4f6e0`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `protected bool CheckSwipeOff(TouchObject touchObj, TouchControl.TouchStartType touchStartType) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static uint TouchControl_CheckSwipeOff_RVAc4f6e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12908284 = default(uint);
        uint __arm64_flags_left_12908292 = default(uint);
        uint __arm64_flags_right_12908284 = default(uint);
        uint __arm64_flags_right_12908292 = default(uint);
        ulong __arm64_pair_address_12908300 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC4F728;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x2CUL))))));
        x20 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4F728;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = x1;
        __arm64_flags_left_12908284 = unchecked((uint)(x2));
        __arm64_flags_right_12908284 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12908284) - (__arm64_flags_right_12908284))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4F70C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F704UL)));
        }
        __arm64_flags_left_12908292 = unchecked((uint)(x8));
        __arm64_flags_right_12908292 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12908292) - (__arm64_flags_right_12908292))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4F728;
        }
        else
        {
            goto label_0xC4F70C;
        }
        label_0xC4F70C:
        ;
        __arm64_pair_address_12908300 = unchecked((ulong)((x19) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12908300)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12908300) + (0x4UL))))), 0));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC50F2CUL /* metadata target: TouchControl.ScreenToLocalPos */, x0, x1, x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC52734UL /* metadata target: TouchControl.RaycastLocal */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4F738;
        }
        else
        {
            goto label_0xC4F728;
        }
        label_0xC4F728:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4F72C;
        label_0xC4F72C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC4F738:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4D288UL /* metadata target: TouchObject.ReleaseControl */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC4F72C;
        return default(uint);
    }
```

## `TouchControl.RaycastScreen` — RVA `0xc4f750`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public bool RaycastScreen(Vector2 screenPos, Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_RaycastScreen_RVAc4f750(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC50F2CUL /* metadata target: TouchControl.ScreenToLocalPos */, x0, x1, x2, x3);
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC52734UL /* metadata target: TouchControl.RaycastLocal */);
        return default(ulong);
    }
```

## `TouchControl.CanShareTouchWith` — RVA `0xc4f768`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public virtual bool CanShareTouchWith(TouchControl c) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_CanShareTouchWith_RVAc4f768(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.CanBeSwipedOverFromNothingDefault` — RVA `0xc4f770`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `protected bool CanBeSwipedOverFromNothingDefault(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchControl_CanBeSwipedOverFromNothingDefault_RVAc4f770(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12908412 = default(uint);
        uint __arm64_flags_result_12908412 = default(uint);
        uint __arm64_flags_right_12908412 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x26UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC4F788:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
            __arm64_flags_left_12908412 = unchecked((uint)(x8));
            __arm64_flags_right_12908412 = unchecked((uint)0xFFFFFFBFUL);
            __arm64_flags_result_12908412 = unchecked((uint)((__arm64_flags_left_12908412) & (__arm64_flags_right_12908412)));
            x0 = unchecked((ulong)(((__arm64_flags_result_12908412 == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `TouchControl.CanBeSwipedOverFromRestrictedListDefault` — RVA `0xc4f790`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `protected bool CanBeSwipedOverFromRestrictedListDefault(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_CanBeSwipedOverFromRestrictedListDefault_RVAc4f790(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12908436 = default(uint);
        uint __arm64_flags_result_12908436 = default(uint);
        uint __arm64_flags_right_12908436 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12908436 = unchecked((uint)(x8));
        __arm64_flags_right_12908436 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12908436 = unchecked((uint)((__arm64_flags_left_12908436) & (__arm64_flags_right_12908436)));
        x0 = unchecked((ulong)(((__arm64_flags_result_12908436 == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.CanSwipeOverOthersDefault` — RVA `0xc4f7a0`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `protected bool CanSwipeOverOthersDefault(TouchObject touchObj, TouchObject myTouchObj, TouchControl.TouchStartType touchStartType) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static uint TouchControl_CanSwipeOverOthersDefault_RVAc4f7a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12908448 = default(ulong);
        uint __arm64_flags_left_12908460 = default(uint);
        ulong __arm64_flags_left_12908468 = default(ulong);
        uint __arm64_flags_left_12908480 = default(uint);
        uint __arm64_flags_left_12908488 = default(uint);
        ulong __arm64_flags_right_12908448 = default(ulong);
        uint __arm64_flags_right_12908460 = default(uint);
        ulong __arm64_flags_right_12908468 = default(ulong);
        uint __arm64_flags_right_12908480 = default(uint);
        uint __arm64_flags_right_12908488 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12908448 = x2;
        __arm64_flags_right_12908448 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12908448) - (__arm64_flags_right_12908448))) == 0x0UL))))
        {
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x28UL))))));
            __arm64_flags_left_12908460 = unchecked((uint)(x8));
            __arm64_flags_right_12908460 = unchecked((uint)0x1UL);
            if ((!((unchecked((uint)((__arm64_flags_left_12908460) - (__arm64_flags_right_12908460))) == unchecked((uint)0x0UL)))))
            {
                label_0xC4F7C0:
                ;
                __arm64_flags_left_12908480 = unchecked((uint)(x8));
                __arm64_flags_right_12908480 = unchecked((uint)0x2UL);
                x8 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12908480) - (__arm64_flags_right_12908480))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                __arm64_flags_left_12908488 = unchecked((uint)(x3));
                __arm64_flags_right_12908488 = unchecked((uint)0x2UL);
                x9 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12908488) - (__arm64_flags_right_12908488))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
                return unchecked((uint)(x0));
            }
        }
        label_0xC4F7B4:
        ;
        __arm64_flags_left_12908468 = x2;
        __arm64_flags_right_12908468 = x1;
        x0 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12908468) - (__arm64_flags_right_12908468))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.CanBeTouchedDirectly` — RVA `0xc4f7d8`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public virtual bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchControl_CanBeTouchedDirectly_RVAc4f7d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12908524 = default(uint);
        uint __arm64_flags_result_12908524 = default(uint);
        uint __arm64_flags_right_12908524 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x23UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC4F7E8:
            ;
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x50UL))))));
            __arm64_flags_left_12908524 = unchecked((uint)(x8));
            __arm64_flags_right_12908524 = unchecked((uint)0xFFFFFFBFUL);
            __arm64_flags_result_12908524 = unchecked((uint)((__arm64_flags_left_12908524) & (__arm64_flags_right_12908524)));
            x0 = unchecked((ulong)(((__arm64_flags_result_12908524 == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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

## `TouchControl.CanBeActivatedByOtherControl` — RVA `0xc4f7f8`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public virtual bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_CanBeActivatedByOtherControl_RVAc4f7f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12908540 = default(uint);
        uint __arm64_flags_result_12908540 = default(uint);
        uint __arm64_flags_right_12908540 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12908540 = unchecked((uint)(x8));
        __arm64_flags_right_12908540 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12908540 = unchecked((uint)((__arm64_flags_left_12908540) & (__arm64_flags_right_12908540)));
        x0 = unchecked((ulong)(((__arm64_flags_result_12908540 == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.CompareByDepth` — RVA `0xc4f808`

- Lift status: **partial**; input span: 376 bytes; span to next metadata RVA: 376 bytes.
- Metadata signature: `public static int CompareByDepth(TouchControl a, TouchControl b) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=48 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cneg' at 0xc4f900; reason: Unknown IR expression at 0xc4f900; reason: Unsupported instruction 'fabd' at 0xc4f948; reason: Unsupported instruction 'csinc' at 0xc4f95c; reason: Unknown IR expression at 0xc4f95c

```csharp
public static uint TouchControl_CompareByDepth_RVAc4f808(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12908792 = default(uint);
        uint __arm64_flags_result_12908792 = default(uint);
        uint __arm64_flags_right_12908792 = default(uint);
        float __arm64_float_flags_left_12908876 = default(float);
        float __arm64_float_flags_left_12908884 = default(float);
        float __arm64_float_flags_right_12908876 = default(float);
        float __arm64_float_flags_right_12908884 = default(float);
        ulong __arm64_load_address_12908916 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x24CUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F848;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x24CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4F848;
        label_0xC4F848:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F858;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F854UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4F858;
        label_0xC4F858:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F890;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F87C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F878UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4F87C;
        label_0xC4F87C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4F908;
        }
        else
        {
            goto label_0xC4F890;
        }
        label_0xC4F890:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F8A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F89CUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4F8A0;
        label_0xC4F8A0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4F8D8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F8C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F8C0UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4F8C4;
        label_0xC4F8C4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F964;
        }
        else
        {
            goto label_0xC4F8D8;
        }
        label_0xC4F8D8:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F8E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F8E4UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4F8E8;
        label_0xC4F8E8:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        __arm64_flags_left_12908792 = unchecked((uint)(x0));
        __arm64_flags_right_12908792 = unchecked((uint)0x1UL);
        __arm64_flags_result_12908792 = unchecked((uint)((__arm64_flags_left_12908792) & (__arm64_flags_right_12908792)));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("cneg", 0xC4F900UL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((-(unchecked((uint)(x8)))))) : unchecked((uint)(x8)))));
        goto label_0xC4F968;
        label_0xC4F908:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC4F97C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F97C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v8 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F97C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        RuntimeCalls.Unsupported("fabd", 0xC4F948UL);
        __arm64_float_flags_left_12908876 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12908876 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12908876 < __arm64_float_flags_right_12908876))
        {
            goto label_0xC4F964;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC4F954UL)));
        }
        __arm64_float_flags_left_12908884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12908884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeCalls.Unsupported("csinc", 0xC4F95CUL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)((unchecked((uint)0x0UL)) + (unchecked((uint)0x1UL)))))));
        goto label_0xC4F968;
        label_0xC4F964:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4F968;
        label_0xC4F968:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_12908916 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12908916)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12908916) + (0x30UL)));
        return unchecked((uint)(x0));
        label_0xC4F97C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `TouchControl.ShowOrHideControl` — RVA `0xc4f980`

- Lift status: **partial**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public void ShowOrHideControl(bool show, bool noAnim = false) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=12 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xc4f9a4; reason: Unknown IR expression at 0xc4f9a4

```csharp
public static ulong TouchControl_ShowOrHideControl_RVAc4f980(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12908956 = default(uint);
        uint __arm64_flags_result_12908956 = default(uint);
        uint __arm64_flags_right_12908956 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        x9 = unchecked((ulong)((~(unchecked((uint)(x1))))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x20 = x0;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)0xFFFFFFFFFFFFFFFEUL))))) | (unchecked((uint)((unchecked((uint)((unchecked((uint)(x9))) >> (int)(unchecked((int)(unchecked((uint)0x0UL))))))) & (unchecked((uint)0x1UL)))))))));
        __arm64_flags_left_12908956 = unchecked((uint)(x8));
        __arm64_flags_right_12908956 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12908956 = unchecked((uint)((__arm64_flags_left_12908956) & (__arm64_flags_right_12908956)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x50UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.eq", 0xC4F9A4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4F9BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC4F9BC;
        label_0xC4F9BC:
        ;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)(0x1UL)))))));
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4FA14UL /* metadata target: TouchControl.SyncBaseAlphaToHidingConditions */);
        return default(ulong);
    }
```

## `TouchControl.SetHidingFlag` — RVA `0xc4f9d0`

- Lift status: **partial**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `public void SetHidingFlag(int flagBit, bool state) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=7 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc4f9f0; reason: Unknown IR expression at 0xc4f9f0; reason: Unsupported instruction 'b.eq' at 0xc4f9fc; reason: Unknown IR expression at 0xc4f9fc

```csharp
public static ulong TouchControl_SetHidingFlag_RVAc4f9d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909008 = default(uint);
        uint __arm64_flags_left_12909028 = default(uint);
        uint __arm64_flags_left_12909044 = default(uint);
        uint __arm64_flags_result_12909028 = default(uint);
        uint __arm64_flags_result_12909044 = default(uint);
        uint __arm64_flags_right_12909008 = default(uint);
        uint __arm64_flags_right_12909028 = default(uint);
        uint __arm64_flags_right_12909044 = default(uint);
        ulong x10 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12909008 = unchecked((uint)(x1));
        __arm64_flags_right_12909008 = unchecked((uint)0x1FUL);
        if (((__arm64_flags_left_12909008 >= __arm64_flags_right_12909008) && (!((unchecked((uint)((__arm64_flags_left_12909008) - (__arm64_flags_right_12909008))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC4FA10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x1)))))))));
        __arm64_flags_left_12909028 = unchecked((uint)(x2));
        __arm64_flags_right_12909028 = unchecked((uint)0x1UL);
        __arm64_flags_result_12909028 = unchecked((uint)((__arm64_flags_left_12909028) & (__arm64_flags_right_12909028)));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) | (unchecked((uint)(x9)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & ((~(unchecked((uint)(x9)))))))));
        RuntimeCalls.Unsupported("csel", 0xC4F9F0UL);
        x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x10)) : unchecked((uint)(x8)))));
        __arm64_flags_left_12909044 = unchecked((uint)(x8));
        __arm64_flags_right_12909044 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12909044 = unchecked((uint)((__arm64_flags_left_12909044) & (__arm64_flags_right_12909044)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x50UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.eq", 0xC4F9FCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4FA10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC4FA10:
        ;
        return x0;
        return default(ulong);
    }
```

## `TouchControl.SyncBaseAlphaToHidingConditions` — RVA `0xc4fa14`

- Lift status: **partial**; input span: 252 bytes; span to next metadata RVA: 252 bytes.
- Metadata signature: `private void SyncBaseAlphaToHidingConditions(bool noAnim) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=25 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fcsel' at 0xc4fa64; reason: Unknown IR expression at 0xc4fa64; reason: Unsupported instruction 'fabd' at 0xc4fa7c

```csharp
public static ulong TouchControl_SyncBaseAlphaToHidingConditions_RVAc4fa14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909144 = default(uint);
        uint __arm64_flags_left_12909160 = default(uint);
        uint __arm64_flags_right_12909144 = default(uint);
        uint __arm64_flags_right_12909160 = default(uint);
        float __arm64_float_flags_left_12909184 = default(float);
        float __arm64_float_flags_left_12909268 = default(float);
        float __arm64_float_flags_right_12909184 = default(float);
        float __arm64_float_flags_right_12909268 = default(float);
        ulong __arm64_pair_address_12909076 = default(ulong);
        ulong __arm64_pair_address_12909272 = default(ulong);
        ulong __arm64_pair_address_12909316 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12909076 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12909076, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12909076) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12909076;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x251UL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FA48;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x251UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4FA48;
        label_0xC4FA48:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x71UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_flags_left_12909144 = unchecked((uint)(x8));
        __arm64_flags_right_12909144 = unchecked((uint)0x0UL);
        x10 = unchecked((ulong)(unchecked((uint)(0x78UL))));
        x11 = unchecked((ulong)(unchecked((uint)(0x7CUL))));
        RuntimeCalls.Unsupported("fcsel", 0xC4FA64UL);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))), 0));
        __arm64_flags_left_12909160 = unchecked((uint)(x9));
        __arm64_flags_right_12909160 = unchecked((uint)0x0UL);
        x8 = ((unchecked((uint)((__arm64_flags_left_12909160) - (__arm64_flags_right_12909160))) == unchecked((uint)0x0UL)) ? x11 : x10);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (x8))))), 0));
        x8 = 0x432000UL;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        RuntimeCalls.Unsupported("fabd", 0xC4FA7CUL);
        __arm64_float_flags_left_12909184 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12909184 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12909184 <= __arm64_float_flags_right_12909184) || ((__arm64_float_flags_left_12909184 != __arm64_float_flags_left_12909184) || (__arm64_float_flags_right_12909184 != __arm64_float_flags_right_12909184))))
        {
            goto label_0xC4FAFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4FA88UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FAA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4FAA4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4FAA8;
        label_0xC4FAA8:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4FB0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4FAC4UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x54UL))))), 0));
        goto label_0xC4FAC8;
        label_0xC4FAC8:
        ;
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x7CUL))))), 0));
        __arm64_float_flags_left_12909268 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12909268 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_pair_address_12909272 = unchecked((ulong)((x19) + (0x74UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12909272, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12909272) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        if ((__arm64_float_flags_left_12909268 <= __arm64_float_flags_right_12909268))
        {
            goto label_0xC4FAF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x84UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x71UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x80UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        goto label_0xC4FAFC;
        label_0xC4FAF4:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x71UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x7CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        goto label_0xC4FAFC;
        label_0xC4FAFC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_pair_address_12909316 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12909316)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12909316) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12909316) + (0x30UL)));
        return x0;
        label_0xC4FB0C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.ShowControl` — RVA `0xc4fb10`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void ShowControl(bool noAnim = false) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchControl_ShowControl_RVAc4fb10(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return RuntimeCalls.InvokeDirect(0xC4F980UL /* metadata target: TouchControl.ShowOrHideControl */);
        return default(ulong);
    }
```

## `TouchControl.HideControl` — RVA `0xc4fb1c`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void HideControl(bool noAnim = false) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchControl_HideControl_RVAc4fb1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return RuntimeCalls.InvokeDirect(0xC4F980UL /* metadata target: TouchControl.ShowOrHideControl */);
        return default(ulong);
    }
```

## `TouchControl.IsHiddenManually` — RVA `0xc4fb28`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsHiddenManually() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchControl_IsHiddenManually_RVAc4fb28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909356 = default(uint);
        uint __arm64_flags_right_12909356 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12909356 = unchecked((uint)(x8));
        __arm64_flags_right_12909356 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12909356) - (__arm64_flags_right_12909356))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.ToggleVisibility` — RVA `0xc4fb38`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `public void ToggleVisibility(bool noAnim) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_ToggleVisibility_RVAc4fb38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909376 = default(uint);
        uint __arm64_flags_right_12909376 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12909376 = unchecked((uint)(x8));
        __arm64_flags_right_12909376 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12909376) - (__arm64_flags_right_12909376))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x8))));
        return RuntimeCalls.InvokeDirect(0xC4F980UL /* metadata target: TouchControl.ShowOrHideControl */);
        return default(ulong);
    }
```

## `TouchControl.ToggleVisibility` — RVA `0xc4fb50`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void ToggleVisibility() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchControl_ToggleVisibility_RVAc4fb50(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909400 = default(uint);
        uint __arm64_flags_right_12909400 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        __arm64_flags_left_12909400 = unchecked((uint)(x8));
        __arm64_flags_right_12909400 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12909400) - (__arm64_flags_right_12909400))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return RuntimeCalls.InvokeDirect(0xC4F980UL /* metadata target: TouchControl.ShowOrHideControl */);
        return default(ulong);
    }
```

## `TouchControl.IsActiveButInvisible` — RVA `0xc4fb64`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public bool IsActiveButInvisible() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static uint TouchControl_IsActiveButInvisible_RVAc4fb64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909420 = default(uint);
        uint __arm64_flags_result_12909420 = default(uint);
        uint __arm64_flags_right_12909420 = default(uint);
        float __arm64_float_flags_left_12909460 = default(float);
        float __arm64_float_flags_right_12909460 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12909420 = unchecked((uint)(x8));
        __arm64_flags_right_12909420 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12909420 = unchecked((uint)((__arm64_flags_left_12909420) & (__arm64_flags_right_12909420)));
        if ((__arm64_flags_result_12909420 == unchecked((uint)0x0UL)))
        {
            label_0xC4FB7C:
            ;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)(unchecked((uint)(x0)))));
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x358UL))));
            x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x360UL))));
            x0 = RuntimeCalls.InvokeIndirect(x9, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
            x8 = 0x432000UL;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
            __arm64_float_flags_left_12909460 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12909460 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            x0 = unchecked((ulong)(((__arm64_float_flags_left_12909460 <= __arm64_float_flags_right_12909460) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        label_0xC4FB9C:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.IsActiveAndVisible` — RVA `0xc4fba4`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public bool IsActiveAndVisible() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static uint TouchControl_IsActiveAndVisible_RVAc4fba4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909484 = default(uint);
        uint __arm64_flags_result_12909484 = default(uint);
        uint __arm64_flags_right_12909484 = default(uint);
        float __arm64_float_flags_left_12909524 = default(float);
        float __arm64_float_flags_right_12909524 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12909484 = unchecked((uint)(x8));
        __arm64_flags_right_12909484 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12909484 = unchecked((uint)((__arm64_flags_left_12909484) & (__arm64_flags_right_12909484)));
        if ((__arm64_flags_result_12909484 == unchecked((uint)0x0UL)))
        {
            label_0xC4FBBC:
            ;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)(unchecked((uint)(x0)))));
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x358UL))));
            x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x360UL))));
            x0 = RuntimeCalls.InvokeIndirect(x9, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
            x8 = 0x432000UL;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
            __arm64_float_flags_left_12909524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12909524 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            x0 = unchecked((ulong)(((__arm64_float_flags_left_12909524 > __arm64_float_flags_right_12909524) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        label_0xC4FBDC:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.SyncDisablingConditions` — RVA `0xc4fbe4`

- Lift status: **partial**; input span: 380 bytes; span to next metadata RVA: 380 bytes.
- Metadata signature: `public void SyncDisablingConditions(bool skipAnim) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=55 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc4fc44; reason: Unknown IR expression at 0xc4fc44; reason: Unsupported instruction 'b.eq' at 0xc4fc70; reason: Unknown IR expression at 0xc4fc70; reason: Unsupported instruction 'csel' at 0xc4fcc8; reason: Unknown IR expression at 0xc4fcc8; reason: Unsupported instruction 'b.eq' at 0xc4fcdc; reason: Unknown IR expression at 0xc4fcdc

```csharp
public static ulong TouchControl_SyncDisablingConditions_RVAc4fbe4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12909628 = default(uint);
        uint __arm64_flags_left_12909672 = default(uint);
        uint __arm64_flags_left_12909760 = default(uint);
        uint __arm64_flags_left_12909780 = default(uint);
        uint __arm64_flags_left_12909836 = default(uint);
        uint __arm64_flags_result_12909628 = default(uint);
        uint __arm64_flags_result_12909672 = default(uint);
        uint __arm64_flags_result_12909760 = default(uint);
        uint __arm64_flags_result_12909780 = default(uint);
        uint __arm64_flags_result_12909836 = default(uint);
        uint __arm64_flags_right_12909628 = default(uint);
        uint __arm64_flags_right_12909672 = default(uint);
        uint __arm64_flags_right_12909760 = default(uint);
        uint __arm64_flags_right_12909780 = default(uint);
        uint __arm64_flags_right_12909836 = default(uint);
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
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x24DUL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FC14;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x24DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4FC14;
        label_0xC4FC14:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791624UL /* metadata target: Behaviour.get_enabled */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4FC4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4FD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794D50UL /* metadata target: GameObject.get_activeInHierarchy */, x0, x1, x2, x3);
        __arm64_flags_left_12909628 = unchecked((uint)(x0));
        __arm64_flags_right_12909628 = unchecked((uint)0x1UL);
        __arm64_flags_result_12909628 = unchecked((uint)((__arm64_flags_left_12909628) & (__arm64_flags_right_12909628)));
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        RuntimeCalls.Unsupported("csel", 0xC4FC44UL);
        x8 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x0UL) : unchecked((uint)(x8)))));
        goto label_0xC4FC50;
        label_0xC4FC4C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        goto label_0xC4FC50;
        label_0xC4FC50:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC4FD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(0xFFFFFFFDUL)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) | (unchecked((uint)(x8)))))));
        __arm64_flags_left_12909672 = unchecked((uint)(x8));
        __arm64_flags_right_12909672 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12909672 = unchecked((uint)((__arm64_flags_left_12909672) & (__arm64_flags_right_12909672)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x50UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.eq", 0xC4FC70UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4FC88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC4FC88;
        label_0xC4FC88:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FC9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4FC98UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4FC9C;
        label_0xC4FC9C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4FD2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4FD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4FCB8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC4FD60UL /* metadata target: DisablingConditionSet.IsInEffect */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        __arm64_flags_left_12909760 = unchecked((uint)(x0));
        __arm64_flags_right_12909760 = unchecked((uint)0x1UL);
        __arm64_flags_result_12909760 = unchecked((uint)((__arm64_flags_left_12909760) & (__arm64_flags_right_12909760)));
        x9 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        RuntimeCalls.Unsupported("csel", 0xC4FCC8UL);
        x9 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)0x0UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0xFFFFFFEFUL)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) | (unchecked((uint)(x9)))))));
        __arm64_flags_left_12909780 = unchecked((uint)(x8));
        __arm64_flags_right_12909780 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12909780 = unchecked((uint)((__arm64_flags_left_12909780) & (__arm64_flags_right_12909780)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x50UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.eq", 0xC4FCDCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4FCF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC4FCF4;
        label_0xC4FCF4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4FD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(0xFFFFFFDFUL)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) | (unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x5UL))))))))))));
        __arm64_flags_left_12909836 = unchecked((uint)(x8));
        __arm64_flags_right_12909836 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12909836 = unchecked((uint)((__arm64_flags_left_12909836) & (__arm64_flags_right_12909836)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x50UL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.eq", 0xC4FD14UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC4FD2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC4FD2C;
        label_0xC4FD2C:
        ;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4FA14UL /* metadata target: TouchControl.SyncBaseAlphaToHidingConditions */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4FD50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4FE90UL /* metadata target: TouchControl.UpdateAnimators */);
        label_0xC4FD50:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4FD5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `TouchControl.UpdateAnimators` — RVA `0xc4fe90`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `protected void UpdateAnimators(bool skipAnim) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=24 (informational only).

```csharp
public static ulong TouchControl_UpdateAnimators_RVAc4fe90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12910316 = default(uint);
        uint __arm64_flags_right_12910316 = default(uint);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x250UL))))))));
        x21 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FED0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x250UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4FED0;
        label_0xC4FED0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4FF1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD48UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)(0x1UL)))))));
        goto label_0xC4FEE8;
        label_0xC4FEE8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12910316 = unchecked((uint)(x20));
        __arm64_flags_right_12910316 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12910316) - (__arm64_flags_right_12910316))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12910316)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12910316)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12910316) - (__arm64_flags_right_12910316))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12910316)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC4FF20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC4FF1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC635C4UL /* metadata target: TouchControlAnimatorBase.UpdateAnimator */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC4FEE8;
        }
        else
        {
            goto label_0xC4FF1C;
        }
        label_0xC4FF1C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC4FF20;
        label_0xC4FF20:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `TouchControl.AddAnimator` — RVA `0xc4ff30`

- Lift status: **exact**; input span: 228 bytes; span to next metadata RVA: 228 bytes.
- Metadata signature: `public void AddAnimator(TouchControlAnimatorBase a) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=37 (informational only).

```csharp
public static ulong TouchControl_AddAnimator_RVAc4ff30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12910536 = default(uint);
        uint __arm64_flags_right_12910536 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x24EUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4FF6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x24EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4FF6C;
        label_0xC4FF6C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC50010;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD58UL))));
        x1 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A36C0UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4FF98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4FF98:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC50010;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD50UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC50010;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12910536 = unchecked((uint)(x10));
        __arm64_flags_right_12910536 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12910536 >= __arm64_flags_right_12910536))
        {
            goto label_0xC4FFF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x19);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = x8;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC4FFF4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x10A3390UL);
        label_0xC50010:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.RemoveAnimator` — RVA `0xc50014`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `public void RemoveAnimator(TouchControlAnimatorBase a) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong TouchControl_RemoveAnimator_RVAc50014(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x24FUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50050;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x24FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50050;
        label_0xC50050:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC500A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD58UL))));
        x1 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A36C0UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50094;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC500A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD60UL))));
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x10A4650UL);
        label_0xC50094:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC500A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.GetAnimatorList` — RVA `0xc500a4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public List<TouchControlAnimatorBase> GetAnimatorList() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchControl_GetAnimatorList_RVAc500a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.StartAlphaAnim` — RVA `0xc500ac`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void StartAlphaAnim(float targetAlpha, float duration) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchControl_StartAlphaAnim_RVAc500ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12910776 = default(float);
        float __arm64_float_flags_right_12910776 = default(float);
        ulong __arm64_pair_address_12910780 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2E8UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x7CUL))))), 0));
        __arm64_float_flags_left_12910776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12910776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_pair_address_12910780 = unchecked((ulong)((x0) + (0x74UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12910780, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12910780) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((__arm64_float_flags_left_12910776 <= __arm64_float_flags_right_12910776))
        {
            label_0xC500D8:
            ;
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x71UL))), unchecked((byte)(unchecked((uint)0x0UL))));
            RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x7CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            return x0;
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x84UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x71UL))), unchecked((byte)(unchecked((uint)(x8)))));
            RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x80UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.UpdateBaseAlpha` — RVA `0xc500e4`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `private void UpdateBaseAlpha() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_UpdateBaseAlpha_RVAc500e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12910860 = default(float);
        float __arm64_float_flags_left_12910884 = default(float);
        float __arm64_float_flags_right_12910860 = default(float);
        float __arm64_float_flags_right_12910884 = default(float);
        float __arm64_fp_left_12910880 = default(float);
        float __arm64_fp_right_12910880 = default(float);
        ulong __arm64_load_address_12910928 = default(ulong);
        ulong __arm64_pair_address_12910868 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x71UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x84UL))))), 0));
            x19 = x0;
            x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, x1, x2, x3);
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x80UL))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x84UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            __arm64_float_flags_left_12910860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12910860 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            if ((__arm64_float_flags_left_12910860 >= __arm64_float_flags_right_12910860))
            {
                label_0xC50140:
                ;
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x78UL))))), 0));
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x71UL))), unchecked((byte)(unchecked((uint)0x0UL))));
            }
            else
            {
                __arm64_pair_address_12910868 = unchecked((ulong)((x19) + (0x74UL)));
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12910868)), 0));
                v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12910868) + (0x4UL))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
                __arm64_fp_left_12910880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                __arm64_fp_right_12910880 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12910880 != __arm64_fp_left_12910880) ? __arm64_fp_left_12910880 : ((__arm64_fp_right_12910880 != __arm64_fp_right_12910880) ? __arm64_fp_right_12910880 : (((__arm64_fp_left_12910880 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12910880 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12910880), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12910880), 0))))), 0) : ((__arm64_fp_left_12910880 <= __arm64_fp_right_12910880) ? __arm64_fp_left_12910880 : __arm64_fp_right_12910880))))), 0));
                __arm64_float_flags_left_12910884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
                __arm64_float_flags_right_12910884 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12910884 >= __arm64_float_flags_right_12910884) || ((__arm64_float_flags_left_12910884 != __arm64_float_flags_left_12910884) || (__arm64_float_flags_right_12910884 != __arm64_float_flags_right_12910884))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
                v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
                v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            }
            label_0xC50148:
            ;
            RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x7CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        }
        label_0xC5014C:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12910928 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12910928)), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.GetBaseAlpha` — RVA `0xc50158`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float GetBaseAlpha() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_GetBaseAlpha_RVAc50158(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x7CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.GetAlpha` — RVA `0xc50160`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public virtual float GetAlpha() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_GetAlpha_RVAc50160(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x7CUL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.SetRig` — RVA `0xc50168`

- Lift status: **exact**; input span: 376 bytes; span to next metadata RVA: 376 bytes.
- Metadata signature: `public void SetRig(InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong TouchControl_SetRig_RVAc50168(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x21 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x253UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC501A4;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x253UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC501A4;
        label_0xC501A4:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC501B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC501B0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC501B4;
        label_0xC501B4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC501FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC501C8UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC502DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x21UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC501DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC501FC;
        label_0xC501DC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC501FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC501FC;
        label_0xC501FC:
        ;
        x21 = x19;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x58UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50214;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50210UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50214;
        label_0xC50214:
        ;
        x0 = x22;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC502B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x22 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5023C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50238UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5023C;
        label_0xC5023C:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50264;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC502DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3C0ACUL /* metadata target: InputRig.RemoveControl */, x0, x1, x2, x3);
        goto label_0xC50264;
        label_0xC50264:
        ;
        x0 = x21;
        x1 = x20;
        RuntimeMemory.WriteU64(x21, x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50288;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50284UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50288;
        label_0xC50288:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC502B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC502DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BFE4UL /* metadata target: InputRig.AddControl */, x0, x1, x2, x3);
        goto label_0xC502B0;
        label_0xC502B0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC502DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4FBE4UL /* metadata target: TouchControl.SyncDisablingConditions */);
        label_0xC502DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `TouchControl.SetTouchControlPanel` — RVA `0xc50318`

- Lift status: **exact**; input span: 352 bytes; span to next metadata RVA: 352 bytes.
- Metadata signature: `public void SetTouchControlPanel(TouchControlPanel panel) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=52 (informational only).

```csharp
public static ulong TouchControl_SetTouchControlPanel_RVAc50318(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x20 = 0x1BAB000UL;
        x23 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x254UL))))))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xD8UL))));
        x21 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50354;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x254UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50354;
        label_0xC50354:
        ;
        x20 = x19;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5036C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50368UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5036C;
        label_0xC5036C:
        ;
        x0 = x22;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x22 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50394;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50390UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50394;
        label_0xC50394:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC503B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC50474;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC50478UL /* metadata target: TouchControlPanel.RemoveControl */, x0, x1, x2, x3);
        goto label_0xC503B8;
        label_0xC503B8:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC503C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC503C4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC503C8;
        label_0xC503C8:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC503DCUL);
        }
        if ((x21 == 0x0UL))
        {
            goto label_0xC50474;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x21UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC503F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x0UL;
        goto label_0xC50410;
        label_0xC503F0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50410;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x21);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = x21;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC50410;
        label_0xC50410:
        ;
        x0 = x20;
        x1 = x21;
        RuntimeMemory.WriteU64(x20, x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x21 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50434;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50430UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50434;
        label_0xC50434:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC50474;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC50500UL /* metadata target: TouchControlPanel.AddControl */);
        label_0xC50464:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC50474:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.InvalidateHierarchy` — RVA `0xc5060c`

- Lift status: **exact**; input span: 808 bytes; span to next metadata RVA: 808 bytes.
- Metadata signature: `public virtual void InvalidateHierarchy() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=125 (informational only).

```csharp
public static ulong TouchControl_InvalidateHierarchy_RVAc5060c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12912488 = default(uint);
        uint __arm64_flags_left_12912564 = default(uint);
        uint __arm64_flags_left_12912640 = default(uint);
        uint __arm64_flags_result_12912488 = default(uint);
        uint __arm64_flags_result_12912564 = default(uint);
        uint __arm64_flags_result_12912640 = default(uint);
        uint __arm64_flags_right_12912488 = default(uint);
        uint __arm64_flags_right_12912564 = default(uint);
        uint __arm64_flags_right_12912640 = default(uint);
        ulong sp = default(ulong);
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
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x255UL))))))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x255UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50670;
        label_0xC50670:
        ;
        x0 = x20;
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC50930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x27 = 0x1A8C000UL;
        x28 = 0x1A8C000UL;
        x29 = 0x1A8C000UL;
        x19 = 0x1A8C000UL;
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xD8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0xD78UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0xD70UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD68UL))));
        x23 = x0;
        x22 = 0x0UL;
        x20 = 0x0UL;
        x21 = 0x0UL;
        goto label_0xC506B4;
        label_0xC506B4:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D400UL /* metadata target: Transform.get_parent */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x27);
        x23 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC506D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC506D8;
        label_0xC506D8:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50874;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC506ECUL);
        }
        if ((x23 == 0x0UL))
        {
            goto label_0xC50930;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x28);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x29);
        x26 = x0;
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x19);
        x25 = x0;
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x27);
        x24 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50734;
        label_0xC50734:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50770;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50758;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50754UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50758;
        label_0xC50758:
        ;
        x0 = x26;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        __arm64_flags_left_12912488 = unchecked((uint)(x0));
        __arm64_flags_right_12912488 = unchecked((uint)0x1UL);
        __arm64_flags_result_12912488 = unchecked((uint)((__arm64_flags_left_12912488) & (__arm64_flags_right_12912488)));
        x20 = ((!((__arm64_flags_result_12912488 == unchecked((uint)0x0UL)))) ? x26 : x20);
        goto label_0xC50770;
        label_0xC50770:
        ;
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5077CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50780;
        label_0xC50780:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC507BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC507A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC507A0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC507A4;
        label_0xC507A4:
        ;
        x0 = x25;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        __arm64_flags_left_12912564 = unchecked((uint)(x0));
        __arm64_flags_right_12912564 = unchecked((uint)0x1UL);
        __arm64_flags_result_12912564 = unchecked((uint)((__arm64_flags_left_12912564) & (__arm64_flags_right_12912564)));
        x21 = ((!((__arm64_flags_result_12912564 == unchecked((uint)0x0UL)))) ? x25 : x21);
        goto label_0xC507BC;
        label_0xC507BC:
        ;
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC507CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC507C8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC507CC;
        label_0xC507CC:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50808;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC507F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC507ECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC507F0;
        label_0xC507F0:
        ;
        x0 = x24;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        __arm64_flags_left_12912640 = unchecked((uint)(x0));
        __arm64_flags_right_12912640 = unchecked((uint)0x1UL);
        __arm64_flags_result_12912640 = unchecked((uint)((__arm64_flags_left_12912640) & (__arm64_flags_right_12912640)));
        x22 = ((!((__arm64_flags_result_12912640 == unchecked((uint)0x0UL)))) ? x24 : x22);
        goto label_0xC50808;
        label_0xC50808:
        ;
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50818;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50814UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50818;
        label_0xC50818:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC506B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5083C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50838UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5083C;
        label_0xC5083C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC506B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x27);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50860;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5085CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50860;
        label_0xC50860:
        ;
        x0 = x22;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC506B4;
        }
        else
        {
            goto label_0xC50874;
        }
        label_0xC50874:
        ;
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x1 = x22;
        x23 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0x60UL))), x22);
        x0 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x27);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xFFFFFFFFFFFFFFF8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC508A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5089CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC508A0;
        label_0xC508A0:
        ;
        x0 = x22;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC508C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC50168UL /* metadata target: TouchControl.SetRig */, x0, x1, x2, x3);
        goto label_0xC508C0;
        label_0xC508C0:
        ;
        x0 = RuntimeMemory.ReadU64(x27);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC508D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC508D0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC508D4;
        label_0xC508D4:
        ;
        x0 = x21;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50910;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = x20;
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
        return RuntimeCalls.InvokeDirect(0xC50318UL /* metadata target: TouchControl.SetTouchControlPanel */);
        label_0xC50910:
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
        return x0;
        label_0xC50930:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.GetWorldPos` — RVA `0xc50934`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public Vector3 GetWorldPos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchControl_GetWorldPos_RVAc50934(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC50950;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */);
        label_0xC50950:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.SetWorldPos` — RVA `0xc50954`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public virtual void SetWorldPos(Vector2 pos2D) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_SetWorldPos_RVAc50954(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC50958UL /* metadata target: TouchControl.SetWorldPosRaw */);
        return default(ulong);
    }
```

## `TouchControl.SetWorldPosRaw` — RVA `0xc50958`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `protected void SetWorldPosRaw(Vector2 pos2D) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong TouchControl_SetWorldPosRaw_RVAc50958(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12912984 = default(ulong);
        ulong __arm64_pair_address_12913044 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        __arm64_pair_address_12912984 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12912984, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12912984) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12912984;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        v8 = v1;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC5099C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = v9;
        v1 = v8;
        x1 = 0x0UL;
        __arm64_pair_address_12913044 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12913044)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12913044) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12913044) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0x179D5A8UL /* metadata target: Transform.set_position */);
        label_0xC5099C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.GetLocalRect` — RVA `0xc509a0`

- Lift status: **exact**; input span: 260 bytes; span to next metadata RVA: 260 bytes.
- Metadata signature: `public virtual Rect GetLocalRect() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=43 (informational only).

```csharp
public static ulong TouchControl_GetLocalRect_RVAc509a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12913152 = default(ulong);
        uint __arm64_flags_left_12913248 = default(uint);
        ulong __arm64_flags_right_12913152 = default(ulong);
        uint __arm64_flags_right_12913248 = default(uint);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x256UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC509D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x256UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC509D8;
        label_0xC509D8:
        ;
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC50A0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1C8UL))));
        x9 = RuntimeMemory.ReadU64(x0);
        x8 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12913152 = x9;
        __arm64_flags_right_12913152 = x8;
        x20 = ((unchecked((ulong)((__arm64_flags_left_12913152) - (__arm64_flags_right_12913152))) == 0x0UL) ? x0 : 0x0UL);
        goto label_0xC50A10;
        label_0xC50A0C:
        ;
        x20 = 0x0UL;
        goto label_0xC50A10;
        label_0xC50A10:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50A20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50A1CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50A20;
        label_0xC50A20:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50A48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50A44UL);
        }
        goto label_0xC50A94;
        label_0xC50A48:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC50AA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179C4BCUL /* metadata target: RectTransform.get_rect */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x38UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12913248 = unchecked((uint)(x8));
        __arm64_flags_right_12913248 = unchecked((uint)0x1UL);
        if (((__arm64_flags_left_12913248 >= __arm64_flags_right_12913248) && (!((unchecked((uint)((__arm64_flags_left_12913248) - (__arm64_flags_right_12913248))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC50A94;
        }
        else
        {
            goto label_0xC50A94;
        }
        label_0xC50A94:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC50AA0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.ScreenToWorldPos` — RVA `0xc50aa4`

- Lift status: **partial**; input span: 844 bytes; span to next metadata RVA: 844 bytes.
- Metadata signature: `protected Vector3 ScreenToWorldPos(Vector2 sp, Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=86 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmaxnm' at 0xc50cf8; reason: Unsupported instruction 'fabd' at 0xc50d18

```csharp
public static ulong TouchControl_ScreenToWorldPos_RVAc50aa4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12913548 = default(float);
        float __arm64_float_flags_left_12913748 = default(float);
        float __arm64_float_flags_left_12913936 = default(float);
        float __arm64_float_flags_left_12913948 = default(float);
        float __arm64_float_flags_left_12914016 = default(float);
        float __arm64_float_flags_right_12913548 = default(float);
        float __arm64_float_flags_right_12913748 = default(float);
        float __arm64_float_flags_right_12913936 = default(float);
        float __arm64_float_flags_right_12913948 = default(float);
        float __arm64_float_flags_right_12914016 = default(float);
        ulong __arm64_pair_address_12913320 = default(ulong);
        ulong __arm64_pair_address_12913324 = default(ulong);
        ulong __arm64_pair_address_12913328 = default(ulong);
        ulong __arm64_pair_address_12913332 = default(ulong);
        ulong __arm64_pair_address_12913600 = default(ulong);
        ulong __arm64_pair_address_12913616 = default(ulong);
        ulong __arm64_pair_address_12913620 = default(ulong);
        ulong __arm64_pair_address_12913664 = default(ulong);
        ulong __arm64_pair_address_12913820 = default(ulong);
        ulong __arm64_pair_address_12913828 = default(ulong);
        ulong __arm64_pair_address_12913956 = default(ulong);
        ulong __arm64_pair_address_12913960 = default(ulong);
        ulong __arm64_pair_address_12914024 = default(ulong);
        ulong __arm64_pair_address_12914132 = default(ulong);
        ulong __arm64_pair_address_12914136 = default(ulong);
        ulong __arm64_pair_address_12914140 = default(ulong);
        ulong __arm64_pair_address_12914144 = default(ulong);
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
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        __arm64_pair_address_12913320 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12913320, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12913320) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_12913324 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12913324, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12913324) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12913328 = unchecked((ulong)((sp) + (0x50UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12913328, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12913328) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12913332 = unchecked((ulong)((sp) + (0x60UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12913332, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12913332) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x70UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x257UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        v9 = v1;
        v8 = v0;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50AFC;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x257UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50AFC;
        label_0xC50AFC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50B20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50B20;
        label_0xC50B20:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC50DEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50B34UL);
        }
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50DB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D9B8UL /* metadata target: Transform.get_forward */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xC50DEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        v11 = v0;
        v12 = v1;
        v10 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC50DEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D9B8UL /* metadata target: Transform.get_forward */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3C0UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12913548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12913548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12913548 >= __arm64_float_flags_right_12913548))
        {
            goto label_0xC50D94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x18UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x19;
        v0 = v8;
        v1 = v9;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F898UL /* metadata target: Camera.ScreenPointToRay */, x0, x1, x2, x3);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x18UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x1CUL))))), 0));
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12913600 = unchecked((ulong)((sp) + (0xCUL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12913600, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12913600) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x20UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x24UL))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x14UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        __arm64_pair_address_12913616 = unchecked((ulong)((sp) + (0x28UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12913616)), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12913616) + (0x4UL))))), 0));
        __arm64_pair_address_12913620 = unchecked((ulong)((sp) + (0x78UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12913620, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12913620) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x179D9B8UL /* metadata target: Transform.get_forward */, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        v13 = v0;
        v14 = v1;
        v15 = v2;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2C8UL))))))));
        v11 = v2;
        __arm64_pair_address_12913664 = unchecked((ulong)((sp) + (0x4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12913664, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12913664) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50C1C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2C8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50C1C;
        label_0xC50C1C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50C34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50C30UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC50C34;
        label_0xC50C34:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_12913748 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12913748 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12913748 <= __arm64_float_flags_right_12913748) || ((__arm64_float_flags_left_12913748 != __arm64_float_flags_left_12913748) || (__arm64_float_flags_right_12913748 != __arm64_float_flags_right_12913748))))
        {
            goto label_0xC50C6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50C5CUL);
        }
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC50CA4;
        label_0xC50C6C:
        ;
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2C9UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50C8C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2C9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50C8C;
        label_0xC50C8C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12913820 = x8;
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12913820)), 0));
        v14 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12913820) + (0x4UL))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x8UL))))), 0));
        goto label_0xC50CA4;
        label_0xC50CA4:
        ;
        __arm64_pair_address_12913828 = unchecked((ulong)((sp) + (0x78UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12913828)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12913828) + (0x4UL))))), 0));
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CAUL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50CDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD80UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2CAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50CDC;
        label_0xC50CDC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD80UL))));
        x9 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x474UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        x8 = RuntimeMemory.ReadU64(x8);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        RuntimeCalls.Unsupported("fmaxnm", 0xC50CF8UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(x8)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12913936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12913936 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_float_flags_left_12913936 > __arm64_float_flags_right_12913936) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        RuntimeCalls.Unsupported("fabd", 0xC50D18UL);
        __arm64_float_flags_left_12913948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12913948 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12913948 < __arm64_float_flags_right_12913948))
        {
            goto label_0xC50D94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50D24UL);
        }
        __arm64_pair_address_12913956 = unchecked((ulong)((sp) + (0x4UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12913956)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12913956) + (0x4UL))))), 0));
        __arm64_pair_address_12913960 = unchecked((ulong)((sp) + (0xCUL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12913960)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12913960) + (0x4UL))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x14UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12914016 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12914016 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12914016 <= __arm64_float_flags_right_12914016) || ((__arm64_float_flags_left_12914016 != __arm64_float_flags_left_12914016) || (__arm64_float_flags_right_12914016 != __arm64_float_flags_right_12914016))))
        {
            goto label_0xC50D94;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC50D68UL);
        }
        __arm64_pair_address_12914024 = unchecked((ulong)((sp) + (0x78UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12914024)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12914024) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x10UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x14UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        goto label_0xC50DC0;
        label_0xC50D94:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x0 = x19;
        v0 = v8;
        v1 = v9;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F6C8UL /* metadata target: Camera.ScreenToWorldPoint */, x0, x1, x2, x3);
        v8 = v0;
        v9 = v1;
        goto label_0xC50DB4;
        label_0xC50DB4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        goto label_0xC50DC0;
        label_0xC50DC0:
        ;
        v0 = v8;
        v1 = v9;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        __arm64_pair_address_12914132 = unchecked((ulong)((sp) + (0x60UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914132)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914132) + (0x8UL))))), 0));
        __arm64_pair_address_12914136 = unchecked((ulong)((sp) + (0x50UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914136)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914136) + (0x8UL))))), 0));
        __arm64_pair_address_12914140 = unchecked((ulong)((sp) + (0x40UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914140)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914140) + (0x8UL))))), 0));
        __arm64_pair_address_12914144 = unchecked((ulong)((sp) + (0x30UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914144)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914144) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xA0UL)));
        return x0;
        label_0xC50DEC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.WorldToLocalPos` — RVA `0xc50df0`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `protected Vector2 WorldToLocalPos(Vector3 wp, Vector2 worldOffset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong TouchControl_WorldToLocalPos_RVAc50df0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12914168 = default(ulong);
        ulong __arm64_pair_address_12914172 = default(ulong);
        ulong __arm64_pair_address_12914208 = default(ulong);
        ulong __arm64_pair_address_12914212 = default(ulong);
        ulong __arm64_pair_address_12914236 = default(ulong);
        ulong __arm64_pair_address_12914240 = default(ulong);
        ulong __arm64_pair_address_12914256 = default(ulong);
        ulong __arm64_pair_address_12914272 = default(ulong);
        ulong __arm64_pair_address_12914284 = default(ulong);
        ulong __arm64_pair_address_12914288 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xB0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x80UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12914168 = unchecked((ulong)((sp) + (0x88UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914168, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914168) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12914172 = unchecked((ulong)((sp) + (0x98UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914172, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914172) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA8UL))), x30);
        v12 = v0;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x1 = 0x0UL;
        v9 = v4;
        v10 = v3;
        v8 = v2;
        v11 = v1;
        __arm64_pair_address_12914208 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12914208, v0);
#else
        __WriteVector128(__arm64_pair_address_12914208, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12914208) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12914208) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12914212 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12914212, v0);
#else
        __WriteVector128(__arm64_pair_address_12914212, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12914212) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12914212) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC50E80:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179DEA0UL /* metadata target: Transform.get_worldToLocalMatrix */, x0, x1, x2, x3);
            __arm64_pair_address_12914236 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12914236);
#else
            v2 = __ReadVector128(__arm64_pair_address_12914236);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12914236) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12914236) + (0x10UL))));
#endif
            __arm64_pair_address_12914240 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v4 = RuntimeMemory.ReadVector128(__arm64_pair_address_12914240);
#else
            v4 = __ReadVector128(__arm64_pair_address_12914240);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v5 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12914240) + (0x10UL))));
#else
            v5 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12914240) + (0x10UL))));
#endif
            __arm64_pair_address_12914256 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12914256, v2);
#else
            __WriteVector128(__arm64_pair_address_12914256, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12914256) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12914256) + (0x10UL))), v3);
#endif
            x0 = unchecked((ulong)((sp) + (0x40UL)));
            x1 = 0x0UL;
            __arm64_pair_address_12914272 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12914272, v4);
#else
            __WriteVector128(__arm64_pair_address_12914272, v4);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12914272) + (0x10UL))), v5);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12914272) + (0x10UL))), v5);
#endif
            x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA8UL))));
            __arm64_pair_address_12914284 = unchecked((ulong)((sp) + (0x98UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914284)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914284) + (0x8UL))))), 0));
            __arm64_pair_address_12914288 = unchecked((ulong)((sp) + (0x88UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914288)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914288) + (0x8UL))))), 0));
            v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x80UL))))), 0));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.WorldToLocalPos` — RVA `0xc50e84`

- Lift status: **exact**; input span: 120 bytes; span to next metadata RVA: 120 bytes.
- Metadata signature: `protected Vector2 WorldToLocalPos(Vector3 wp) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong TouchControl_WorldToLocalPos_RVAc50e84(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12914420 = default(ulong);
        ulong __arm64_pair_address_12914312 = default(ulong);
        ulong __arm64_pair_address_12914404 = default(ulong);
        ulong __arm64_pair_address_12914416 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        __arm64_pair_address_12914312 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914312, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914312) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        v8 = v2;
        v9 = v1;
        v10 = v0;
        x19 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50EC4;
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
        goto label_0xC50EC4;
        label_0xC50EC4:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x0 = x19;
        v1 = v9;
        v2 = v8;
        x8 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_12914404 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914404)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914404) + (0x8UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        v0 = v10;
        __arm64_pair_address_12914416 = x8;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12914416)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12914416) + (0x4UL))))), 0));
        __arm64_load_address_12914420 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12914420)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12914420) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC50DF0UL /* metadata target: TouchControl.WorldToLocalPos */);
        return default(ulong);
    }
```

## `TouchControl.ScreenToLocalPos` — RVA `0xc50efc`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `protected Vector2 ScreenToLocalPos(Vector2 sp, Camera cam, Vector2 worldOffset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong TouchControl_ScreenToLocalPos_RVAc50efc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12914428 = default(ulong);
        ulong __arm64_pair_address_12914468 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        __arm64_pair_address_12914428 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914428, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914428) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12914428;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v8 = v3;
        v9 = v2;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC50AA4UL /* metadata target: TouchControl.ScreenToWorldPos */, x0, x1, x2, x3);
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v3 = v9;
        v4 = v8;
        __arm64_pair_address_12914468 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914468)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914468) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12914468) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0xC50DF0UL /* metadata target: TouchControl.WorldToLocalPos */);
        return default(ulong);
    }
```

## `TouchControl.ScreenToLocalPos` — RVA `0xc50f2c`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `protected Vector2 ScreenToLocalPos(Vector2 sp, Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong TouchControl_ScreenToLocalPos_RVAc50f2c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12914476 = default(ulong);
        ulong __arm64_pair_address_12914576 = default(ulong);
        ulong __arm64_pair_address_12914580 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12914476 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914476, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914476) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12914476;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1E0UL))))))));
        x19 = x1;
        v8 = v1;
        v9 = v0;
        x20 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50F68;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC50F68;
        label_0xC50F68:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = v9;
        v1 = v8;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12914576 = x8;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12914576)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12914576) + (0x4UL))))), 0));
        __arm64_pair_address_12914580 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914580)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914580) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12914580) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC50EFCUL /* metadata target: TouchControl.ScreenToLocalPos */);
        return default(ulong);
    }
```

## `TouchControl.ScreenToNormalizedPos` — RVA `0xc50f9c`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `protected Vector2 ScreenToNormalizedPos(Vector2 sp, Camera cam, Vector2 worldOffset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong TouchControl_ScreenToNormalizedPos_RVAc50f9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12914588 = default(ulong);
        ulong __arm64_pair_address_12914696 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12914588 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914588, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914588) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12914588;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v8 = v3;
        v9 = v2;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC50AA4UL /* metadata target: TouchControl.ScreenToWorldPos */, x0, x1, x2, x3);
        x0 = x19;
        v3 = v9;
        v4 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xC50DF0UL /* metadata target: TouchControl.WorldToLocalPos */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        v8 = v0;
        v9 = v1;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12914696 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914696)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914696) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12914696) + (0x20UL)));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.LocalToNormalizedPos` — RVA `0xc51010`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `protected Vector2 LocalToNormalizedPos(Vector2 lp) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchControl_LocalToNormalizedPos_RVAc51010(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12914704 = default(ulong);
        ulong __arm64_pair_address_12914776 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12914704 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914704, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914704) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12914704;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        x8 = RuntimeMemory.ReadU64(x0);
        v8 = v1;
        v9 = v0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12914776 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914776)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914776) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12914776) + (0x20UL)));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.ScreenToNormalizedPos` — RVA `0xc51060`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `protected Vector2 ScreenToNormalizedPos(Vector2 sp, Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong TouchControl_ScreenToNormalizedPos_RVAc51060(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12914784 = default(ulong);
        ulong __arm64_pair_address_12914884 = default(ulong);
        ulong __arm64_pair_address_12914888 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12914784 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914784, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914784) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12914784;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1E0UL))))))));
        x19 = x1;
        v8 = v1;
        v9 = v0;
        x20 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5109C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5109C;
        label_0xC5109C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = v9;
        v1 = v8;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12914884 = x8;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12914884)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12914884) + (0x4UL))))), 0));
        __arm64_pair_address_12914888 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914888)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914888) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12914888) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC50F9CUL /* metadata target: TouchControl.ScreenToNormalizedPos */);
        return default(ulong);
    }
```

## `TouchControl.WorldToNormalizedPos` — RVA `0xc510d0`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `protected Vector2 WorldToNormalizedPos(Vector2 wp, Vector2 worldOffset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong TouchControl_WorldToNormalizedPos_RVAc510d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12914896 = default(ulong);
        ulong __arm64_pair_address_12914992 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12914896 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12914896, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12914896) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12914896;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        v4 = v3;
        v3 = v2;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC50DF0UL /* metadata target: TouchControl.WorldToLocalPos */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        v8 = v0;
        v9 = v1;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12914992 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12914992)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12914992) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12914992) + (0x20UL)));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.WorldToNormalizedPos` — RVA `0xc51138`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `protected Vector2 WorldToNormalizedPos(Vector2 wp) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong TouchControl_WorldToNormalizedPos_RVAc51138(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12915000 = default(ulong);
        ulong __arm64_pair_address_12915092 = default(ulong);
        ulong __arm64_pair_address_12915096 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12915000 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915000, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915000) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12915000;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        v8 = v1;
        v9 = v0;
        x19 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC51170;
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
        goto label_0xC51170;
        label_0xC51170:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        v0 = v9;
        v1 = v8;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12915092 = x8;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12915092)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12915092) + (0x4UL))))), 0));
        __arm64_pair_address_12915096 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915096)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915096) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12915096) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC510D0UL /* metadata target: TouchControl.WorldToNormalizedPos */);
        return default(ulong);
    }
```

## `TouchControl.NormalizedToLocalPos` — RVA `0xc511a0`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `protected Vector2 NormalizedToLocalPos(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchControl_NormalizedToLocalPos_RVAc511a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12915104 = default(ulong);
        ulong __arm64_pair_address_12915176 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12915104 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915104, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915104) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12915104;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        x8 = RuntimeMemory.ReadU64(x0);
        v8 = v1;
        v9 = v0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12915176 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915176)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915176) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12915176) + (0x20UL)));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.NormalizedToLocalOffset` — RVA `0xc511f0`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `protected Vector2 NormalizedToLocalOffset(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchControl_NormalizedToLocalOffset_RVAc511f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12915184 = default(ulong);
        ulong __arm64_pair_address_12915240 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12915184 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915184, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915184) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12915184;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        x8 = RuntimeMemory.ReadU64(x0);
        v8 = v1;
        v9 = v0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12915240 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915240)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915240) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12915240) + (0x20UL)));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.NormalizedToWorldPos` — RVA `0xc51230`

- Lift status: **exact**; input span: 208 bytes; span to next metadata RVA: 208 bytes.
- Metadata signature: `protected Vector3 NormalizedToWorldPos(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=21 (informational only).

```csharp
public static ulong TouchControl_NormalizedToWorldPos_RVAc51230(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12915252 = default(ulong);
        ulong __arm64_pair_address_12915256 = default(ulong);
        ulong __arm64_pair_address_12915260 = default(ulong);
        ulong __arm64_pair_address_12915276 = default(ulong);
        ulong __arm64_pair_address_12915280 = default(ulong);
        ulong __arm64_pair_address_12915388 = default(ulong);
        ulong __arm64_pair_address_12915392 = default(ulong);
        ulong __arm64_pair_address_12915404 = default(ulong);
        ulong __arm64_pair_address_12915408 = default(ulong);
        ulong __arm64_pair_address_12915432 = default(ulong);
        ulong __arm64_pair_address_12915436 = default(ulong);
        ulong __arm64_pair_address_12915440 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        __arm64_pair_address_12915252 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915252, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915252) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12915256 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915256, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915256) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12915260 = unchecked((ulong)((sp) + (0xA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915260, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915260) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        v8 = v1;
        v1 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_12915276 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915276, v1);
#else
        __WriteVector128(__arm64_pair_address_12915276, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915276) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915276) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12915280 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915280, v1);
#else
        __WriteVector128(__arm64_pair_address_12915280, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915280) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915280) + (0x10UL))), v1);
#endif
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x0;
        v9 = v0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v10 = v0;
        v11 = v1;
        v12 = v2;
        v13 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC512FC:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            x8 = sp;
            x1 = 0x0UL;
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
            __arm64_pair_address_12915388 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12915388);
#else
            v0 = __ReadVector128(__arm64_pair_address_12915388);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12915388) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12915388) + (0x10UL))));
#endif
            __arm64_pair_address_12915392 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12915392);
#else
            v2 = __ReadVector128(__arm64_pair_address_12915392);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12915392) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12915392) + (0x10UL))));
#endif
            x0 = unchecked((ulong)((sp) + (0x40UL)));
            x1 = 0x0UL;
            __arm64_pair_address_12915404 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12915404, v0);
#else
            __WriteVector128(__arm64_pair_address_12915404, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915404) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915404) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12915408 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12915408, v2);
#else
            __WriteVector128(__arm64_pair_address_12915408, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915408) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915408) + (0x10UL))), v3);
#endif
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            v0 = v9;
            v1 = v8;
            x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
            __arm64_pair_address_12915432 = unchecked((ulong)((sp) + (0xA0UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915432)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915432) + (0x8UL))))), 0));
            __arm64_pair_address_12915436 = unchecked((ulong)((sp) + (0x90UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915436)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915436) + (0x8UL))))), 0));
            __arm64_pair_address_12915440 = unchecked((ulong)((sp) + (0x80UL)));
            v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915440)), 0));
            v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915440) + (0x8UL))))), 0));
            sp = unchecked((ulong)((sp) + (0xC0UL)));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.NormalizedToWorldOffset` — RVA `0xc51300`

- Lift status: **exact**; input span: 176 bytes; span to next metadata RVA: 176 bytes.
- Metadata signature: `protected Vector2 NormalizedToWorldOffset(Vector2 np) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong TouchControl_NormalizedToWorldOffset_RVAc51300(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12915460 = default(ulong);
        ulong __arm64_pair_address_12915464 = default(ulong);
        ulong __arm64_pair_address_12915480 = default(ulong);
        ulong __arm64_pair_address_12915484 = default(ulong);
        ulong __arm64_pair_address_12915568 = default(ulong);
        ulong __arm64_pair_address_12915572 = default(ulong);
        ulong __arm64_pair_address_12915584 = default(ulong);
        ulong __arm64_pair_address_12915588 = default(ulong);
        ulong __arm64_pair_address_12915612 = default(ulong);
        ulong __arm64_pair_address_12915616 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xB0UL)));
        __arm64_pair_address_12915460 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915460, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915460) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12915464 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915464, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915464) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x19);
        v8 = v1;
        v1 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_12915480 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915480, v1);
#else
        __WriteVector128(__arm64_pair_address_12915480, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915480) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915480) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12915484 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915484, v1);
#else
        __WriteVector128(__arm64_pair_address_12915484, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915484) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915484) + (0x10UL))), v1);
#endif
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x0;
        v9 = v0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v10 = v2;
        v11 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC513AC:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            x8 = sp;
            x1 = 0x0UL;
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
            __arm64_pair_address_12915568 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12915568);
#else
            v0 = __ReadVector128(__arm64_pair_address_12915568);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12915568) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12915568) + (0x10UL))));
#endif
            __arm64_pair_address_12915572 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12915572);
#else
            v2 = __ReadVector128(__arm64_pair_address_12915572);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12915572) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12915572) + (0x10UL))));
#endif
            x0 = unchecked((ulong)((sp) + (0x40UL)));
            x1 = 0x0UL;
            __arm64_pair_address_12915584 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12915584, v0);
#else
            __WriteVector128(__arm64_pair_address_12915584, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915584) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915584) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12915588 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12915588, v2);
#else
            __WriteVector128(__arm64_pair_address_12915588, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915588) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915588) + (0x10UL))), v3);
#endif
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            v0 = v9;
            v1 = v8;
            x0 = RuntimeCalls.InvokeDirect(0x1787244UL /* metadata target: Matrix4x4.MultiplyVector */, x0, x1, x2, x3);
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
            __arm64_pair_address_12915612 = unchecked((ulong)((sp) + (0x90UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915612)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915612) + (0x8UL))))), 0));
            __arm64_pair_address_12915616 = unchecked((ulong)((sp) + (0x80UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915616)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915616) + (0x8UL))))), 0));
            sp = unchecked((ulong)((sp) + (0xB0UL)));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.WorldToScreenPos` — RVA `0xc513b0`

- Lift status: **exact**; input span: 184 bytes; span to next metadata RVA: 184 bytes.
- Metadata signature: `protected Vector3 WorldToScreenPos(Vector3 wp, Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static ulong TouchControl_WorldToScreenPos_RVAc513b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12915804 = default(ulong);
        ulong __arm64_pair_address_12915636 = default(ulong);
        ulong __arm64_pair_address_12915796 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        __arm64_pair_address_12915636 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915636, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915636) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x258UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        v8 = v2;
        v9 = v1;
        v10 = v0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC513F8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x258UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC513F8;
        label_0xC513F8:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC51408;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC51404UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC51408;
        label_0xC51408:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC51444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5141CUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC51464;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F6B8UL /* metadata target: Camera.WorldToScreenPoint */, x0, x1, x2, x3);
        v10 = v0;
        v9 = v1;
        v8 = v2;
        goto label_0xC51444;
        label_0xC51444:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12915796 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12915796)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12915796) + (0x8UL))))), 0));
        __arm64_load_address_12915804 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12915804)), 0));
        return x0;
        label_0xC51464:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.LocalToScreenPos` — RVA `0xc51468`

- Lift status: **exact**; input span: 288 bytes; span to next metadata RVA: 288 bytes.
- Metadata signature: `protected Vector2 LocalToScreenPos(Vector2 lp, Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=38 (informational only).

```csharp
public static ulong TouchControl_LocalToScreenPos_RVAc51468(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12915820 = default(ulong);
        ulong __arm64_pair_address_12915900 = default(ulong);
        ulong __arm64_pair_address_12915904 = default(ulong);
        ulong __arm64_pair_address_12915972 = default(ulong);
        ulong __arm64_pair_address_12915976 = default(ulong);
        ulong __arm64_pair_address_12915988 = default(ulong);
        ulong __arm64_pair_address_12915992 = default(ulong);
        ulong __arm64_pair_address_12916036 = default(ulong);
        ulong __arm64_pair_address_12916040 = default(ulong);
        ulong __arm64_pair_address_12916052 = default(ulong);
        ulong __arm64_pair_address_12916056 = default(ulong);
        ulong __arm64_pair_address_12916088 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        __arm64_pair_address_12915820 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12915820, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12915820) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x90UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x259UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        v8 = v1;
        v9 = v0;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC514B4;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x259UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC514B4;
        label_0xC514B4:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_12915900 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915900, v0);
#else
        __WriteVector128(__arm64_pair_address_12915900, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915900) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915900) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12915904 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915904, v0);
#else
        __WriteVector128(__arm64_pair_address_12915904, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915904) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915904) + (0x10UL))), v0);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC514D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC514CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC514D0;
        label_0xC514D0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC51584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC51540;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC51500UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12915972 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12915972);
#else
        v0 = __ReadVector128(__arm64_pair_address_12915972);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12915972) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12915972) + (0x10UL))));
#endif
        __arm64_pair_address_12915976 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12915976);
#else
        v2 = __ReadVector128(__arm64_pair_address_12915976);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12915976) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12915976) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        x1 = 0x0UL;
        __arm64_pair_address_12915988 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915988, v0);
#else
        __WriteVector128(__arm64_pair_address_12915988, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915988) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915988) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12915992 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12915992, v2);
#else
        __WriteVector128(__arm64_pair_address_12915992, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12915992) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12915992) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xC51584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F6B8UL /* metadata target: Camera.WorldToScreenPoint */, x0, x1, x2, x3);
        goto label_0xC5156C;
        label_0xC51540:
        ;
        x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12916036 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916036);
#else
        v0 = __ReadVector128(__arm64_pair_address_12916036);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916036) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916036) + (0x10UL))));
#endif
        __arm64_pair_address_12916040 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916040);
#else
        v2 = __ReadVector128(__arm64_pair_address_12916040);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916040) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916040) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x40UL)));
        x1 = 0x0UL;
        __arm64_pair_address_12916052 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12916052, v0);
#else
        __WriteVector128(__arm64_pair_address_12916052, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916052) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916052) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12916056 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12916056, v2);
#else
        __WriteVector128(__arm64_pair_address_12916056, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916056) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916056) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
        goto label_0xC5156C;
        label_0xC5156C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        __arm64_pair_address_12916088 = unchecked((ulong)((sp) + (0x80UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12916088)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12916088) + (0x8UL))))), 0));
        return x0;
        label_0xC51584:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.ScreenToOrientedPos` — RVA `0xc51588`

- Lift status: **exact**; input span: 124 bytes; span to next metadata RVA: 124 bytes.
- Metadata signature: `public Vector2 ScreenToOrientedPos(Vector2 sp, Camera cam) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=17 (informational only).

```csharp
public static ulong TouchControl_ScreenToOrientedPos_RVAc51588(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12916104 = default(ulong);
        ulong __arm64_pair_address_12916216 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12916104 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916104, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916104) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12916104;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2CBUL))))))));
        v8 = v1;
        v9 = v0;
        x19 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC515C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2CBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC515C0;
        label_0xC515C0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC51600;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D6F0UL /* metadata target: Transform.get_rotation */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178AEECUL /* metadata target: Quaternion.Inverse */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v4 = v9;
        v5 = v8;
        x0 = 0x0UL;
        __arm64_pair_address_12916216 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12916216)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12916216) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12916216) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0x178B504UL /* metadata target: Quaternion.op_Multiply */);
        label_0xC51600:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.GetWorldSpaceCenter` — RVA `0xc51604`

- Lift status: **exact**; input span: 292 bytes; span to next metadata RVA: 292 bytes.
- Metadata signature: `public Vector3 GetWorldSpaceCenter() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=31 (informational only).

```csharp
public static ulong TouchControl_GetWorldSpaceCenter_RVAc51604(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12916416 = default(float);
        float __arm64_float_flags_right_12916416 = default(float);
        ulong __arm64_pair_address_12916232 = default(ulong);
        ulong __arm64_pair_address_12916236 = default(ulong);
        ulong __arm64_pair_address_12916240 = default(ulong);
        ulong __arm64_pair_address_12916256 = default(ulong);
        ulong __arm64_pair_address_12916260 = default(ulong);
        ulong __arm64_pair_address_12916356 = default(ulong);
        ulong __arm64_pair_address_12916448 = default(ulong);
        ulong __arm64_pair_address_12916452 = default(ulong);
        ulong __arm64_pair_address_12916464 = default(ulong);
        ulong __arm64_pair_address_12916468 = default(ulong);
        ulong __arm64_pair_address_12916496 = default(ulong);
        ulong __arm64_pair_address_12916500 = default(ulong);
        ulong __arm64_pair_address_12916504 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v12 = default(RuntimeVector128);
        RuntimeVector128 v13 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        __arm64_pair_address_12916232 = unchecked((ulong)((sp) + (0x80UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916232, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916232) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12916236 = unchecked((ulong)((sp) + (0x90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916236, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916236) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12916240 = unchecked((ulong)((sp) + (0xA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916240, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916240) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xB0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_12916256 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12916256, v0);
#else
        __WriteVector128(__arm64_pair_address_12916256, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916256) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916256) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12916260 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12916260, v0);
#else
        __WriteVector128(__arm64_pair_address_12916260, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916260) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916260) + (0x10UL))), v0);
#endif
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        v8 = v0;
        v9 = v1;
        v10 = v2;
        v11 = v3;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC5166C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x0 = x19;
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12916356 = x8;
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12916356)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12916356) + (0x4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC51724:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
            x8 = 0x432000UL;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2ECUL))))), 0));
            v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            __arm64_float_flags_left_12916416 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12916416 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
            if (((__arm64_float_flags_left_12916416 >= __arm64_float_flags_right_12916416) || ((__arm64_float_flags_left_12916416 != __arm64_float_flags_left_12916416) || (__arm64_float_flags_right_12916416 != __arm64_float_flags_right_12916416))))
            {
                label_0xC516D4:
                ;
                x8 = sp;
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
                __arm64_pair_address_12916448 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916448);
#else
                v0 = __ReadVector128(__arm64_pair_address_12916448);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916448) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916448) + (0x10UL))));
#endif
                __arm64_pair_address_12916452 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916452);
#else
                v2 = __ReadVector128(__arm64_pair_address_12916452);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916452) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916452) + (0x10UL))));
#endif
                x0 = unchecked((ulong)((sp) + (0x40UL)));
                x1 = 0x0UL;
                __arm64_pair_address_12916464 = unchecked((ulong)((sp) + (0x40UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_12916464, v0);
#else
                __WriteVector128(__arm64_pair_address_12916464, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916464) + (0x10UL))), v1);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916464) + (0x10UL))), v1);
#endif
                __arm64_pair_address_12916468 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(__arm64_pair_address_12916468, v2);
#else
                __WriteVector128(__arm64_pair_address_12916468, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916468) + (0x10UL))), v3);
#else
                __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916468) + (0x10UL))), v3);
#endif
                v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
                v0 = v8;
                v1 = v9;
                x0 = RuntimeCalls.InvokeDirect(0x17871ECUL /* metadata target: Matrix4x4.MultiplyPoint3x4 */, x0, x1, x2, x3);
            }
            else
            {
                x1 = 0x0UL;
                x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
            }
            label_0xC51708:
            ;
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
            __arm64_pair_address_12916496 = unchecked((ulong)((sp) + (0xA0UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12916496)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12916496) + (0x8UL))))), 0));
            __arm64_pair_address_12916500 = unchecked((ulong)((sp) + (0x90UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12916500)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12916500) + (0x8UL))))), 0));
            __arm64_pair_address_12916504 = unchecked((ulong)((sp) + (0x80UL)));
            v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12916504)), 0));
            v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12916504) + (0x8UL))))), 0));
            sp = unchecked((ulong)((sp) + (0xD0UL)));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.GetWorldSpaceSize` — RVA `0xc51728`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public Vector3 GetWorldSpaceSize() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong TouchControl_GetWorldSpaceSize_RVAc51728(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12916536 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC51758UL /* metadata target: TouchControl.GetWorldSpaceAABB */, x0, x1, x2, x3);
        __arm64_pair_address_12916536 = unchecked((ulong)((sp) + (0x14UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12916536)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12916536) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x1CUL))))), 0));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.GetWorldSpaceAABB` — RVA `0xc51758`

- Lift status: **exact**; input span: 256 bytes; span to next metadata RVA: 256 bytes.
- Metadata signature: `public Bounds GetWorldSpaceAABB() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=27 (informational only).

```csharp
public static ulong TouchControl_GetWorldSpaceAABB_RVAc51758(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12916680 = default(uint);
        uint __arm64_flags_left_12916712 = default(uint);
        uint __arm64_flags_right_12916680 = default(uint);
        uint __arm64_flags_right_12916712 = default(uint);
        ulong __arm64_pair_address_12916572 = default(ulong);
        ulong __arm64_pair_address_12916576 = default(ulong);
        ulong __arm64_pair_address_12916656 = default(ulong);
        ulong __arm64_pair_address_12916660 = default(ulong);
        ulong __arm64_pair_address_12916668 = default(ulong);
        ulong __arm64_pair_address_12916672 = default(ulong);
        ulong __arm64_pair_address_12916688 = default(ulong);
        ulong __arm64_pair_address_12916692 = default(ulong);
        ulong __arm64_pair_address_12916704 = default(ulong);
        ulong __arm64_pair_address_12916708 = default(ulong);
        ulong __arm64_pair_address_12916720 = default(ulong);
        ulong __arm64_pair_address_12916724 = default(ulong);
        ulong __arm64_pair_address_12916728 = default(ulong);
        ulong __arm64_pair_address_12916732 = default(ulong);
        ulong __arm64_pair_address_12916744 = default(ulong);
        ulong __arm64_pair_address_12916748 = default(ulong);
        ulong __arm64_pair_address_12916752 = default(ulong);
        ulong __arm64_pair_address_12916756 = default(ulong);
        ulong __arm64_pair_address_12916792 = default(ulong);
        ulong __arm64_pair_address_12916808 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x120UL)));
        __arm64_pair_address_12916572 = unchecked((ulong)((sp) + (0xE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916572, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916572) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12916576 = unchecked((ulong)((sp) + (0xF0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12916576, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12916576) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))), x19);
        x9 = RuntimeMemory.ReadU64(x0);
        x20 = x0;
        x19 = x8;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        v11 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC51854:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)((sp) + (0xA0UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
            __arm64_pair_address_12916656 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916656);
#else
            v0 = __ReadVector128(__arm64_pair_address_12916656);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916656) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916656) + (0x10UL))));
#endif
            __arm64_pair_address_12916660 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916660);
#else
            v2 = __ReadVector128(__arm64_pair_address_12916660);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916660) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916660) + (0x10UL))));
#endif
            x8 = unchecked((ulong)((sp) + (0xA0UL)));
            __arm64_pair_address_12916668 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916668, v0);
#else
            __WriteVector128(__arm64_pair_address_12916668, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916668) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916668) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12916672 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916672, v2);
#else
            __WriteVector128(__arm64_pair_address_12916672, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916672) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916672) + (0x10UL))), v3);
#endif
            x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x38UL))))));
            __arm64_flags_left_12916680 = unchecked((uint)(x9));
            __arm64_flags_right_12916680 = unchecked((uint)0x2UL);
            if ((!((unchecked((uint)((__arm64_flags_left_12916680) - (__arm64_flags_right_12916680))) == unchecked((uint)0x0UL)))))
            {
                label_0xC517E0:
                ;
                __arm64_pair_address_12916704 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916704);
#else
                v0 = __ReadVector128(__arm64_pair_address_12916704);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916704) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916704) + (0x10UL))));
#endif
                __arm64_pair_address_12916708 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916708);
#else
                v2 = __ReadVector128(__arm64_pair_address_12916708);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916708) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916708) + (0x10UL))));
#endif
                __arm64_flags_left_12916712 = unchecked((uint)(x9));
                __arm64_flags_right_12916712 = unchecked((uint)0x3UL);
                x1 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12916712) - (__arm64_flags_right_12916712))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            }
            else
            {
                __arm64_pair_address_12916688 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916688);
#else
                v0 = __ReadVector128(__arm64_pair_address_12916688);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916688) + (0x10UL))));
#else
                v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916688) + (0x10UL))));
#endif
                __arm64_pair_address_12916692 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
                v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916692);
#else
                v2 = __ReadVector128(__arm64_pair_address_12916692);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
                v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916692) + (0x10UL))));
#else
                v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916692) + (0x10UL))));
#endif
                x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            }
            label_0xC517F0:
            ;
            __arm64_pair_address_12916720 = unchecked((ulong)((sp) + (0xA0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916720, v0);
#else
            __WriteVector128(__arm64_pair_address_12916720, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916720) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916720) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12916724 = unchecked((ulong)((sp) + (0xC0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916724, v2);
#else
            __WriteVector128(__arm64_pair_address_12916724, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916724) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916724) + (0x10UL))), v3);
#endif
            __arm64_pair_address_12916728 = unchecked((ulong)((x8) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916728);
#else
            v1 = __ReadVector128(__arm64_pair_address_12916728);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916728) + (0x10UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916728) + (0x10UL))));
#endif
            __arm64_pair_address_12916732 = x8;
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_12916732);
#else
            v3 = __ReadVector128(__arm64_pair_address_12916732);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12916732) + (0x10UL))));
#else
            v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12916732) + (0x10UL))));
#endif
            x8 = unchecked((ulong)((sp) + (0x48UL)));
            x0 = sp;
            __arm64_pair_address_12916744 = unchecked((ulong)((sp) + (0x80UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916744, v1);
#else
            __WriteVector128(__arm64_pair_address_12916744, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916744) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916744) + (0x10UL))), v0);
#endif
            __arm64_pair_address_12916748 = unchecked((ulong)((sp) + (0x60UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916748, v3);
#else
            __WriteVector128(__arm64_pair_address_12916748, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916748) + (0x10UL))), v2);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916748) + (0x10UL))), v2);
#endif
            __arm64_pair_address_12916752 = sp;
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916752, v3);
#else
            __WriteVector128(__arm64_pair_address_12916752, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916752) + (0x10UL))), v2);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916752) + (0x10UL))), v2);
#endif
            __arm64_pair_address_12916756 = unchecked((ulong)((sp) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12916756, v1);
#else
            __WriteVector128(__arm64_pair_address_12916756, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12916756) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12916756) + (0x10UL))), v0);
#endif
            v0 = v8;
            v1 = v9;
            v2 = v10;
            v3 = v11;
            x0 = RuntimeCalls.InvokeDirect(0xC51858UL /* metadata target: CFUtils.TransformRectAsBounds */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x58UL))));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((sp) + (0x48UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((sp) + (0x48UL))));
#endif
            x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))));
            __arm64_pair_address_12916792 = unchecked((ulong)((sp) + (0xF0UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12916792)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12916792) + (0x8UL))))), 0));
            RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x10UL))), x8);
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(x19, v0);
#else
            __WriteVector128(x19, v0);
#endif
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x110UL)))) + (0x8UL))));
            __arm64_pair_address_12916808 = unchecked((ulong)((sp) + (0xE0UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12916808)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12916808) + (0x8UL))))), 0));
            sp = unchecked((ulong)((sp) + (0x120UL)));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.GetWorldToNormalizedMatrix` — RVA `0xc51b9c`

- Lift status: **exact**; input span: 500 bytes; span to next metadata RVA: 500 bytes.
- Metadata signature: `public Matrix4x4 GetWorldToNormalizedMatrix() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong TouchControl_GetWorldToNormalizedMatrix_RVAc51b9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12917660 = default(ulong);
        ulong __arm64_pair_address_12917664 = default(ulong);
        ulong __arm64_pair_address_12917668 = default(ulong);
        ulong __arm64_pair_address_12917756 = default(ulong);
        ulong __arm64_pair_address_12917764 = default(ulong);
        ulong __arm64_pair_address_12917780 = default(ulong);
        ulong __arm64_pair_address_12917796 = default(ulong);
        ulong __arm64_pair_address_12917856 = default(ulong);
        ulong __arm64_pair_address_12917860 = default(ulong);
        ulong __arm64_pair_address_12917960 = default(ulong);
        ulong __arm64_pair_address_12917964 = default(ulong);
        ulong __arm64_pair_address_12917976 = default(ulong);
        ulong __arm64_pair_address_12917980 = default(ulong);
        ulong __arm64_pair_address_12917984 = default(ulong);
        ulong __arm64_pair_address_12917988 = default(ulong);
        ulong __arm64_pair_address_12918000 = default(ulong);
        ulong __arm64_pair_address_12918004 = default(ulong);
        ulong __arm64_pair_address_12918012 = default(ulong);
        ulong __arm64_pair_address_12918016 = default(ulong);
        ulong __arm64_pair_address_12918028 = default(ulong);
        ulong __arm64_pair_address_12918032 = default(ulong);
        ulong __arm64_pair_address_12918056 = default(ulong);
        ulong __arm64_pair_address_12918060 = default(ulong);
        ulong __arm64_pair_address_12918072 = default(ulong);
        ulong __arm64_pair_address_12918076 = default(ulong);
        ulong __arm64_pair_address_12918080 = default(ulong);
        ulong __arm64_pair_address_12918084 = default(ulong);
        ulong __arm64_pair_address_12918096 = default(ulong);
        ulong __arm64_pair_address_12918100 = default(ulong);
        ulong __arm64_pair_address_12918108 = default(ulong);
        ulong __arm64_pair_address_12918112 = default(ulong);
        ulong __arm64_pair_address_12918116 = default(ulong);
        ulong __arm64_pair_address_12918120 = default(ulong);
        ulong __arm64_pair_address_12918140 = default(ulong);
        ulong __arm64_pair_address_12918144 = default(ulong);
        ulong __arm64_pair_address_12918148 = default(ulong);
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
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12917660 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12917660, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12917660) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = __arm64_pair_address_12917660;
        __arm64_pair_address_12917664 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12917664, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12917664) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12917668 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12917668, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12917668) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x1D0UL)));
        x9 = RuntimeMemory.ReadU64(x0);
        x20 = x0;
        x19 = x8;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        v9 = v1;
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40000000UL)), 0)), 0));
        v8 = v0;
        v10 = v2;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)((sp) + (0x150UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x0 = 0x0UL;
        v11 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x178728CUL /* metadata target: Matrix4x4.Scale */, x0, x1, x2, x3);
        __arm64_pair_address_12917756 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12917756);
#else
        v0 = __ReadVector128(__arm64_pair_address_12917756);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12917756) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12917756) + (0x10UL))));
#endif
        x21 = 0x1BAB000UL;
        __arm64_pair_address_12917764 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12917764);
#else
        v2 = __ReadVector128(__arm64_pair_address_12917764);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12917764) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12917764) + (0x10UL))));
#endif
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CBUL))))))));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12917780 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12917780, v0);
#else
        __WriteVector128(__arm64_pair_address_12917780, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12917780) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12917780) + (0x10UL))), v1);
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v5.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_pair_address_12917796 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12917796, v2);
#else
        __WriteVector128(__arm64_pair_address_12917796, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12917796) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12917796) + (0x10UL))), v3);
#endif
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2CBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC51C40:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD88UL))));
        x21 = 0x1BAB000UL;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1E1UL))))))));
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)))), 0));
        x8 = RuntimeMemory.ReadU64(x8);
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12917856 = x8;
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12917856)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12917856) + (0x4UL))))), 0));
        __arm64_pair_address_12917860 = unchecked((ulong)((x8) + (0x8UL)));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12917860)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12917860) + (0x4UL))))), 0));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1E8UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1E1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC51C80:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1E8UL))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v1 = v13;
        v3 = v11;
        x8 = RuntimeMemory.ReadU64(x8);
        v4 = v9;
        v5 = v10;
        v6 = v8;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x14UL))))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCUL))));
        x8 = unchecked((ulong)((sp) + (0x150UL)));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v0 = v12;
        RuntimeMemory.WriteU64(sp, x9);
        x0 = RuntimeCalls.InvokeDirect(0x17862BCUL /* metadata target: Matrix4x4.TRS */, x0, x1, x2, x3);
        __arm64_pair_address_12917960 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12917960);
#else
        v0 = __ReadVector128(__arm64_pair_address_12917960);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12917960) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12917960) + (0x10UL))));
#endif
        __arm64_pair_address_12917964 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12917964);
#else
        v2 = __ReadVector128(__arm64_pair_address_12917964);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12917964) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12917964) + (0x10UL))));
#endif
        x8 = unchecked((ulong)((sp) + (0x110UL)));
        x0 = unchecked((ulong)((sp) + (0xD0UL)));
        __arm64_pair_address_12917976 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12917976, v0);
#else
        __WriteVector128(__arm64_pair_address_12917976, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12917976) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12917976) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12917980 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12917980);
#else
        v0 = __ReadVector128(__arm64_pair_address_12917980);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12917980) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12917980) + (0x10UL))));
#endif
        __arm64_pair_address_12917984 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12917984, v2);
#else
        __WriteVector128(__arm64_pair_address_12917984, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12917984) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12917984) + (0x10UL))), v3);
#endif
        __arm64_pair_address_12917988 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12917988);
#else
        v2 = __ReadVector128(__arm64_pair_address_12917988);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12917988) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12917988) + (0x10UL))));
#endif
        x1 = unchecked((ulong)((sp) + (0x90UL)));
        x2 = 0x0UL;
        __arm64_pair_address_12918000 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12918000, v0);
#else
        __WriteVector128(__arm64_pair_address_12918000, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918000) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918000) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12918004 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12918004, v2);
#else
        __WriteVector128(__arm64_pair_address_12918004, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918004) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918004) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1786E8CUL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
        __arm64_pair_address_12918012 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918012);
#else
        v0 = __ReadVector128(__arm64_pair_address_12918012);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918012) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918012) + (0x10UL))));
#endif
        __arm64_pair_address_12918016 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918016);
#else
        v2 = __ReadVector128(__arm64_pair_address_12918016);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918016) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918016) + (0x10UL))));
#endif
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12918028 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12918028, v0);
#else
        __WriteVector128(__arm64_pair_address_12918028, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918028) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918028) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12918032 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12918032, v2);
#else
        __WriteVector128(__arm64_pair_address_12918032, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918032) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918032) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC51D8C:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)((sp) + (0x110UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179DEA0UL /* metadata target: Transform.get_worldToLocalMatrix */, x0, x1, x2, x3);
            __arm64_pair_address_12918056 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918056);
#else
            v0 = __ReadVector128(__arm64_pair_address_12918056);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918056) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918056) + (0x10UL))));
#endif
            __arm64_pair_address_12918060 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918060);
#else
            v2 = __ReadVector128(__arm64_pair_address_12918060);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918060) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918060) + (0x10UL))));
#endif
            x8 = unchecked((ulong)((sp) + (0x110UL)));
            x0 = unchecked((ulong)((sp) + (0x50UL)));
            __arm64_pair_address_12918072 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918072, v0);
#else
            __WriteVector128(__arm64_pair_address_12918072, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918072) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918072) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12918076 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918076);
#else
            v0 = __ReadVector128(__arm64_pair_address_12918076);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918076) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918076) + (0x10UL))));
#endif
            __arm64_pair_address_12918080 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918080, v2);
#else
            __WriteVector128(__arm64_pair_address_12918080, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918080) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918080) + (0x10UL))), v3);
#endif
            __arm64_pair_address_12918084 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918084);
#else
            v2 = __ReadVector128(__arm64_pair_address_12918084);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918084) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918084) + (0x10UL))));
#endif
            x1 = unchecked((ulong)((sp) + (0x10UL)));
            x2 = 0x0UL;
            __arm64_pair_address_12918096 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918096, v0);
#else
            __WriteVector128(__arm64_pair_address_12918096, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918096) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918096) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12918100 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918100, v2);
#else
            __WriteVector128(__arm64_pair_address_12918100, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918100) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918100) + (0x10UL))), v3);
#endif
            x0 = RuntimeCalls.InvokeDirect(0x1786E8CUL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
            __arm64_pair_address_12918108 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918108);
#else
            v1 = __ReadVector128(__arm64_pair_address_12918108);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918108) + (0x10UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918108) + (0x10UL))));
#endif
            __arm64_pair_address_12918112 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918112);
#else
            v3 = __ReadVector128(__arm64_pair_address_12918112);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918112) + (0x10UL))));
#else
            v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918112) + (0x10UL))));
#endif
            __arm64_pair_address_12918116 = unchecked((ulong)((x19) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918116, v1);
#else
            __WriteVector128(__arm64_pair_address_12918116, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918116) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918116) + (0x10UL))), v0);
#endif
            __arm64_pair_address_12918120 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918120, v3);
#else
            __WriteVector128(__arm64_pair_address_12918120, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918120) + (0x10UL))), v2);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918120) + (0x10UL))), v2);
#endif
            sp = unchecked((ulong)((sp) + (0x1D0UL)));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
            x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
            __arm64_pair_address_12918140 = unchecked((ulong)((sp) + (0x20UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918140)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918140) + (0x8UL))))), 0));
            __arm64_pair_address_12918144 = unchecked((ulong)((sp) + (0x10UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918144)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918144) + (0x8UL))))), 0));
            __arm64_pair_address_12918148 = sp;
            v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918148)), 0));
            v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918148) + (0x8UL))))), 0));
            sp = unchecked((ulong)((__arm64_pair_address_12918148) + (0x60UL)));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.GetNormalizedToWorldMatrix` — RVA `0xc51d90`

- Lift status: **exact**; input span: 304 bytes; span to next metadata RVA: 304 bytes.
- Metadata signature: `public Matrix4x4 GetNormalizedToWorldMatrix() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong TouchControl_GetNormalizedToWorldMatrix_RVAc51d90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12918164 = default(ulong);
        ulong __arm64_pair_address_12918168 = default(ulong);
        ulong __arm64_pair_address_12918252 = default(ulong);
        ulong __arm64_pair_address_12918256 = default(ulong);
        ulong __arm64_pair_address_12918276 = default(ulong);
        ulong __arm64_pair_address_12918280 = default(ulong);
        ulong __arm64_pair_address_12918344 = default(ulong);
        ulong __arm64_pair_address_12918348 = default(ulong);
        ulong __arm64_pair_address_12918360 = default(ulong);
        ulong __arm64_pair_address_12918368 = default(ulong);
        ulong __arm64_pair_address_12918372 = default(ulong);
        ulong __arm64_pair_address_12918384 = default(ulong);
        ulong __arm64_pair_address_12918388 = default(ulong);
        ulong __arm64_pair_address_12918392 = default(ulong);
        ulong __arm64_pair_address_12918396 = default(ulong);
        ulong __arm64_pair_address_12918408 = default(ulong);
        ulong __arm64_pair_address_12918412 = default(ulong);
        ulong __arm64_pair_address_12918420 = default(ulong);
        ulong __arm64_pair_address_12918424 = default(ulong);
        ulong __arm64_pair_address_12918432 = default(ulong);
        ulong __arm64_pair_address_12918436 = default(ulong);
        ulong __arm64_pair_address_12918440 = default(ulong);
        ulong __arm64_pair_address_12918448 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v5 = default(RuntimeVector128);
        RuntimeVector128 v6 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x150UL)));
        __arm64_pair_address_12918164 = unchecked((ulong)((sp) + (0x110UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12918164, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12918164) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12918168 = unchecked((ulong)((sp) + (0x120UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12918168, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12918168) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x8UL))), x19);
        x9 = RuntimeMemory.ReadU64(x0);
        x20 = x0;
        x19 = x8;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        v8 = v0;
        v9 = v1;
        v10 = v2;
        v11 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC51EBC:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x8 = unchecked((ulong)((sp) + (0x90UL)));
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
            x20 = 0x1BAB000UL;
            __arm64_pair_address_12918252 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918252);
#else
            v0 = __ReadVector128(__arm64_pair_address_12918252);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918252) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918252) + (0x10UL))));
#endif
            __arm64_pair_address_12918256 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918256);
#else
            v2 = __ReadVector128(__arm64_pair_address_12918256);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918256) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918256) + (0x10UL))));
#endif
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2CBUL))))))));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
            v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
            v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
            __arm64_pair_address_12918276 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918276, v0);
#else
            __WriteVector128(__arm64_pair_address_12918276, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918276) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918276) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12918280 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918280, v2);
#else
            __WriteVector128(__arm64_pair_address_12918280, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918280) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918280) + (0x10UL))), v3);
#endif
            if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x0 = 0x1A8C000UL;
                x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD88UL))));
                // Likely IL2CPP class initialization helper (guarded call).
                x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2CBUL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
            label_0xC51E24:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD88UL))));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
            x9 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
            x8 = RuntimeMemory.ReadU64(x8);
            v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            x0 = 0x0UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            __arm64_pair_address_12918344 = x8;
            v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12918344)), 0));
            v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12918344) + (0x4UL))))), 0));
            __arm64_pair_address_12918348 = unchecked((ulong)((x8) + (0x8UL)));
            v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12918348)), 0));
            v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12918348) + (0x4UL))))), 0));
            x8 = unchecked((ulong)((sp) + (0x90UL)));
            RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x8UL))), unchecked((uint)(x9)));
            __arm64_pair_address_12918360 = sp;
            RuntimeMemory.WriteF32(__arm64_pair_address_12918360, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12918360) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0));
            x0 = RuntimeCalls.InvokeDirect(0x17862BCUL /* metadata target: Matrix4x4.TRS */, x0, x1, x2, x3);
            __arm64_pair_address_12918368 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918368);
#else
            v0 = __ReadVector128(__arm64_pair_address_12918368);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918368) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918368) + (0x10UL))));
#endif
            __arm64_pair_address_12918372 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918372);
#else
            v2 = __ReadVector128(__arm64_pair_address_12918372);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918372) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918372) + (0x10UL))));
#endif
            x8 = unchecked((ulong)((sp) + (0x90UL)));
            x0 = unchecked((ulong)((sp) + (0x50UL)));
            __arm64_pair_address_12918384 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918384, v0);
#else
            __WriteVector128(__arm64_pair_address_12918384, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918384) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918384) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12918388 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918388);
#else
            v0 = __ReadVector128(__arm64_pair_address_12918388);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918388) + (0x10UL))));
#else
            v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918388) + (0x10UL))));
#endif
            __arm64_pair_address_12918392 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918392, v2);
#else
            __WriteVector128(__arm64_pair_address_12918392, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918392) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918392) + (0x10UL))), v3);
#endif
            __arm64_pair_address_12918396 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918396);
#else
            v2 = __ReadVector128(__arm64_pair_address_12918396);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918396) + (0x10UL))));
#else
            v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918396) + (0x10UL))));
#endif
            x1 = unchecked((ulong)((sp) + (0x10UL)));
            x2 = 0x0UL;
            __arm64_pair_address_12918408 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918408, v0);
#else
            __WriteVector128(__arm64_pair_address_12918408, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918408) + (0x10UL))), v1);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918408) + (0x10UL))), v1);
#endif
            __arm64_pair_address_12918412 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918412, v2);
#else
            __WriteVector128(__arm64_pair_address_12918412, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918412) + (0x10UL))), v3);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918412) + (0x10UL))), v3);
#endif
            x0 = RuntimeCalls.InvokeDirect(0x1786E8CUL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
            __arm64_pair_address_12918420 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918420);
#else
            v1 = __ReadVector128(__arm64_pair_address_12918420);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918420) + (0x10UL))));
#else
            v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918420) + (0x10UL))));
#endif
            __arm64_pair_address_12918424 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_12918424);
#else
            v3 = __ReadVector128(__arm64_pair_address_12918424);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12918424) + (0x10UL))));
#else
            v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12918424) + (0x10UL))));
#endif
            x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x130UL))));
            x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x130UL)))) + (0x8UL))));
            __arm64_pair_address_12918432 = unchecked((ulong)((sp) + (0x120UL)));
            v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918432)), 0));
            v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918432) + (0x8UL))))), 0));
            __arm64_pair_address_12918436 = unchecked((ulong)((x19) + (0x20UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918436, v1);
#else
            __WriteVector128(__arm64_pair_address_12918436, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918436) + (0x10UL))), v0);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918436) + (0x10UL))), v0);
#endif
            __arm64_pair_address_12918440 = x19;
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(__arm64_pair_address_12918440, v3);
#else
            __WriteVector128(__arm64_pair_address_12918440, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
            RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12918440) + (0x10UL))), v2);
#else
            __WriteVector128(unchecked((ulong)((__arm64_pair_address_12918440) + (0x10UL))), v2);
#endif
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x140UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x140UL)))) + (0x8UL))));
            __arm64_pair_address_12918448 = unchecked((ulong)((sp) + (0x110UL)));
            v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918448)), 0));
            v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918448) + (0x8UL))))), 0));
            sp = unchecked((ulong)((sp) + (0x150UL)));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchControl.GetFollowPos` — RVA `0xc51ec0`

- Lift status: **exact**; input span: 260 bytes; span to next metadata RVA: 260 bytes.
- Metadata signature: `protected Vector3 GetFollowPos(Vector3 targetWorldPos, Vector2 worldOffset, out bool posWasOutside) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong TouchControl_GetFollowPos_RVAc51ec0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12918524 = default(uint);
        uint __arm64_flags_right_12918524 = default(uint);
        float __arm64_float_flags_left_12918556 = default(float);
        float __arm64_float_flags_left_12918576 = default(float);
        float __arm64_float_flags_left_12918588 = default(float);
        float __arm64_float_flags_left_12918596 = default(float);
        float __arm64_float_flags_left_12918608 = default(float);
        float __arm64_float_flags_right_12918556 = default(float);
        float __arm64_float_flags_right_12918576 = default(float);
        float __arm64_float_flags_right_12918588 = default(float);
        float __arm64_float_flags_right_12918596 = default(float);
        float __arm64_float_flags_right_12918608 = default(float);
        ulong __arm64_pair_address_12918464 = default(ulong);
        ulong __arm64_pair_address_12918468 = default(ulong);
        ulong __arm64_pair_address_12918472 = default(ulong);
        ulong __arm64_pair_address_12918708 = default(ulong);
        ulong __arm64_pair_address_12918712 = default(ulong);
        ulong __arm64_pair_address_12918716 = default(ulong);
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
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12918464 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12918464, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12918464) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        sp = __arm64_pair_address_12918464;
        __arm64_pair_address_12918468 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12918468, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12918468) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12918472 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12918472, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12918472) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x30UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        v8 = v2;
        x19 = x1;
        v9 = v1;
        v10 = v0;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC510D0UL /* metadata target: TouchControl.WorldToNormalizedPos */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x38UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0xFFFFFFFEUL)))))));
        __arm64_flags_left_12918524 = unchecked((uint)(x8));
        __arm64_flags_right_12918524 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12918524) - (__arm64_flags_right_12918524))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC51F2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC51F04UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12918556 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918556 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12918556 <= __arm64_float_flags_right_12918556))
        {
            goto label_0xC51F58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC51F24UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC51FC4UL /* metadata target: CFUtils.ClampInsideUnitCircle */, x0, x1, x2, x3);
        goto label_0xC51F64;
        label_0xC51F2C:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12918576 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918576 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12918576 > __arm64_float_flags_right_12918576) || ((__arm64_float_flags_left_12918576 != __arm64_float_flags_left_12918576) || (__arm64_float_flags_right_12918576 != __arm64_float_flags_right_12918576))))
        {
            goto label_0xC51F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC51F38UL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF800000UL)), 0)), 0));
        __arm64_float_flags_left_12918588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918588 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12918588 < __arm64_float_flags_right_12918588) || ((__arm64_float_flags_left_12918588 != __arm64_float_flags_left_12918588) || (__arm64_float_flags_right_12918588 != __arm64_float_flags_right_12918588))))
        {
            goto label_0xC51F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC51F44UL);
        }
        __arm64_float_flags_left_12918596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918596 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12918596 < __arm64_float_flags_right_12918596) || ((__arm64_float_flags_left_12918596 != __arm64_float_flags_left_12918596) || (__arm64_float_flags_right_12918596 != __arm64_float_flags_right_12918596))))
        {
            goto label_0xC51F60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC51F4CUL);
        }
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12918608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12918608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12918608 > __arm64_float_flags_right_12918608) || ((__arm64_float_flags_left_12918608 != __arm64_float_flags_left_12918608) || (__arm64_float_flags_right_12918608 != __arm64_float_flags_right_12918608))))
        {
            goto label_0xC51F60;
        }
        else
        {
            goto label_0xC51F58;
        }
        label_0xC51F58:
        ;
        RuntimeMemory.WriteU8(x19, unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC51FA0;
        label_0xC51F60:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC52094UL /* metadata target: CFUtils.ClampInsideUnitSquare */, x0, x1, x2, x3);
        goto label_0xC51F64;
        label_0xC51F64:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC51230UL /* metadata target: TouchControl.NormalizedToWorldPos */, x0, x1, x2, x3);
        x0 = x20;
        v11 = v0;
        v12 = v1;
        v13 = v2;
        x0 = RuntimeCalls.InvokeDirect(0xC51604UL /* metadata target: TouchControl.GetWorldSpaceCenter */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteU8(x19, unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC51FA0;
        label_0xC51FA0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        __arm64_pair_address_12918708 = unchecked((ulong)((sp) + (0x20UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918708)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918708) + (0x8UL))))), 0));
        __arm64_pair_address_12918712 = unchecked((ulong)((sp) + (0x10UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918712)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918712) + (0x8UL))))), 0));
        __arm64_pair_address_12918716 = sp;
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12918716)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12918716) + (0x8UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `TouchControl.GetFollowPos` — RVA `0xc520fc`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `protected Vector3 GetFollowPos(Vector3 targetWorldPos, Vector3 worldOffset) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong TouchControl_GetFollowPos_RVAc520fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x1 = unchecked((ulong)((sp) + (0xCUL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((sp) + (0xCUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC51EC0UL /* metadata target: TouchControl.GetFollowPos */, x0, x1, x2, x3);
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `TouchControl.ClampInsideCanvas` — RVA `0xc52114`

- Lift status: **exact**; input span: 784 bytes; span to next metadata RVA: 784 bytes.
- Metadata signature: `protected Vector3 ClampInsideCanvas(Vector3 targetWorldPos, Canvas limiterCanvas) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=96 (informational only).

```csharp
public static ulong TouchControl_ClampInsideCanvas_RVAc52114(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12919248 = default(ulong);
        uint __arm64_flags_left_12919576 = default(uint);
        ulong __arm64_flags_right_12919248 = default(ulong);
        uint __arm64_flags_right_12919576 = default(uint);
        float __arm64_float_flags_left_12919704 = default(float);
        float __arm64_float_flags_right_12919704 = default(float);
        ulong __arm64_pair_address_12919060 = default(ulong);
        ulong __arm64_pair_address_12919064 = default(ulong);
        ulong __arm64_pair_address_12919068 = default(ulong);
        ulong __arm64_pair_address_12919072 = default(ulong);
        ulong __arm64_pair_address_12919172 = default(ulong);
        ulong __arm64_pair_address_12919176 = default(ulong);
        ulong __arm64_pair_address_12919360 = default(ulong);
        ulong __arm64_pair_address_12919392 = default(ulong);
        ulong __arm64_pair_address_12919396 = default(ulong);
        ulong __arm64_pair_address_12919408 = default(ulong);
        ulong __arm64_pair_address_12919412 = default(ulong);
        ulong __arm64_pair_address_12919436 = default(ulong);
        ulong __arm64_pair_address_12919440 = default(ulong);
        ulong __arm64_pair_address_12919452 = default(ulong);
        ulong __arm64_pair_address_12919460 = default(ulong);
        ulong __arm64_pair_address_12919484 = default(ulong);
        ulong __arm64_pair_address_12919488 = default(ulong);
        ulong __arm64_pair_address_12919500 = default(ulong);
        ulong __arm64_pair_address_12919504 = default(ulong);
        ulong __arm64_pair_address_12919508 = default(ulong);
        ulong __arm64_pair_address_12919512 = default(ulong);
        ulong __arm64_pair_address_12919524 = default(ulong);
        ulong __arm64_pair_address_12919528 = default(ulong);
        ulong __arm64_pair_address_12919536 = default(ulong);
        ulong __arm64_pair_address_12919540 = default(ulong);
        ulong __arm64_pair_address_12919548 = default(ulong);
        ulong __arm64_pair_address_12919552 = default(ulong);
        ulong __arm64_pair_address_12919560 = default(ulong);
        ulong __arm64_pair_address_12919568 = default(ulong);
        ulong __arm64_pair_address_12919600 = default(ulong);
        ulong __arm64_pair_address_12919672 = default(ulong);
        ulong __arm64_pair_address_12919740 = default(ulong);
        ulong __arm64_pair_address_12919744 = default(ulong);
        ulong __arm64_pair_address_12919756 = default(ulong);
        ulong __arm64_pair_address_12919760 = default(ulong);
        ulong __arm64_pair_address_12919820 = default(ulong);
        ulong __arm64_pair_address_12919824 = default(ulong);
        ulong __arm64_pair_address_12919828 = default(ulong);
        ulong __arm64_pair_address_12919832 = default(ulong);
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
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12919060 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12919060, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12919060) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_12919060;
        __arm64_pair_address_12919064 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12919064, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12919064) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12919068 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12919068, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12919068) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12919072 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12919072, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12919072) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x210UL)));
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x25BUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x1;
        v8 = v2;
        v9 = v1;
        v10 = v0;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5217C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x25BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5217C;
        label_0xC5217C:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_12919172 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919172, v0);
#else
        __WriteVector128(__arm64_pair_address_12919172, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919172) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919172) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12919176 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919176, v0);
#else
        __WriteVector128(__arm64_pair_address_12919176, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919176) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919176) + (0x10UL))), v0);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52198;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52194UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC52198;
        label_0xC52198:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC523F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC521ACUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC52420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC521DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x1C8UL))));
        x9 = RuntimeMemory.ReadU64(x0);
        x8 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12919248 = x9;
        __arm64_flags_right_12919248 = x8;
        x21 = ((unchecked((ulong)((__arm64_flags_left_12919248) - (__arm64_flags_right_12919248))) == 0x0UL) ? x0 : 0x0UL);
        goto label_0xC521E0;
        label_0xC521DC:
        ;
        x21 = 0x0UL;
        goto label_0xC521E0;
        label_0xC521E0:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC521F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC521ECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC521F0;
        label_0xC521F0:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC523F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0xCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x21 == 0x0UL))
        {
            goto label_0xC52420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = 0x0UL;
        v11 = v1;
        v12 = v2;
        v13 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x179C4BCUL /* metadata target: RectTransform.get_rect */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        __arm64_pair_address_12919360 = unchecked((ulong)((sp) + (0x4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12919360, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12919360) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        v14 = v2;
        v15 = v3;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC52420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x1D0UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DEA0UL /* metadata target: Transform.get_worldToLocalMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12919392 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919392);
#else
        v0 = __ReadVector128(__arm64_pair_address_12919392);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919392) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919392) + (0x10UL))));
#endif
        __arm64_pair_address_12919396 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919396);
#else
        v2 = __ReadVector128(__arm64_pair_address_12919396);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919396) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919396) + (0x10UL))));
#endif
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12919408 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919408, v0);
#else
        __WriteVector128(__arm64_pair_address_12919408, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919408) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919408) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12919412 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919412, v2);
#else
        __WriteVector128(__arm64_pair_address_12919412, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919412) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919412) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC52420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x1D0UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12919436 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919436);
#else
        v4 = __ReadVector128(__arm64_pair_address_12919436);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919436) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919436) + (0x10UL))));
#endif
        __arm64_pair_address_12919440 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919440);
#else
        v1 = __ReadVector128(__arm64_pair_address_12919440);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919440) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919440) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x110UL)));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        __arm64_pair_address_12919452 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919452, v4);
#else
        __WriteVector128(__arm64_pair_address_12919452, v4);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919452) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919452) + (0x10UL))), v0);
#endif
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x14CUL))))), 0));
        __arm64_pair_address_12919460 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919460, v1);
#else
        __WriteVector128(__arm64_pair_address_12919460, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919460) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919460) + (0x10UL))), v2);
#endif
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178708CUL /* metadata target: Matrix4x4.SetColumn */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_12919484 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919484);
#else
        v0 = __ReadVector128(__arm64_pair_address_12919484);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919484) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919484) + (0x10UL))));
#endif
        __arm64_pair_address_12919488 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919488);
#else
        v2 = __ReadVector128(__arm64_pair_address_12919488);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919488) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919488) + (0x10UL))));
#endif
        x8 = unchecked((ulong)((sp) + (0xD0UL)));
        x0 = unchecked((ulong)((sp) + (0x90UL)));
        __arm64_pair_address_12919500 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919500, v0);
#else
        __WriteVector128(__arm64_pair_address_12919500, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919500) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919500) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12919504 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919504);
#else
        v0 = __ReadVector128(__arm64_pair_address_12919504);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919504) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919504) + (0x10UL))));
#endif
        __arm64_pair_address_12919508 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919508, v2);
#else
        __WriteVector128(__arm64_pair_address_12919508, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919508) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919508) + (0x10UL))), v3);
#endif
        __arm64_pair_address_12919512 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919512);
#else
        v2 = __ReadVector128(__arm64_pair_address_12919512);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919512) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919512) + (0x10UL))));
#endif
        x1 = unchecked((ulong)((sp) + (0x50UL)));
        x2 = 0x0UL;
        __arm64_pair_address_12919524 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919524, v0);
#else
        __WriteVector128(__arm64_pair_address_12919524, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919524) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919524) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12919528 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919528, v2);
#else
        __WriteVector128(__arm64_pair_address_12919528, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919528) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919528) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1786E8CUL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
        __arm64_pair_address_12919536 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919536);
#else
        v1 = __ReadVector128(__arm64_pair_address_12919536);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919536) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919536) + (0x10UL))));
#endif
        __arm64_pair_address_12919540 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919540);
#else
        v3 = __ReadVector128(__arm64_pair_address_12919540);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919540) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919540) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x10UL)));
        __arm64_pair_address_12919548 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919548, v1);
#else
        __WriteVector128(__arm64_pair_address_12919548, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919548) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919548) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12919552 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919552, v3);
#else
        __WriteVector128(__arm64_pair_address_12919552, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919552) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919552) + (0x10UL))), v2);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x38UL))))));
        __arm64_pair_address_12919560 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919560, v1);
#else
        __WriteVector128(__arm64_pair_address_12919560, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919560) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919560) + (0x10UL))), v0);
#endif
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        __arm64_pair_address_12919568 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919568, v3);
#else
        __WriteVector128(__arm64_pair_address_12919568, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919568) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919568) + (0x10UL))), v2);
#endif
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0xFFFFFFFEUL)))))));
        __arm64_flags_left_12919576 = unchecked((uint)(x8));
        __arm64_flags_right_12919576 = unchecked((uint)0x2UL);
        x1 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12919576) - (__arm64_flags_right_12919576))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        v1 = v11;
        v2 = v12;
        v3 = v13;
        x0 = RuntimeCalls.InvokeDirect(0xC52460UL /* metadata target: CFUtils.TransformRect */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_12919600 = unchecked((ulong)((sp) + (0x4UL)));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12919600)), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12919600) + (0x4UL))))), 0));
        v6 = v14;
        v7 = v15;
        x0 = RuntimeCalls.InvokeDirect(0xC59144UL /* metadata target: CFUtils.ClampRectInsideRect */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        v11 = v0;
        v12 = v1;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52368;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC52368;
        label_0xC52368:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12919672 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12919672)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12919672) + (0x4UL))))), 0));
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2ECUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12919704 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12919704 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12919704 < __arm64_float_flags_right_12919704))
        {
            goto label_0xC523F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC52420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x150UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12919740 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919740);
#else
        v0 = __ReadVector128(__arm64_pair_address_12919740);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919740) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919740) + (0x10UL))));
#endif
        __arm64_pair_address_12919744 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12919744);
#else
        v2 = __ReadVector128(__arm64_pair_address_12919744);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12919744) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12919744) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x190UL)));
        x1 = 0x0UL;
        __arm64_pair_address_12919756 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919756, v0);
#else
        __WriteVector128(__arm64_pair_address_12919756, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919756) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919756) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12919760 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12919760, v2);
#else
        __WriteVector128(__arm64_pair_address_12919760, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12919760) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12919760) + (0x10UL))), v3);
#endif
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = v11;
        v1 = v12;
        x0 = RuntimeCalls.InvokeDirect(0x1787244UL /* metadata target: Matrix4x4.MultiplyVector */, x0, x1, x2, x3);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC523F0;
        label_0xC523F0:
        ;
        v0 = v10;
        v1 = v9;
        v2 = v8;
        sp = unchecked((ulong)((sp) + (0x210UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_12919820 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12919820)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12919820) + (0x8UL))))), 0));
        __arm64_pair_address_12919824 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12919824)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12919824) + (0x8UL))))), 0));
        __arm64_pair_address_12919828 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12919828)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12919828) + (0x8UL))))), 0));
        __arm64_pair_address_12919832 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12919832)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12919832) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12919832) + (0x70UL)));
        return x0;
        label_0xC52420:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.ClampInsideOther` — RVA `0xc524b8`

- Lift status: **exact**; input span: 636 bytes; span to next metadata RVA: 636 bytes.
- Metadata signature: `protected Vector3 ClampInsideOther(Vector3 targetWorldPos, TouchControl limiter) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=72 (informational only).

```csharp
public static ulong TouchControl_ClampInsideOther_RVAc524b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12920332 = default(uint);
        uint __arm64_flags_left_12920368 = default(uint);
        uint __arm64_flags_right_12920332 = default(uint);
        uint __arm64_flags_right_12920368 = default(uint);
        float __arm64_float_flags_left_12920492 = default(float);
        float __arm64_float_flags_right_12920492 = default(float);
        ulong __arm64_pair_address_12919992 = default(ulong);
        ulong __arm64_pair_address_12919996 = default(ulong);
        ulong __arm64_pair_address_12920000 = default(ulong);
        ulong __arm64_pair_address_12920004 = default(ulong);
        ulong __arm64_pair_address_12920028 = default(ulong);
        ulong __arm64_pair_address_12920032 = default(ulong);
        ulong __arm64_pair_address_12920120 = default(ulong);
        ulong __arm64_pair_address_12920148 = default(ulong);
        ulong __arm64_pair_address_12920152 = default(ulong);
        ulong __arm64_pair_address_12920164 = default(ulong);
        ulong __arm64_pair_address_12920168 = default(ulong);
        ulong __arm64_pair_address_12920192 = default(ulong);
        ulong __arm64_pair_address_12920196 = default(ulong);
        ulong __arm64_pair_address_12920208 = default(ulong);
        ulong __arm64_pair_address_12920216 = default(ulong);
        ulong __arm64_pair_address_12920240 = default(ulong);
        ulong __arm64_pair_address_12920244 = default(ulong);
        ulong __arm64_pair_address_12920256 = default(ulong);
        ulong __arm64_pair_address_12920260 = default(ulong);
        ulong __arm64_pair_address_12920264 = default(ulong);
        ulong __arm64_pair_address_12920268 = default(ulong);
        ulong __arm64_pair_address_12920280 = default(ulong);
        ulong __arm64_pair_address_12920284 = default(ulong);
        ulong __arm64_pair_address_12920292 = default(ulong);
        ulong __arm64_pair_address_12920296 = default(ulong);
        ulong __arm64_pair_address_12920304 = default(ulong);
        ulong __arm64_pair_address_12920308 = default(ulong);
        ulong __arm64_pair_address_12920320 = default(ulong);
        ulong __arm64_pair_address_12920324 = default(ulong);
        ulong __arm64_pair_address_12920376 = default(ulong);
        ulong __arm64_pair_address_12920392 = default(ulong);
        ulong __arm64_pair_address_12920460 = default(ulong);
        ulong __arm64_pair_address_12920528 = default(ulong);
        ulong __arm64_pair_address_12920532 = default(ulong);
        ulong __arm64_pair_address_12920544 = default(ulong);
        ulong __arm64_pair_address_12920548 = default(ulong);
        ulong __arm64_pair_address_12920604 = default(ulong);
        ulong __arm64_pair_address_12920608 = default(ulong);
        ulong __arm64_pair_address_12920612 = default(ulong);
        ulong __arm64_pair_address_12920616 = default(ulong);
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
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x29 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12919992 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12919992, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12919992) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        sp = __arm64_pair_address_12919992;
        __arm64_pair_address_12919996 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12919996, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12919996) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12920000 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12920000, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12920000) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12920004 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12920004, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12920004) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        sp = unchecked((ulong)((sp) - (0x210UL)));
        v9 = v1;
        v1 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        __arm64_pair_address_12920028 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920028, v1);
#else
        __WriteVector128(__arm64_pair_address_12920028, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920028) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920028) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12920032 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920032, v1);
#else
        __WriteVector128(__arm64_pair_address_12920032, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920032) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920032) + (0x10UL))), v1);
#endif
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x1;
        v8 = v2;
        x20 = x0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        v10 = v0;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xC52730;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        v15 = v0;
        v11 = v1;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        v12 = v2;
        v13 = v3;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        v14 = v0;
        __arm64_pair_address_12920120 = unchecked((ulong)((sp) + (0x4UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12920120, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12920120) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0xCUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC52730;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x1D0UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DEA0UL /* metadata target: Transform.get_worldToLocalMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12920148 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920148);
#else
        v0 = __ReadVector128(__arm64_pair_address_12920148);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920148) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920148) + (0x10UL))));
#endif
        __arm64_pair_address_12920152 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920152);
#else
        v2 = __ReadVector128(__arm64_pair_address_12920152);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920152) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920152) + (0x10UL))));
#endif
        x0 = x20;
        x1 = 0x0UL;
        __arm64_pair_address_12920164 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920164, v0);
#else
        __WriteVector128(__arm64_pair_address_12920164, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920164) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920164) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12920168 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920168, v2);
#else
        __WriteVector128(__arm64_pair_address_12920168, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920168) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920168) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC52730;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x1D0UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12920192 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v4 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920192);
#else
        v4 = __ReadVector128(__arm64_pair_address_12920192);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920192) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920192) + (0x10UL))));
#endif
        __arm64_pair_address_12920196 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920196);
#else
        v1 = __ReadVector128(__arm64_pair_address_12920196);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920196) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920196) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x110UL)));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        __arm64_pair_address_12920208 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920208, v4);
#else
        __WriteVector128(__arm64_pair_address_12920208, v4);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920208) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920208) + (0x10UL))), v0);
#endif
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x14CUL))))), 0));
        __arm64_pair_address_12920216 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920216, v1);
#else
        __WriteVector128(__arm64_pair_address_12920216, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920216) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920216) + (0x10UL))), v2);
#endif
        v0 = v10;
        v1 = v9;
        v2 = v8;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178708CUL /* metadata target: Matrix4x4.SetColumn */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_pair_address_12920240 = unchecked((ulong)((sp) + (0x110UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920240);
#else
        v0 = __ReadVector128(__arm64_pair_address_12920240);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920240) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920240) + (0x10UL))));
#endif
        __arm64_pair_address_12920244 = unchecked((ulong)((sp) + (0x130UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920244);
#else
        v2 = __ReadVector128(__arm64_pair_address_12920244);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920244) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920244) + (0x10UL))));
#endif
        x8 = unchecked((ulong)((sp) + (0xD0UL)));
        x0 = unchecked((ulong)((sp) + (0x90UL)));
        __arm64_pair_address_12920256 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920256, v0);
#else
        __WriteVector128(__arm64_pair_address_12920256, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920256) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920256) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12920260 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920260);
#else
        v0 = __ReadVector128(__arm64_pair_address_12920260);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920260) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920260) + (0x10UL))));
#endif
        __arm64_pair_address_12920264 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920264, v2);
#else
        __WriteVector128(__arm64_pair_address_12920264, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920264) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920264) + (0x10UL))), v3);
#endif
        __arm64_pair_address_12920268 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920268);
#else
        v2 = __ReadVector128(__arm64_pair_address_12920268);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920268) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920268) + (0x10UL))));
#endif
        x1 = unchecked((ulong)((sp) + (0x50UL)));
        x2 = 0x0UL;
        __arm64_pair_address_12920280 = unchecked((ulong)((sp) + (0x90UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920280, v0);
#else
        __WriteVector128(__arm64_pair_address_12920280, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920280) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920280) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12920284 = unchecked((ulong)((sp) + (0xB0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920284, v2);
#else
        __WriteVector128(__arm64_pair_address_12920284, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920284) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920284) + (0x10UL))), v3);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x1786E8CUL /* metadata target: Matrix4x4.op_Multiply */, x0, x1, x2, x3);
        __arm64_pair_address_12920292 = unchecked((ulong)((sp) + (0xF0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920292);
#else
        v1 = __ReadVector128(__arm64_pair_address_12920292);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920292) + (0x10UL))));
#else
        v0 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920292) + (0x10UL))));
#endif
        __arm64_pair_address_12920296 = unchecked((ulong)((sp) + (0xD0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920296);
#else
        v3 = __ReadVector128(__arm64_pair_address_12920296);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920296) + (0x10UL))));
#else
        v2 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920296) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x10UL)));
        __arm64_pair_address_12920304 = unchecked((ulong)((sp) + (0x1F0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920304, v1);
#else
        __WriteVector128(__arm64_pair_address_12920304, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920304) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920304) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12920308 = unchecked((ulong)((sp) + (0x1D0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920308, v3);
#else
        __WriteVector128(__arm64_pair_address_12920308, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920308) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920308) + (0x10UL))), v2);
#endif
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x38UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x38UL))))));
        __arm64_pair_address_12920320 = unchecked((ulong)((sp) + (0x10UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920320, v3);
#else
        __WriteVector128(__arm64_pair_address_12920320, v3);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920320) + (0x10UL))), v2);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920320) + (0x10UL))), v2);
#endif
        __arm64_pair_address_12920324 = unchecked((ulong)((sp) + (0x30UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920324, v1);
#else
        __WriteVector128(__arm64_pair_address_12920324, v1);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920324) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920324) + (0x10UL))), v0);
#endif
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)(0xFFFFFFFEUL)))))));
        __arm64_flags_left_12920332 = unchecked((uint)(x8));
        __arm64_flags_right_12920332 = unchecked((uint)0x2UL);
        x1 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12920332) - (__arm64_flags_right_12920332))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        v0 = v15;
        v1 = v11;
        v2 = v12;
        v3 = v13;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(0xFFFFFFFEUL)))))));
        x0 = RuntimeCalls.InvokeDirect(0xC52460UL /* metadata target: CFUtils.TransformRect */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        v4 = v14;
        __arm64_flags_left_12920368 = unchecked((uint)(x20));
        __arm64_flags_right_12920368 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12920368) - (__arm64_flags_right_12920368))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC52648;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC52638UL);
        }
        __arm64_pair_address_12920376 = unchecked((ulong)((sp) + (0x4UL)));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12920376)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12920376) + (0x4UL))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC58F50UL /* metadata target: CFUtils.ClampEllipseInsideEllipse */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC52654;
        label_0xC52648:
        ;
        __arm64_pair_address_12920392 = unchecked((ulong)((sp) + (0x4UL)));
        v5 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12920392)), 0));
        v6 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12920392) + (0x4UL))))), 0));
        v7 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC59144UL /* metadata target: CFUtils.ClampRectInsideRect */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC52654;
        label_0xC52654:
        ;
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        v11 = v0;
        v12 = v1;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5267C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5267C;
        label_0xC5267C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x138UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12920460 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12920460)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12920460) + (0x4UL))))), 0));
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x2ECUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12920492 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12920492 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12920492 < __arm64_float_flags_right_12920492))
        {
            goto label_0xC52704;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC52730;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((sp) + (0x150UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D12CUL /* metadata target: Transform.get_localToWorldMatrix */, x0, x1, x2, x3);
        __arm64_pair_address_12920528 = unchecked((ulong)((sp) + (0x150UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v0 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920528);
#else
        v0 = __ReadVector128(__arm64_pair_address_12920528);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v1 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920528) + (0x10UL))));
#else
        v1 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920528) + (0x10UL))));
#endif
        __arm64_pair_address_12920532 = unchecked((ulong)((sp) + (0x170UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        v2 = RuntimeMemory.ReadVector128(__arm64_pair_address_12920532);
#else
        v2 = __ReadVector128(__arm64_pair_address_12920532);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        v3 = RuntimeMemory.ReadVector128(unchecked((ulong)((__arm64_pair_address_12920532) + (0x10UL))));
#else
        v3 = __ReadVector128(unchecked((ulong)((__arm64_pair_address_12920532) + (0x10UL))));
#endif
        x0 = unchecked((ulong)((sp) + (0x190UL)));
        x1 = 0x0UL;
        __arm64_pair_address_12920544 = unchecked((ulong)((sp) + (0x190UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920544, v0);
#else
        __WriteVector128(__arm64_pair_address_12920544, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920544) + (0x10UL))), v1);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920544) + (0x10UL))), v1);
#endif
        __arm64_pair_address_12920548 = unchecked((ulong)((sp) + (0x1B0UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12920548, v2);
#else
        __WriteVector128(__arm64_pair_address_12920548, v2);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12920548) + (0x10UL))), v3);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12920548) + (0x10UL))), v3);
#endif
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = v11;
        v1 = v12;
        x0 = RuntimeCalls.InvokeDirect(0x1787244UL /* metadata target: Matrix4x4.MultiplyVector */, x0, x1, x2, x3);
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC52704;
        label_0xC52704:
        ;
        v0 = v10;
        v1 = v9;
        v2 = v8;
        sp = unchecked((ulong)((sp) + (0x210UL)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        __arm64_pair_address_12920604 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12920604)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12920604) + (0x8UL))))), 0));
        __arm64_pair_address_12920608 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12920608)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12920608) + (0x8UL))))), 0));
        __arm64_pair_address_12920612 = unchecked((ulong)((sp) + (0x10UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12920612)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12920612) + (0x8UL))))), 0));
        __arm64_pair_address_12920616 = sp;
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12920616)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12920616) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12920616) + (0x60UL)));
        return x0;
        label_0xC52730:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControl.RaycastLocal` — RVA `0xc52734`

- Lift status: **partial**; input span: 236 bytes; span to next metadata RVA: 236 bytes.
- Metadata signature: `public bool RaycastLocal(Vector2 localPos) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=10 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lt' at 0xc527ac; reason: Unknown IR expression at 0xc527ac

```csharp
public static uint TouchControl_RaycastLocal_RVAc52734(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12920668 = default(uint);
        uint __arm64_flags_left_12920676 = default(uint);
        uint __arm64_flags_left_12920684 = default(uint);
        uint __arm64_flags_right_12920668 = default(uint);
        uint __arm64_flags_right_12920676 = default(uint);
        uint __arm64_flags_right_12920684 = default(uint);
        float __arm64_float_flags_left_12920740 = default(float);
        float __arm64_float_flags_left_12920752 = default(float);
        float __arm64_float_flags_left_12920764 = default(float);
        float __arm64_float_flags_left_12920776 = default(float);
        float __arm64_float_flags_left_12920836 = default(float);
        float __arm64_float_flags_right_12920740 = default(float);
        float __arm64_float_flags_right_12920752 = default(float);
        float __arm64_float_flags_right_12920764 = default(float);
        float __arm64_float_flags_right_12920776 = default(float);
        float __arm64_float_flags_right_12920836 = default(float);
        ulong __arm64_pair_address_12920628 = default(ulong);
        ulong __arm64_pair_address_12920856 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_pair_address_12920628 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12920628, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12920628) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12920628;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(x0);
        v8 = v1;
        x19 = x0;
        v9 = v0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x38UL))))));
        __arm64_flags_left_12920668 = unchecked((uint)(x8));
        __arm64_flags_right_12920668 = unchecked((uint)0x2UL);
        if ((!((__arm64_flags_left_12920668 >= __arm64_flags_right_12920668))))
        {
            goto label_0xC527A4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52764UL)));
        }
        __arm64_flags_left_12920676 = unchecked((uint)(x8));
        __arm64_flags_right_12920676 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_12920676) - (__arm64_flags_right_12920676))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC527D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5276CUL)));
        }
        __arm64_flags_left_12920684 = unchecked((uint)(x8));
        __arm64_flags_right_12920684 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12920684) - (__arm64_flags_right_12920684))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC52810;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52774UL)));
        }
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        goto label_0xC52804;
        label_0xC527A4:
        ;
        __arm64_float_flags_left_12920740 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12920740 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeCalls.Unsupported("b.lt", 0xC527ACUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC52814;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC527B0UL)));
        }
        __arm64_float_flags_left_12920752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12920752 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12920752 < __arm64_float_flags_right_12920752) || ((__arm64_float_flags_left_12920752 != __arm64_float_flags_left_12920752) || (__arm64_float_flags_right_12920752 != __arm64_float_flags_right_12920752))))
        {
            goto label_0xC52814;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC527B8UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12920764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12920764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12920764 > __arm64_float_flags_right_12920764) || ((__arm64_float_flags_left_12920764 != __arm64_float_flags_left_12920764) || (__arm64_float_flags_right_12920764 != __arm64_float_flags_right_12920764))))
        {
            goto label_0xC52814;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC527C4UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12920776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12920776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        goto label_0xC52808;
        label_0xC527D0:
        ;
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC52804;
        label_0xC52804:
        ;
        __arm64_float_flags_left_12920836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12920836 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        goto label_0xC52808;
        label_0xC52808:
        ;
        x0 = unchecked((ulong)(((__arm64_float_flags_left_12920836 <= __arm64_float_flags_right_12920836) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC52814;
        label_0xC52810:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC52814;
        label_0xC52814:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_pair_address_12920856 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12920856)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12920856) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12920856) + (0x20UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchControl.HitTest` — RVA `0xc52820`

- Lift status: **partial**; input span: 1144 bytes; span to next metadata RVA: 1144 bytes.
- Metadata signature: `public bool HitTest(Vector2 sp, Camera cam, float fingerRadPx, TouchControl.Hit hit) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=113 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fcsel' at 0xc52c28; reason: Unknown IR expression at 0xc52c28; reason: Unsupported instruction 'fcsel' at 0xc52c2c; reason: Unknown IR expression at 0xc52c2c

```csharp
public static uint TouchControl_HitTest_RVAc52820(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12920968 = default(uint);
        uint __arm64_flags_left_12921132 = default(uint);
        uint __arm64_flags_left_12921144 = default(uint);
        uint __arm64_flags_left_12921164 = default(uint);
        uint __arm64_flags_left_12921880 = default(uint);
        uint __arm64_flags_right_12920968 = default(uint);
        uint __arm64_flags_right_12921132 = default(uint);
        uint __arm64_flags_right_12921144 = default(uint);
        uint __arm64_flags_right_12921164 = default(uint);
        uint __arm64_flags_right_12921880 = default(uint);
        float __arm64_float_flags_left_12920976 = default(float);
        float __arm64_float_flags_left_12921188 = default(float);
        float __arm64_float_flags_left_12921296 = default(float);
        float __arm64_float_flags_left_12921320 = default(float);
        float __arm64_float_flags_left_12921332 = default(float);
        float __arm64_float_flags_left_12921348 = default(float);
        float __arm64_float_flags_left_12921364 = default(float);
        float __arm64_float_flags_left_12921404 = default(float);
        float __arm64_float_flags_left_12921420 = default(float);
        float __arm64_float_flags_left_12921516 = default(float);
        float __arm64_float_flags_left_12921812 = default(float);
        float __arm64_float_flags_right_12920976 = default(float);
        float __arm64_float_flags_right_12921188 = default(float);
        float __arm64_float_flags_right_12921296 = default(float);
        float __arm64_float_flags_right_12921320 = default(float);
        float __arm64_float_flags_right_12921332 = default(float);
        float __arm64_float_flags_right_12921348 = default(float);
        float __arm64_float_flags_right_12921364 = default(float);
        float __arm64_float_flags_right_12921404 = default(float);
        float __arm64_float_flags_right_12921420 = default(float);
        float __arm64_float_flags_right_12921516 = default(float);
        float __arm64_float_flags_right_12921812 = default(float);
        ulong __arm64_pair_address_12920868 = default(ulong);
        ulong __arm64_pair_address_12920872 = default(ulong);
        ulong __arm64_pair_address_12920876 = default(ulong);
        ulong __arm64_pair_address_12920880 = default(ulong);
        ulong __arm64_pair_address_12921004 = default(ulong);
        ulong __arm64_pair_address_12921020 = default(ulong);
        ulong __arm64_pair_address_12921128 = default(ulong);
        ulong __arm64_pair_address_12921548 = default(ulong);
        ulong __arm64_pair_address_12921604 = default(ulong);
        ulong __arm64_pair_address_12921612 = default(ulong);
        ulong __arm64_pair_address_12921656 = default(ulong);
        ulong __arm64_pair_address_12921660 = default(ulong);
        ulong __arm64_pair_address_12921712 = default(ulong);
        ulong __arm64_pair_address_12921716 = default(ulong);
        ulong __arm64_pair_address_12921876 = default(ulong);
        ulong __arm64_pair_address_12921892 = default(ulong);
        ulong __arm64_pair_address_12921904 = default(ulong);
        ulong __arm64_pair_address_12921948 = default(ulong);
        ulong __arm64_pair_address_12921952 = default(ulong);
        ulong __arm64_pair_address_12921980 = default(ulong);
        ulong __arm64_pair_address_12921984 = default(ulong);
        ulong __arm64_pair_address_12921988 = default(ulong);
        ulong __arm64_pair_address_12921992 = default(ulong);
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
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        __arm64_pair_address_12920868 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12920868, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v15.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12920868) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v14.GetUInt64(0)))));
        __arm64_pair_address_12920872 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12920872, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v13.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12920872) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_12920876 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12920876, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12920876) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_12920880 = unchecked((ulong)((sp) + (0x40UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12920880, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12920880) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x50UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x19);
        if ((x2 == 0x0UL))
        {
            goto label_0xC52C94;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = x2;
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x10UL))), 0x0UL);
        x20 = x1;
        x21 = x0;
        x0 = x22;
        x1 = 0x0UL;
        x19 = x2;
        v10 = v2;
        v8 = v1;
        v9 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x26 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x22UL))))))));
        x8 = 0x432000UL;
        v15 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x534UL))))), 0));
        x0 = x21;
        __arm64_flags_left_12920968 = unchecked((uint)(x26));
        __arm64_flags_right_12920968 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12920968) - (__arm64_flags_right_12920968))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_float_flags_left_12920976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12920976 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0);
        x9 = unchecked((ulong)((((__arm64_float_flags_left_12920976 >= __arm64_float_flags_right_12920976) || ((__arm64_float_flags_left_12920976 != __arm64_float_flags_left_12920976) || (__arm64_float_flags_right_12920976 != __arm64_float_flags_right_12920976))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        v0 = v9;
        v1 = v8;
        x1 = x20;
        RuntimeMemory.WriteF32(sp, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0));
        x23 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
        __arm64_pair_address_12921004 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12921004, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12921004) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC50F2CUL /* metadata target: TouchControl.ScreenToLocalPos */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x21;
        __arm64_pair_address_12921020 = unchecked((ulong)((sp) + (0x58UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12921020, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12921020) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x390UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x24 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x1E0UL))))))));
        v12 = v0;
        v14 = v1;
        v8 = v2;
        v9 = v3;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC528FC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC528FC;
        label_0xC528FC:
        ;
        x25 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x138UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        x8 = RuntimeMemory.ReadU64(x25);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x38UL))))));
        __arm64_pair_address_12921128 = x9;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921128)), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921128) + (0x4UL))))), 0));
        __arm64_flags_left_12921132 = unchecked((uint)(x8));
        __arm64_flags_right_12921132 = unchecked((uint)0x2UL);
        if ((!((__arm64_flags_left_12921132 >= __arm64_flags_right_12921132))))
        {
            goto label_0xC529E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52934UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x58UL))))), 0));
        __arm64_flags_left_12921144 = unchecked((uint)(x8));
        __arm64_flags_right_12921144 = unchecked((uint)0x3UL);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x5CUL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0))))), 0));
        if ((unchecked((uint)((__arm64_flags_left_12921144) - (__arm64_flags_right_12921144))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52A24;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5294CUL)));
        }
        __arm64_flags_left_12921164 = unchecked((uint)(x8));
        __arm64_flags_right_12921164 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12921164) - (__arm64_flags_right_12921164))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC52AC0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52954UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12921188 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921188 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(((__arm64_float_flags_left_12921188 <= __arm64_float_flags_right_12921188) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if ((__arm64_float_flags_left_12921188 <= __arm64_float_flags_right_12921188))
        {
            goto label_0xC52AF8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) ^ (unchecked((uint)(0x1UL)))))));
        if ((unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52AF8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x26 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x243UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC529A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        v12 = v2;
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        v2 = v12;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC529A0;
        label_0xC529A0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC529C0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        v12 = v2;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        v2 = v12;
        goto label_0xC529C0;
        label_0xC529C0:
        ;
        x8 = 0x432000UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))))), 0));
        v15 = v2;
        __arm64_float_flags_left_12921296 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921296 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12921296 <= __arm64_float_flags_right_12921296) || ((__arm64_float_flags_left_12921296 != __arm64_float_flags_left_12921296) || (__arm64_float_flags_right_12921296 != __arm64_float_flags_right_12921296))))
        {
            goto label_0xC52B14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC529D8UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC52B3C;
        label_0xC529E4:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x5CUL))))), 0));
        __arm64_float_flags_left_12921320 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921320 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12921320 < __arm64_float_flags_right_12921320) || ((__arm64_float_flags_left_12921320 != __arm64_float_flags_left_12921320) || (__arm64_float_flags_right_12921320 != __arm64_float_flags_right_12921320))))
        {
            goto label_0xC52AC8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC529F0UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x58UL))))), 0));
        __arm64_float_flags_left_12921332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921332 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12921332 < __arm64_float_flags_right_12921332) || ((__arm64_float_flags_left_12921332 != __arm64_float_flags_left_12921332) || (__arm64_float_flags_right_12921332 != __arm64_float_flags_right_12921332))))
        {
            goto label_0xC52AC8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC529FCUL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x58UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12921348 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921348 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12921348 > __arm64_float_flags_right_12921348) || ((__arm64_float_flags_left_12921348 != __arm64_float_flags_left_12921348) || (__arm64_float_flags_right_12921348 != __arm64_float_flags_right_12921348))))
        {
            goto label_0xC52AC8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52A0CUL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x5CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12921364 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921364 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12921364 > __arm64_float_flags_right_12921364) || ((__arm64_float_flags_left_12921364 != __arm64_float_flags_left_12921364) || (__arm64_float_flags_right_12921364 != __arm64_float_flags_right_12921364))))
        {
            goto label_0xC52AC8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        v15 = v2;
        goto label_0xC52B00;
        label_0xC52A24:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_float_flags_left_12921404 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921404 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        x8 = unchecked((ulong)(((__arm64_float_flags_left_12921404 <= __arm64_float_flags_right_12921404) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if ((__arm64_float_flags_left_12921404 <= __arm64_float_flags_right_12921404))
        {
            goto label_0xC52AF8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52A48UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        __arm64_float_flags_left_12921420 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921420 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v15.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12921420 < __arm64_float_flags_right_12921420))
        {
            goto label_0xC52AF8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52A54UL)));
        }
        if ((unchecked((uint)(x26)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52AF8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x26 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x26) + (0x243UL))))))));
        v15 = v2;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52A7C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x26) + (0x243UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC52A7C;
        label_0xC52A7C:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA60UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52A94;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52A90UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC52A94;
        label_0xC52A94:
        ;
        x8 = 0x432000UL;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x41CUL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(global::System.Math.Sqrt(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))))), 0));
        __arm64_float_flags_left_12921516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921516 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12921516 <= __arm64_float_flags_right_12921516) || ((__arm64_float_flags_left_12921516 != __arm64_float_flags_left_12921516) || (__arm64_float_flags_right_12921516 != __arm64_float_flags_right_12921516))))
        {
            goto label_0xC52B4C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52AB4UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC52B74;
        label_0xC52AC0:
        ;
        v15 = v2;
        goto label_0xC52B0C;
        label_0xC52AC8:
        ;
        if ((unchecked((uint)(x23)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52BDC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC52ACCUL)));
        }
        __arm64_pair_address_12921548 = unchecked((ulong)((sp) + (0x58UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921548)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921548) + (0x4UL))))), 0));
        v15 = v2;
        v2 = v12;
        v3 = v14;
        v4 = v8;
        v5 = v9;
        x0 = RuntimeCalls.InvokeDirect(0xC52CA4UL /* metadata target: CFUtils.ClampInsideRect */, x0, x1, x2, x3);
        v3 = v0;
        v13 = v1;
        x24 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC52B04;
        label_0xC52AF8:
        ;
        v15 = v2;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52B0C;
        }
        else
        {
            goto label_0xC52B00;
        }
        label_0xC52B00:
        ;
        x24 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC52B04;
        label_0xC52B04:
        ;
        __arm64_pair_address_12921604 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921604)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921604) + (0x4UL))))), 0));
        goto label_0xC52B8C;
        label_0xC52B0C:
        ;
        __arm64_pair_address_12921612 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921612)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921612) + (0x4UL))))), 0));
        goto label_0xC52B80;
        label_0xC52B14:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x24))))) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52B30;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x24))))) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC52B30;
        label_0xC52B30:
        ;
        x8 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12921656 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921656)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921656) + (0x4UL))))), 0));
        goto label_0xC52B3C;
        label_0xC52B3C:
        ;
        __arm64_pair_address_12921660 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921660)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921660) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC52B80;
        label_0xC52B4C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x24))))) + (0x1E0UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52B68;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x24))))) + (0x1E0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC52B68;
        label_0xC52B68:
        ;
        x8 = RuntimeMemory.ReadU64(x25);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        __arm64_pair_address_12921712 = x8;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921712)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921712) + (0x4UL))))), 0));
        goto label_0xC52B74;
        label_0xC52B74:
        ;
        __arm64_pair_address_12921716 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921716)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921716) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v13 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        goto label_0xC52B80;
        label_0xC52B80:
        ;
        x24 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        if ((unchecked((uint)(x23)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52C68;
        }
        else
        {
            goto label_0xC52B8C;
        }
        label_0xC52B8C:
        ;
        x0 = x21;
        v0 = v3;
        v1 = v13;
        x1 = x20;
        v10 = v3;
        x0 = RuntimeCalls.InvokeDirect(0xC51468UL /* metadata target: TouchControl.LocalToScreenPos */, x0, x1, x2, x3);
        v14 = v0;
        v12 = v1;
        if ((unchecked((uint)((unchecked((uint)(x24))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52BB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC52BE8;
        label_0xC52BB8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(sp)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        __arm64_float_flags_left_12921812 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12921812 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12921812 <= __arm64_float_flags_right_12921812))
        {
            goto label_0xC52BE4;
        }
        else
        {
            goto label_0xC52BDC;
        }
        label_0xC52BDC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC52C68;
        label_0xC52BE4:
        ;
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC52BE8;
        label_0xC52BE8:
        ;
        x0 = x22;
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x10UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x21;
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1CUL))), unchecked((byte)(unchecked((uint)(x23)))));
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC52C94;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179D508UL /* metadata target: Transform.get_position */, x0, x1, x2, x3);
        __arm64_pair_address_12921876 = unchecked((ulong)((sp) + (0x58UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12921876)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12921876) + (0x4UL))))), 0));
        __arm64_flags_left_12921880 = unchecked((uint)(x24));
        __arm64_flags_right_12921880 = unchecked((uint)0x0UL);
        x0 = x21;
        x1 = x20;
        __arm64_pair_address_12921892 = unchecked((ulong)((x19) + (0x20UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12921892, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12921892) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        RuntimeCalls.Unsupported("fcsel", 0xC52C28UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))), 0));
        RuntimeCalls.Unsupported("fcsel", 0xC52C2CUL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((__Unsupported<bool>("Unknown IR expression") ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v13.GetUInt64(0)))), 0))), 0));
        __arm64_pair_address_12921904 = unchecked((ulong)((x19) + (0x28UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12921904, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12921904) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x4UL))))), 0));
        v1 = v15;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x18UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC51468UL /* metadata target: TouchControl.LocalToScreenPos */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        __arm64_pair_address_12921948 = unchecked((ulong)((x19) + (0x30UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12921948, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12921948) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0));
        __arm64_pair_address_12921952 = unchecked((ulong)((x19) + (0x38UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12921952, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v14.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12921952) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x40UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC52C68;
        label_0xC52C68:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        __arm64_pair_address_12921980 = unchecked((ulong)((sp) + (0x40UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12921980)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12921980) + (0x8UL))))), 0));
        __arm64_pair_address_12921984 = unchecked((ulong)((sp) + (0x30UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12921984)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12921984) + (0x8UL))))), 0));
        __arm64_pair_address_12921988 = unchecked((ulong)((sp) + (0x20UL)));
        v13 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12921988)), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12921988) + (0x8UL))))), 0));
        __arm64_pair_address_12921992 = unchecked((ulong)((sp) + (0x10UL)));
        v15 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12921992)), 0));
        v14 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12921992) + (0x8UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xA0UL)));
        return unchecked((uint)(x0));
        label_0xC52C94:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `TouchControl.OnInitComponent` — RVA `0xc52d44`

- Lift status: **partial**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'fmov' at 0xc52d50

```csharp
public static ulong TouchControl_OnInitComponent_RVAc52d44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x7CUL))))), 0));
        x8 = RuntimeMemory.ReadU64(x0);
        RuntimeCalls.Unsupported("fmov", 0xC52D50UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x71UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x78UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x74UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x368UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x370UL))));
        x19 = x0;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x210UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4FBE4UL /* metadata target: TouchControl.SyncDisablingConditions */);
        return default(ulong);
    }
```

## `TouchControl.OnEnableComponent` — RVA `0xc52d94`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `protected override void OnEnableComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong TouchControl_OnEnableComponent_RVAc52d94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(x0);
        x19 = x0;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x298UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4FBE4UL /* metadata target: TouchControl.SyncDisablingConditions */);
        return default(ulong);
    }
```

## `TouchControl.OnDisableComponent` — RVA `0xc52dbc`

- Lift status: **exact**; input span: 60 bytes; span to next metadata RVA: 60 bytes.
- Metadata signature: `protected override void OnDisableComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong TouchControl_OnDisableComponent_RVAc52dbc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC4FBE4UL /* metadata target: TouchControl.SyncDisablingConditions */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x298UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `TouchControl.OnDestroyComponent` — RVA `0xc52df8`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static ulong TouchControl_OnDestroyComponent_RVAc52df8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC50168UL /* metadata target: TouchControl.SetRig */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC50318UL /* metadata target: TouchControl.SetTouchControlPanel */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x228UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x230UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `TouchControl.UpdateControl` — RVA `0xc52e2c`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `public void UpdateControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong TouchControl_UpdateControl_RVAc52e2c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52E40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC52E40:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        x19 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC52E64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC52E64;
        label_0xC52E64:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC500E4UL /* metadata target: TouchControl.UpdateBaseAlpha */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x218UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x220UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4FE90UL /* metadata target: TouchControl.UpdateAnimators */);
        return default(ulong);
    }
```

## `TouchControl.DrawDefaultGizmo` — RVA `0xc52e90`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `protected void DrawDefaultGizmo(bool drawFullRect) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_DrawDefaultGizmo_RVAc52e90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `TouchControl.DrawDefaultGizmo` — RVA `0xc52e94`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `protected void DrawDefaultGizmo(bool drawFullRect, float fullRectColorShade) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControl_DrawDefaultGizmo_RVAc52e94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `TouchControl.DrawCustomGizmos` — RVA `0xc52e98`

- Lift status: **exact**; input span: 112 bytes; span to next metadata RVA: 112 bytes.
- Metadata signature: `protected virtual void DrawCustomGizmos(bool selected) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong TouchControl_DrawCustomGizmos_RVAc52e98(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12922552 = default(uint);
        uint __arm64_flags_result_12922552 = default(uint);
        uint __arm64_flags_right_12922552 = default(uint);
        ulong __arm64_pair_address_12922520 = default(ulong);
        ulong __arm64_pair_address_12922524 = default(ulong);
        ulong __arm64_pair_address_12922608 = default(ulong);
        ulong __arm64_pair_address_12922624 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        __arm64_pair_address_12922520 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12922520, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12922520) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_12922520;
        __arm64_pair_address_12922524 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12922524, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12922524) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x0 = 0x0UL;
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x0 = RuntimeCalls.InvokeDirect(0x1776F08UL /* metadata target: Gizmos.get_color */, x0, x1, x2, x3);
        v8 = v0;
        v9 = v1;
        __arm64_flags_left_12922552 = unchecked((uint)(x19));
        __arm64_flags_right_12922552 = unchecked((uint)0x1UL);
        __arm64_flags_result_12922552 = unchecked((uint)((__arm64_flags_left_12922552) & (__arm64_flags_right_12922552)));
        v10 = v2;
        v11 = v3;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1776F8CUL /* metadata target: Gizmos.set_color */, x0, x1, x2, x3);
        v0 = v8;
        v1 = v9;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        __arm64_pair_address_12922608 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12922608)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12922608) + (0x8UL))))), 0));
        v2 = v10;
        v3 = v11;
        x0 = 0x0UL;
        __arm64_pair_address_12922624 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12922624)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12922624) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12922624) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0x1776F8CUL /* metadata target: Gizmos.set_color */);
        return default(ulong);
    }
```

## `TouchControl.OnDrawGizmos` — RVA `0xc52f08`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `private void OnDrawGizmos() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong TouchControl_OnDrawGizmos_RVAc52f08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52F24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3A0UL))));
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC52F24:
        ;
        return x0;
        return default(ulong);
    }
```

## `TouchControl.OnDrawGizmosSelected` — RVA `0xc52f28`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `private void OnDrawGizmosSelected() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong TouchControl_OnDrawGizmosSelected_RVAc52f28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC52F44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3A0UL))));
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC52F44:
        ;
        return x0;
        return default(ulong);
    }
```
