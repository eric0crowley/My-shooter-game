# `GamepadManager.Gamepad` — TypeDefIndex 4959

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `GamepadManager` | `manager` |
| `0x18` | `GamepadProfile` | `profile` |
| `0x20` | `bool` | `isActivated` |
| `0x21` | `bool` | `isConnected` |
| `0x22` | `bool` | `isBlocked` |
| `0x28` | `string` | `internalJoyName` |
| `0x30` | `int` | `internalJoyId` |
| `0x34` | `int` | `slot` |
| `0x38` | `GamepadManager.Gamepad.JoyState` | `leftStick` |
| `0x40` | `GamepadManager.Gamepad.JoyState` | `rightStick` |
| `0x48` | `GamepadManager.Gamepad.JoyState` | `dpad` |
| `0x50` | `GamepadManager.Gamepad.KeyState[]` | `keys` |
| `0x58` | `GamepadManager.Gamepad.InternalAxisState[]` | `internalAxes` |
| `0x60` | `GamepadManager.Gamepad.InternalKeyState[]` | `internalKeys` |

## `GamepadManager.Gamepad.ctor` — RVA `0xc2af14`

- Lift status: **exact**; input span: 960 bytes; span to next metadata RVA: 960 bytes.
- Metadata signature: `public void .ctor(GamepadManager manager) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=147 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_ctor_RVAc2af14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12759092 = default(ulong);
        ulong __arm64_flags_left_12759144 = default(ulong);
        ulong __arm64_flags_left_12759212 = default(ulong);
        ulong __arm64_flags_left_12759276 = default(ulong);
        ulong __arm64_flags_left_12759536 = default(ulong);
        uint __arm64_flags_left_12759548 = default(uint);
        ulong __arm64_flags_left_12759640 = default(ulong);
        ulong __arm64_flags_right_12759092 = default(ulong);
        ulong __arm64_flags_right_12759144 = default(ulong);
        ulong __arm64_flags_right_12759212 = default(ulong);
        ulong __arm64_flags_right_12759276 = default(ulong);
        ulong __arm64_flags_right_12759536 = default(ulong);
        uint __arm64_flags_right_12759548 = default(uint);
        ulong __arm64_flags_right_12759640 = default(ulong);
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
        x23 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x117UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xA8UL))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2AFAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x117UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2AFAC;
        label_0xC2AFAC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(0xAUL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x22 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x58UL))), x0);
        x1 = x0;
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x14UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x60UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x25 = RuntimeMemory.ReadU64(x22);
        if ((x25 == 0x0UL))
        {
            goto label_0xC2B2C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x29 = 0x1A8C000UL;
        x27 = 0x1A8C000UL;
        x24 = 0x1A8C000UL;
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((x29) + (0xB0UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((x27) + (0xB8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xD0UL))));
        x28 = 0x0UL;
        x26 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xC2B030;
        label_0xC2B030:
        ;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x25) + (0x18UL))))))));
        __arm64_flags_left_12759092 = x28;
        __arm64_flags_right_12759092 = x8;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12759092) - (__arm64_flags_right_12759092))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_12759092)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_12759092)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12759092) - (__arm64_flags_right_12759092))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_12759092)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC2B098;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x29);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2D8E8UL /* metadata target: GamepadManager.Gamepad.InternalAxisState.ctor */, x0, x1, x2, x3);
        if ((x23 == 0x0UL))
        {
            goto label_0xC2B064;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x25);
        x0 = x23;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2B2C8;
        }
        else
        {
            goto label_0xC2B064;
        }
        label_0xC2B064:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x25) + (0x18UL))))));
        __arm64_flags_left_12759144 = x28;
        __arm64_flags_right_12759144 = x8;
        if ((__arm64_flags_left_12759144 >= __arm64_flags_right_12759144))
        {
            goto label_0xC2B2C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x25) + (unchecked((ulong)((x28) << (int)(unchecked((int)(0x3UL))))))));
        x0 = unchecked((ulong)((x25) + (unchecked((ulong)(unchecked((uint)(x26)))))));
        x1 = x23;
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x25 = RuntimeMemory.ReadU64(x22);
        x28 = unchecked((ulong)((x28) + (0x1UL)));
        x26 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x26))) + (unchecked((uint)(0x8UL)))))));
        if ((x25 != 0x0UL))
        {
            goto label_0xC2B030;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B094UL);
        }
        goto label_0xC2B2C0;
        label_0xC2B098:
        ;
        x28 = RuntimeMemory.ReadU64(x21);
        if ((x28 == 0x0UL))
        {
            goto label_0xC2B2C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x0UL;
        x25 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        goto label_0xC2B0A8;
        label_0xC2B0A8:
        ;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x28) + (0x18UL))))))));
        __arm64_flags_left_12759212 = x23;
        __arm64_flags_right_12759212 = x8;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12759212) - (__arm64_flags_right_12759212))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_12759212)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_12759212)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12759212) - (__arm64_flags_right_12759212))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_12759212)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC2B11C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x27);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x16UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x14UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x8 = RuntimeMemory.ReadU64(x28);
        x0 = x22;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2B2C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x28) + (0x18UL))))));
        __arm64_flags_left_12759276 = x23;
        __arm64_flags_right_12759276 = x8;
        if ((__arm64_flags_left_12759276 >= __arm64_flags_right_12759276))
        {
            goto label_0xC2B2C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x28) + (unchecked((ulong)((x23) << (int)(unchecked((int)(0x3UL))))))));
        x0 = unchecked((ulong)((x28) + (unchecked((ulong)(unchecked((uint)(x25)))))));
        x1 = x22;
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x28 = RuntimeMemory.ReadU64(x21);
        x23 = unchecked((ulong)((x23) + (0x1UL)));
        x25 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x25))) + (unchecked((uint)(0x8UL)))))));
        if ((x28 != 0x0UL))
        {
            goto label_0xC2B0A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B118UL);
        }
        goto label_0xC2B2C0;
        label_0xC2B11C:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC2B2C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC0UL))));
        x0 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = x21;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2D97CUL /* metadata target: GamepadManager.Gamepad.JoyState.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x22);
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = x21;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2D97CUL /* metadata target: GamepadManager.Gamepad.JoyState.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x22);
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x2 = x21;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2D97CUL /* metadata target: GamepadManager.Gamepad.JoyState.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x22);
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0xCUL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x50UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x27 = RuntimeMemory.ReadU64(x21);
        if ((x27 == 0x0UL))
        {
            goto label_0xC2B2C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x28 = 0x432000UL;
        x25 = 0x0UL;
        x26 = unchecked((ulong)(unchecked((uint)(0x20UL))));
        x28 = unchecked((ulong)((x28) + (0x2D8UL)));
        goto label_0xC2B1EC;
        label_0xC2B1EC:
        ;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x27) + (0x18UL))))))));
        __arm64_flags_left_12759536 = x25;
        __arm64_flags_right_12759536 = x8;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12759536) - (__arm64_flags_right_12759536))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_12759536)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_12759536)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12759536) - (__arm64_flags_right_12759536))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_12759536)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC2B2A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x25))) - (unchecked((uint)(0x6UL)))))));
        __arm64_flags_left_12759548 = unchecked((uint)(x8));
        __arm64_flags_right_12759548 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_12759548 >= __arm64_flags_right_12759548) && (!((unchecked((uint)((__arm64_flags_left_12759548) - (__arm64_flags_right_12759548))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC2B284;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0xC2B214UL;
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x28) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x9 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x9);
        label_0xC2B238:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC2DA14UL /* metadata target: GamepadManager.Gamepad.KeyState.ctor */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC2B254;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x27);
        x0 = x22;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2B2C8;
        }
        else
        {
            goto label_0xC2B254;
        }
        label_0xC2B254:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x27) + (0x18UL))))));
        __arm64_flags_left_12759640 = x25;
        __arm64_flags_right_12759640 = x8;
        if ((__arm64_flags_left_12759640 >= __arm64_flags_right_12759640))
        {
            goto label_0xC2B2C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((x27) + (unchecked((ulong)(unchecked((uint)(x26)))))));
        x1 = x22;
        RuntimeMemory.WriteU64(x0, x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x27 = RuntimeMemory.ReadU64(x21);
        x25 = unchecked((ulong)((x25) + (0x1UL)));
        x26 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x26))) + (unchecked((uint)(0x8UL)))))));
        if ((x27 != 0x0UL))
        {
            goto label_0xC2B1EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B280UL);
        }
        goto label_0xC2B2C0;
        label_0xC2B284:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x22 = x0;
        x1 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        goto label_0xC2B238;
        label_0xC2B2A0:
        ;
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
        return RuntimeCalls.InvokeDirect(0xC2CF0CUL /* metadata target: GamepadManager.Gamepad.OnDisconnect */);
        label_0xC2B2C0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2B2C4;
        label_0xC2B2C4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2B2C8;
        label_0xC2B2C8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.SetRig` — RVA `0xc2bd0c`

- Lift status: **exact**; input span: 760 bytes; span to next metadata RVA: 760 bytes.
- Metadata signature: `public void SetRig(InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=97 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_SetRig_RVAc2bd0c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12762716 = default(uint);
        uint __arm64_flags_left_12762820 = default(uint);
        uint __arm64_flags_left_12762924 = default(uint);
        uint __arm64_flags_left_12763028 = default(uint);
        uint __arm64_flags_right_12762716 = default(uint);
        uint __arm64_flags_right_12762820 = default(uint);
        uint __arm64_flags_right_12762924 = default(uint);
        uint __arm64_flags_right_12763028 = default(uint);
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
        x21 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x119UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BD48;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x119UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2BD48;
        label_0xC2BD48:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x38UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BD58UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2BD5C;
        label_0xC2BD5C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BD7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BD70UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0xC8UL)));
        goto label_0xC2BD88;
        label_0xC2BD7C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (0x48UL)));
        goto label_0xC2BD88;
        label_0xC2BD88:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BDB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BDB0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2BDB4;
        label_0xC2BDB4:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BDD4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BDC8UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0xD0UL)));
        goto label_0xC2BDE0;
        label_0xC2BDD4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (0x50UL)));
        goto label_0xC2BDE0;
        label_0xC2BDE0:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BE0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BE08UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2BE0C;
        label_0xC2BE0C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BE2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BE20UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0xC0UL)));
        goto label_0xC2BE38;
        label_0xC2BE2C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (0x40UL)));
        goto label_0xC2BE38;
        label_0xC2BE38:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12762716 = unchecked((uint)(x9));
        __arm64_flags_right_12762716 = unchecked((uint)0x6UL);
        if (((!((__arm64_flags_left_12762716 >= __arm64_flags_right_12762716))) || (unchecked((uint)((__arm64_flags_left_12762716) - (__arm64_flags_right_12762716))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2C000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BE78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BE74UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2BE78;
        label_0xC2BE78:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BE98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BE8CUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0xD8UL)));
        goto label_0xC2BEA4;
        label_0xC2BE98:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (0x58UL)));
        goto label_0xC2BEA4;
        label_0xC2BEA4:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x20UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12762820 = unchecked((uint)(x9));
        __arm64_flags_right_12762820 = unchecked((uint)0x8UL);
        if (((!((__arm64_flags_left_12762820 >= __arm64_flags_right_12762820))) || (unchecked((uint)((__arm64_flags_left_12762820) - (__arm64_flags_right_12762820))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2C000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x60UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BEE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BEDCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2BEE0;
        label_0xC2BEE0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BF00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BEF4UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0xD8UL)));
        goto label_0xC2BF0C;
        label_0xC2BF00:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (0x58UL)));
        goto label_0xC2BF0C;
        label_0xC2BF0C:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x20UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12762924 = unchecked((uint)(x9));
        __arm64_flags_right_12762924 = unchecked((uint)0x7UL);
        if (((!((__arm64_flags_left_12762924 >= __arm64_flags_right_12762924))) || (unchecked((uint)((__arm64_flags_left_12762924) - (__arm64_flags_right_12762924))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2C000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x58UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BF48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BF44UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2BF48;
        label_0xC2BF48:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BF68;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BF5CUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0xE0UL)));
        goto label_0xC2BF74;
        label_0xC2BF68:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (0x60UL)));
        goto label_0xC2BF74;
        label_0xC2BF74:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x20UL))), x1);
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12763028 = unchecked((uint)(x9));
        __arm64_flags_right_12763028 = unchecked((uint)0x9UL);
        if (((!((__arm64_flags_left_12763028 >= __arm64_flags_right_12763028))) || (unchecked((uint)((__arm64_flags_left_12763028) - (__arm64_flags_right_12763028))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2C000;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x68UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BFB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BFACUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2BFB0;
        label_0xC2BFB0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BFD0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BFC4UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x19) + (0xE0UL)));
        goto label_0xC2BFDC;
        label_0xC2BFD0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (0x60UL)));
        goto label_0xC2BFDC;
        label_0xC2BFDC:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BFFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x20UL))), x1);
        x0 = x21;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC2BFFC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2C000;
        label_0xC2C000:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.Update` — RVA `0xc2c1fc`

- Lift status: **exact**; input span: 264 bytes; span to next metadata RVA: 264 bytes.
- Metadata signature: `public void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_Update_RVAc2c1fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12763680 = default(uint);
        uint __arm64_flags_left_12763688 = default(uint);
        uint __arm64_flags_left_12763744 = default(uint);
        uint __arm64_flags_left_12763752 = default(uint);
        uint __arm64_flags_left_12763844 = default(uint);
        uint __arm64_flags_left_12763852 = default(uint);
        uint __arm64_flags_right_12763680 = default(uint);
        uint __arm64_flags_right_12763688 = default(uint);
        uint __arm64_flags_right_12763744 = default(uint);
        uint __arm64_flags_right_12763752 = default(uint);
        uint __arm64_flags_right_12763844 = default(uint);
        uint __arm64_flags_right_12763852 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        x19 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C290;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC2C21C;
        label_0xC2C21C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12763680 = unchecked((uint)(x20));
        __arm64_flags_right_12763680 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763680) - (__arm64_flags_right_12763680))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12763680)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12763680)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763680) - (__arm64_flags_right_12763680))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12763680)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C250;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C228UL);
        }
        __arm64_flags_left_12763688 = unchecked((uint)(x20));
        __arm64_flags_right_12763688 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12763688 >= __arm64_flags_right_12763688))
        {
            goto label_0xC2C300;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C23CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E444UL /* metadata target: GamepadManager.Gamepad.InternalKeyState.Update */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC2C21C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C24CUL);
        }
        goto label_0xC2C2F0;
        label_0xC2C250:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC2C25C;
        label_0xC2C25C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12763744 = unchecked((uint)(x20));
        __arm64_flags_right_12763744 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763744) - (__arm64_flags_right_12763744))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12763744)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12763744)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763744) - (__arm64_flags_right_12763744))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12763744)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C290;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C268UL);
        }
        __arm64_flags_left_12763752 = unchecked((uint)(x20));
        __arm64_flags_right_12763752 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12763752 >= __arm64_flags_right_12763752))
        {
            goto label_0xC2C300;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C27CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E488UL /* metadata target: GamepadManager.Gamepad.InternalAxisState.Update */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC2C25C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C28CUL);
        }
        goto label_0xC2C2F0;
        label_0xC2C290:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C298UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E4CCUL /* metadata target: GamepadManager.Gamepad.JoyState.Update */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C2A4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E4CCUL /* metadata target: GamepadManager.Gamepad.JoyState.Update */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C2B0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E4CCUL /* metadata target: GamepadManager.Gamepad.JoyState.Update */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x0UL;
        goto label_0xC2C2C0;
        label_0xC2C2C0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12763844 = unchecked((uint)(x20));
        __arm64_flags_right_12763844 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763844) - (__arm64_flags_right_12763844))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12763844)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12763844)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763844) - (__arm64_flags_right_12763844))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12763844)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C2F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C2CCUL);
        }
        __arm64_flags_left_12763852 = unchecked((uint)(x20));
        __arm64_flags_right_12763852 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12763852 >= __arm64_flags_right_12763852))
        {
            goto label_0xC2C300;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x20) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C2E0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E4F0UL /* metadata target: GamepadManager.Gamepad.KeyState.Update */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x20 = unchecked((ulong)((x20) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC2C2C0;
        }
        else
        {
            goto label_0xC2C2F0;
        }
        label_0xC2C2F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2C2F4;
        label_0xC2C2F4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2C300:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.ApplyGamepadState` — RVA `0xc2c304`

- Lift status: **exact**; input span: 296 bytes; span to next metadata RVA: 296 bytes.
- Metadata signature: `public void ApplyGamepadState(GamepadManager.Gamepad g) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=32 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_ApplyGamepadState_RVAc2c304(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12764048 = default(uint);
        uint __arm64_flags_left_12764076 = default(uint);
        uint __arm64_flags_left_12764096 = default(uint);
        uint __arm64_flags_left_12764176 = default(uint);
        uint __arm64_flags_right_12764048 = default(uint);
        uint __arm64_flags_right_12764076 = default(uint);
        uint __arm64_flags_right_12764096 = default(uint);
        uint __arm64_flags_right_12764176 = default(uint);
        float __arm64_float_flags_left_12764148 = default(float);
        float __arm64_float_flags_left_12764160 = default(float);
        float __arm64_float_flags_right_12764148 = default(float);
        float __arm64_float_flags_right_12764160 = default(float);
        float __arm64_fp_left_12764156 = default(float);
        float __arm64_fp_right_12764156 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x14 = default(ulong);
        ulong x15 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC2C418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        x20 = x0;
        if ((x9 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x38UL))));
        x19 = x1;
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61064UL /* metadata target: JoystickState.ApplyState */, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61064UL /* metadata target: JoystickState.ApplyState */, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC61064UL /* metadata target: JoystickState.ApplyState */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12764048 = unchecked((uint)(x9));
        __arm64_flags_right_12764048 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764048) - (__arm64_flags_right_12764048))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12764048)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12764048)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764048) - (__arm64_flags_right_12764048))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12764048)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x12 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x11 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2C3AC;
        label_0xC2C3AC:
        ;
        __arm64_flags_left_12764076 = unchecked((uint)(x12));
        __arm64_flags_right_12764076 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12764076 >= __arm64_flags_right_12764076))
        {
            goto label_0xC2C428;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C3B4UL);
        }
        if ((x10 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x18UL))))));
        x12 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x12))))));
        __arm64_flags_left_12764096 = unchecked((uint)(x12));
        __arm64_flags_right_12764096 = unchecked((uint)(x13));
        if ((__arm64_flags_left_12764096 >= __arm64_flags_right_12764096))
        {
            goto label_0xC2C428;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x12))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x14 = RuntimeMemory.ReadU64(unchecked((ulong)((x13) + (0x20UL))));
        if ((x14 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x13 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x12))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x13 = RuntimeMemory.ReadU64(unchecked((ulong)((x13) + (0x20UL))));
        if ((x13 == 0x0UL))
        {
            goto label_0xC2C424;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x15 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x14) + (0x3CUL))))))));
        if ((unchecked((uint)(x15)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C3EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C3E8UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x13) + (0x30UL))), unchecked((byte)(unchecked((uint)(x11)))));
        goto label_0xC2C3EC;
        label_0xC2C3EC:
        ;
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x14) + (0x38UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x13) + (0x2CUL))))), 0));
        __arm64_float_flags_left_12764148 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12764148 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12764148 >= __arm64_float_flags_right_12764148) || ((__arm64_float_flags_left_12764148 != __arm64_float_flags_left_12764148) || (__arm64_float_flags_right_12764148 != __arm64_float_flags_right_12764148))))
        {
            goto label_0xC2C40C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C3FCUL);
        }
        __arm64_fp_left_12764156 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_fp_right_12764156 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12764156 != __arm64_fp_left_12764156) ? __arm64_fp_left_12764156 : ((__arm64_fp_right_12764156 != __arm64_fp_right_12764156) ? __arm64_fp_right_12764156 : (((__arm64_fp_left_12764156 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12764156 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12764156), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12764156), 0))))), 0) : ((__arm64_fp_left_12764156 <= __arm64_fp_right_12764156) ? __arm64_fp_left_12764156 : __arm64_fp_right_12764156))))), 0));
        __arm64_float_flags_left_12764160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12764160 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12764160 >= __arm64_float_flags_right_12764160) || ((__arm64_float_flags_left_12764160 != __arm64_float_flags_left_12764160) || (__arm64_float_flags_right_12764160 != __arm64_float_flags_right_12764160))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x13) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0));
        goto label_0xC2C40C;
        label_0xC2C40C:
        ;
        x12 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x12))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12764176 = unchecked((uint)(x12));
        __arm64_flags_right_12764176 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764176) - (__arm64_flags_right_12764176))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12764176)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12764176)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764176) - (__arm64_flags_right_12764176))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12764176)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C3AC;
        }
        else
        {
            goto label_0xC2C418;
        }
        label_0xC2C418:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2C424:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2C428;
        label_0xC2C428:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.OnActivate` — RVA `0xc2cd54`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void OnActivate(int slot) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_OnActivate_RVAc2cd54(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x34UL))), unchecked((uint)(x1)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return RuntimeCalls.InvokeDirect(0xC2DB9CUL /* metadata target: GamepadManager.Gamepad.Reset */);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.OnDisactivate` — RVA `0xc2cf04`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void OnDisactivate() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_OnDisactivate_RVAc2cf04(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return RuntimeCalls.InvokeDirect(0xC2DB9CUL /* metadata target: GamepadManager.Gamepad.Reset */);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.OnDisconnect` — RVA `0xc2cf0c`

- Lift status: **exact**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `public void OnDisconnect() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_OnDisconnect_RVAc2cf0c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x11AUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x48UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CF40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x11AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2CF40;
        label_0xC2CF40:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC2CF60UL /* metadata target: GamepadManager.Gamepad.ConnectToJoy */);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.ConnectToJoy` — RVA `0xc2cf60`

- Lift status: **partial**; input span: 324 bytes; span to next metadata RVA: 324 bytes.
- Metadata signature: `public void ConnectToJoy(int internalJoyId, string joyName) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=37 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.hs' at 0xc2cfe4; reason: Unknown IR expression at 0xc2cfe4; reason: Unsupported instruction 'ccmp' at 0xc2d06c; reason: Unknown IR expression at 0xc2d070; reason: Unsupported instruction 'b.lt' at 0xc2d084; reason: Unknown IR expression at 0xc2d084

```csharp
public static ulong GamepadManager_Gamepad_ConnectToJoy_RVAc2cf60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12767196 = default(uint);
        uint __arm64_flags_left_12767284 = default(uint);
        uint __arm64_flags_left_12767308 = default(uint);
        uint __arm64_flags_left_12767328 = default(uint);
        uint __arm64_flags_left_12767340 = default(uint);
        uint __arm64_flags_left_12767348 = default(uint);
        uint __arm64_flags_right_12767196 = default(uint);
        uint __arm64_flags_right_12767284 = default(uint);
        uint __arm64_flags_right_12767308 = default(uint);
        uint __arm64_flags_right_12767328 = default(uint);
        uint __arm64_flags_right_12767340 = default(uint);
        uint __arm64_flags_right_12767348 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
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
        x22 = x0;
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x18UL))), 0x0UL);
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        x0 = x22;
        x1 = 0x0UL;
        x21 = x2;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x22;
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(x22, 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0xAUL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CFC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x21);
        x1 = x21;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x8UL))), unchecked((uint)(x20)));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2CFC8;
        label_0xC2CFC4:
        ;
        x9 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2CFC8;
        label_0xC2CFC8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x21UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2D09C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2CFD8;
        label_0xC2CFD8:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12767196 = unchecked((uint)(x21));
        __arm64_flags_right_12767196 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12767196) - (__arm64_flags_right_12767196))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12767196)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12767196)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12767196) - (__arm64_flags_right_12767196))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12767196)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2D028;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2CFE4UL);
        }
        RuntimeCalls.Unsupported("b.hs", 0xC2CFE4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2D0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC2D09C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC2AA48UL /* metadata target: GamepadManager.GetJoyAxisName */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x22) + (0x10UL))), unchecked((ulong)(unchecked((uint)(x0)))));
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU16(unchecked((ulong)((x22) + (0x10UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x8UL))), 0x0UL);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC2CFD8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D024UL);
        }
        goto label_0xC2D09C;
        label_0xC2D028:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2D09C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12767284 = unchecked((uint)(x9));
        __arm64_flags_right_12767284 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12767284) - (__arm64_flags_right_12767284))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12767284)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12767284)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12767284) - (__arm64_flags_right_12767284))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12767284)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2D088;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(unchecked((uint)(0x14UL))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) * (unchecked((uint)(x11)))))));
        x10 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x15EUL)))))));
        goto label_0xC2D04C;
        label_0xC2D04C:
        ;
        __arm64_flags_left_12767308 = unchecked((uint)(x10));
        __arm64_flags_right_12767308 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12767308 >= __arm64_flags_right_12767308))
        {
            goto label_0xC2D0A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x12) + (0x20UL))));
        if ((x12 == 0x0UL))
        {
            goto label_0xC2D09C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D060UL);
        }
        __arm64_flags_left_12767328 = unchecked((uint)(x10));
        __arm64_flags_right_12767328 = unchecked((uint)0x14UL);
        x13 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(x10)))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeCalls.Unsupported("ccmp", 0xC2D06CUL);
        __arm64_flags_left_12767340 = unchecked((uint)(x20));
        __arm64_flags_right_12767340 = unchecked((uint)0x4UL);
        x13 = unchecked((ulong)(((__Unsupported<bool>("Unknown IR expression") ? (!((__arm64_flags_left_12767340 >= __arm64_flags_right_12767340))) : (!(true))) ? unchecked((uint)(x13)) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12767348 = unchecked((uint)(x10));
        __arm64_flags_right_12767348 = unchecked((uint)(x9));
        RuntimeMemory.WriteU16(unchecked((ulong)((x12) + (0x14UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x12) + (0x10UL))), unchecked((uint)(x13)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x12) + (0x16UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.lt", 0xC2D084UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2D04C;
        }
        else
        {
            goto label_0xC2D088;
        }
        label_0xC2D088:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC2DB9CUL /* metadata target: GamepadManager.Gamepad.Reset */);
        label_0xC2D09C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2D0A0;
        label_0xC2D0A0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.SetProfile` — RVA `0xc2d0fc`

- Lift status: **partial**; input span: 304 bytes; span to next metadata RVA: 304 bytes.
- Metadata signature: `public void SetProfile(GamepadProfile profile) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=28 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'rev64' at 0xc2d1e4

```csharp
public static ulong GamepadManager_Gamepad_SetProfile_RVAc2d0fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12767632 = default(uint);
        uint __arm64_flags_left_12767640 = default(uint);
        ulong __arm64_flags_left_12767688 = default(ulong);
        uint __arm64_flags_right_12767632 = default(uint);
        uint __arm64_flags_right_12767640 = default(uint);
        ulong __arm64_flags_right_12767688 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x21 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x18UL))), x1);
        x19 = x0;
        x0 = x21;
        x20 = x1;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC2D134;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x38UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2D13C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D130UL);
        }
        goto label_0xC2D210;
        label_0xC2D134:
        ;
        x1 = 0x0UL;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D210;
        }
        else
        {
            goto label_0xC2D13C;
        }
        label_0xC2D13C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC2DCCCUL /* metadata target: GamepadManager.Gamepad.JoyState.ConnectToJoy */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC2D154;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2D15C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D150UL);
        }
        goto label_0xC2D210;
        label_0xC2D154:
        ;
        x1 = 0x0UL;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D210;
        }
        else
        {
            goto label_0xC2D15C;
        }
        label_0xC2D15C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC2DCCCUL /* metadata target: GamepadManager.Gamepad.JoyState.ConnectToJoy */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC2D174;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x48UL))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2D17C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D170UL);
        }
        goto label_0xC2D210;
        label_0xC2D174:
        ;
        x1 = 0x0UL;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D210;
        }
        else
        {
            goto label_0xC2D17C;
        }
        label_0xC2D17C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC2DCCCUL /* metadata target: GamepadManager.Gamepad.JoyState.ConnectToJoy */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2D210;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x0UL;
        goto label_0xC2D18C;
        label_0xC2D18C:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12767632 = unchecked((uint)(x21));
        __arm64_flags_right_12767632 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12767632) - (__arm64_flags_right_12767632))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12767632)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12767632)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12767632) - (__arm64_flags_right_12767632))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12767632)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2D214;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D198UL);
        }
        __arm64_flags_left_12767640 = unchecked((uint)(x21));
        __arm64_flags_right_12767640 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12767640 >= __arm64_flags_right_12767640))
        {
            goto label_0xC2D228;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC2D1C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC2DD88UL /* metadata target: GamepadProfile.GetKeySource */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x22 != 0x0UL))
        {
            goto label_0xC2D1C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D1BCUL);
        }
        goto label_0xC2D210;
        label_0xC2D1C0:
        ;
        x0 = 0x0UL;
        if ((x22 == 0x0UL))
        {
            goto label_0xC2D210;
        }
        else
        {
            goto label_0xC2D1C8;
        }
        label_0xC2D1C8:
        ;
        __arm64_flags_left_12767688 = x0;
        __arm64_flags_right_12767688 = 0x0UL;
        x8 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12767688) - (__arm64_flags_right_12767688))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL) | RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x28UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x22) + (0x40UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D1F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2D1E0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x0) + (0x10UL))))), 0));
        RuntimeCalls.Unsupported("rev64", 0xC2D1E4UL);
        RuntimeMemory.WriteF64(unchecked((ulong)((x22) + (0x40UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x18UL))))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x48UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2D1F4;
        label_0xC2D1F4:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x2CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x34UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x22) + (0x3BUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x8 != 0x0UL))
        {
            goto label_0xC2D18C;
        }
        else
        {
            goto label_0xC2D210;
        }
        label_0xC2D210:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2D214;
        label_0xC2D214:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC2DB9CUL /* metadata target: GamepadManager.Gamepad.Reset */);
        label_0xC2D228:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.IsSupported` — RVA `0xc2d22c`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public bool IsSupported() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_IsSupported_RVAc2d22c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12767792 = default(ulong);
        ulong __arm64_flags_right_12767792 = default(ulong);
        ulong x8 = default(ulong);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        __arm64_flags_left_12767792 = x8;
        __arm64_flags_right_12767792 = 0x0UL;
        x0 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12767792) - (__arm64_flags_right_12767792))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.AnyInternalKeyOrAxisPressed` — RVA `0xc2d23c`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public bool AnyInternalKeyOrAxisPressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint GamepadManager_Gamepad_AnyInternalKeyOrAxisPressed_RVAc2d23c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2E278UL /* metadata target: GamepadManager.Gamepad.AnyInternalKeyPressed */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2D258;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC2D258:
        ;
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E2E4UL /* metadata target: GamepadManager.Gamepad.AnyInternalAxisPressed */)));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.IsConnected` — RVA `0xc2da80`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsConnected() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_IsConnected_RVAc2da80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.IsActivated` — RVA `0xc2da88`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsActivated() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_IsActivated_RVAc2da88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetSlot` — RVA `0xc2da90`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public int GetSlot() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_GetSlot_RVAc2da90(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x34UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetInternalJoyName` — RVA `0xc2da98`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public string GetInternalJoyName() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetInternalJoyName_RVAc2da98(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetInternalJoyId` — RVA `0xc2daa0`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public int GetInternalJoyId() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_GetInternalJoyId_RVAc2daa0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x30UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetProfileName` — RVA `0xc2daa8`

- Lift status: **exact**; input span: 92 bytes; span to next metadata RVA: 92 bytes.
- Metadata signature: `public string GetProfileName() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetProfileName_RVAc2daa8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x118UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x118UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2DAD4:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            label_0xC2DAE4:
            ;
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
            x8 = RuntimeMemory.ReadU64(x8);
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        }
        else
        {
            x8 = unchecked((ulong)((x8) + (0x10UL)));
        }
        label_0xC2DAF4:
        ;
        x0 = RuntimeMemory.ReadU64(x8);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.Block` — RVA `0xc2db04`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void Block(bool block) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_Block_RVAc2db04(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x22UL))), unchecked((byte)(unchecked((uint)(x8)))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.IsBlocked` — RVA `0xc2db10`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsBlocked() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_IsBlocked_RVAc2db10(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x22UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.Reset` — RVA `0xc2db9c`

- Lift status: **partial**; input span: 296 bytes; span to next metadata RVA: 296 bytes.
- Metadata signature: `public void Reset() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.hs' at 0xc2dc04; reason: Unknown IR expression at 0xc2dc04; reason: Unsupported instruction 'b.hs' at 0xc2dc4c; reason: Unknown IR expression at 0xc2dc4c; reason: Unsupported instruction 'b.lt' at 0xc2dcb0; reason: Unknown IR expression at 0xc2dcb0

```csharp
public static ulong GamepadManager_Gamepad_Reset_RVAc2db9c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12770300 = default(uint);
        uint __arm64_flags_left_12770372 = default(uint);
        uint __arm64_flags_left_12770432 = default(uint);
        uint __arm64_flags_left_12770444 = default(uint);
        uint __arm64_flags_left_12770468 = default(uint);
        uint __arm64_flags_right_12770300 = default(uint);
        uint __arm64_flags_right_12770372 = default(uint);
        uint __arm64_flags_right_12770432 = default(uint);
        uint __arm64_flags_right_12770444 = default(uint);
        uint __arm64_flags_right_12770468 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC60B98UL /* metadata target: JoystickState.Reset */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC60B98UL /* metadata target: JoystickState.Reset */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC60B98UL /* metadata target: JoystickState.Reset */, x0, x1, x2, x3);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2DBF8;
        label_0xC2DBF8:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_12770300 = unchecked((uint)(x8));
        __arm64_flags_right_12770300 = unchecked((uint)(x10));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770300) - (__arm64_flags_right_12770300))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12770300)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12770300)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770300) - (__arm64_flags_right_12770300))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12770300)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2DC34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DC04UL);
        }
        RuntimeCalls.Unsupported("b.hs", 0xC2DC04UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2DCC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DC14UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x9) + (0x2CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x9) + (0x34UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x9) + (0x3BUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        if ((x9 != 0x0UL))
        {
            goto label_0xC2DBF8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DC30UL);
        }
        goto label_0xC2DCBC;
        label_0xC2DC34:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2DC40;
        label_0xC2DC40:
        ;
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_12770372 = unchecked((uint)(x8));
        __arm64_flags_right_12770372 = unchecked((uint)(x10));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770372) - (__arm64_flags_right_12770372))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12770372)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12770372)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770372) - (__arm64_flags_right_12770372))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12770372)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2DC74;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DC4CUL);
        }
        RuntimeCalls.Unsupported("b.hs", 0xC2DC4CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2DCC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DC5CUL);
        }
        RuntimeMemory.WriteU16(unchecked((ulong)((x9) + (0x20UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x9) + (0x18UL))), 0x0UL);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x58UL))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        if ((x9 != 0x0UL))
        {
            goto label_0xC2DC40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DC70UL);
        }
        goto label_0xC2DCBC;
        label_0xC2DC74:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12770432 = unchecked((uint)(x9));
        __arm64_flags_right_12770432 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770432) - (__arm64_flags_right_12770432))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12770432)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12770432)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770432) - (__arm64_flags_right_12770432))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12770432)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2DCB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2DC8C;
        label_0xC2DC8C:
        ;
        __arm64_flags_left_12770444 = unchecked((uint)(x10));
        __arm64_flags_right_12770444 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12770444 >= __arm64_flags_right_12770444))
        {
            goto label_0xC2DCC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x11) + (0x20UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC2DCBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12770468 = unchecked((uint)(x10));
        __arm64_flags_right_12770468 = unchecked((uint)(x9));
        RuntimeMemory.WriteU16(unchecked((ulong)((x11) + (0x14UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x11) + (0x16UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeCalls.Unsupported("b.lt", 0xC2DCB0UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2DC8C;
        }
        else
        {
            goto label_0xC2DCB4;
        }
        label_0xC2DCB4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC2DCBC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2DCC0;
        label_0xC2DCC0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetProfile` — RVA `0xc2dcc4`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public GamepadProfile GetProfile() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetProfile_RVAc2dcc4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetKey` — RVA `0xc2dea0`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public bool GetKey(GamepadManager.GamepadKey key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static uint GamepadManager_Gamepad_GetKey_RVAc2dea0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12770992 = default(uint);
        uint __arm64_flags_right_12770992 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DED0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12770992 = unchecked((uint)(x9));
        __arm64_flags_right_12770992 = unchecked((uint)(x1));
        if (((!((__arm64_flags_left_12770992 >= __arm64_flags_right_12770992))) || (unchecked((uint)((__arm64_flags_left_12770992) - (__arm64_flags_right_12770992))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2DED4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DED0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3DUL))))))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2DED0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2DED4;
        label_0xC2DED4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetKeyDown` — RVA `0xc2ded8`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public bool GetKeyDown(GamepadManager.GamepadKey key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static uint GamepadManager_Gamepad_GetKeyDown_RVAc2ded8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771048 = default(uint);
        uint __arm64_flags_left_12771080 = default(uint);
        uint __arm64_flags_right_12771048 = default(uint);
        uint __arm64_flags_right_12771080 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DF20;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771048 = unchecked((uint)(x9));
        __arm64_flags_right_12771048 = unchecked((uint)(x1));
        if (((!((__arm64_flags_left_12771048 >= __arm64_flags_right_12771048))) || (unchecked((uint)((__arm64_flags_left_12771048) - (__arm64_flags_right_12771048))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2DF24;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DF20;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3DUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2DF14;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3EUL))))))));
        __arm64_flags_left_12771080 = unchecked((uint)(x8));
        __arm64_flags_right_12771080 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12771080) - (__arm64_flags_right_12771080))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC2DF18;
        label_0xC2DF14:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2DF18;
        label_0xC2DF18:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2DF20:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2DF24;
        label_0xC2DF24:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetKeyUp` — RVA `0xc2df48`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public bool GetKeyUp(GamepadManager.GamepadKey key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static uint GamepadManager_Gamepad_GetKeyUp_RVAc2df48(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771160 = default(uint);
        uint __arm64_flags_left_12771200 = default(uint);
        uint __arm64_flags_right_12771160 = default(uint);
        uint __arm64_flags_right_12771200 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DF90;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771160 = unchecked((uint)(x9));
        __arm64_flags_right_12771160 = unchecked((uint)(x1));
        if (((!((__arm64_flags_left_12771160 >= __arm64_flags_right_12771160))) || (unchecked((uint)((__arm64_flags_left_12771160) - (__arm64_flags_right_12771160))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2DF94;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DF90;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3DUL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2DF7C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2DF88;
        label_0xC2DF7C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x3EUL))))))));
        __arm64_flags_left_12771200 = unchecked((uint)(x8));
        __arm64_flags_right_12771200 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12771200) - (__arm64_flags_right_12771200))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC2DF88;
        label_0xC2DF88:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2DF90:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2DF94;
        label_0xC2DF94:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetKeyAnalog` — RVA `0xc2dfb8`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public float GetKeyAnalog(GamepadManager.GamepadKey key) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetKeyAnalog_RVAc2dfb8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771272 = default(uint);
        uint __arm64_flags_right_12771272 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x50UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DFE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771272 = unchecked((uint)(x9));
        __arm64_flags_right_12771272 = unchecked((uint)(x1));
        if (((!((__arm64_flags_left_12771272 >= __arm64_flags_right_12771272))) || (unchecked((uint)((__arm64_flags_left_12771272) - (__arm64_flags_right_12771272))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC2DFEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DFE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DFDCUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x34UL))))), 0));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2DFE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2DFEC;
        label_0xC2DFEC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetStickVec` — RVA `0xc2dff0`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public Vector2 GetStickVec(GamepadManager.GamepadStick s) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetStickVec_RVAc2dff0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12771324 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC2E00CUL /* metadata target: GamepadManager.Gamepad.GetStick */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            label_0xC2E008:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        }
        else
        {
            __arm64_pair_address_12771324 = unchecked((ulong)((x0) + (0x24UL)));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12771324)), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12771324) + (0x4UL))))), 0));
            x30 = RuntimeMemory.ReadU64(sp);
            return x0;
        }
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetStick` — RVA `0xc2e00c`

- Lift status: **exact**; input span: 60 bytes; span to next metadata RVA: 60 bytes.
- Metadata signature: `public JoystickState GetStick(GamepadManager.GamepadStick s) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetStick_RVAc2e00c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771344 = default(uint);
        uint __arm64_flags_right_12771344 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        __arm64_flags_left_12771344 = unchecked((uint)(x1));
        __arm64_flags_right_12771344 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12771344) - (__arm64_flags_right_12771344))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E028;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E018UL);
        }
        if ((unchecked((uint)(x1)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E03C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC2E030;
        }
        else
        {
            goto label_0xC2E024;
        }
        label_0xC2E024:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2E028;
        label_0xC2E028:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E024;
        }
        else
        {
            goto label_0xC2E030;
        }
        label_0xC2E030:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2E03C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC2E030;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E044UL);
        }
        goto label_0xC2E024;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetStickDir8` — RVA `0xc2e048`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public Dir GetStickDir8(GamepadManager.GamepadStick s) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetStickDir8_RVAc2e048(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC2E00CUL /* metadata target: GamepadManager.Gamepad.GetStick */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E060;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC60D84UL /* metadata target: JoystickState.GetDir8 */);
        label_0xC2E060:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetStickDir4` — RVA `0xc2e064`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public Dir GetStickDir4(GamepadManager.GamepadStick s) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetStickDir4_RVAc2e064(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC2E00CUL /* metadata target: GamepadManager.Gamepad.GetStick */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E07C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC60D68UL /* metadata target: JoystickState.GetDir4 */);
        label_0xC2E07C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetStickDir` — RVA `0xc2e080`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public Dir GetStickDir(GamepadManager.GamepadStick s) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_GetStickDir_RVAc2e080(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC2E00CUL /* metadata target: GamepadManager.Gamepad.GetStick */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E098;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC60D4CUL /* metadata target: JoystickState.GetDir */);
        label_0xC2E098:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetInternalKeyState` — RVA `0xc2e09c`

- Lift status: **partial**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public bool GetInternalKeyState(int keyId) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=8 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ls' at 0xc2e0b8; reason: Unknown IR expression at 0xc2e0b8

```csharp
public static uint GamepadManager_Gamepad_GetInternalKeyState_RVAc2e09c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771504 = default(uint);
        uint __arm64_flags_left_12771540 = default(uint);
        uint __arm64_flags_right_12771504 = default(uint);
        uint __arm64_flags_right_12771540 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E0E0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E0EC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771504 = unchecked((uint)(x9));
        __arm64_flags_right_12771504 = unchecked((uint)(x1));
        if (((unchecked((uint)((__arm64_flags_left_12771504) - (__arm64_flags_right_12771504))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771504) - (__arm64_flags_right_12771504))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12771504)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12771504)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771504) - (__arm64_flags_right_12771504))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12771504)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2E0E0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E0B8UL)));
        }
        RuntimeCalls.Unsupported("b.ls", 0xC2E0B8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2E0F0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E0EC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x16UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E0E0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x14UL))))))));
        __arm64_flags_left_12771540 = unchecked((uint)(x8));
        __arm64_flags_right_12771540 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12771540) - (__arm64_flags_right_12771540))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC2E0E4;
        label_0xC2E0E0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E0E4;
        label_0xC2E0E4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2E0EC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2E0F0;
        label_0xC2E0F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetInternalAxisAnalog` — RVA `0xc2e114`

- Lift status: **partial**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `public float GetInternalAxisAnalog(int axisId) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=6 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ls' at 0xc2e134; reason: Unknown IR expression at 0xc2e134

```csharp
public static ulong GamepadManager_Gamepad_GetInternalAxisAnalog_RVAc2e114(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771628 = default(uint);
        uint __arm64_flags_right_12771628 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E158;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771628 = unchecked((uint)(x9));
        __arm64_flags_right_12771628 = unchecked((uint)(x1));
        if (((unchecked((uint)((__arm64_flags_left_12771628) - (__arm64_flags_right_12771628))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771628) - (__arm64_flags_right_12771628))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12771628)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12771628)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771628) - (__arm64_flags_right_12771628))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12771628)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2E150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E134UL);
        }
        RuntimeCalls.Unsupported("b.ls", 0xC2E134UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2E15C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E158;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x20UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E150;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E14CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x18UL))))), 0));
        goto label_0xC2E150;
        label_0xC2E150:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2E158:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2E15C;
        label_0xC2E15C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.GetInternalAxisDigital` — RVA `0xc2e178`

- Lift status: **partial**; input span: 116 bytes; span to next metadata RVA: 116 bytes.
- Metadata signature: `public int GetInternalAxisDigital(int axisId) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=9 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ls' at 0xc2e194; reason: Unknown IR expression at 0xc2e194

```csharp
public static uint GamepadManager_Gamepad_GetInternalAxisDigital_RVAc2e178(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771724 = default(uint);
        uint __arm64_flags_right_12771724 = default(uint);
        float __arm64_float_flags_left_12771768 = default(float);
        float __arm64_float_flags_left_12771776 = default(float);
        float __arm64_float_flags_right_12771768 = default(float);
        float __arm64_float_flags_right_12771776 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E1D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E1E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771724 = unchecked((uint)(x9));
        __arm64_flags_right_12771724 = unchecked((uint)(x1));
        if (((unchecked((uint)((__arm64_flags_left_12771724) - (__arm64_flags_right_12771724))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771724) - (__arm64_flags_right_12771724))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12771724)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12771724)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771724) - (__arm64_flags_right_12771724))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12771724)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2E1D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E194UL)));
        }
        RuntimeCalls.Unsupported("b.ls", 0xC2E194UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2E1E8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E1E4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x20UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E1D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E1ACUL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x18UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12771768 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12771768 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12771768 <= __arm64_float_flags_right_12771768) || ((__arm64_float_flags_left_12771768 != __arm64_float_flags_left_12771768) || (__arm64_float_flags_right_12771768 != __arm64_float_flags_right_12771768))))
        {
            goto label_0xC2E1D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E1C0UL)));
        }
        __arm64_float_flags_left_12771776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12771776 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if (((__arm64_float_flags_left_12771776 <= __arm64_float_flags_right_12771776) || ((__arm64_float_flags_left_12771776 != __arm64_float_flags_left_12771776) || (__arm64_float_flags_right_12771776 != __arm64_float_flags_right_12771776))))
        {
            goto label_0xC2E1DC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2E1D4;
        label_0xC2E1D0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E1D4;
        label_0xC2E1D4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2E1DC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        goto label_0xC2E1D4;
        label_0xC2E1E4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2E1E8;
        label_0xC2E1E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.IsInternalAxisFullyAnalog` — RVA `0xc2e228`

- Lift status: **partial**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public bool IsInternalAxisFullyAnalog(int axisId) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=7 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ls' at 0xc2e244; reason: Unknown IR expression at 0xc2e244

```csharp
public static uint GamepadManager_Gamepad_IsInternalAxisFullyAnalog_RVAc2e228(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771900 = default(uint);
        uint __arm64_flags_left_12771928 = default(uint);
        uint __arm64_flags_right_12771900 = default(uint);
        uint __arm64_flags_right_12771928 = default(uint);
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E264;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E270;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771900 = unchecked((uint)(x9));
        __arm64_flags_right_12771900 = unchecked((uint)(x1));
        if (((unchecked((uint)((__arm64_flags_left_12771900) - (__arm64_flags_right_12771900))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771900) - (__arm64_flags_right_12771900))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12771900)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12771900)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771900) - (__arm64_flags_right_12771900))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12771900)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2E264;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E244UL)));
        }
        RuntimeCalls.Unsupported("b.ls", 0xC2E244UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2E274;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E270;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x21UL))))))));
        __arm64_flags_left_12771928 = unchecked((uint)(x8));
        __arm64_flags_right_12771928 = unchecked((uint)0x0UL);
        x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12771928) - (__arm64_flags_right_12771928))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC2E268;
        label_0xC2E264:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E268;
        label_0xC2E268:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2E270:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2E274;
        label_0xC2E274:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.AnyInternalKeyPressed` — RVA `0xc2e278`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public bool AnyInternalKeyPressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static uint GamepadManager_Gamepad_AnyInternalKeyPressed_RVAc2e278(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771976 = default(uint);
        uint __arm64_flags_left_12771984 = default(uint);
        uint __arm64_flags_left_12771996 = default(uint);
        uint __arm64_flags_left_12772036 = default(uint);
        uint __arm64_flags_right_12771976 = default(uint);
        uint __arm64_flags_right_12771984 = default(uint);
        uint __arm64_flags_right_12771996 = default(uint);
        uint __arm64_flags_right_12772036 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E2E0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12771976 = unchecked((uint)(x9));
        __arm64_flags_right_12771976 = unchecked((uint)0x0UL);
        x10 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_12771976) - (__arm64_flags_right_12771976))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771976) - (__arm64_flags_right_12771976))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12771976)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12771976)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771976) - (__arm64_flags_right_12771976))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12771976)) < unchecked((int)0x0UL)))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12771984 = unchecked((uint)(x9));
        __arm64_flags_right_12771984 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771984) - (__arm64_flags_right_12771984))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12771984)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12771984)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12771984) - (__arm64_flags_right_12771984))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12771984)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2E2D0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x11 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E29C;
        label_0xC2E29C:
        ;
        __arm64_flags_left_12771996 = unchecked((uint)(x11));
        __arm64_flags_right_12771996 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12771996 >= __arm64_flags_right_12771996))
        {
            goto label_0xC2E2DC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x12 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x12) + (0x20UL))));
        if ((x12 == 0x0UL))
        {
            goto label_0xC2E2E0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x13 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x12) + (0x16UL))))))));
        if ((unchecked((uint)(x13)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E2C0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x12 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x12) + (0x14UL))))))));
        if ((unchecked((uint)(x12)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E2D0;
        }
        else
        {
            goto label_0xC2E2C0;
        }
        label_0xC2E2C0:
        ;
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12772036 = unchecked((uint)(x11));
        __arm64_flags_right_12772036 = unchecked((uint)(x9));
        x10 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772036) - (__arm64_flags_right_12772036))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772036)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772036)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772036) - (__arm64_flags_right_12772036))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772036)) < unchecked((int)0x0UL))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772036) - (__arm64_flags_right_12772036))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772036)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772036)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772036) - (__arm64_flags_right_12772036))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772036)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2E29C;
        }
        else
        {
            goto label_0xC2E2D0;
        }
        label_0xC2E2D0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)(0x1UL)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2E2DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2E2E0;
        label_0xC2E2E0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.AnyInternalAxisPressed` — RVA `0xc2e2e4`

- Lift status: **exact**; input span: 120 bytes; span to next metadata RVA: 120 bytes.
- Metadata signature: `public bool AnyInternalAxisPressed() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=9 (informational only).

```csharp
public static uint GamepadManager_Gamepad_AnyInternalAxisPressed_RVAc2e2e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12772084 = default(uint);
        uint __arm64_flags_left_12772092 = default(uint);
        uint __arm64_flags_left_12772108 = default(uint);
        uint __arm64_flags_left_12772156 = default(uint);
        uint __arm64_flags_right_12772084 = default(uint);
        uint __arm64_flags_right_12772092 = default(uint);
        uint __arm64_flags_right_12772108 = default(uint);
        uint __arm64_flags_right_12772156 = default(uint);
        float __arm64_float_flags_left_12772144 = default(float);
        float __arm64_float_flags_right_12772144 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x13 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E358;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12772084 = unchecked((uint)(x9));
        __arm64_flags_right_12772084 = unchecked((uint)0x0UL);
        x10 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_12772084) - (__arm64_flags_right_12772084))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772084) - (__arm64_flags_right_12772084))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12772084)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772084)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772084) - (__arm64_flags_right_12772084))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772084)) < unchecked((int)0x0UL)))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        __arm64_flags_left_12772092 = unchecked((uint)(x9));
        __arm64_flags_right_12772092 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772092) - (__arm64_flags_right_12772092))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772092)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772092)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772092) - (__arm64_flags_right_12772092))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772092)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2E348;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x11 = unchecked((ulong)(unchecked((uint)0x0UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        goto label_0xC2E30C;
        label_0xC2E30C:
        ;
        __arm64_flags_left_12772108 = unchecked((uint)(x11));
        __arm64_flags_right_12772108 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12772108 >= __arm64_flags_right_12772108))
        {
            goto label_0xC2E354;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x12 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x12 = RuntimeMemory.ReadU64(unchecked((ulong)((x12) + (0x20UL))));
        if ((x12 == 0x0UL))
        {
            goto label_0xC2E358;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x13 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x12) + (0x20UL))))))));
        if ((unchecked((uint)(x13)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E338;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E328UL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x12) + (0x18UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12772144 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12772144 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12772144 > __arm64_float_flags_right_12772144))
        {
            goto label_0xC2E348;
        }
        else
        {
            goto label_0xC2E338;
        }
        label_0xC2E338:
        ;
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12772156 = unchecked((uint)(x11));
        __arm64_flags_right_12772156 = unchecked((uint)(x9));
        x10 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772156) - (__arm64_flags_right_12772156))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772156)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772156)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772156) - (__arm64_flags_right_12772156))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772156)) < unchecked((int)0x0UL))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772156) - (__arm64_flags_right_12772156))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772156)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772156)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772156) - (__arm64_flags_right_12772156))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772156)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2E30C;
        }
        else
        {
            goto label_0xC2E348;
        }
        label_0xC2E348:
        ;
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)(0x1UL)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2E354:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        goto label_0xC2E358;
        label_0xC2E358:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetPressedInternalKey` — RVA `0xc2e35c`

- Lift status: **partial**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public int GetPressedInternalKey(int start = 0) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=12 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.lt' at 0xc2e3a8; reason: Unknown IR expression at 0xc2e3a8

```csharp
public static uint GamepadManager_Gamepad_GetPressedInternalKey_RVAc2e35c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12772204 = default(uint);
        uint __arm64_flags_left_12772220 = default(uint);
        uint __arm64_flags_left_12772256 = default(uint);
        uint __arm64_flags_right_12772204 = default(uint);
        uint __arm64_flags_right_12772220 = default(uint);
        uint __arm64_flags_right_12772256 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2E3C0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_12772204 = unchecked((uint)(x8));
        __arm64_flags_right_12772204 = unchecked((uint)(x1));
        if (((unchecked((uint)((__arm64_flags_left_12772204) - (__arm64_flags_right_12772204))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772204) - (__arm64_flags_right_12772204))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772204)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772204)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772204) - (__arm64_flags_right_12772204))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772204)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2E3AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x9 = unchecked((ulong)((x9) + (0x20UL)));
        goto label_0xC2E37C;
        label_0xC2E37C:
        ;
        __arm64_flags_left_12772220 = unchecked((uint)(x1));
        __arm64_flags_right_12772220 = unchecked((uint)(x8));
        if ((__arm64_flags_left_12772220 >= __arm64_flags_right_12772220))
        {
            goto label_0xC2E3BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = RuntimeMemory.ReadU64(x9);
        if ((x10 == 0x0UL))
        {
            goto label_0xC2E3C0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x16UL))))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E39C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x14UL))))))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E3B0;
        }
        else
        {
            goto label_0xC2E39C;
        }
        label_0xC2E39C:
        ;
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x1))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12772256 = unchecked((uint)(x1));
        __arm64_flags_right_12772256 = unchecked((uint)(x8));
        x9 = unchecked((ulong)((x9) + (0x8UL)));
        RuntimeCalls.Unsupported("b.lt", 0xC2E3A8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2E37C;
        }
        else
        {
            goto label_0xC2E3AC;
        }
        label_0xC2E3AC:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        goto label_0xC2E3B0;
        label_0xC2E3B0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x1))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2E3BC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2E3C0;
        label_0xC2E3C0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.GetPressedInternalAxis` — RVA `0xc2e3c4`

- Lift status: **exact**; input span: 128 bytes; span to next metadata RVA: 128 bytes.
- Metadata signature: `public int GetPressedInternalAxis(out bool positiveSide, int start = 0) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static uint GamepadManager_Gamepad_GetPressedInternalAxis_RVAc2e3c4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12772308 = default(uint);
        uint __arm64_flags_left_12772320 = default(uint);
        uint __arm64_flags_left_12772368 = default(uint);
        uint __arm64_flags_right_12772308 = default(uint);
        uint __arm64_flags_right_12772320 = default(uint);
        uint __arm64_flags_right_12772368 = default(uint);
        float __arm64_float_flags_left_12772356 = default(float);
        float __arm64_float_flags_left_12772400 = default(float);
        float __arm64_float_flags_right_12772356 = default(float);
        float __arm64_float_flags_right_12772400 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2E440;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12772308 = unchecked((uint)(x9));
        __arm64_flags_right_12772308 = unchecked((uint)(x2));
        if (((unchecked((uint)((__arm64_flags_left_12772308) - (__arm64_flags_right_12772308))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772308) - (__arm64_flags_right_12772308))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772308)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772308)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772308) - (__arm64_flags_right_12772308))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772308)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2E418;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E3DCUL)));
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        goto label_0xC2E3E0;
        label_0xC2E3E0:
        ;
        __arm64_flags_left_12772320 = unchecked((uint)(x2));
        __arm64_flags_right_12772320 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12772320 >= __arm64_flags_right_12772320))
        {
            goto label_0xC2E43C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x10) + (0x20UL))));
        if ((x10 == 0x0UL))
        {
            goto label_0xC2E440;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x20UL))))))));
        if ((unchecked((uint)(x11)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E40C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E3FCUL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x10) + (0x18UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0)), 0)) & (unchecked((uint)0x7FFFFFFFUL))))), 0)), 0));
        __arm64_float_flags_left_12772356 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12772356 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12772356 > __arm64_float_flags_right_12772356))
        {
            goto label_0xC2E430;
        }
        else
        {
            goto label_0xC2E40C;
        }
        label_0xC2E40C:
        ;
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12772368 = unchecked((uint)(x2));
        __arm64_flags_right_12772368 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772368) - (__arm64_flags_right_12772368))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12772368)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12772368)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12772368) - (__arm64_flags_right_12772368))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12772368)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2E3E0;
        }
        else
        {
            goto label_0xC2E418;
        }
        label_0xC2E418:
        ;
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        goto label_0xC2E420;
        label_0xC2E420:
        ;
        RuntimeMemory.WriteU8(x1, unchecked((byte)(unchecked((uint)(x8)))));
        x0 = unchecked((ulong)(unchecked((uint)(x2))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC2E430:
        ;
        __arm64_float_flags_left_12772400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12772400 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        x8 = unchecked((ulong)(((__arm64_float_flags_left_12772400 > __arm64_float_flags_right_12772400) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC2E420;
        label_0xC2E43C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2E440;
        label_0xC2E440:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```
