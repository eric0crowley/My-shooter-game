# `GamepadManager.Gamepad.KeyState` — TypeDefIndex 4956

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `GamepadManager.Gamepad` | `gamepad` |
| `0x18` | `bool` | `isTrigger` |
| `0x20` | `AnalogConfig` | `analogConfig` |
| `0x28` | `bool` | `isConnectedToHardware` |
| `0x2C` | `float` | `frAnalog` |
| `0x30` | `bool` | `frDigital` |
| `0x34` | `float` | `analogCur` |
| `0x38` | `float` | `analogRawCur` |
| `0x3C` | `bool` | `digiCurRaw` |
| `0x3D` | `bool` | `digiCur` |
| `0x3E` | `bool` | `digiPrev` |
| `0x40` | `int` | `srcAxisId` |
| `0x44` | `int` | `srcKeyId` |
| `0x48` | `bool` | `srcAxisSign` |

## `GamepadManager.Gamepad.KeyState.ctor` — RVA `0xc2da14`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `public void .ctor(GamepadManager.Gamepad gamepad, bool isTrigger, AnalogConfig analogConfig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_ctor_RVAc2da14(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x20 = x1;
        x1 = 0x0UL;
        x19 = x3;
        x21 = x0;
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x20UL))), x19);
        x0 = x21;
        x1 = x19;
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((byte)(unchecked((uint)(x22)))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x8UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x10UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x14UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x1BUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.ConnectToJoy` — RVA `0xc2de18`

- Lift status: **partial**; input span: 64 bytes; span to next metadata RVA: 64 bytes.
- Metadata signature: `public void ConnectToJoy(GamepadProfile.KeySource src) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'rev64' at 0xc2de34

```csharp
public static ulong GamepadManager_Gamepad_KeyState_ConnectToJoy_RVAc2de18(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12770840 = default(ulong);
        ulong __arm64_flags_right_12770840 = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        __arm64_flags_left_12770840 = x1;
        __arm64_flags_right_12770840 = 0x0UL;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL) | RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x8 = unchecked((ulong)(((!((unchecked((ulong)((__arm64_flags_left_12770840) - (__arm64_flags_right_12770840))) == 0x0UL))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x28UL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x40UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        if ((x1 == 0x0UL))
        {
        }
        else
        {
            v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x1) + (0x10UL))))), 0));
            RuntimeCalls.Unsupported("rev64", 0xC2DE34UL);
            RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x40UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x1) + (0x18UL))))))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x48UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2DE44:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x2CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x34UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x3BUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.Reset` — RVA `0xc2de74`

- Lift status: **exact**; input span: 20 bytes; span to next metadata RVA: 20 bytes.
- Metadata signature: `public void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_Reset_RVAc2de74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x2CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x34UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x0) + (0x3BUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.GetDigitalDown` — RVA `0xc2df28`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool GetDigitalDown() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint GamepadManager_Gamepad_KeyState_GetDigitalDown_RVAc2df28(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771124 = default(uint);
        uint __arm64_flags_right_12771124 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x3DUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC2DF40:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x3EUL))))))));
            __arm64_flags_left_12771124 = unchecked((uint)(x8));
            __arm64_flags_right_12771124 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((unchecked((uint)((__arm64_flags_left_12771124) - (__arm64_flags_right_12771124))) == unchecked((uint)0x0UL)) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `GamepadManager.Gamepad.KeyState.GetDigitalUp` — RVA `0xc2df98`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool GetDigitalUp() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint GamepadManager_Gamepad_KeyState_GetDigitalUp_RVAc2df98(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771244 = default(uint);
        uint __arm64_flags_right_12771244 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x3DUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC2DFA8:
            ;
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x0))))) + (0x3EUL))))))));
            __arm64_flags_left_12771244 = unchecked((uint)(x8));
            __arm64_flags_right_12771244 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12771244) - (__arm64_flags_right_12771244))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
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

## `GamepadManager.Gamepad.KeyState.Update` — RVA `0xc2e4f0`

- Lift status: **partial**; input span: 192 bytes; span to next metadata RVA: 192 bytes.
- Metadata signature: `public void Update() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=13 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc2e514; reason: Unknown IR expression at 0xc2e514

```csharp
public static uint GamepadManager_Gamepad_KeyState_Update_RVAc2e4f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12772620 = default(uint);
        uint __arm64_flags_left_12772652 = default(uint);
        uint __arm64_flags_left_12772712 = default(uint);
        uint __arm64_flags_right_12772620 = default(uint);
        uint __arm64_flags_right_12772652 = default(uint);
        uint __arm64_flags_right_12772712 = default(uint);
        float __arm64_float_flags_left_12772764 = default(float);
        float __arm64_float_flags_right_12772764 = default(float);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2E838UL /* metadata target: GamepadManager.Gamepad.KeyState.ReadHardwareState */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x30UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x3DUL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x2CUL))))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        __arm64_flags_left_12772620 = unchecked((uint)(x8));
        __arm64_flags_right_12772620 = unchecked((uint)0x0UL);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x3EUL))), unchecked((byte)(unchecked((uint)(x9)))));
        RuntimeCalls.Unsupported("csel", 0xC2E514UL);
        x9 = (__Unsupported<bool>("Unknown IR expression") ? x19 : 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x2CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x3CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E568;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E52CUL)));
        }
        __arm64_flags_left_12772652 = unchecked((uint)(x8));
        __arm64_flags_right_12772652 = unchecked((uint)0x0UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12772652) - (__arm64_flags_right_12772652))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC574F8UL /* metadata target: AnalogConfig.GetAnalogVal */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x3CUL))))))));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x34UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E580;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E5AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x3EUL))))))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x38UL))))), 0));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC5AD10UL /* metadata target: AnalogConfig.GetDigitalVal */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2E584;
        label_0xC2E568:
        ;
        __arm64_flags_left_12772712 = unchecked((uint)(x8));
        __arm64_flags_right_12772712 = unchecked((uint)0x0UL);
        x10 = ((unchecked((uint)((__arm64_flags_left_12772712) - (__arm64_flags_right_12772712))) == unchecked((uint)0x0UL)) ? 0x0UL : x19);
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E594;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E574UL)));
        }
        if ((x10 == 0x0UL))
        {
            goto label_0xC2E5AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x10) + (0x34UL))), unchecked((uint)(x8)));
        goto label_0xC2E580;
        label_0xC2E580:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2E584;
        label_0xC2E584:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x3DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC2E594:
        ;
        if ((x9 == 0x0UL))
        {
            goto label_0xC2E5AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2E598UL)));
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        __arm64_float_flags_left_12772764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12772764 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        RuntimeMemory.WriteF32(unchecked((ulong)((x9) + (0x34UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = unchecked((ulong)(((__arm64_float_flags_left_12772764 > __arm64_float_flags_right_12772764) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        goto label_0xC2E584;
        label_0xC2E5AC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `GamepadManager.Gamepad.KeyState.SetDigital` — RVA `0xc2e5b0`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void SetDigital(bool state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_SetDigital_RVAc2e5b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x30UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2E5BC:
        ;
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.SetAnalog` — RVA `0xc2e5c0`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void SetAnalog(float val) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_SetAnalog_RVAc2e5c0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12772804 = default(float);
        float __arm64_float_flags_left_12772816 = default(float);
        float __arm64_float_flags_right_12772804 = default(float);
        float __arm64_float_flags_right_12772816 = default(float);
        float __arm64_fp_left_12772820 = default(float);
        float __arm64_fp_right_12772820 = default(float);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x2CUL))))), 0));
        __arm64_float_flags_left_12772804 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12772804 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12772804 >= __arm64_float_flags_right_12772804) || ((__arm64_float_flags_left_12772804 != __arm64_float_flags_left_12772804) || (__arm64_float_flags_right_12772804 != __arm64_float_flags_right_12772804))))
        {
        }
        else
        {
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
            __arm64_float_flags_left_12772816 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_float_flags_right_12772816 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
            __arm64_fp_left_12772820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
            __arm64_fp_right_12772820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12772820 != __arm64_fp_left_12772820) ? __arm64_fp_left_12772820 : ((__arm64_fp_right_12772820 != __arm64_fp_right_12772820) ? __arm64_fp_right_12772820 : (((__arm64_fp_left_12772820 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12772820 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12772820), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12772820), 0))))), 0) : ((__arm64_fp_left_12772820 <= __arm64_fp_right_12772820) ? __arm64_fp_left_12772820 : __arm64_fp_right_12772820))))), 0));
            v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
            v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((((__arm64_float_flags_left_12772816 >= __arm64_float_flags_right_12772816) || ((__arm64_float_flags_left_12772816 != __arm64_float_flags_left_12772816) || (__arm64_float_flags_right_12772816 != __arm64_float_flags_right_12772816))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))), 0));
            RuntimeMemory.WriteF32(unchecked((ulong)((x0) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        }
        label_0xC2E5E4:
        ;
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.SetConfig` — RVA `0xc2e808`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void SetConfig(AnalogConfig config) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_SetConfig_RVAc2e808(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x1);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.GetDigitalRaw` — RVA `0xc2e810`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool GetDigitalRaw() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_KeyState_GetDigitalRaw_RVAc2e810(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x3CUL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.KeyState.GetDigital` — RVA `0xc2e818`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool GetDigital() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_KeyState_GetDigital_RVAc2e818(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x3DUL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.KeyState.GetAnalog` — RVA `0xc2e820`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float GetAnalog() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_GetAnalog_RVAc2e820(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x34UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.GetAnalogRaw` — RVA `0xc2e828`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public float GetAnalogRaw() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_GetAnalogRaw_RVAc2e828(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x38UL))))), 0));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.IsTrigger` — RVA `0xc2e830`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public bool IsTrigger() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_Gamepad_KeyState_IsTrigger_RVAc2e830(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x18UL))))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.KeyState.ReadHardwareState` — RVA `0xc2e838`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `private void ReadHardwareState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_ReadHardwareState_RVAc2e838(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12773520 = default(uint);
        uint __arm64_flags_right_12773520 = default(uint);
        float __arm64_float_flags_left_12773528 = default(float);
        float __arm64_float_flags_left_12773548 = default(float);
        float __arm64_float_flags_right_12773528 = default(float);
        float __arm64_float_flags_right_12773548 = default(float);
        float __arm64_fp_left_12773540 = default(float);
        float __arm64_fp_left_12773560 = default(float);
        float __arm64_fp_right_12773540 = default(float);
        float __arm64_fp_right_12773560 = default(float);
        ulong __arm64_load_address_12773588 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x28UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E8CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x44UL))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E86C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E8DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E860UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E09CUL /* metadata target: GamepadManager.Gamepad.GetInternalKeyState */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        goto label_0xC2E870;
        label_0xC2E86C:
        ;
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2E870;
        label_0xC2E870:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x40UL))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        if ((unchecked((uint)((unchecked((uint)(x1))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2E8A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2E8DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E884UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2E114UL /* metadata target: GamepadManager.Gamepad.GetInternalAxisAnalog */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x48UL))))))));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes((-(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)))), 0));
        __arm64_flags_left_12773520 = unchecked((uint)(x8));
        __arm64_flags_right_12773520 = unchecked((uint)0x0UL);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12773520) - (__arm64_flags_right_12773520))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        __arm64_float_flags_left_12773528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12773528 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_12773528 < __arm64_float_flags_right_12773528))
        {
            goto label_0xC2E8A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E8A0UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_fp_left_12773540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_fp_right_12773540 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12773540 != __arm64_fp_left_12773540) ? __arm64_fp_left_12773540 : ((__arm64_fp_right_12773540 != __arm64_fp_right_12773540) ? __arm64_fp_right_12773540 : (((__arm64_fp_left_12773540 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12773540 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12773540), 0)) | (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12773540), 0))))), 0) : ((__arm64_fp_left_12773540 <= __arm64_fp_right_12773540) ? __arm64_fp_left_12773540 : __arm64_fp_right_12773540))))), 0));
        goto label_0xC2E8A8;
        label_0xC2E8A8:
        ;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x2CUL))))), 0));
        __arm64_float_flags_left_12773548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12773548 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        if (((__arm64_float_flags_left_12773548 >= __arm64_float_flags_right_12773548) || ((__arm64_float_flags_left_12773548 != __arm64_float_flags_left_12773548) || (__arm64_float_flags_right_12773548 != __arm64_float_flags_right_12773548))))
        {
            goto label_0xC2E8C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E8B4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        __arm64_fp_left_12773560 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0);
        __arm64_fp_right_12773560 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((__arm64_fp_left_12773560 != __arm64_fp_left_12773560) ? __arm64_fp_left_12773560 : ((__arm64_fp_right_12773560 != __arm64_fp_right_12773560) ? __arm64_fp_right_12773560 : (((__arm64_fp_left_12773560 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)) && (__arm64_fp_right_12773560 == global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0))) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)((global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_left_12773560), 0)) & (global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(__arm64_fp_right_12773560), 0))))), 0) : ((__arm64_fp_left_12773560 >= __arm64_fp_right_12773560) ? __arm64_fp_left_12773560 : __arm64_fp_right_12773560))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x2CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        goto label_0xC2E8C0;
        label_0xC2E8C0:
        ;
        if ((unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E8CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x30UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2E8CC;
        label_0xC2E8CC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        __arm64_load_address_12773588 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12773588)), 0));
        return x0;
        label_0xC2E8DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.SyncDigital` — RVA `0xc2e8e0`

- Lift status: **exact**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public void SyncDigital(DigitalBinding bind, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=7 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_SyncDigital_RVAc2e8e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x3DUL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2E908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x1;
        if ((x1 == 0x0UL))
        {
            goto label_0xC2E910;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x4 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC4F00CUL /* metadata target: DigitalBinding.Sync */);
        label_0xC2E908:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2E910:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.KeyState.SyncAnalog` — RVA `0xc2e914`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public void SyncAnalog(AxisBinding bind, InputRig rig) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_KeyState_SyncAnalog_RVAc2e914(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12773716 = default(uint);
        uint __arm64_flags_right_12773716 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC2E970;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2E920UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x0) + (0x34UL))))), 0));
        x20 = x1;
        x21 = x0;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x20;
        x3 = 0x0UL;
        x19 = x2;
        x0 = RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x3CUL))))))));
        x0 = x20;
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        __arm64_flags_left_12773716 = unchecked((uint)(x8));
        __arm64_flags_right_12773716 = unchecked((uint)0x0UL);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(((unchecked((uint)((__arm64_flags_left_12773716) - (__arm64_flags_right_12773716))) == unchecked((uint)0x0UL)) ? global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0) : global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))), 0));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4F160UL /* metadata target: AxisBinding.SyncFloat */);
        label_0xC2E970:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```
