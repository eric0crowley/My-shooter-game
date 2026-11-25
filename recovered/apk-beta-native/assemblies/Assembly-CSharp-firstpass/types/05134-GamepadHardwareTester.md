# `GamepadHardwareTester` — TypeDefIndex 5134

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `GUISkin` | `skin` |

## `GamepadHardwareTester.GetJoyAxisName` — RVA `0xc699c0`

- Lift status: **exact**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public static string GetJoyAxisName(int joyId, int axisId) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong GamepadHardwareTester_GetJoyAxisName_RVAc699c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), unchecked((uint)(x1)));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x4UL))), unchecked((uint)(x0)));
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x323UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x50UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x323UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC699F4:
        ;
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x19 = x0;
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x2 = x0;
        x1 = x19;
        x3 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadHardwareTester.GetJoyKeyCode` — RVA `0xc69a34`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public static KeyCode GetJoyKeyCode(int joyId, int keyId) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint GamepadHardwareTester_GetJoyKeyCode_RVAc69a34(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13015604 = default(uint);
        uint __arm64_flags_left_13015628 = default(uint);
        uint __arm64_flags_right_13015604 = default(uint);
        uint __arm64_flags_right_13015628 = default(uint);
        ulong x8 = default(ulong);
        __arm64_flags_left_13015604 = unchecked((uint)(x0));
        __arm64_flags_right_13015604 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_13015604 >= __arm64_flags_right_13015604) && (!((unchecked((uint)((__arm64_flags_left_13015604) - (__arm64_flags_right_13015604))) == unchecked((uint)0x0UL))))))
        {
        }
        else
        {
            if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x8 = unchecked((ulong)(unchecked((uint)(0x14UL))));
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x0))) * (unchecked((uint)(x8)))))) + (unchecked((uint)(x1)))))));
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x15EUL)))))));
                __arm64_flags_left_13015628 = unchecked((uint)(x1));
                __arm64_flags_right_13015628 = unchecked((uint)0x14UL);
                x0 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_13015628) - (__arm64_flags_right_13015628))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13015628)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13015628)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13015628) - (__arm64_flags_right_13015628))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13015628)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)0x0UL))));
                return unchecked((uint)(x0));
            }
        }
        label_0xC69A58:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadHardwareTester.GetAxisCode` — RVA `0xc69a60`

- Lift status: **partial**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `private string GetAxisCode(int axis, bool positiveSide) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=28 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc69adc; reason: Unknown IR expression at 0xc69adc

```csharp
public static ulong GamepadHardwareTester_GetAxisCode_RVAc69a60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13015764 = default(uint);
        uint __arm64_flags_result_13015764 = default(uint);
        uint __arm64_flags_right_13015764 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x40UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x1)));
        x21 = 0x1A8C000UL;
        x20 = 0x1A8D000UL;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x324UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA50UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x2F0UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x2F8UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA50UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x324UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC69AC8:
        ;
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        __arm64_flags_left_13015764 = unchecked((uint)(x19));
        __arm64_flags_right_13015764 = unchecked((uint)0x1UL);
        __arm64_flags_result_13015764 = unchecked((uint)((__arm64_flags_left_13015764) & (__arm64_flags_right_13015764)));
        x8 = RuntimeMemory.ReadU64(x21);
        RuntimeCalls.Unsupported("csel", 0xC69ADCUL);
        x9 = (__Unsupported<bool>("Unknown IR expression") ? x20 : x22);
        x2 = RuntimeMemory.ReadU64(x9);
        x1 = x0;
        x0 = x8;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return x0;
        return default(ulong);
    }
```

## `GamepadHardwareTester.GetAxisName` — RVA `0xc69b08`

- Lift status: **partial**; input span: 192 bytes; span to next metadata RVA: 192 bytes.
- Metadata signature: `private string GetAxisName(int axis, bool positiveSide) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=32 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc69b98; reason: Unknown IR expression at 0xc69b98

```csharp
public static ulong GamepadHardwareTester_GetAxisName_RVAc69b08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13015952 = default(uint);
        uint __arm64_flags_result_13015952 = default(uint);
        uint __arm64_flags_right_13015952 = default(uint);
        ulong sp = default(ulong);
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
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x1)));
        x24 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x22 = 0x1A8D000UL;
        x20 = 0x1A8D000UL;
        x23 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x24) + (0x325UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xEB8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x300UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x2F0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x2F8UL))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xEB8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F0UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x300UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x24) + (0x325UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC69B84:
        ;
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        __arm64_flags_left_13015952 = unchecked((uint)(x19));
        __arm64_flags_right_13015952 = unchecked((uint)0x1UL);
        __arm64_flags_result_13015952 = unchecked((uint)((__arm64_flags_left_13015952) & (__arm64_flags_right_13015952)));
        x8 = RuntimeMemory.ReadU64(x22);
        RuntimeCalls.Unsupported("csel", 0xC69B98UL);
        x9 = (__Unsupported<bool>("Unknown IR expression") ? x20 : x23);
        x2 = RuntimeMemory.ReadU64(x21);
        x3 = RuntimeMemory.ReadU64(x9);
        x1 = x0;
        x0 = x8;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F693CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadHardwareTester.GetAxisState` — RVA `0xc69bc8`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `private float GetAxisState(int axis) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong GamepadHardwareTester_GetAxisState_RVAc69bc8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x1)));
        x19 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x326UL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x308UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x308UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x326UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC69BFC:
        ;
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7130UL /* metadata target: Input.GetAxis */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadHardwareTester.GetKeyCode` — RVA `0xc69c30`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `private string GetKeyCode(int key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static ulong GamepadHardwareTester_GetKeyCode_RVAc69c30(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x1)));
        x19 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x327UL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x310UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x310UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x327UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC69C64:
        ;
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadHardwareTester.GetKeyState` — RVA `0xc69c90`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `private bool GetKeyState(int key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong GamepadHardwareTester_GetKeyState_RVAc69c90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) + (unchecked((uint)(0x15EUL)))))));
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */);
        return default(ulong);
    }
```

## `GamepadHardwareTester.OnGUI` — RVA `0xc69c9c`

- Lift status: **partial**; input span: 2160 bytes; span to next metadata RVA: 2160 bytes.
- Metadata signature: `private void OnGUI() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=326 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'ccmp' at 0xc69fec; reason: Unsupported instruction 'csel' at 0xc69ff4; reason: Unknown IR expression at 0xc69ff4; reason: Unsupported instruction 'b.lt' at 0xc6a038; reason: Unknown IR expression at 0xc6a038; reason: Unsupported instruction 'csel' at 0xc6a064; reason: Unknown IR expression at 0xc6a064; reason: Unsupported instruction 'csel' at 0xc6a16c

```csharp
public static ulong GamepadHardwareTester_OnGUI_RVAc69c9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13016728 = default(uint);
        uint __arm64_flags_left_13016844 = default(uint);
        uint __arm64_flags_left_13016876 = default(uint);
        uint __arm64_flags_left_13016932 = default(uint);
        uint __arm64_flags_left_13016964 = default(uint);
        uint __arm64_flags_left_13017004 = default(uint);
        uint __arm64_flags_left_13017056 = default(uint);
        uint __arm64_flags_left_13017068 = default(uint);
        uint __arm64_flags_left_13017136 = default(uint);
        uint __arm64_flags_left_13017172 = default(uint);
        uint __arm64_flags_left_13017252 = default(uint);
        uint __arm64_flags_left_13017296 = default(uint);
        uint __arm64_flags_left_13017308 = default(uint);
        uint __arm64_flags_left_13017344 = default(uint);
        uint __arm64_flags_left_13017384 = default(uint);
        uint __arm64_flags_left_13017444 = default(uint);
        uint __arm64_flags_left_13017556 = default(uint);
        uint __arm64_flags_result_13017172 = default(uint);
        uint __arm64_flags_right_13016728 = default(uint);
        uint __arm64_flags_right_13016844 = default(uint);
        uint __arm64_flags_right_13016876 = default(uint);
        uint __arm64_flags_right_13016932 = default(uint);
        uint __arm64_flags_right_13016964 = default(uint);
        uint __arm64_flags_right_13017004 = default(uint);
        uint __arm64_flags_right_13017056 = default(uint);
        uint __arm64_flags_right_13017068 = default(uint);
        uint __arm64_flags_right_13017136 = default(uint);
        uint __arm64_flags_right_13017172 = default(uint);
        uint __arm64_flags_right_13017252 = default(uint);
        uint __arm64_flags_right_13017296 = default(uint);
        uint __arm64_flags_right_13017308 = default(uint);
        uint __arm64_flags_right_13017344 = default(uint);
        uint __arm64_flags_right_13017384 = default(uint);
        uint __arm64_flags_right_13017444 = default(uint);
        uint __arm64_flags_right_13017556 = default(uint);
        float __arm64_float_flags_left_13016760 = default(float);
        float __arm64_float_flags_left_13016828 = default(float);
        float __arm64_float_flags_right_13016760 = default(float);
        float __arm64_float_flags_right_13016828 = default(float);
        ulong __arm64_pair_address_13016228 = default(ulong);
        ulong __arm64_pair_address_13016232 = default(ulong);
        ulong __arm64_pair_address_13018352 = default(ulong);
        ulong __arm64_pair_address_13018356 = default(ulong);
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
        sp = unchecked((ulong)((sp) - (0xA0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v12.GetUInt64(0)))));
        __arm64_pair_address_13016228 = unchecked((ulong)((sp) + (0x20UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13016228, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13016228) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        __arm64_pair_address_13016232 = unchecked((ulong)((sp) + (0x30UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13016232, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13016232) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x328UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69DFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x248UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x318UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x320UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x328UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x330UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x338UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x340UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x348UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x350UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x358UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x360UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x368UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x370UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x378UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x380UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x388UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x310UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x390UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x328UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC69DFC;
        label_0xC69DFC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x18UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x29 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0x230UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC69E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC69E24UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC69E28;
        label_0xC69E28:
        ;
        x28 = 0x1A8C000UL;
        x27 = 0x1A8D000UL;
        x24 = 0x1A8D000UL;
        x26 = 0x1A8D000UL;
        x25 = 0x1A8D000UL;
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0x3A0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x368UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x338UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x310UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x318UL))));
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B3680UL /* metadata target: GUI.set_skin */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7518UL /* metadata target: Input.GetJoystickNames */, x0, x1, x2, x3);
        x8 = 0x432000UL;
        x20 = RuntimeMemory.ReadU64(x29);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x458UL))))), 0));
        x9 = x0;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41200000UL)), 0)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40A00000UL)), 0)), 0));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xC0A00000UL)), 0)), 0));
        x19 = unchecked((ulong)(unchecked((uint)(0x14UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU64(sp, x9);
        goto label_0xC69E90;
        label_0xC69E90:
        ;
        if ((x9 == 0x0UL))
        {
            goto label_0xC69FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13016728 = unchecked((uint)(x0));
        __arm64_flags_right_13016728 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13016728) - (__arm64_flags_right_13016728))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13016728)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13016728)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13016728) - (__arm64_flags_right_13016728))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13016728)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC69FC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC69EA4;
        label_0xC69EA4:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC699C0UL /* metadata target: GamepadHardwareTester.GetJoyAxisName */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C71A8UL /* metadata target: Input.GetAxisRaw */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_13016760 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13016760 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        RuntimeMemory.WriteF32(unchecked((ulong)((sp) + (0x18UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((__arm64_float_flags_left_13016760 <= __arm64_float_flags_right_13016760))
        {
            goto label_0xC69FAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x28);
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC6A508;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x22 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((x23) + (0x20UL))), x20);
        x0 = x23;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x18UL))))), 0));
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        __arm64_float_flags_left_13016828 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13016828 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x2 = unchecked((ulong)(((__arm64_float_flags_left_13016828 > __arm64_float_flags_right_13016828) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC69B08UL /* metadata target: GamepadHardwareTester.GetAxisName */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0xFFFFFFFFFFFFFFF8UL))))));
        __arm64_flags_left_13016844 = unchecked((uint)(x8));
        __arm64_flags_right_13016844 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13016844 >= __arm64_flags_right_13016844))) || (unchecked((uint)((__arm64_flags_left_13016844) - (__arm64_flags_right_13016844))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x28UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFF0UL))))));
        __arm64_flags_left_13016876 = unchecked((uint)(x8));
        __arm64_flags_right_13016876 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13016876 >= __arm64_flags_right_13016876))) || (unchecked((uint)((__arm64_flags_left_13016876) - (__arm64_flags_right_13016876))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x398UL))));
        x20 = x22;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x30UL))), x1);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = RuntimeMemory.ReadU64(x27);
        x0 = unchecked((ulong)((sp) + (0x18UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1559570UL /* metadata target: Single.ToString */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFE8UL))))));
        __arm64_flags_left_13016932 = unchecked((uint)(x8));
        __arm64_flags_right_13016932 = unchecked((uint)0x3UL);
        if (((!((__arm64_flags_left_13016932 >= __arm64_flags_right_13016932))) || (unchecked((uint)((__arm64_flags_left_13016932) - (__arm64_flags_right_13016932))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x38UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFE0UL))))));
        __arm64_flags_left_13016964 = unchecked((uint)(x8));
        __arm64_flags_right_13016964 = unchecked((uint)0x4UL);
        if (((!((__arm64_flags_left_13016964 >= __arm64_flags_right_13016964))) || (unchecked((uint)((__arm64_flags_left_13016964) - (__arm64_flags_right_13016964))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6A44UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC69FAC;
        label_0xC69FAC:
        ;
        __arm64_flags_left_13017004 = unchecked((uint)(x21));
        __arm64_flags_right_13017004 = unchecked((uint)0x9UL);
        if ((unchecked((uint)((__arm64_flags_left_13017004) - (__arm64_flags_right_13017004))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC69FD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x1CUL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        goto label_0xC69EA4;
        label_0xC69FC0:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x388UL))));
        x20 = RuntimeMemory.ReadU64(x8);
        goto label_0xC6A150;
        label_0xC69FD0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x21 = x29;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC69FDC;
        label_0xC69FDC:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x1CUL))))));
        __arm64_flags_left_13017056 = unchecked((uint)(x8));
        __arm64_flags_right_13017056 = unchecked((uint)0x1UL);
        x1 = 0x0UL;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x9))) * (unchecked((uint)(x19)))))) + (unchecked((uint)(x8)))))));
        RuntimeCalls.Unsupported("ccmp", 0xC69FECUL);
        __arm64_flags_left_13017068 = unchecked((uint)(x9));
        __arm64_flags_right_13017068 = unchecked((uint)0x4UL);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x15EUL)))))));
        RuntimeCalls.Unsupported("csel", 0xC69FF4UL);
        x0 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A028;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x26);
        x3 = RuntimeMemory.ReadU64(x25);
        x2 = x0;
        x0 = x20;
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F693CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A028;
        label_0xC6A028:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0xCUL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13017136 = unchecked((uint)(x8));
        __arm64_flags_right_13017136 = unchecked((uint)0x14UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        RuntimeCalls.Unsupported("b.lt", 0xC6A038UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC69FDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x350UL))));
        __arm64_flags_left_13017172 = unchecked((uint)(x0));
        __arm64_flags_right_13017172 = unchecked((uint)0x1UL);
        __arm64_flags_result_13017172 = unchecked((uint)((__arm64_flags_left_13017172) & (__arm64_flags_right_13017172)));
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x9 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(x28);
        RuntimeCalls.Unsupported("csel", 0xC6A064UL);
        x21 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x20);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x0;
        x0 = unchecked((ulong)((sp) + (0x1CUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC6A508;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x20UL))), x0);
        x1 = x0;
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0xFFFFFFFFFFFFFFF8UL))))));
        __arm64_flags_left_13017252 = unchecked((uint)(x8));
        __arm64_flags_right_13017252 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13017252 >= __arm64_flags_right_13017252))) || (unchecked((uint)((__arm64_flags_left_13017252) - (__arm64_flags_right_13017252))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x378UL))));
        x0 = x20;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x10 = RuntimeMemory.ReadU64(sp);
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((sp) + (0x1CUL))))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x18UL))))));
        __arm64_flags_left_13017296 = unchecked((uint)(x8));
        __arm64_flags_right_13017296 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13017296 >= __arm64_flags_right_13017296))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13017308 = unchecked((uint)(x9));
        __arm64_flags_right_13017308 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13017308 >= __arm64_flags_right_13017308))) || (unchecked((uint)((__arm64_flags_left_13017308) - (__arm64_flags_right_13017308))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x10) + (unchecked((ulong)((x8) << (int)(unchecked((int)(0x3UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x22 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x30UL))), x1);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0xFFFFFFFFFFFFFFE8UL))))));
        __arm64_flags_left_13017344 = unchecked((uint)(x8));
        __arm64_flags_right_13017344 = unchecked((uint)0x3UL);
        if (((!((__arm64_flags_left_13017344 >= __arm64_flags_right_13017344))) || (unchecked((uint)((__arm64_flags_left_13017344) - (__arm64_flags_right_13017344))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x328UL))));
        x22 = x20;
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x38UL))), x1);
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0xFFFFFFFFFFFFFFE0UL))))));
        __arm64_flags_left_13017384 = unchecked((uint)(x8));
        __arm64_flags_right_13017384 = unchecked((uint)0x4UL);
        if (((!((__arm64_flags_left_13017384 >= __arm64_flags_right_13017384))) || (unchecked((uint)((__arm64_flags_left_13017384) - (__arm64_flags_right_13017384))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC6A504;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6A44UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A150;
        label_0xC6A150:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, x1, x2, x3);
        v12 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0x1CUL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x14UL)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x11UL)))))));
        __arm64_flags_left_13017444 = unchecked((uint)(x8));
        __arm64_flags_right_13017444 = unchecked((uint)0x0UL);
        x0 = 0x0UL;
        RuntimeCalls.Unsupported("csel", 0xC6A16CUL);
        x21 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x9)) : unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x82UL)))))));
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6A194;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC6A194;
        label_0xC6A194:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((int)((unchecked((int)(unchecked((uint)(x21))))) >> (int)(unchecked((int)(0x2UL)))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v12.GetUInt64(0)))), 0)))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v11.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v10.GetUInt64(0)))), 0))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x22))))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41200000UL)), 0)), 0));
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5034UL /* metadata target: GUI.Box */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0x1CUL))))));
        x20 = RuntimeMemory.ReadU64(x29);
        x9 = RuntimeMemory.ReadU64(sp);
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13017556 = unchecked((uint)(x0));
        __arm64_flags_right_13017556 = unchecked((uint)0x4UL);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x1CUL))), unchecked((uint)(x0)));
        RuntimeCalls.Unsupported("b.lt", 0xC6A1DCUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC69E90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)(0x1BUL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A20C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x370UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A20C;
        label_0xC6A20C:
        ;
        x21 = 0x1A8D000UL;
        x22 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x24 = 0x1A8D000UL;
        x25 = 0x1A8D000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x380UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x8A8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x248UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x348UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x390UL))));
        x0 = unchecked((ulong)(unchecked((uint)(0xDUL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A260;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x320UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A260;
        label_0xC6A260:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x130UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A28C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x340UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A28C;
        label_0xC6A28C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x12FUL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A2B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x358UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A2B8;
        label_0xC6A2B8:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x132UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A2E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3A0UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A2E4;
        label_0xC6A2E4:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x131UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A310;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x360UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A310;
        label_0xC6A310:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A33C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x330UL))));
        x0 = x20;
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x20 = x0;
        goto label_0xC6A33C;
        label_0xC6A33C:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, x1, x2, x3);
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xCE0UL))));
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) - (unchecked((uint)(0x64UL)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) - (unchecked((uint)(0x14UL)))))));
        x0 = RuntimeMemory.ReadU64(x9);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x10))))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6A37C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6A378UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC6A37C;
        label_0xC6A37C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x42480000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41200000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v1 = v8;
        v2 = v9;
        x0 = x20;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5034UL /* metadata target: GUI.Box */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x25);
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x28UL)))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x9))))))), 0));
        x9 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41200000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41F00000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5444UL /* metadata target: GUI.Button */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A3D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C74F0UL /* metadata target: Input.ResetInputAxes */, x0, x1, x2, x3);
        goto label_0xC6A3D8;
        label_0xC6A3D8:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) - (unchecked((uint)(0x28UL)))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x10))))))), 0));
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6A404;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC6A404;
        label_0xC6A404:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x8 = unchecked((ulong)(unchecked((uint)(0x42E60000UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x42C80000UL))));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41F00000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x9))), 0)), 0));
        v1 = v8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5444UL /* metadata target: GUI.Button */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6A444;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6A43C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6A438UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC6A43C;
        label_0xC6A43C:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176D458UL /* metadata target: Application.Quit */, x0, x1, x2, x3);
        goto label_0xC6A444;
        label_0xC6A444:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6A470;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC6A470;
        label_0xC6A470:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176D568UL /* metadata target: Application.get_unityVersion */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = x0;
        x3 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCE0UL))));
        x21 = x0;
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6A4B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC6A4B0;
        label_0xC6A4B0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) - (unchecked((uint)(0xE6UL)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) - (unchecked((uint)(0x28UL)))))));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x8))))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x435C0000UL))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x9))))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x41F00000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(x8))), 0)), 0));
        x0 = x21;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5034UL /* metadata target: GUI.Box */, x0, x1, x2, x3);
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
        __arm64_pair_address_13018352 = unchecked((ulong)((sp) + (0x30UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13018352)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13018352) + (0x8UL))))), 0));
        __arm64_pair_address_13018356 = unchecked((ulong)((sp) + (0x20UL)));
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13018356)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13018356) + (0x8UL))))), 0));
        v12 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x10UL))))), 0));
        sp = unchecked((ulong)((sp) + (0xA0UL)));
        return x0;
        label_0xC6A504:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC6A508;
        label_0xC6A508:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadHardwareTester.ctor` — RVA `0xc6a50c`

- Lift status: **exact**; input span: 424 bytes; span to next metadata RVA: 424 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=105 (informational only).

```csharp
public static ulong GamepadHardwareTester_ctor_RVAc6a50c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
