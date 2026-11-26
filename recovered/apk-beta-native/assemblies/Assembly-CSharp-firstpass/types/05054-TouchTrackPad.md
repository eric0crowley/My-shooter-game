# `TouchTrackPad` — TypeDefIndex 5054

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x88` | `float` | `touchSmoothing` |
| `0x90` | `DigitalBinding` | `pressBinding` |
| `0x98` | `AxisBinding` | `horzSwipeBinding` |
| `0xA0` | `AxisBinding` | `vertSwipeBinding` |
| `0xA8` | `bool` | `emulateTouchPressure` |
| `0xB0` | `AxisBinding` | `touchPressureBinding` |
| `0xB8` | `TouchObject` | `touchObj` |
| `0xC0` | `TouchControl.TouchStartType` | `touchStartType` |
| `0xC8` | `TouchGestureBasicState` | `touchState` |

## `TouchTrackPad.ctor` — RVA `0xc57978`

- Lift status: **exact**; input span: 400 bytes; span to next metadata RVA: 400 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=64 (informational only).

```csharp
public static ulong TouchTrackPad_ctor_RVAc57978(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x21 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x294UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x958UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x988UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x990UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x550UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x530UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC57A04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x990UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x958UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x530UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x550UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x294UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC57A04;
        label_0xC57A04:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4F488UL /* metadata target: TouchControl.ctor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F000000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x88UL))), unchecked((uint)(x8)));
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC61AE0UL /* metadata target: TouchGestureBasicState.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xC8UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5D544UL /* metadata target: InputBindingBase.ctor */, x0, x1, x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5BE6CUL /* metadata target: DigitalBinding.BasicConstructor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x90UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56D68UL /* metadata target: AxisBinding.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x98UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(x22);
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56D68UL /* metadata target: AxisBinding.ctor */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xA0UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xA8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5D544UL /* metadata target: InputBindingBase.ctor */, x0, x1, x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5B3B8UL /* metadata target: AxisBinding.BasicConstructor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xB0UL))), x20);
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

## `TouchTrackPad.Pressed` — RVA `0xc57b08`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public bool Pressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchTrackPad_Pressed_RVAc57b08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            label_0xC57B20:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1CUL))))))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `TouchTrackPad.JustPressed` — RVA `0xc57b24`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public bool JustPressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchTrackPad_JustPressed_RVAc57b24(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57B3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC61BF0UL /* metadata target: TouchGestureBasicState.JustPressedRaw */);
        label_0xC57B3C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPad.JustReleased` — RVA `0xc57b40`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public bool JustReleased() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchTrackPad_JustReleased_RVAc57b40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57B58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC61C10UL /* metadata target: TouchGestureBasicState.JustReleasedRaw */);
        label_0xC57B58:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPad.IsTouchPressureSensitive` — RVA `0xc57b5c`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public bool IsTouchPressureSensitive() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static uint TouchTrackPad_IsTouchPressureSensitive_RVAc57b5c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57B88;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC57B7C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC61CE4UL /* metadata target: TouchGestureBasicState.IsPressureSensitive */)));
        label_0xC57B7C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC57B88:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `TouchTrackPad.GetTouchPressure` — RVA `0xc57b8c`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public float GetTouchPressure() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchTrackPad_GetTouchPressure_RVAc57b8c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57BB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC57BAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC61D04UL /* metadata target: TouchGestureBasicState.GetPressure */);
        label_0xC57BAC:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC57BB8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPad.GetSwipeDelta` — RVA `0xc57bbc`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public Vector2 GetSwipeDelta() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchTrackPad_GetSwipeDelta_RVAc57bbc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57BD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC61C94UL /* metadata target: TouchGestureBasicState.GetDeltaVecSmooth */);
        label_0xC57BD4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPad.SetTouchSmoothing` — RVA `0xc57bd8`

- Lift status: **exact**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public void SetTouchSmoothing(float smTime) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchTrackPad_SetTouchSmoothing_RVAc57bd8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12942312 = default(float);
        float __arm64_float_flags_right_12942312 = default(float);
        float __arm64_fp_left_12942308 = default(float);
        float __arm64_fp_right_12942308 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_fp_left_12942308 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12942308 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12942308 != __arm64_fp_left_12942308) ? __arm64_fp_left_12942308 : ((__arm64_fp_right_12942308 != __arm64_fp_right_12942308) ? __arm64_fp_right_12942308 : (((__arm64_fp_left_12942308 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12942308 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12942308), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12942308), 0))))), 0) : ((__arm64_fp_left_12942308 <= __arm64_fp_right_12942308) ? __arm64_fp_left_12942308 : __arm64_fp_right_12942308))))), 0));
        __arm64_float_flags_left_12942312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12942312 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12942312 >= __arm64_float_flags_right_12942312) || ((__arm64_float_flags_left_12942312 != __arm64_float_flags_left_12942312) || (__arm64_float_flags_right_12942312 != __arm64_float_flags_right_12942312))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x88UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            label_0xC57C14:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x9 = 0x432000UL;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x3B8UL))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0xA4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            x30 = RuntimeMemory.ReadU64(sp);
            return x0;
        }
        return default(ulong);
    }
```

## `TouchTrackPad.OnInitControl` — RVA `0xc57c18`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `protected override void OnInitControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong TouchTrackPad_OnInitControl_RVAc57c18(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12942400 = default(float);
        float __arm64_float_flags_right_12942400 = default(float);
        float __arm64_fp_left_12942396 = default(float);
        float __arm64_fp_right_12942396 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
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
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x88UL))))), 0));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_fp_left_12942396 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12942396 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12942396 != __arm64_fp_left_12942396) ? __arm64_fp_left_12942396 : ((__arm64_fp_right_12942396 != __arm64_fp_right_12942396) ? __arm64_fp_right_12942396 : (((__arm64_fp_left_12942396 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12942396 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12942396), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12942396), 0))))), 0) : ((__arm64_fp_left_12942396 <= __arm64_fp_right_12942396) ? __arm64_fp_left_12942396 : __arm64_fp_right_12942396))))), 0));
        __arm64_float_flags_left_12942400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12942400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12942400 >= __arm64_float_flags_right_12942400) || ((__arm64_float_flags_left_12942400 != __arm64_float_flags_left_12942400) || (__arm64_float_flags_right_12942400 != __arm64_float_flags_right_12942400))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x88UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x8 == 0x0UL))
        {
            label_0xC57C6C:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            x9 = 0x432000UL;
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x9) + (0x3B8UL))))), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((x8) + (0xA4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
            x30 = RuntimeMemory.ReadU64(sp);
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
            return x0;
        }
        return default(ulong);
    }
```

## `TouchTrackPad.OnDestroyControl` — RVA `0xc57c70`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `protected override void OnDestroyControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong TouchTrackPad_OnDestroyControl_RVAc57c70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x298UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A0UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        return default(ulong);
    }
```

## `TouchTrackPad.ResetControl` — RVA `0xc57c80`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public override void ResetControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong TouchTrackPad_ResetControl_RVAc57c80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57CB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC57CB0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPad.OnUpdateControl` — RVA `0xc57cb4`

- Lift status: **exact**; input span: 180 bytes; span to next metadata RVA: 180 bytes.
- Metadata signature: `protected override void OnUpdateControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong TouchTrackPad_OnUpdateControl_RVAc57cb4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12942656 = default(uint);
        uint __arm64_flags_result_12942656 = default(uint);
        uint __arm64_flags_right_12942656 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x295UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC57CE0;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x295UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC57CE0;
        label_0xC57CE0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC57D28;
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
            goto label_0xC57D04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC57D00UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC57D04;
        label_0xC57D04:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC57D28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57D64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BCB8UL /* metadata target: InputRig.WakeTouchControlsUp */, x0, x1, x2, x3);
        goto label_0xC57D28;
        label_0xC57D28:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57D64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        __arm64_flags_left_12942656 = unchecked((uint)(x8));
        __arm64_flags_right_12942656 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12942656 = unchecked((uint)((__arm64_flags_left_12942656) & (__arm64_flags_right_12942656)));
        if ((__arm64_flags_result_12942656 == unchecked((uint)0x0UL)))
        {
            goto label_0xC57D54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC57D54:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC57D68UL /* metadata target: TouchTrackPad.SyncRigState */);
        label_0xC57D64:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchTrackPad.SyncRigState` — RVA `0xc57d68`

- Lift status: **exact**; input span: 212 bytes; span to next metadata RVA: 212 bytes.
- Metadata signature: `private void SyncRigState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=30 (informational only).

```csharp
public static ulong TouchTrackPad_SyncRigState_RVAc57d68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12942896 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC57E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x1CUL))))))));
        x19 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC57DEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC57B5CUL /* metadata target: TouchTrackPad.IsTouchPressureSensitive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC57DCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC57B8CUL /* metadata target: TouchTrackPad.GetTouchPressure */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC57E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        goto label_0xC57DE8;
        label_0xC57DCC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xA8UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC57DEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC57DE8;
        label_0xC57DE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC57DEC;
        label_0xC57DEC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61C94UL /* metadata target: TouchGestureBasicState.GetDeltaVecSmooth */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        v8 = v1;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57E38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        v0 = v8;
        __arm64_load_address_12942896 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12942896)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12942896) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */);
        label_0xC57E38:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchTrackPad.OnIsBoundToAxis` — RVA `0xc57e3c`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static uint TouchTrackPad_OnIsBoundToAxis_RVAc57e3c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57ECC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x3 = 0x0UL;
        x19 = x2;
        x20 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC57E9C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57ECC;
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
            goto label_0xC57E9C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57ECC;
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
            goto label_0xC57EAC;
        }
        else
        {
            goto label_0xC57E9C;
        }
        label_0xC57E9C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC57EAC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57ECC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5DE34UL /* metadata target: InputBindingBase.IsBoundToAxis */)));
        label_0xC57ECC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `TouchTrackPad.OnIsBoundToKey` — RVA `0xc57ed0`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static uint TouchTrackPad_OnIsBoundToKey_RVAc57ed0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57F60;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x3 = 0x0UL;
        x19 = x2;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x0 = RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC57F30;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57F60;
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
            goto label_0xC57F30;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x98UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57F60;
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
            goto label_0xC57F40;
        }
        else
        {
            goto label_0xC57F30;
        }
        label_0xC57F30:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC57F40:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC57F60;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5DE28UL /* metadata target: InputBindingBase.IsBoundToKey */)));
        label_0xC57F60:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `TouchTrackPad.OnGetSubBindingDescriptions` — RVA `0xc57f64`

- Lift status: **exact**; input span: 276 bytes; span to next metadata RVA: 276 bytes.
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=53 (informational only).

```csharp
public static ulong TouchTrackPad_OnGetSubBindingDescriptions_RVAc57f64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x296UL))))))));
        x19 = x3;
        x20 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC57FC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x296UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC57FC4;
        label_0xC57FC4:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC58074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD08UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x90UL))));
        x22 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x2 = RuntimeMemory.ReadU64(x8);
        x24 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xEB0UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xEA8UL))));
        x0 = x20;
        x3 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xB0UL))));
        x3 = RuntimeMemory.ReadU64(x22);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x98UL))));
        x3 = RuntimeMemory.ReadU64(x23);
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA0UL))));
        x3 = RuntimeMemory.ReadU64(x24);
        x0 = x20;
        x4 = x19;
        x5 = x21;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x6 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */);
        label_0xC58074:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `TouchTrackPad.CanBeTouchedDirectly` — RVA `0xc58078`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public override bool CanBeTouchedDirectly(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint TouchTrackPad_CanBeTouchedDirectly_RVAc58078(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12943492 = default(uint);
        ulong __arm64_flags_left_12943512 = default(ulong);
        uint __arm64_flags_result_12943492 = default(uint);
        uint __arm64_flags_right_12943492 = default(uint);
        ulong __arm64_flags_right_12943512 = default(ulong);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x23UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
            __arm64_flags_left_12943492 = unchecked((uint)(x8));
            __arm64_flags_right_12943492 = unchecked((uint)0xFFFFFFBFUL);
            __arm64_flags_result_12943492 = unchecked((uint)((__arm64_flags_left_12943492) & (__arm64_flags_right_12943492)));
            if ((__arm64_flags_result_12943492 == unchecked((uint)0x0UL)))
            {
                label_0xC58094:
                ;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0xB8UL))));
                __arm64_flags_left_12943512 = x8;
                __arm64_flags_right_12943512 = 0x0UL;
                x0 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12943512) - (__arm64_flags_right_12943512))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                return unchecked((uint)(x0));
            }
        }
        label_0xC5808C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchTrackPad.CanBeActivatedByOtherControl` — RVA `0xc580a4`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public override bool CanBeActivatedByOtherControl(TouchControl c, TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchTrackPad_CanBeActivatedByOtherControl_RVAc580a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12943528 = default(uint);
        ulong __arm64_flags_left_12943548 = default(ulong);
        uint __arm64_flags_result_12943528 = default(uint);
        uint __arm64_flags_right_12943528 = default(uint);
        ulong __arm64_flags_right_12943548 = default(ulong);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12943528 = unchecked((uint)(x8));
        __arm64_flags_right_12943528 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12943528 = unchecked((uint)((__arm64_flags_left_12943528) & (__arm64_flags_right_12943528)));
        if ((__arm64_flags_result_12943528 == unchecked((uint)0x0UL)))
        {
            label_0xC580B8:
            ;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0xB8UL))));
            __arm64_flags_left_12943548 = x8;
            __arm64_flags_right_12943548 = 0x0UL;
            x0 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12943548) - (__arm64_flags_right_12943548))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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

## `TouchTrackPad.CanBeSwipedOverFromNothing` — RVA `0xc580c8`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public override bool CanBeSwipedOverFromNothing(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint TouchTrackPad_CanBeSwipedOverFromNothing_RVAc580c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12943572 = default(uint);
        ulong __arm64_flags_left_12943592 = default(ulong);
        uint __arm64_flags_result_12943572 = default(uint);
        uint __arm64_flags_right_12943572 = default(uint);
        ulong __arm64_flags_right_12943592 = default(ulong);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x26UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
            __arm64_flags_left_12943572 = unchecked((uint)(x8));
            __arm64_flags_right_12943572 = unchecked((uint)0xFFFFFFBFUL);
            __arm64_flags_result_12943572 = unchecked((uint)((__arm64_flags_left_12943572) & (__arm64_flags_right_12943572)));
            if ((__arm64_flags_result_12943572 == unchecked((uint)0x0UL)))
            {
                label_0xC580E4:
                ;
                x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0xB8UL))));
                __arm64_flags_left_12943592 = x8;
                __arm64_flags_right_12943592 = 0x0UL;
                x0 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12943592) - (__arm64_flags_right_12943592))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                return unchecked((uint)(x0));
            }
        }
        label_0xC580DC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchTrackPad.CanBeSwipedOverFromRestrictedList` — RVA `0xc580f4`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public override bool CanBeSwipedOverFromRestrictedList(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchTrackPad_CanBeSwipedOverFromRestrictedList_RVAc580f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12943608 = default(uint);
        ulong __arm64_flags_left_12943628 = default(ulong);
        uint __arm64_flags_result_12943608 = default(uint);
        uint __arm64_flags_right_12943608 = default(uint);
        ulong __arm64_flags_right_12943628 = default(ulong);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x50UL))))));
        __arm64_flags_left_12943608 = unchecked((uint)(x8));
        __arm64_flags_right_12943608 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12943608 = unchecked((uint)((__arm64_flags_left_12943608) & (__arm64_flags_right_12943608)));
        if ((__arm64_flags_result_12943608 == unchecked((uint)0x0UL)))
        {
            label_0xC58108:
            ;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0xB8UL))));
            __arm64_flags_left_12943628 = x8;
            __arm64_flags_right_12943628 = 0x0UL;
            x0 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12943628) - (__arm64_flags_right_12943628))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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

## `TouchTrackPad.CanSwipeOverOthers` — RVA `0xc58118`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `public override bool CanSwipeOverOthers(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static uint TouchTrackPad_CanSwipeOverOthers_RVAc58118(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12943644 = default(ulong);
        uint __arm64_flags_left_12943664 = default(uint);
        uint __arm64_flags_left_12943684 = default(uint);
        uint __arm64_flags_left_12943692 = default(uint);
        ulong __arm64_flags_right_12943644 = default(ulong);
        uint __arm64_flags_right_12943664 = default(uint);
        uint __arm64_flags_right_12943684 = default(uint);
        uint __arm64_flags_right_12943692 = default(uint);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        __arm64_flags_left_12943644 = x8;
        __arm64_flags_right_12943644 = x1;
        if ((unchecked((ulong)((__arm64_flags_left_12943644) - (__arm64_flags_right_12943644))) == 0x0UL))
        {
            label_0xC5812C:
            ;
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x28UL))))));
            __arm64_flags_left_12943664 = unchecked((uint)(x8));
            __arm64_flags_right_12943664 = unchecked((uint)0x1UL);
            if ((!((unchecked((uint)((__arm64_flags_left_12943664) - (__arm64_flags_right_12943664))) == unchecked((uint)0x0UL)))))
            {
                label_0xC58140:
                ;
                x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0xC0UL))))));
                __arm64_flags_left_12943684 = unchecked((uint)(x8));
                __arm64_flags_right_12943684 = unchecked((uint)0x2UL);
                x8 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12943684) - (__arm64_flags_right_12943684))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                __arm64_flags_left_12943692 = unchecked((uint)(x9));
                __arm64_flags_right_12943692 = unchecked((uint)0x2UL);
                x9 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12943692) - (__arm64_flags_right_12943692))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
                x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
                return unchecked((uint)(x0));
            }
            else
            {
                x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                return unchecked((uint)(x0));
            }
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `TouchTrackPad.ReleaseAllTouches` — RVA `0xc5815c`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong TouchTrackPad_ReleaseAllTouches_RVAc5815c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = x0;
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC58198;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4D288UL /* metadata target: TouchObject.ReleaseControl */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0xB8UL))), 0x0UL);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC58198:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `TouchTrackPad.OnTouchStart` — RVA `0xc581a4`

- Lift status: **partial**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public override bool OnTouchStart(TouchObject touchObj, TouchControl sender, TouchControl.TouchStartType touchStartType) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=15 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cset' at 0xc5821c; reason: Unknown IR expression at 0xc5821c

```csharp
public static uint TouchTrackPad_OnTouchStart_RVAc581a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12943888 = default(ulong);
        ulong __arm64_flags_right_12943888 = default(ulong);
        ulong __arm64_pair_address_12943844 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x20 = x0;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        if ((x22 != 0x0UL))
        {
            goto label_0xC58210;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)(x3))));
        x19 = x1;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0xB8UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB8UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0xC0UL))), unchecked((uint)(x21)));
        if ((x0 == 0x0UL))
        {
            goto label_0xC58228;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC4D6E4UL /* metadata target: TouchObject.AddControl */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xC58228;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC581E4UL)));
        }
        __arm64_pair_address_12943844 = unchecked((ulong)((x19) + (0x28UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12943844)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12943844) + (0x4UL))))), 0));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC51588UL /* metadata target: TouchControl.ScreenToOrientedPos */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC58228;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC581F8UL)));
        }
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v2 = v0;
        v3 = v1;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61F0CUL /* metadata target: TouchGestureBasicState.OnTouchStart */, x0, x1, x2, x3);
        goto label_0xC58210;
        label_0xC58210:
        ;
        __arm64_flags_left_12943888 = x22;
        __arm64_flags_right_12943888 = 0x0UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        RuntimeCalls.Unsupported("cset", 0xC5821CUL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC58228:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `TouchTrackPad.OnTouchEnd` — RVA `0xc5822c`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public override bool OnTouchEnd(TouchObject touchObj, TouchControl.TouchEndType touchEndType) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static uint TouchTrackPad_OnTouchEnd_RVAc5822c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12943932 = default(ulong);
        ulong __arm64_flags_left_12943940 = default(ulong);
        uint __arm64_flags_left_12943952 = default(uint);
        uint __arm64_flags_left_12943984 = default(uint);
        ulong __arm64_flags_right_12943932 = default(ulong);
        ulong __arm64_flags_right_12943940 = default(ulong);
        uint __arm64_flags_right_12943952 = default(uint);
        uint __arm64_flags_right_12943984 = default(uint);
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
        x20 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        __arm64_flags_left_12943932 = x8;
        __arm64_flags_right_12943932 = 0x0UL;
        x9 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12943932) - (__arm64_flags_right_12943932))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12943940 = x8;
        __arm64_flags_right_12943940 = x1;
        x8 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12943940) - (__arm64_flags_right_12943940))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x19 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
        __arm64_flags_left_12943952 = unchecked((uint)(x19));
        __arm64_flags_right_12943952 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12943952) - (__arm64_flags_right_12943952))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC58280;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)(x2))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0xB8UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC58290;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC58270UL)));
        }
        __arm64_flags_left_12943984 = unchecked((uint)(x21));
        __arm64_flags_right_12943984 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12943984) - (__arm64_flags_right_12943984))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC62008UL /* metadata target: TouchGestureBasicState.OnTouchEnd */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC58280;
        label_0xC58280:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x19))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC58290:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `TouchTrackPad.OnTouchMove` — RVA `0xc58294`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public override bool OnTouchMove(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static uint TouchTrackPad_OnTouchMove_RVAc58294(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12944032 = default(ulong);
        ulong __arm64_flags_left_12944040 = default(ulong);
        uint __arm64_flags_left_12944052 = default(uint);
        ulong __arm64_flags_right_12944032 = default(ulong);
        ulong __arm64_flags_right_12944040 = default(ulong);
        uint __arm64_flags_right_12944052 = default(uint);
        ulong __arm64_pair_address_12944068 = default(ulong);
        ulong __arm64_pair_address_12944088 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
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
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        __arm64_flags_left_12944032 = x8;
        __arm64_flags_right_12944032 = 0x0UL;
        x9 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12944032) - (__arm64_flags_right_12944032))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12944040 = x8;
        __arm64_flags_right_12944040 = x1;
        x8 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12944040) - (__arm64_flags_right_12944040))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
        __arm64_flags_left_12944052 = unchecked((uint)(x20));
        __arm64_flags_right_12944052 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12944052) - (__arm64_flags_right_12944052))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC582EC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = x1;
        if ((x1 == 0x0UL))
        {
            goto label_0xC582FC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC582C4UL)));
        }
        __arm64_pair_address_12944068 = unchecked((ulong)((x19) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12944068)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12944068) + (0x4UL))))), 0));
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC51588UL /* metadata target: TouchControl.ScreenToOrientedPos */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xC8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC582FC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC582D8UL)));
        }
        __arm64_pair_address_12944088 = unchecked((ulong)((x8) + (0xB0UL)));
        RuntimeMemory.WriteF32(__arm64_pair_address_12944088, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((__arm64_pair_address_12944088) + (0x4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0));
        x2 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0xC0UL))))));
        x0 = x21;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC4F6E0UL /* metadata target: TouchControl.CheckSwipeOff */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC582EC;
        label_0xC582EC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC582FC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `TouchTrackPad.OnTouchPressureChange` — RVA `0xc58300`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public override bool OnTouchPressureChange(TouchObject touchObj) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static uint TouchTrackPad_OnTouchPressureChange_RVAc58300(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12944136 = default(ulong);
        ulong __arm64_flags_left_12944144 = default(ulong);
        uint __arm64_flags_left_12944156 = default(uint);
        ulong __arm64_flags_right_12944136 = default(ulong);
        ulong __arm64_flags_right_12944144 = default(ulong);
        uint __arm64_flags_right_12944156 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        __arm64_flags_left_12944136 = x8;
        __arm64_flags_right_12944136 = 0x0UL;
        x9 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12944136) - (__arm64_flags_right_12944136))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12944144 = x8;
        __arm64_flags_right_12944144 = x1;
        x8 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12944144) - (__arm64_flags_right_12944144))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x19 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)(x8)))))));
        __arm64_flags_left_12944156 = unchecked((uint)(x19));
        __arm64_flags_right_12944156 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12944156) - (__arm64_flags_right_12944156))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC5833C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC58324UL)));
        }
        if ((x1 == 0x0UL))
        {
            goto label_0xC58348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC58348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC58330UL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x1) + (0x14UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61FA8UL /* metadata target: TouchGestureBasicState.OnTouchPressureChange */, x0, x1, x2, x3);
        goto label_0xC5833C;
        label_0xC5833C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x19))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC58348:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```
