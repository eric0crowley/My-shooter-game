# `BuiltInGamepadProfileBankOSX` — TypeDefIndex 4974

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## `BuiltInGamepadProfileBankOSX.ctor` — RVA `0xc31990`

- Lift status: **exact**; input span: 1784 bytes; span to next metadata RVA: 1784 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=272 (informational only).

```csharp
public static ulong BuiltInGamepadProfileBankOSX_ctor_RVAc31990(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12787000 = default(uint);
        uint __arm64_flags_left_12787380 = default(uint);
        uint __arm64_flags_left_12787760 = default(uint);
        uint __arm64_flags_right_12787000 = default(uint);
        uint __arm64_flags_right_12787380 = default(uint);
        uint __arm64_flags_right_12787760 = default(uint);
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
        sp = unchecked((ulong)((sp) - (0x110UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x19 = 0x1A8C000UL;
        x27 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x13BUL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x288UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0x2F0UL))));
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC31A40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x288UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x290UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x298UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2D0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x300UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x13BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC31A40;
        label_0xC31A40:
        ;
        x0 = x21;
        x1 = 0x0UL;
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x78UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = x0;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA8UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x98UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x90UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x88UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x28 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x29 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30780UL /* metadata target: GamepadProfile.KeySource.PlusAxis */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30780UL /* metadata target: GamepadProfile.KeySource.PlusAxis */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x290UL))));
        x26 = unchecked((ulong)(unchecked((uint)(x0))));
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x2 = RuntimeMemory.ReadU64(x27);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x88UL))));
        x6 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x8UL))), x28);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x27 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x0UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x8UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x0UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x8UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), x9);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x98UL))));
        x7 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x98UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x0UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x8UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x8UL))), x19);
        RuntimeMemory.WriteU64(sp, x8);
        x0 = RuntimeCalls.InvokeDirect(0xC30188UL /* metadata target: GamepadProfile.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC32084;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC31BA4UL);
        }
        if ((x27 == 0x0UL))
        {
            goto label_0xC31BBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x27;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC32078;
        }
        else
        {
            goto label_0xC31BBC;
        }
        label_0xC31BBC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC32074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x27);
        x1 = x27;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA8UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x98UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x90UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x88UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x28 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x29 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30780UL /* metadata target: GamepadProfile.KeySource.PlusAxis */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30780UL /* metadata target: GamepadProfile.KeySource.PlusAxis */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x290UL))));
        x26 = unchecked((ulong)(unchecked((uint)(x0))));
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2A8UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x300UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x88UL))));
        x6 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA8UL))));
        x27 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x0UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x8UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x0UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x8UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x0UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x8UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x8UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), x9);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x98UL))));
        x7 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x98UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(sp, x8);
        x0 = RuntimeCalls.InvokeDirect(0xC30188UL /* metadata target: GamepadProfile.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x27 == 0x0UL))
        {
            goto label_0xC31D34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x27;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC32078;
        }
        else
        {
            goto label_0xC31D34;
        }
        label_0xC31D34:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_12787000 = unchecked((uint)(x8));
        __arm64_flags_right_12787000 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_12787000 >= __arm64_flags_right_12787000))) || (unchecked((uint)((__arm64_flags_left_12787000) - (__arm64_flags_right_12787000))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC32074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x27);
        x1 = x27;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA8UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC304F4UL /* metadata target: GamepadProfile.JoystickSource.Dpad */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x98UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0xEUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x90UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0xDUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x88UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0xCUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0xFUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x28 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x29 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0xBUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x290UL))));
        x26 = unchecked((ulong)(unchecked((uint)(x0))));
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2F8UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x298UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x88UL))));
        x6 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA8UL))));
        x27 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x0UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x8UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x0UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x8UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x0UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x8UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x8UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), x9);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x98UL))));
        x7 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x98UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(sp, x8);
        x0 = RuntimeCalls.InvokeDirect(0xC30188UL /* metadata target: GamepadProfile.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x27 == 0x0UL))
        {
            goto label_0xC31EB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x27;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC32078;
        }
        else
        {
            goto label_0xC31EB0;
        }
        label_0xC31EB0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_12787380 = unchecked((uint)(x8));
        __arm64_flags_right_12787380 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_12787380 >= __arm64_flags_right_12787380))) || (unchecked((uint)((__arm64_flags_left_12787380) - (__arm64_flags_right_12787380))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC32074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x28 = 0x1A8C000UL;
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((x28) + (0x2B0UL))));
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x27);
        x1 = x27;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA8UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xA0UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC305D0UL /* metadata target: GamepadProfile.JoystickSource.Axes */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x98UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x90UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x88UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x80UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x0 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x27 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x19 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x9UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x29 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x6UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x7UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x24 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x25 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)(0xBUL))));
        x0 = RuntimeCalls.InvokeDirect(0xC30718UL /* metadata target: GamepadProfile.KeySource.Key */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x290UL))));
        x26 = unchecked((ulong)(unchecked((uint)(x0))));
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x8 = 0x1A8C000UL;
        x1 = RuntimeMemory.ReadU64(x28);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2D0UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x88UL))));
        x6 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA8UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x4 = 0x0UL;
        x5 = 0x0UL;
        x28 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x18UL)))) + (0x8UL))), x27);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x0UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x58UL)))) + (0x8UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x0UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x48UL)))) + (0x8UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x0UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x38UL)))) + (0x8UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), x9);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x98UL))));
        x7 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x98UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x0UL))), x19);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x28UL)))) + (0x8UL))), x29);
        RuntimeMemory.WriteU64(sp, x8);
        x0 = RuntimeCalls.InvokeDirect(0xC30188UL /* metadata target: GamepadProfile.ctor */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x28 == 0x0UL))
        {
            goto label_0xC3202C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x28;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC32078;
        }
        else
        {
            goto label_0xC3202C;
        }
        label_0xC3202C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_12787760 = unchecked((uint)(x8));
        __arm64_flags_right_12787760 = unchecked((uint)0x3UL);
        if (((!((__arm64_flags_left_12787760 >= __arm64_flags_right_12787760))) || (unchecked((uint)((__arm64_flags_left_12787760) - (__arm64_flags_right_12787760))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC32074;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x28);
        x1 = x28;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x78UL))));
        x1 = x20;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xF0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x100UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD0UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xD0UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x110UL)));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC32074:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC32078;
        label_0xC32078:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC32084;
        label_0xC32084:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```
