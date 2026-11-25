# `GamepadManager.Gamepad.JoyState` — TypeDefIndex 4955

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `GamepadManager.Gamepad` | `gamepad` |
| `0x18` | `JoystickState` | `state` |
| `0x20` | `bool` | `isConnectedToHardware` |
| `0x24` | `int` | `srcAxisIdL` |
| `0x28` | `int` | `srcAxisIdR` |
| `0x2C` | `int` | `srcAxisIdU` |
| `0x30` | `int` | `srcAxisIdD` |
| `0x34` | `bool` | `srcAxisFlipL` |
| `0x35` | `bool` | `srcAxisFlipR` |
| `0x36` | `bool` | `srcAxisFlipU` |
| `0x37` | `bool` | `srcAxisFlipD` |
| `0x38` | `int` | `srcKeyU` |
| `0x3C` | `int` | `srcKeyR` |
| `0x40` | `int` | `srcKeyD` |
| `0x44` | `int` | `srcKeyL` |

## `GamepadManager.Gamepad.JoyState.ctor` — RVA `0xc2d97c`

- Lift status: **exact**; input span: 152 bytes; span to next metadata RVA: 152 bytes.
- Metadata signature: `public void .ctor(GamepadManager.Gamepad gamepad, JoystickConfig config) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_ctor_RVAc2d97c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x11BUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x130UL))));
        x20 = x2;
        x21 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x130UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x11BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2D9BC:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC60AC0UL /* metadata target: JoystickState.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x21);
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.JoyState.SetConfig` — RVA `0xc2db18`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void SetConfig(JoystickConfig config) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_SetConfig_RVAc2db18(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2DB30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2DB24UL);
        }
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC2DB30:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.JoyState.ConnectToJoy` — RVA `0xc2dccc`

- Lift status: **exact**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public void ConnectToJoy(GamepadProfile.JoystickSource joySrc) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_ConnectToJoy_RVAc2dccc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12770512 = default(ulong);
        ulong __arm64_flags_right_12770512 = default(ulong);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x12 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        __arm64_flags_left_12770512 = x1;
        __arm64_flags_right_12770512 = 0x0UL;
        x8 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12770512) - (__arm64_flags_right_12770512))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC2DD70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2DD84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x24UL))), unchecked((uint)(x9)));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x18UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) ^ (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x34UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x20UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC2DD84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x14UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x28UL))), unchecked((uint)(x10)));
        x10 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (0x18UL))))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) ^ (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x35UL))), unchecked((byte)(unchecked((uint)(x10)))));
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x10UL))));
        if ((x10 == 0x0UL))
        {
            goto label_0xC2DD84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x14UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x2CUL))), unchecked((uint)(x11)));
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x10) + (0x18UL))))))));
        x11 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) ^ (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x36UL))), unchecked((byte)(unchecked((uint)(x11)))));
        x11 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x18UL))));
        if ((x11 == 0x0UL))
        {
            goto label_0xC2DD84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x12 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x11) + (0x14UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x30UL))), unchecked((uint)(x12)));
        x12 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x11) + (0x18UL))))))));
        x12 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x12))) ^ (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x37UL))), unchecked((byte)(unchecked((uint)(x12)))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x10UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x44UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x10UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x3CUL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x10UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x38UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x11) + (0x10UL))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x40UL))), unchecked((uint)(x8)));
        goto label_0xC2DD70;
        label_0xC2DD70:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2DD84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC60B98UL /* metadata target: JoystickState.Reset */);
        label_0xC2DD84:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.JoyState.Reset` — RVA `0xc2de58`

- Lift status: **exact**; input span: 28 bytes; span to next metadata RVA: 28 bytes.
- Metadata signature: `public void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_Reset_RVAc2de58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2DE70;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC60B98UL /* metadata target: JoystickState.Reset */);
        label_0xC2DE70:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.JoyState.Update` — RVA `0xc2e4cc`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_Update_RVAc2e4cc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2E5E8UL /* metadata target: GamepadManager.Gamepad.JoyState.ReadHardwareState */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E4EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC610C4UL /* metadata target: JoystickState.Update */);
        label_0xC2E4EC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.JoyState.ReadHardwareState` — RVA `0xc2e5e8`

- Lift status: **exact**; input span: 336 bytes; span to next metadata RVA: 336 bytes.
- Metadata signature: `private void ReadHardwareState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=50 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_ReadHardwareState_RVAc2e5e8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_pair_address_12772840 = default(ulong);
        ulong __arm64_pair_address_12772988 = default(ulong);
        ulong __arm64_pair_address_12773164 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        __arm64_pair_address_12772840 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12772840, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12772840) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = __arm64_pair_address_12772840;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E670;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1E0UL))))))));
        x19 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E624;
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
        goto label_0xC2E624;
        label_0xC2E624:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x35UL))))))));
        x3 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x24UL))))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x19) + (0x24UL)))) + (0x4UL))))));
        x4 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x34UL))))))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2E738UL /* metadata target: GamepadManager.Gamepad.JoyState.GetCompositeAnalogVal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x36UL))))))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x2CUL))))));
        x3 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x19) + (0x2CUL)))) + (0x4UL))))));
        x4 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x37UL))))))));
        x0 = x19;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0xC2E738UL /* metadata target: GamepadManager.Gamepad.JoyState.GetCompositeAnalogVal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x38UL))))));
        v9 = v0;
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E684;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E664UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E09CUL /* metadata target: GamepadManager.Gamepad.GetInternalKeyState */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        goto label_0xC2E688;
        label_0xC2E670:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_pair_address_12772988 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12772988)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12772988) + (0x8UL))))), 0));
        return x0;
        label_0xC2E684:
        ;
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E688;
        label_0xC2E688:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x40UL))))));
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E6A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E698UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E09CUL /* metadata target: GamepadManager.Gamepad.GetInternalKeyState */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x21 = unchecked((ulong)(unchecked((uint)(x0))));
        goto label_0xC2E6A8;
        label_0xC2E6A4:
        ;
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E6A8;
        label_0xC2E6A8:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x3CUL))))));
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E6C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E6B8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E09CUL /* metadata target: GamepadManager.Gamepad.GetInternalKeyState */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        goto label_0xC2E6C8;
        label_0xC2E6C4:
        ;
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E6C8;
        label_0xC2E6C8:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x44UL))))));
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E6E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E6D8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E09CUL /* metadata target: GamepadManager.Gamepad.GetInternalKeyState */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        x23 = unchecked((ulong)(unchecked((uint)(x0))));
        goto label_0xC2E6E8;
        label_0xC2E6E4:
        ;
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E6E8;
        label_0xC2E6E8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v0 = v8;
        v1 = v9;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC60EC4UL /* metadata target: JoystickState.ApplyClampedVec */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E734;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
        x2 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)(0x1UL)))))));
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)(0x1UL)))))));
        x4 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)(0x1UL)))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x5 = 0x0UL;
        __arm64_pair_address_12773164 = sp;
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12773164)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12773164) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_12773164) + (0x40UL)));
        return RuntimeCalls.InvokeDirect(0xC61020UL /* metadata target: JoystickState.ApplyDigital */);
        label_0xC2E734:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.JoyState.GetCompositeAnalogVal` — RVA `0xc2e738`

- Lift status: **exact**; input span: 172 bytes; span to next metadata RVA: 172 bytes.
- Metadata signature: `private float GetCompositeAnalogVal(int posAxisId, bool posFlip, int negAxisId, bool negFlip) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_GetCompositeAnalogVal_RVAc2e738(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12773228 = default(uint);
        uint __arm64_flags_left_12773240 = default(uint);
        uint __arm64_flags_result_12773228 = default(uint);
        uint __arm64_flags_right_12773228 = default(uint);
        uint __arm64_flags_right_12773240 = default(uint);
        ulong __arm64_load_address_12773336 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x21 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E7E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = unchecked((ulong)(unchecked((uint)(x4))));
        x20 = unchecked((ulong)(unchecked((uint)(x3))));
        x23 = unchecked((ulong)(unchecked((uint)(x2))));
        x22 = unchecked((ulong)(unchecked((uint)(x1))));
        x0 = RuntimeCalls.InvokeDirect(0xC2E114UL /* metadata target: GamepadManager.Gamepad.GetInternalAxisAnalog */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_flags_left_12773228 = unchecked((uint)(x23));
        __arm64_flags_right_12773228 = unchecked((uint)0x1UL);
        __arm64_flags_result_12773228 = unchecked((uint)((__arm64_flags_left_12773228) & (__arm64_flags_right_12773228)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((!((__arm64_flags_result_12773228 == unchecked((uint)0x0UL)))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        if ((unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E788;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E778UL);
        }
        __arm64_flags_left_12773240 = unchecked((uint)(x22));
        __arm64_flags_right_12773240 = unchecked((uint)(x20));
        if ((!((unchecked((uint)((__arm64_flags_left_12773240) - (__arm64_flags_right_12773240))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC2E788;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E784UL);
        }
        goto label_0xC2E7CC;
        label_0xC2E788:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E7E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0xC2E114UL /* metadata target: GamepadManager.Gamepad.GetInternalAxisAnalog */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2E7CC;
        label_0xC2E7CC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12773336 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12773336)), 0));
        return x0;
        label_0xC2E7E0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.JoyState.SyncJoyState` — RVA `0xc2e7e4`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public void SyncJoyState(JoystickStateBinding bind, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_JoyState_SyncJoyState_RVAc2e7e4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        if ((x1 == 0x0UL))
        {
            goto label_0xC2E804;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        x0 = x1;
        x3 = 0x0UL;
        x1 = x8;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC5DFFCUL /* metadata target: JoystickStateBinding.SyncJoyState */);
        label_0xC2E804:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
