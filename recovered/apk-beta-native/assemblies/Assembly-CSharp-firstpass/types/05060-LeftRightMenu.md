# `LeftRightMenu` — TypeDefIndex 5060

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x100` | `Button` | `buttonLeft` |
| `0x108` | `Button` | `buttonRight` |
| `0x110` | `Button` | `buttonBack` |
| `0x118` | `RectTransform` | `contentPlaceholder` |
| `0x120` | `Text` | `titleText` |
| `0x128` | `Action` | `onBackPressed` |
| `0x130` | `LeftRightMenu.OptionSwitchCallback` | `onOptionSwitch` |
| `0x138` | `RectTransform[]` | `optionItems` |

## `LeftRightMenu.OnSelect` — RVA `0xc5a654`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override void OnSelect(BaseEventData data) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong LeftRightMenu_OnSelect_RVAc5a654(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x2 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x198E078UL /* metadata target: Selectable.OnSelect */);
        return default(ulong);
    }
```

## `LeftRightMenu.OnDeselect` — RVA `0xc5a65c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public override void OnDeselect(BaseEventData data) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong LeftRightMenu_OnDeselect_RVAc5a65c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x2 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x198E084UL /* metadata target: Selectable.OnDeselect */);
        return default(ulong);
    }
```

## `LeftRightMenu.OnMove` — RVA `0xc5a664`

- Lift status: **partial**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public override void OnMove(AxisEventData data) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=15 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cneg' at 0xc5a688; reason: Unknown IR expression at 0xc5a688

```csharp
public static ulong LeftRightMenu_OnMove_RVAc5a664(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12953208 = default(uint);
        uint __arm64_flags_left_12953216 = default(uint);
        uint __arm64_flags_right_12953208 = default(uint);
        uint __arm64_flags_right_12953216 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC5A6CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x1) + (0x28UL))))));
        x19 = x1;
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) | (unchecked((uint)(0x2UL)))))));
        __arm64_flags_left_12953208 = unchecked((uint)(x9));
        __arm64_flags_right_12953208 = unchecked((uint)0x2UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12953208) - (__arm64_flags_right_12953208))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC5A6BC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A680UL);
        }
        __arm64_flags_left_12953216 = unchecked((uint)(x8));
        __arm64_flags_right_12953216 = unchecked((uint)0x0UL);
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeCalls.Unsupported("cneg", 0xC5A688UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)((-(unchecked((uint)(x8)))))) : unchecked((uint)(x8)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A6CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5A6A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5A6A8;
        label_0xC5A6A8:
        ;
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC5A6BC:
        ;
        x1 = x19;
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x19885A4UL /* metadata target: Selectable.OnMove */);
        label_0xC5A6CC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `LeftRightMenu.OnSwitch` — RVA `0xc5a6d0`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `private void OnSwitch(int dir) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong LeftRightMenu_OnSwitch_RVAc5a6d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5A6E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC5A6E8:
        ;
        return x0;
        return default(ulong);
    }
```

## `LeftRightMenu.GetItemCount` — RVA `0xc5a6ec`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public int GetItemCount() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint LeftRightMenu_GetItemCount_RVAc5a6ec(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x138UL))));
        if ((x8 == 0x0UL))
        {
            label_0xC5A704:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `LeftRightMenu.SetItemActive` — RVA `0xc5a708`

- Lift status: **partial**; input span: 212 bytes; span to next metadata RVA: 212 bytes.
- Metadata signature: `public void SetItemActive(int id) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=28 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc5a758; reason: Unsupported instruction 'b.ge' at 0xc5a75c; reason: Unknown IR expression at 0xc5a75c

```csharp
public static ulong LeftRightMenu_SetItemActive_RVAc5a708(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12953440 = default(ulong);
        ulong __arm64_flags_left_12953512 = default(ulong);
        ulong __arm64_flags_right_12953440 = default(ulong);
        ulong __arm64_flags_right_12953512 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x2A0UL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A73C;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x2A0UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5A73C;
        label_0xC5A73C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5A7C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x21 = 0x0UL;
        x23 = unchecked((ulong)(unchecked((uint)(x20))));
        goto label_0xC5A754;
        label_0xC5A754:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        RuntimeCalls.Unsupported("cmp", 0xC5A758UL);
        RuntimeCalls.Unsupported("b.ge", 0xC5A75CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC5A7C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A760UL);
        }
        __arm64_flags_left_12953440 = x21;
        __arm64_flags_right_12953440 = x9;
        if ((__arm64_flags_left_12953440 >= __arm64_flags_right_12953440))
        {
            goto label_0xC5A7D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A780;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A77CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5A780;
        label_0xC5A780:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A7B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A794UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC5A7C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A7C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A7A8UL);
        }
        __arm64_flags_left_12953512 = x23;
        __arm64_flags_right_12953512 = x21;
        x1 = unchecked((ulong)(((unchecked((ulong)((__arm64_flags_left_12953512) - (__arm64_flags_right_12953512))) == 0x0UL) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5A7B8;
        label_0xC5A7B8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC5A754;
        }
        else
        {
            goto label_0xC5A7C4;
        }
        label_0xC5A7C4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5A7C8;
        label_0xC5A7C8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC5A7D8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `LeftRightMenu.SetTitle` — RVA `0xc5a7dc`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `public void SetTitle(string title) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong LeftRightMenu_SetTitle_RVAc5a7dc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x2A1UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A818;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x2A1UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5A818;
        label_0xC5A818:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x120UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A82C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A828UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5A82C;
        label_0xC5A82C:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5A868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5A878;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC5A868:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC5A878:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `LeftRightMenu.OnEnable` — RVA `0xc5a87c`

- Lift status: **partial**; input span: 492 bytes; span to next metadata RVA: 492 bytes.
- Metadata signature: `protected override void OnEnable() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=79 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc5a9d4; reason: Unsupported instruction 'b.ge' at 0xc5a9d8; reason: Unknown IR expression at 0xc5a9d8

```csharp
public static ulong LeftRightMenu_OnEnable_RVAc5a87c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12954076 = default(ulong);
        ulong __arm64_flags_right_12954076 = default(ulong);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2A2UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A8DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2A2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5A8DC;
        label_0xC5A8DC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1987698UL /* metadata target: Selectable.OnEnable */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x100UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF00UL))));
        x21 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x100UL))));
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xEF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = x19;
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17A27A0UL /* metadata target: UnityAction.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A2870UL /* metadata target: UnityEvent.AddListener */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x100UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xEF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = x19;
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17A27A0UL /* metadata target: UnityAction.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A2870UL /* metadata target: UnityEvent.AddListener */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x100UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xEE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = x19;
        x3 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17A27A0UL /* metadata target: UnityAction.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = x21;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A2870UL /* metadata target: UnityEvent.AddListener */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x21 = 0x0UL;
        goto label_0xC5A9D0;
        label_0xC5A9D0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        RuntimeCalls.Unsupported("cmp", 0xC5A9D4UL);
        RuntimeCalls.Unsupported("b.ge", 0xC5A9D8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC5AA54;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A9DCUL);
        }
        __arm64_flags_left_12954076 = x21;
        __arm64_flags_right_12954076 = x9;
        if ((__arm64_flags_left_12954076 >= __arm64_flags_right_12954076))
        {
            goto label_0xC5AA64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5A9FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5A9F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5A9FC;
        label_0xC5A9FC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5AA44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5AA10UL);
        }
        if ((x20 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        x0 = x20;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179DE4CUL /* metadata target: Transform.SetParent */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC5AA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5AA44;
        label_0xC5AA44:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x138UL))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC5A9D0;
        }
        else
        {
            goto label_0xC5AA50;
        }
        label_0xC5AA50:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5AA54;
        label_0xC5AA54:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC5AA64:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `LeftRightMenu.OnDisable` — RVA `0xc5aa68`

- Lift status: **exact**; input span: 100 bytes; span to next metadata RVA: 100 bytes.
- Metadata signature: `protected override void OnDisable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong LeftRightMenu_OnDisable_RVAc5aa68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x100UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5AAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A26E4UL /* metadata target: UnityEventBase.RemoveAllListeners */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x108UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5AAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A26E4UL /* metadata target: UnityEventBase.RemoveAllListeners */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x100UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5AAC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17A26E4UL /* metadata target: UnityEventBase.RemoveAllListeners */, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1987988UL /* metadata target: Selectable.OnDisable */);
        label_0xC5AAC8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `LeftRightMenu.OnBackPressed` — RVA `0xc5aacc`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `private void OnBackPressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong LeftRightMenu_OnBackPressed_RVAc5aacc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x128UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AAE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC5AAE4:
        ;
        return x0;
        return default(ulong);
    }
```

## `LeftRightMenu.OnLeftPressed` — RVA `0xc5aae8`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `private void OnLeftPressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong LeftRightMenu_OnLeftPressed_RVAc5aae8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AB04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC5AB04:
        ;
        return x0;
        return default(ulong);
    }
```

## `LeftRightMenu.OnRightPressed` — RVA `0xc5ab08`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `private void OnRightPressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong LeftRightMenu_OnRightPressed_RVAc5ab08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC5AB24;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC5AB24:
        ;
        return x0;
        return default(ulong);
    }
```

## `LeftRightMenu.ctor` — RVA `0xc5ab28`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong LeftRightMenu_ctor_RVAc5ab28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x2A3UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF08UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5AB5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF08UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x2A3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5AB5C;
        label_0xC5AB5C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5AB6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5AB68UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5AB6C;
        label_0xC5AB6C:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1987234UL /* metadata target: Selectable.ctor */);
        return default(ulong);
    }
```
