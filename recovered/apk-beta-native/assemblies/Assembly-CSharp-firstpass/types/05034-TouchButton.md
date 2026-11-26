# `TouchButton` — TypeDefIndex 5034

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x174` | `bool` | `toggle` |
| `0x178` | `TouchButton.ToggleOnAction` | `toggleOnAction` |
| `0x17C` | `TouchButton.ToggleOffAction` | `toggleOffAction` |
| `0x180` | `bool` | `toggleOffWhenHiding` |
| `0x181` | `bool` | `autoToggleOff` |
| `0x184` | `float` | `autoToggleOffTimeOut` |
| `0x188` | `bool` | `linkToggleToRigSwitch` |
| `0x190` | `string` | `toggleRigSwitchName` |
| `0x198` | `int` | `toggleRigSwitchId` |
| `0x1A0` | `DigitalBinding` | `pressBinding` |
| `0x1A8` | `DigitalBinding` | `toggleOnlyBinding` |
| `0x1B0` | `bool` | `emulateTouchPressure` |
| `0x1B8` | `AxisBinding` | `touchPressureBinding` |
| `0x1C0` | `bool` | `toggledCur` |
| `0x1C1` | `bool` | `toggledPrev` |
| `0x1C2` | `bool` | `curTouchToggledOn` |
| `0x1C4` | `float` | `elapsedSinceToggled` |

## `TouchButton.ctor` — RVA `0xc4e98c`

- Lift status: **exact**; input span: 284 bytes; span to next metadata RVA: 284 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=41 (informational only).

```csharp
public static ulong TouchButton_ctor_RVAc4e98c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x22 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x247UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x988UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x990UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x990UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x247UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC4E9D8:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC475DCUL /* metadata target: DynamicTouchControl.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5D544UL /* metadata target: InputBindingBase.ctor */, x0, x1, x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5BE6CUL /* metadata target: DigitalBinding.BasicConstructor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x1A0UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x1A0UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5D544UL /* metadata target: InputBindingBase.ctor */, x0, x1, x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5BE6CUL /* metadata target: DigitalBinding.BasicConstructor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x1A8UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x1A8UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x22 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1B0UL))), unchecked((byte)(unchecked((uint)(x22)))));
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x2 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC5D544UL /* metadata target: InputBindingBase.ctor */, x0, x1, x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC5B3B8UL /* metadata target: AxisBinding.BasicConstructor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x1B8UL)));
        x1 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x1B8UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xB88UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x9EUL))), unchecked((byte)(unchecked((uint)(x22)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x181UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x178UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x184UL))), unchecked((uint)(x8)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `TouchButton.Toggled` — RVA `0xc4eae0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool Toggled() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint TouchButton_Toggled_RVAc4eae0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1C0UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchButton.JustToggled` — RVA `0xc4eae8`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool JustToggled() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchButton_JustToggled_RVAc4eae8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12905204 = default(uint);
        uint __arm64_flags_right_12905204 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1C0UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC4EB00:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1C1UL))))))));
            __arm64_flags_left_12905204 = unchecked((uint)(x8));
            __arm64_flags_right_12905204 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12905204) - (__arm64_flags_right_12905204))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `TouchButton.JustUntoggled` — RVA `0xc4eb08`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool JustUntoggled() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint TouchButton_JustUntoggled_RVAc4eb08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12905244 = default(uint);
        uint __arm64_flags_right_12905244 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x1C0UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC4EB18:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x1C1UL))))))));
            __arm64_flags_left_12905244 = unchecked((uint)(x8));
            __arm64_flags_right_12905244 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12905244) - (__arm64_flags_right_12905244))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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

## `TouchButton.PressedOrToggled` — RVA `0xc4eb28`

- Lift status: **exact**; input span: 48 bytes; span to next metadata RVA: 48 bytes.
- Metadata signature: `public bool PressedOrToggled() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint TouchButton_PressedOrToggled_RVAc4eb28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12905288 = default(uint);
        uint __arm64_flags_right_12905288 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC44B14UL /* metadata target: DynamicTouchControl.Pressed */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            label_0xC4EB44:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C0UL))))))));
            __arm64_flags_left_12905288 = unchecked((uint)(x8));
            __arm64_flags_right_12905288 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12905288) - (__arm64_flags_right_12905288))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        else
        {
            x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        }
        label_0xC4EB50:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `TouchButton.OnInitControl` — RVA `0xc4eb58`

- Lift status: **exact**; input span: 224 bytes; span to next metadata RVA: 224 bytes.
- Metadata signature: `protected override void OnInitControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong TouchButton_OnInitControl_RVAc4eb58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x248UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EB84;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x248UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4EB84;
        label_0xC4EB84:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC47718UL /* metadata target: DynamicTouchControl.OnInitControl */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x174UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EC18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x188UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EC18;
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
            goto label_0xC4EBBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4EBB8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4EBBC;
        label_0xC4EBBC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EC18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4EC34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        x2 = unchecked((ulong)((x19) + (0x198UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3C280UL /* metadata target: InputRig.GetSwitchState */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x249UL))))))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EC10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x249UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4EC10;
        label_0xC4EC10:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1C0UL))), unchecked((byte)(unchecked((uint)(x20)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x1C4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC4EC18;
        label_0xC4EC18:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x298UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC4EC34:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchButton.ChangeToggleState` — RVA `0xc4ec38`

- Lift status: **exact**; input span: 196 bytes; span to next metadata RVA: 196 bytes.
- Metadata signature: `private void ChangeToggleState(bool toggleState, bool syncRigSwitch) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=30 (informational only).

```csharp
public static ulong TouchButton_ChangeToggleState_RVAc4ec38(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x249UL))))))));
        x21 = unchecked((ulong)(unchecked((uint)(x2))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EC74;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x249UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4EC74;
        label_0xC4EC74:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1C0UL))), unchecked((byte)(unchecked((uint)(x22)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x1C4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ECE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x188UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ECE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x58UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4ECA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4ECA0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC4ECA4;
        label_0xC4ECA4:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ECE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4ECF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4ECF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x190UL))));
        x2 = unchecked((ulong)((x20) + (0x198UL)));
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)(0x1UL)))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x4 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC3F140UL /* metadata target: InputRig.RigSwitchCollection.SetSwitchState */);
        label_0xC4ECE8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC4ECF8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchButton.ResetControl` — RVA `0xc4ecfc`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public override void ResetControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong TouchButton_ResetControl_RVAc4ecfc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC47B38UL /* metadata target: DynamicTouchControl.ResetControl */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4ED60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4ED60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4ED60;
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
        label_0xC4ED60:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchButton.OnUpdateControl` — RVA `0xc4ed64`

- Lift status: **exact**; input span: 460 bytes; span to next metadata RVA: 460 bytes.
- Metadata signature: `protected override void OnUpdateControl() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=47 (informational only).

```csharp
public static ulong TouchButton_OnUpdateControl_RVAc4ed64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12905892 = default(uint);
        uint __arm64_flags_left_12906012 = default(uint);
        uint __arm64_flags_left_12906160 = default(uint);
        uint __arm64_flags_left_12906240 = default(uint);
        uint __arm64_flags_result_12906240 = default(uint);
        uint __arm64_flags_right_12905892 = default(uint);
        uint __arm64_flags_right_12906012 = default(uint);
        uint __arm64_flags_right_12906160 = default(uint);
        uint __arm64_flags_right_12906240 = default(uint);
        float __arm64_float_flags_left_12906212 = default(float);
        float __arm64_float_flags_right_12906212 = default(float);
        ulong __arm64_load_address_12906256 = default(ulong);
        ulong __arm64_load_address_12906276 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC482A8UL /* metadata target: DynamicTouchControl.OnUpdateControl */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C0UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x174UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1C1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4ED98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4ED8CUL);
        }
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EDA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x17CUL))))));
        goto label_0xC4EDA4;
        label_0xC4ED98:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1C0UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC4EEFC;
        label_0xC4EDA0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x178UL))))));
        goto label_0xC4EDA4;
        label_0xC4EDA4:
        ;
        __arm64_flags_left_12905892 = unchecked((uint)(x8));
        __arm64_flags_right_12905892 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12905892) - (__arm64_flags_right_12905892))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EDD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4EDACUL);
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EDF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4EF2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61BF0UL /* metadata target: TouchGestureBasicState.JustPressedRaw */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EDF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1C2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4EDFC;
        label_0xC4EDD0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C2UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EDF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4EF2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61C10UL /* metadata target: TouchGestureBasicState.JustReleasedRaw */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EDF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1C2UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        goto label_0xC4EDFC;
        label_0xC4EDF8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4EDFC;
        label_0xC4EDFC:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE0UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC4EF2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x1CUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EE2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4EE0CUL);
        }
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EE34;
        }
        else
        {
            goto label_0xC4EE10;
        }
        label_0xC4EE10:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C0UL))))))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        __arm64_flags_left_12906012 = unchecked((uint)(x8));
        __arm64_flags_right_12906012 = unchecked((uint)0x0UL);
        x1 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12906012) - (__arm64_flags_right_12906012))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC4EC38UL /* metadata target: TouchButton.ChangeToggleState */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC4EE9C;
        label_0xC4EE2C:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1C2UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EE10;
        }
        else
        {
            goto label_0xC4EE34;
        }
        label_0xC4EE34:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x174UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EE9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x188UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EE9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC4EF2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4EF2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C0UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x190UL))));
        x2 = unchecked((ulong)((x19) + (0x198UL)));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3F1F4UL /* metadata target: InputRig.RigSwitchCollection.GetSwitchState */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x249UL))))))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EE8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x249UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4EE8C;
        label_0xC4EE8C:
        ;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x1C0UL))), unchecked((byte)(unchecked((uint)(x20)))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x1C4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)(x20)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EEA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4EE98UL);
        }
        goto label_0xC4EEFC;
        label_0xC4EE9C:
        ;
        x20 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C0UL))))))));
        if ((unchecked((uint)(x20)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EEFC;
        }
        else
        {
            goto label_0xC4EEA4;
        }
        label_0xC4EEA4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x181UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EEB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x17CUL))))));
        __arm64_flags_left_12906160 = unchecked((uint)(x8));
        __arm64_flags_right_12906160 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12906160) - (__arm64_flags_right_12906160))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC4EEFC;
        }
        else
        {
            goto label_0xC4EEB8;
        }
        label_0xC4EEB8:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC44B14UL /* metadata target: DynamicTouchControl.Pressed */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EED0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC4EEC8UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x1C4UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC4EEFC;
        label_0xC4EED0:
        ;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x1C4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC4E208UL /* metadata target: CFUtils.get_realDeltaTime */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x184UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x1C4UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        __arm64_float_flags_left_12906212 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12906212 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12906212 <= __arm64_float_flags_right_12906212) || ((__arm64_float_flags_left_12906212 != __arm64_float_flags_left_12906212) || (__arm64_float_flags_right_12906212 != __arm64_float_flags_right_12906212))))
        {
            goto label_0xC4EEFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4EC38UL /* metadata target: TouchButton.ChangeToggleState */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4EEFC;
        label_0xC4EEFC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x50UL))))));
        __arm64_flags_left_12906240 = unchecked((uint)(x8));
        __arm64_flags_right_12906240 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12906240 = unchecked((uint)((__arm64_flags_left_12906240) & (__arm64_flags_right_12906240)));
        if ((__arm64_flags_result_12906240 == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EF18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12906256 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12906256)), 0));
        return x0;
        label_0xC4EF18:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12906276 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12906276)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12906276) + (0x30UL)));
        return RuntimeCalls.InvokeDirect(0xC4EF40UL /* metadata target: TouchButton.SyncRigState */);
        label_0xC4EF2C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchButton.SyncRigState` — RVA `0xc4ef40`

- Lift status: **exact**; input span: 204 bytes; span to next metadata RVA: 204 bytes.
- Metadata signature: `private void SyncRigState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=29 (informational only).

```csharp
public static ulong TouchButton_SyncRigState_RVAc4ef40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC44B14UL /* metadata target: DynamicTouchControl.Pressed */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4EF60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C0UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EF78;
        }
        else
        {
            goto label_0xC4EF60;
        }
        label_0xC4EF60:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F008;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC4EF78;
        label_0xC4EF78:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F008;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1C0UL))))))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC44B14UL /* metadata target: DynamicTouchControl.Pressed */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC47CB0UL /* metadata target: DynamicTouchControl.IsTouchPressureSensitive */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EFD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1B8UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC47CE0UL /* metadata target: DynamicTouchControl.GetTouchPressure */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC4F008;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        goto label_0xC4EFF0;
        label_0xC4EFD4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x1B0UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4EFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x1B8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F008;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC4EFF0;
        label_0xC4EFF0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */);
        label_0xC4EFFC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4F008:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchButton.OnGetSubBindingDescriptions` — RVA `0xc4f250`

- Lift status: **exact**; input span: 244 bytes; span to next metadata RVA: 244 bytes.
- Metadata signature: `protected override void OnGetSubBindingDescriptions(BindingDescriptionList descList, Object undoObject, string parentMenuPath) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=45 (informational only).

```csharp
public static ulong TouchButton_OnGetSubBindingDescriptions_RVAc4f250(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x24AUL))))))));
        x19 = x3;
        x21 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x24AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC4F2A0;
        label_0xC4F2A0:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC4F340;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD08UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x1A0UL))));
        x22 = 0x1A8C000UL;
        x0 = x21;
        x2 = RuntimeMemory.ReadU64(x8);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD10UL))));
        x3 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x1B8UL))));
        x3 = RuntimeMemory.ReadU64(x22);
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x21;
        x6 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5DAACUL /* metadata target: BindingDescriptionList.Add */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x174UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC4F300;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2CUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC4F330;
        }
        else
        {
            goto label_0xC4F300;
        }
        label_0xC4F300:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD18UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x1A8UL))));
        x0 = x21;
        x3 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x4 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x5 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5D750UL /* metadata target: BindingDescriptionList.Add */);
        label_0xC4F330:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC4F340:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchButton.OnIsBoundToAxis` — RVA `0xc4f344`

- Lift status: **exact**; input span: 120 bytes; span to next metadata RVA: 120 bytes.
- Metadata signature: `protected override bool OnIsBoundToAxis(string axisName, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static uint TouchButton_OnIsBoundToAxis_RVAc4f344(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F3B8;
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
            goto label_0xC4F388;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x1B8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F3B8;
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
            goto label_0xC4F398;
        }
        else
        {
            goto label_0xC4F388;
        }
        label_0xC4F388:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4F398:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F3B8;
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
        label_0xC4F3B8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `TouchButton.OnIsBoundToKey` — RVA `0xc4f3bc`

- Lift status: **exact**; input span: 120 bytes; span to next metadata RVA: 120 bytes.
- Metadata signature: `protected override bool OnIsBoundToKey(KeyCode key, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=18 (informational only).

```csharp
public static uint TouchButton_OnIsBoundToKey_RVAc4f3bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1A0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F430;
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
            goto label_0xC4F400;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x1B8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F430;
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
            goto label_0xC4F410;
        }
        else
        {
            goto label_0xC4F400;
        }
        label_0xC4F400:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC4F410:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x1A8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC4F430;
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
        label_0xC4F430:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `TouchButton.ReleaseAllTouches` — RVA `0xc4f434`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public override void ReleaseAllTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong TouchButton_ReleaseAllTouches_RVAc4f434(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC48CB4UL /* metadata target: DynamicTouchControl.ReleaseAllTouches */, x0, x1, x2, x3);
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x180UL))))))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4EC38UL /* metadata target: TouchButton.ChangeToggleState */);
        return default(ulong);
    }
```
