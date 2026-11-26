# `GamepadManager.Gamepad.InternalKeyState` — TypeDefIndex 4957

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `KeyCode` | `key` |
| `0x14` | `bool` | `stateCur` |
| `0x15` | `bool` | `statePrev` |
| `0x16` | `bool` | `isReadyToUse` |

## `GamepadManager.Gamepad.InternalKeyState.ctor` — RVA `0xc2d958`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_InternalKeyState_ctor_RVAc2d958(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x16UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x14UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.InternalKeyState.ConnectToHardwareKey` — RVA `0xc2db68`

- Lift status: **partial**; input span: 52 bytes; span to next metadata RVA: 52 bytes.
- Metadata signature: `public void ConnectToHardwareKey(int joyId, int keyId) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=4 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.hi' at 0xc2db70; reason: Unknown IR expression at 0xc2db70

```csharp
public static ulong GamepadManager_Gamepad_InternalKeyState_ConnectToHardwareKey_RVAc2db68(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12770152 = default(uint);
        uint __arm64_flags_left_12770180 = default(uint);
        uint __arm64_flags_right_12770152 = default(uint);
        uint __arm64_flags_right_12770180 = default(uint);
        ulong x8 = default(ulong);
        __arm64_flags_left_12770152 = unchecked((uint)(x1));
        __arm64_flags_right_12770152 = unchecked((uint)0x3UL);
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        RuntimeCalls.Unsupported("b.hi", 0xC2DB70UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
        }
        else
        {
            if ((unchecked((uint)((unchecked((uint)(x2))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x8 = unchecked((ulong)(unchecked((uint)(0x14UL))));
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)((unchecked((uint)(x1))) * (unchecked((uint)(x8)))))) + (unchecked((uint)(x2)))))));
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x15EUL)))))));
                __arm64_flags_left_12770180 = unchecked((uint)(x2));
                __arm64_flags_right_12770180 = unchecked((uint)0x14UL);
                x8 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770180) - (__arm64_flags_right_12770180))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12770180)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12770180)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12770180) - (__arm64_flags_right_12770180))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12770180)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)0x0UL))));
            }
        }
        label_0xC2DB8C:
        ;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x10UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x14UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x16UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.InternalKeyState.Reset` — RVA `0xc2de94`

- Lift status: **exact**; input span: 12 bytes; span to next metadata RVA: 12 bytes.
- Metadata signature: `public void Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_Gamepad_InternalKeyState_Reset_RVAc2de94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeMemory.WriteU16(unchecked((ulong)((x0) + (0x14UL))), unchecked((ushort)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x16UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.Gamepad.InternalKeyState.GetState` — RVA `0xc2e0f4`

- Lift status: **exact**; input span: 32 bytes; span to next metadata RVA: 32 bytes.
- Metadata signature: `public bool GetState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=3 (informational only).

```csharp
public static uint GamepadManager_Gamepad_InternalKeyState_GetState_RVAc2e0f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12771584 = default(uint);
        uint __arm64_flags_right_12771584 = default(uint);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x16UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            label_0xC2E10C:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
            return unchecked((uint)(x0));
        }
        else
        {
            x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x14UL))))))));
            __arm64_flags_left_12771584 = unchecked((uint)(x8));
            __arm64_flags_right_12771584 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)(((!((unchecked((uint)((__arm64_flags_left_12771584) - (__arm64_flags_right_12771584))) == unchecked((uint)0x0UL)))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `GamepadManager.Gamepad.InternalKeyState.Update` — RVA `0xc2e444`

- Lift status: **exact**; input span: 68 bytes; span to next metadata RVA: 68 bytes.
- Metadata signature: `public void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static uint GamepadManager_Gamepad_InternalKeyState_Update_RVAc2e444(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x14UL))))))));
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x15UL))), unchecked((byte)(unchecked((uint)(x8)))));
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        label_0xC2E464:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x16UL))))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x14UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
            {
            }
            else
            {
                x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x16UL))), unchecked((byte)(unchecked((uint)(x8)))));
            }
        }
        label_0xC2E480:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.Gamepad.InternalKeyState.ReadHardwareState` — RVA `0xc2e974`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `private void ReadHardwareState() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static uint GamepadManager_Gamepad_InternalKeyState_ReadHardwareState_RVAc2e974(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
        if ((unchecked((uint)(x0)) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x1 = 0x0UL;
            x0 = RuntimeCalls.InvokeDirect(0x17C76BCUL /* metadata target: Input.GetKey */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        label_0xC2E98C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x14UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```
