# `GamepadProfile` — TypeDefIndex 4968

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `string` | `name` |
| `0x18` | `string` | `joystickIdentifier` |
| `0x20` | `GamepadProfile.ProfileMode` | `profileMode` |
| `0x28` | `string` | `unityVerFrom` |
| `0x30` | `string` | `unityVerTo` |
| `0x38` | `GamepadProfile.JoystickSource` | `leftStick` |
| `0x40` | `GamepadProfile.JoystickSource` | `rightStick` |
| `0x48` | `GamepadProfile.JoystickSource` | `dpad` |
| `0x50` | `GamepadProfile.KeySource` | `keyFaceU` |
| `0x58` | `GamepadProfile.KeySource` | `keyFaceR` |
| `0x60` | `GamepadProfile.KeySource` | `keyFaceD` |
| `0x68` | `GamepadProfile.KeySource` | `keyFaceL` |
| `0x70` | `GamepadProfile.KeySource` | `keyStart` |
| `0x78` | `GamepadProfile.KeySource` | `keySelect` |
| `0x80` | `GamepadProfile.KeySource` | `keyL1` |
| `0x88` | `GamepadProfile.KeySource` | `keyR1` |
| `0x90` | `GamepadProfile.KeySource` | `keyL2` |
| `0x98` | `GamepadProfile.KeySource` | `keyR2` |
| `0xA0` | `GamepadProfile.KeySource` | `keyL3` |
| `0xA8` | `GamepadProfile.KeySource` | `keyR3` |

## `GamepadProfile.GetKeySource` — RVA `0xc2dd88`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `public GamepadProfile.KeySource GetKeySource(int id) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=32 (informational only).

```csharp
public static ulong GamepadProfile_GetKeySource_RVAc2dd88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12770696 = default(uint);
        uint __arm64_flags_right_12770696 = default(uint);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        __arm64_flags_left_12770696 = unchecked((uint)(x1));
        __arm64_flags_right_12770696 = unchecked((uint)0xBUL);
        if (((__arm64_flags_left_12770696 >= __arm64_flags_right_12770696) && (!((unchecked((uint)((__arm64_flags_left_12770696) - (__arm64_flags_right_12770696))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC2DE10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x1))));
        x9 = unchecked((ulong)((x9) + (0x2DCUL)));
        x10 = 0xC2DDACUL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC2DE10:
        ;
        x0 = 0x0UL;
        return x0;
        return default(ulong);
    }
```

## `GamepadProfile.ctor` — RVA `0xc2fac0`

- Lift status: **exact**; input span: 572 bytes; span to next metadata RVA: 572 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=74 (informational only).

```csharp
public static ulong GamepadProfile_ctor_RVAc2fac0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x24 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x20 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x25) + (0x127UL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x1F0UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x1F8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x200UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x208UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x210UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FB4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x210UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x208UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x200UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x25) + (0x127UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2FB4C;
        label_0xC2FB4C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x23);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x20UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x1 = RuntimeMemory.ReadU64(x22);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2FCFCUL /* metadata target: GamepadProfile.JoystickSource.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2FCFCUL /* metadata target: GamepadProfile.JoystickSource.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2FCFCUL /* metadata target: GamepadProfile.JoystickSource.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x50UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x60UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x68UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x70UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x78UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x80UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x88UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x90UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x98UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xA0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xA8UL))), x0);
        x1 = x0;
        x0 = x19;
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

## `GamepadProfile.IsCompatible` — RVA `0xc2fe74`

- Lift status: **exact**; input span: 172 bytes; span to next metadata RVA: 172 bytes.
- Metadata signature: `public bool IsCompatible(string deviceName) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static uint GamepadProfile_IsCompatible_RVAc2fe74(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12779176 = default(uint);
        uint __arm64_flags_right_12779176 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x128UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FEA4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x220UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x128UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2FEA4;
        label_0xC2FEA4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x20UL))))));
        __arm64_flags_left_12779176 = unchecked((uint)(x8));
        __arm64_flags_right_12779176 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12779176) - (__arm64_flags_right_12779176))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2FED8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2FEB0UL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FED0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2FEB4UL)));
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2FF1C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x0 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13FA44CUL /* metadata target: String.IndexOf */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FF0C;
        }
        else
        {
            goto label_0xC2FED0;
        }
        label_0xC2FED0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2FF10;
        label_0xC2FED8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x220UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FEF4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC2FEF0UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2FEF4;
        label_0xC2FEF4:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x201UL))));
        x0 = x19;
        x1 = x20;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x16BE788UL /* metadata target: Regex.IsMatch */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FED0;
        }
        else
        {
            goto label_0xC2FF0C;
        }
        label_0xC2FF0C:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2FF10;
        label_0xC2FF10:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC2FF1C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `GamepadProfile.AddSupportedVersion` — RVA `0xc2ff20`

- Lift status: **exact**; input span: 96 bytes; span to next metadata RVA: 96 bytes.
- Metadata signature: `public void AddSupportedVersion(string unityVer) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong GamepadProfile_AddSupportedVersion_RVAc2ff20(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x1;
        x20 = x0;
        x0 = x1;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6920UL /* metadata target: String.IsNullOrEmpty */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FF58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2FF7C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F5794UL /* metadata target: String.CompareTo */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FF64;
        }
        else
        {
            goto label_0xC2FF58;
        }
        label_0xC2FF58:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2FF64:
        ;
        RuntimeMemory.WriteU64(x20, x19);
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC2FF7C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadProfile.GetJoystickSource` — RVA `0xc2ff80`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `public GamepadProfile.JoystickSource GetJoystickSource(int id) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GamepadProfile_GetJoystickSource_RVAc2ff80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12779392 = default(uint);
        uint __arm64_flags_left_12779400 = default(uint);
        uint __arm64_flags_right_12779392 = default(uint);
        uint __arm64_flags_right_12779400 = default(uint);
        ulong x8 = default(ulong);
        __arm64_flags_left_12779392 = unchecked((uint)(x1));
        __arm64_flags_right_12779392 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12779392) - (__arm64_flags_right_12779392))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2FF9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2FF88UL);
        }
        __arm64_flags_left_12779400 = unchecked((uint)(x1));
        __arm64_flags_right_12779400 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_12779400) - (__arm64_flags_right_12779400))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2FFA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2FF90UL);
        }
        if ((unchecked((uint)(x1)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FFB0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x0) + (0x38UL)));
        goto label_0xC2FFA8;
        label_0xC2FF9C:
        ;
        x8 = unchecked((ulong)((x0) + (0x48UL)));
        goto label_0xC2FFA8;
        label_0xC2FFA4:
        ;
        x8 = unchecked((ulong)((x0) + (0x40UL)));
        goto label_0xC2FFA8;
        label_0xC2FFA8:
        ;
        x0 = RuntimeMemory.ReadU64(x8);
        return x0;
        label_0xC2FFB0:
        ;
        x0 = 0x0UL;
        return x0;
        return default(ulong);
    }
```

## `GamepadProfile.IsDuplicateOf` — RVA `0xc2ffb8`

- Lift status: **partial**; input span: 264 bytes; span to next metadata RVA: 264 bytes.
- Metadata signature: `public bool IsDuplicateOf(GamepadProfile profile) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=37 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.eq' at 0xc3006c; reason: Unknown IR expression at 0xc3006c

```csharp
public static uint GamepadProfile_IsDuplicateOf_RVAc2ffb8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12779560 = default(uint);
        uint __arm64_flags_left_12779608 = default(uint);
        uint __arm64_flags_left_12779616 = default(uint);
        uint __arm64_flags_left_12779660 = default(uint);
        uint __arm64_flags_right_12779560 = default(uint);
        uint __arm64_flags_right_12779608 = default(uint);
        uint __arm64_flags_right_12779616 = default(uint);
        uint __arm64_flags_right_12779660 = default(uint);
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
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC300BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC300BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = x1;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x18UL))));
        x2 = unchecked((ulong)(unchecked((uint)(0x5UL))));
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F5B90UL /* metadata target: String.Equals */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC300A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2FFF4;
        label_0xC2FFF4:
        ;
        x0 = x20;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC2DD88UL /* metadata target: GamepadProfile.GetKeySource */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC300BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = x0;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC2DD88UL /* metadata target: GamepadProfile.GetKeySource */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = x0;
        x0 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xC300C0UL /* metadata target: GamepadProfile.KeySource.IsDuplicateOf */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC300A0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12779560 = unchecked((uint)(x21));
        __arm64_flags_right_12779560 = unchecked((uint)0xCUL);
        if ((!((unchecked((uint)((__arm64_flags_left_12779560) - (__arm64_flags_right_12779560))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC2FFF4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x22 = unchecked((ulong)((x20) + (0x48UL)));
        x23 = unchecked((ulong)((x19) + (0x48UL)));
        x24 = unchecked((ulong)((x20) + (0x40UL)));
        x25 = unchecked((ulong)((x19) + (0x40UL)));
        x20 = unchecked((ulong)((x20) + (0x38UL)));
        x19 = unchecked((ulong)((x19) + (0x38UL)));
        goto label_0xC3004C;
        label_0xC3004C:
        ;
        x9 = x20;
        x8 = x19;
        if ((unchecked((uint)(x21)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC3007C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC30058UL)));
        }
        __arm64_flags_left_12779608 = unchecked((uint)(x21));
        __arm64_flags_right_12779608 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12779608) - (__arm64_flags_right_12779608))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC30074;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC30060UL)));
        }
        __arm64_flags_left_12779616 = unchecked((uint)(x21));
        __arm64_flags_right_12779616 = unchecked((uint)0x1UL);
        x9 = x24;
        x8 = x25;
        RuntimeCalls.Unsupported("b.eq", 0xC3006CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC3007C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC30070UL)));
        }
        goto label_0xC300BC;
        label_0xC30074:
        ;
        x9 = x22;
        x8 = x23;
        goto label_0xC3007C;
        label_0xC3007C:
        ;
        x0 = RuntimeMemory.ReadU64(x9);
        if ((x0 == 0x0UL))
        {
            goto label_0xC300BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC3010CUL /* metadata target: GamepadProfile.JoystickSource.IsDuplicateOf */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12779660 = unchecked((uint)(x21));
        __arm64_flags_right_12779660 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_12779660) - (__arm64_flags_right_12779660))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC300A4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC3004C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC3009CUL)));
        }
        goto label_0xC300A4;
        label_0xC300A0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC300A4;
        label_0xC300A4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x30 = RuntimeMemory.ReadU64(sp);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC300BC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(uint);
    }
```

## `GamepadProfile.ctor` — RVA `0xc30188`

- Lift status: **partial**; input span: 756 bytes; span to next metadata RVA: 756 bytes.
- Metadata signature: `public void .ctor(string name, string deviceIdentifier, GamepadProfile.ProfileMode profileMode, string unityVerFrom, string unityVerTo, GamepadProfile.JoystickSource leftStick, GamepadProfile.JoystickSource rightStick, GamepadProfile.JoystickSource dpad, GamepadProfile.KeySource keyFaceD, GamepadProfile.KeySource keyFaceR, GamepadProfile.KeySource keyFaceL, GamepadProfile.KeySource keyFaceU, GamepadProfile.KeySource keySelect, GamepadProfile.KeySource keyStart, GamepadProfile.KeySource keyL1, GamepadProfile.KeySource keyR1, GamepadProfile.KeySource keyL2, GamepadProfile.KeySource keyR2, GamepadProfile.KeySource keyL3, GamepadProfile.KeySource keyR3) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=97 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc30284; reason: Unknown IR expression at 0xc30284; reason: Unsupported instruction 'csel' at 0xc302b0; reason: Unknown IR expression at 0xc302b0

```csharp
public static ulong GamepadProfile_ctor_RVAc30188(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12780152 = default(uint);
        uint __arm64_flags_left_12780196 = default(uint);
        uint __arm64_flags_result_12780152 = default(uint);
        uint __arm64_flags_result_12780196 = default(uint);
        uint __arm64_flags_right_12780152 = default(uint);
        uint __arm64_flags_right_12780196 = default(uint);
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
        sp = unchecked((ulong)((sp) - (0xC0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x29);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x0UL))), x28);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))), x27);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x19);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x120UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x118UL))));
        x20 = 0x1BAB000UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xD8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x9);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x110UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x108UL))));
        x22 = x7;
        x24 = x6;
        x25 = x5;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x9);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x100UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF8UL))));
        x26 = x4;
        x27 = unchecked((ulong)(unchecked((uint)(x3))));
        x28 = x2;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x8);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x9);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xF0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xE0UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xE0UL)))) + (0x8UL))));
        x29 = x1;
        x19 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x9);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x8);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC8UL)))) + (0x8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x8UL))), x8);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x129UL))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x9);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x10);
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC30234;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x208UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x228UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x129UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC30234;
        label_0xC30234:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x29);
        x1 = x29;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x28);
        x1 = x28;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x26;
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x20UL))), unchecked((uint)(x27)));
        x0 = RuntimeCalls.InvokeDirect(0x13F6920UL /* metadata target: String.IsNullOrEmpty */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x228UL))));
        __arm64_flags_left_12780152 = unchecked((uint)(x0));
        __arm64_flags_right_12780152 = unchecked((uint)0x1UL);
        __arm64_flags_result_12780152 = unchecked((uint)((__arm64_flags_left_12780152) & (__arm64_flags_right_12780152)));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(x8);
        RuntimeCalls.Unsupported("csel", 0xC30284UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x8 : x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x25;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6920UL /* metadata target: String.IsNullOrEmpty */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x208UL))));
        __arm64_flags_left_12780196 = unchecked((uint)(x0));
        __arm64_flags_right_12780196 = unchecked((uint)0x1UL);
        __arm64_flags_result_12780196 = unchecked((uint)((__arm64_flags_left_12780196) & (__arm64_flags_right_12780196)));
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(x8);
        RuntimeCalls.Unsupported("csel", 0xC302B0UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x8 : x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        if ((x24 != 0x0UL))
        {
            goto label_0xC302C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC302C0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC3047CUL /* metadata target: GamepadProfile.JoystickSource.Empty */, x0, x1, x2, x3);
        x24 = x0;
        goto label_0xC302C8;
        label_0xC302C8:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x24);
        x1 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        if ((x22 != 0x0UL))
        {
            goto label_0xC302E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC302DCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC3047CUL /* metadata target: GamepadProfile.JoystickSource.Empty */, x0, x1, x2, x3);
        x22 = x0;
        goto label_0xC302E4;
        label_0xC302E4:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x40UL))), x22);
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        if ((x23 != 0x0UL))
        {
            goto label_0xC30300;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC302F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC3047CUL /* metadata target: GamepadProfile.JoystickSource.Empty */, x0, x1, x2, x3);
        x23 = x0;
        goto label_0xC30300;
        label_0xC30300:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x48UL))), x23);
        x1 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        if ((x21 != 0x0UL))
        {
            goto label_0xC3031C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30314UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x21 = x0;
        goto label_0xC3031C;
        label_0xC3031C:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x50UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC3033C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30334UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC3033C;
        label_0xC3033C:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x58UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC30358;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30350UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC30358;
        label_0xC30358:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x60UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC30374;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC3036CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC30374;
        label_0xC30374:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x68UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC30390;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30388UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC30390;
        label_0xC30390:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x70UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x28UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC303AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC303A4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC303AC;
        label_0xC303AC:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x78UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC303C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC303C0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC303C8;
        label_0xC303C8:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x80UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x38UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC303E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC303DCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC303E4;
        label_0xC303E4:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x88UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC30400;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC303F8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC30400;
        label_0xC30400:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x90UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x48UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC3041C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30414UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC3041C;
        label_0xC3041C:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x98UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC30438;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30430UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC30438;
        label_0xC30438:
        ;
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0xA0UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x58UL))));
        if ((x1 != 0x0UL))
        {
            goto label_0xC30454;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC3044CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2FE10UL /* metadata target: GamepadProfile.KeySource.Empty */, x0, x1, x2, x3);
        x1 = x0;
        goto label_0xC30454;
        label_0xC30454:
        ;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0xA8UL))), x1);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xA0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xA0UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x90UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x90UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x80UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x80UL)))) + (0x8UL))));
        x28 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x70UL))));
        x27 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x70UL)))) + (0x8UL))));
        x29 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0xC0UL)));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```
