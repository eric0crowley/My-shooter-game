# `GamepadManager` — TypeDefIndex 4960

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x28` | `CustomGamepadProfileBank` | `customProfileBank` |
| `0x30` | `bool` | `dontDestroyOnLoad` |
| `0x34` | `float` | `connectionCheckInterval` |
| `0x38` | `float` | `elapsedSinceLastConnectionCheck` |
| `0x40` | `JoystickConfig` | `fallbackDpadConfig` |
| `0x48` | `JoystickConfig` | `fallbackLeftStickConfig` |
| `0x50` | `JoystickConfig` | `fallbackRightStickConfig` |
| `0x58` | `AnalogConfig` | `fallbackLeftTriggerAnalogConfig` |
| `0x60` | `AnalogConfig` | `fallbackRightTriggerAnalogConfig` |
| `0x68` | `List<GamepadManager.Gamepad>` | `activeGamepads` |
| `0x70` | `List<GamepadManager.Gamepad>` | `freeGamepads` |
| `0x78` | `List<GamepadManager.Gamepad>` | `connectedGamepads` |
| `0x80` | `GamepadManager.Gamepad` | `gamepadsCombined` |
| `0x88` | `int` | `activeGamepadNum` |
| `0x90` | `string[]` | `deviceConnections` |

## `GamepadManager.get_activeManager` — RVA `0xc2a250`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public static GamepadManager get_activeManager() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong GamepadManager_get_activeManager_RVAc2a250(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0xF2UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xF2UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2A280:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.set_activeManager` — RVA `0xc2a298`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private static void set_activeManager(GamepadManager value) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static ulong GamepadManager_set_activeManager_RVAc2a298(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0xF3UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A2CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0xF3UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A2CC;
        label_0xC2A2CC:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x19);
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `GamepadManager.add_onGamepadDisconnected` — RVA `0xc2a2f0`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void add_onGamepadDisconnected(GamepadManager.OnDisconnectionCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a390; reason: Unknown IR expression at 0xc2a390

```csharp
public static ulong GamepadManager_add_onGamepadDisconnected_RVAc2a2f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12755816 = default(ulong);
        ulong __arm64_flags_left_12755848 = default(ulong);
        ulong __arm64_flags_right_12755816 = default(ulong);
        ulong __arm64_flags_right_12755848 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xF4UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A334;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xF4UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A334;
        label_0xC2A334:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        goto label_0xC2A348;
        label_0xC2A348:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A6B8UL /* metadata target: Delegate.Combine */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A370;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12755816 = x9;
        __arm64_flags_right_12755816 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12755816) - (__arm64_flags_right_12755816))) == 0x0UL))))
        {
            goto label_0xC2A3A4;
        }
        else
        {
            goto label_0xC2A370;
        }
        label_0xC2A370:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12755848 = x20;
        __arm64_flags_right_12755848 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A390UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A348;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A3A4:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.remove_onGamepadDisconnected` — RVA `0xc2a3ac`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void remove_onGamepadDisconnected(GamepadManager.OnDisconnectionCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a44c; reason: Unknown IR expression at 0xc2a44c

```csharp
public static ulong GamepadManager_remove_onGamepadDisconnected_RVAc2a3ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12756004 = default(ulong);
        ulong __arm64_flags_left_12756036 = default(ulong);
        ulong __arm64_flags_right_12756004 = default(ulong);
        ulong __arm64_flags_right_12756036 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xF5UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A3F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xF5UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A3F0;
        label_0xC2A3F0:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        goto label_0xC2A404;
        label_0xC2A404:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A8B0UL /* metadata target: Delegate.Remove */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A42C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12756004 = x9;
        __arm64_flags_right_12756004 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12756004) - (__arm64_flags_right_12756004))) == 0x0UL))))
        {
            goto label_0xC2A460;
        }
        else
        {
            goto label_0xC2A42C;
        }
        label_0xC2A42C:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12756036 = x20;
        __arm64_flags_right_12756036 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A44CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A404;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A460:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.add_onGamepadDisactivated` — RVA `0xc2a468`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void add_onGamepadDisactivated(GamepadManager.OnDisconnectionCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a508; reason: Unknown IR expression at 0xc2a508

```csharp
public static ulong GamepadManager_add_onGamepadDisactivated_RVAc2a468(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12756192 = default(ulong);
        ulong __arm64_flags_left_12756224 = default(ulong);
        ulong __arm64_flags_right_12756192 = default(ulong);
        ulong __arm64_flags_right_12756224 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xF6UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A4AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xF6UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A4AC;
        label_0xC2A4AC:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        goto label_0xC2A4C0;
        label_0xC2A4C0:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A6B8UL /* metadata target: Delegate.Combine */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A4E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12756192 = x9;
        __arm64_flags_right_12756192 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12756192) - (__arm64_flags_right_12756192))) == 0x0UL))))
        {
            goto label_0xC2A51C;
        }
        else
        {
            goto label_0xC2A4E8;
        }
        label_0xC2A4E8:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x10UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12756224 = x20;
        __arm64_flags_right_12756224 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A508UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A4C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A51C:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.remove_onGamepadDisactivated` — RVA `0xc2a524`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void remove_onGamepadDisactivated(GamepadManager.OnDisconnectionCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a5c4; reason: Unknown IR expression at 0xc2a5c4

```csharp
public static ulong GamepadManager_remove_onGamepadDisactivated_RVAc2a524(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12756380 = default(ulong);
        ulong __arm64_flags_left_12756412 = default(ulong);
        ulong __arm64_flags_right_12756380 = default(ulong);
        ulong __arm64_flags_right_12756412 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xF7UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A568;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xF7UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A568;
        label_0xC2A568:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x30UL))));
        goto label_0xC2A57C;
        label_0xC2A57C:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A8B0UL /* metadata target: Delegate.Remove */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A5A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12756380 = x9;
        __arm64_flags_right_12756380 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12756380) - (__arm64_flags_right_12756380))) == 0x0UL))))
        {
            goto label_0xC2A5D8;
        }
        else
        {
            goto label_0xC2A5A4;
        }
        label_0xC2A5A4:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x10UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12756412 = x20;
        __arm64_flags_right_12756412 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A5C4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A57C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A5D8:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.add_onGamepadConnected` — RVA `0xc2a5e0`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void add_onGamepadConnected(GamepadManager.OnConnectionChnageCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a680; reason: Unknown IR expression at 0xc2a680

```csharp
public static ulong GamepadManager_add_onGamepadConnected_RVAc2a5e0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12756568 = default(ulong);
        ulong __arm64_flags_left_12756600 = default(ulong);
        ulong __arm64_flags_right_12756568 = default(ulong);
        ulong __arm64_flags_right_12756600 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xF8UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A624;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xF8UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A624;
        label_0xC2A624:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x38UL))));
        goto label_0xC2A638;
        label_0xC2A638:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A6B8UL /* metadata target: Delegate.Combine */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A660;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12756568 = x9;
        __arm64_flags_right_12756568 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12756568) - (__arm64_flags_right_12756568))) == 0x0UL))))
        {
            goto label_0xC2A694;
        }
        else
        {
            goto label_0xC2A660;
        }
        label_0xC2A660:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x18UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12756600 = x20;
        __arm64_flags_right_12756600 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A680UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A694:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.remove_onGamepadConnected` — RVA `0xc2a69c`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void remove_onGamepadConnected(GamepadManager.OnConnectionChnageCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a73c; reason: Unknown IR expression at 0xc2a73c

```csharp
public static ulong GamepadManager_remove_onGamepadConnected_RVAc2a69c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12756756 = default(ulong);
        ulong __arm64_flags_left_12756788 = default(ulong);
        ulong __arm64_flags_right_12756756 = default(ulong);
        ulong __arm64_flags_right_12756788 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xF9UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A6E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xF9UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A6E0;
        label_0xC2A6E0:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x38UL))));
        goto label_0xC2A6F4;
        label_0xC2A6F4:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A8B0UL /* metadata target: Delegate.Remove */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A71C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12756756 = x9;
        __arm64_flags_right_12756756 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12756756) - (__arm64_flags_right_12756756))) == 0x0UL))))
        {
            goto label_0xC2A750;
        }
        else
        {
            goto label_0xC2A71C;
        }
        label_0xC2A71C:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x18UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12756788 = x20;
        __arm64_flags_right_12756788 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A73CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A6F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A750:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.add_onGamepadActivated` — RVA `0xc2a758`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void add_onGamepadActivated(GamepadManager.OnConnectionChnageCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a7f8; reason: Unknown IR expression at 0xc2a7f8

```csharp
public static ulong GamepadManager_add_onGamepadActivated_RVAc2a758(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12756944 = default(ulong);
        ulong __arm64_flags_left_12756976 = default(ulong);
        ulong __arm64_flags_right_12756944 = default(ulong);
        ulong __arm64_flags_right_12756976 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xFAUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A79C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xFAUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A79C;
        label_0xC2A79C:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x38UL))));
        goto label_0xC2A7B0;
        label_0xC2A7B0:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A6B8UL /* metadata target: Delegate.Combine */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A7D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12756944 = x9;
        __arm64_flags_right_12756944 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12756944) - (__arm64_flags_right_12756944))) == 0x0UL))))
        {
            goto label_0xC2A80C;
        }
        else
        {
            goto label_0xC2A7D8;
        }
        label_0xC2A7D8:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12756976 = x20;
        __arm64_flags_right_12756976 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A7F8UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A7B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A80C:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.remove_onGamepadActivated` — RVA `0xc2a814`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void remove_onGamepadActivated(GamepadManager.OnConnectionChnageCallback value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a8b4; reason: Unknown IR expression at 0xc2a8b4

```csharp
public static ulong GamepadManager_remove_onGamepadActivated_RVAc2a814(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12757132 = default(ulong);
        ulong __arm64_flags_left_12757164 = default(ulong);
        ulong __arm64_flags_right_12757132 = default(ulong);
        ulong __arm64_flags_right_12757164 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xFBUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A858;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xFBUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A858;
        label_0xC2A858:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x38UL))));
        goto label_0xC2A86C;
        label_0xC2A86C:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A8B0UL /* metadata target: Delegate.Remove */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A894;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12757132 = x9;
        __arm64_flags_right_12757132 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12757132) - (__arm64_flags_right_12757132))) == 0x0UL))))
        {
            goto label_0xC2A8C8;
        }
        else
        {
            goto label_0xC2A894;
        }
        label_0xC2A894:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12757164 = x20;
        __arm64_flags_right_12757164 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A8B4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A86C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A8C8:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.add_onChange` — RVA `0xc2a8d0`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void add_onChange(Action value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2a970; reason: Unknown IR expression at 0xc2a970

```csharp
public static ulong GamepadManager_add_onChange_RVAc2a8d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12757320 = default(ulong);
        ulong __arm64_flags_left_12757352 = default(ulong);
        ulong __arm64_flags_right_12757320 = default(ulong);
        ulong __arm64_flags_right_12757352 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xFCUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A914;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xFCUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A914;
        label_0xC2A914:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x40UL))));
        goto label_0xC2A928;
        label_0xC2A928:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A6B8UL /* metadata target: Delegate.Combine */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2A950;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12757320 = x9;
        __arm64_flags_right_12757320 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12757320) - (__arm64_flags_right_12757320))) == 0x0UL))))
        {
            goto label_0xC2A984;
        }
        else
        {
            goto label_0xC2A950;
        }
        label_0xC2A950:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x28UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12757352 = x20;
        __arm64_flags_right_12757352 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2A970UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A928;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2A984:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.remove_onChange` — RVA `0xc2a98c`

- Lift status: **partial**; input span: 188 bytes; span to next metadata RVA: 188 bytes.
- Metadata signature: `public static void remove_onChange(Action value) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=31 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc2aa2c; reason: Unknown IR expression at 0xc2aa2c

```csharp
public static ulong GamepadManager_remove_onChange_RVAc2a98c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12757508 = default(ulong);
        ulong __arm64_flags_left_12757540 = default(ulong);
        ulong __arm64_flags_right_12757508 = default(ulong);
        ulong __arm64_flags_right_12757540 = default(ulong);
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
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0xFDUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2A9D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0xFDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2A9D0;
        label_0xC2A9D0:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x40UL))));
        goto label_0xC2A9E4;
        label_0xC2A9E4:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x158A8B0UL /* metadata target: Delegate.Remove */, x0, x1, x2, x3);
        x8 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2AA0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x22);
        x9 = RuntimeMemory.ReadU64(x8);
        __arm64_flags_left_12757508 = x9;
        __arm64_flags_right_12757508 = x1;
        if ((!((unchecked((ulong)((__arm64_flags_left_12757508) - (__arm64_flags_right_12757508))) == 0x0UL))))
        {
            goto label_0xC2AA40;
        }
        else
        {
            goto label_0xC2AA0C;
        }
        label_0xC2AA0C:
        ;
        x9 = RuntimeMemory.ReadU64(x21);
        x1 = x8;
        x2 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x0 = unchecked((ulong)((x9) + (0x28UL)));
        x0 = RuntimeCalls.InvokeDirect(0xB60EBCUL, x0, x1, x2, x3);
        __arm64_flags_left_12757540 = x20;
        __arm64_flags_right_12757540 = x0;
        x20 = x0;
        RuntimeCalls.Unsupported("b.ne", 0xC2AA2CUL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2A9E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2AA40:
        ;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DF10UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.GetJoyAxisName` — RVA `0xc2aa48`

- Lift status: **exact**; input span: 184 bytes; span to next metadata RVA: 184 bytes.
- Metadata signature: `public static string GetJoyAxisName(int joyId, int axisId) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=30 (informational only).

```csharp
public static ulong GamepadManager_GetJoyAxisName_RVAc2aa48(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12757644 = default(uint);
        uint __arm64_flags_left_12757652 = default(uint);
        uint __arm64_flags_right_12757644 = default(uint);
        uint __arm64_flags_right_12757652 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0xFEUL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = unchecked((ulong)(unchecked((uint)(x0))));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), unchecked((uint)(x1)));
        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x4UL))), unchecked((uint)(x0)));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2AA8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0xFEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2AA8C;
        label_0xC2AA8C:
        ;
        __arm64_flags_left_12757644 = unchecked((uint)(x20));
        __arm64_flags_right_12757644 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_12757644 >= __arm64_flags_right_12757644) && (!((unchecked((uint)((__arm64_flags_left_12757644) - (__arm64_flags_right_12757644))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC2AADC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2AA94UL);
        }
        __arm64_flags_left_12757652 = unchecked((uint)(x19));
        __arm64_flags_right_12757652 = unchecked((uint)0xAUL);
        if ((__arm64_flags_left_12757652 >= __arm64_flags_right_12757652))
        {
            goto label_0xC2AADC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x19 = x0;
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x50UL))));
        x2 = x0;
        x1 = x19;
        x3 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13F661CUL /* metadata target: String.Concat */, x0, x1, x2, x3);
        goto label_0xC2AAF0;
        label_0xC2AADC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        goto label_0xC2AAF0;
        label_0xC2AAF0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.GetJoyKeyCode` — RVA `0xc2ab00`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public static KeyCode GetJoyKeyCode(int joyId, int keyId) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static uint GamepadManager_GetJoyKeyCode_RVAc2ab00(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12757760 = default(uint);
        uint __arm64_flags_left_12757784 = default(uint);
        uint __arm64_flags_right_12757760 = default(uint);
        uint __arm64_flags_right_12757784 = default(uint);
        ulong x8 = default(ulong);
        __arm64_flags_left_12757760 = unchecked((uint)(x0));
        __arm64_flags_right_12757760 = unchecked((uint)0x3UL);
        if (((__arm64_flags_left_12757760 >= __arm64_flags_right_12757760) && (!((unchecked((uint)((__arm64_flags_left_12757760) - (__arm64_flags_right_12757760))) == unchecked((uint)0x0UL))))))
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
                __arm64_flags_left_12757784 = unchecked((uint)(x1));
                __arm64_flags_right_12757784 = unchecked((uint)0x14UL);
                x0 = unchecked((ulong)((((unchecked((int)(unchecked((uint)((__arm64_flags_left_12757784) - (__arm64_flags_right_12757784))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12757784)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12757784)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12757784) - (__arm64_flags_right_12757784))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12757784)) < unchecked((int)0x0UL))))) ? unchecked((uint)(x8)) : unchecked((uint)0x0UL))));
                return unchecked((uint)(x0));
            }
        }
        label_0xC2AB24:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.ctor` — RVA `0xc2ab2c`

- Lift status: **exact**; input span: 860 bytes; span to next metadata RVA: 860 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=128 (informational only).

```csharp
public static ulong GamepadManager_ctor_RVAc2ab2c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12758572 = default(uint);
        uint __arm64_flags_left_12758632 = default(uint);
        uint __arm64_flags_result_12758632 = default(uint);
        uint __arm64_flags_right_12758572 = default(uint);
        uint __arm64_flags_right_12758632 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0xFFUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x58UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x60UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2ABB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x68UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x80UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x88UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0xFFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2ABB8;
        label_0xC2ABB8:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC4F5ACUL /* metadata target: ComponentBase.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2AE88UL /* metadata target: CustomGamepadProfileBank.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x431000UL;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xD78UL))))), 0));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x30UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x34UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC609D8UL /* metadata target: JoystickConfig.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x40UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC2AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(0x999AUL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x23 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E99UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x40UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x23)));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC609D8UL /* metadata target: JoystickConfig.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x48UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC2AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2AC68UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x40UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x23)));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC609D8UL /* metadata target: JoystickConfig.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x50UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC2AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x68UL))));
        x9 = unchecked((ulong)(unchecked((uint)(0x999AUL))));
        x9 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E99UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x40UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x9)));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56BB8UL /* metadata target: AnalogConfig.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x58UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC2AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x23 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3E4CUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x23)));
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC56BB8UL /* metadata target: AnalogConfig.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x60UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        if ((x8 == 0x0UL))
        {
            goto label_0xC2AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x70UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x8) + (0x10UL))), unchecked((uint)(x23)));
        x25 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(x22);
        x23 = 0x1A8C000UL;
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0x88UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x80UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2AF14UL /* metadata target: GamepadManager.Gamepad.ctor */, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x80UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x20 = x0;
        x24 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A2BD4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x70UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2BD4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x68UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2BD4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x78UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x21) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        goto label_0xC2ADF0;
        label_0xC2ADF0:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x19;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2AF14UL /* metadata target: GamepadManager.Gamepad.ctor */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC2AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x23);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2AE84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x20) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12758572 = unchecked((uint)(x10));
        __arm64_flags_right_12758572 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12758572 >= __arm64_flags_right_12758572))
        {
            goto label_0xC2AE50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x0 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC2AE68;
        label_0xC2AE50:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x0 = x20;
        x1 = x21;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3390UL, x0, x1, x2, x3);
        goto label_0xC2AE68;
        label_0xC2AE68:
        ;
        __arm64_flags_left_12758632 = unchecked((uint)(x24));
        __arm64_flags_right_12758632 = unchecked((uint)0x1UL);
        __arm64_flags_result_12758632 = unchecked((uint)((__arm64_flags_left_12758632) - (__arm64_flags_right_12758632)));
        x24 = unchecked((ulong)(__arm64_flags_result_12758632));
        if ((!((unchecked((uint)((__arm64_flags_left_12758632) - (__arm64_flags_right_12758632))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC2ADF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC2AE84:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.OnInitComponent` — RVA `0xc2b2d4`

- Lift status: **exact**; input span: 24 bytes; span to next metadata RVA: 24 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong GamepadManager_OnInitComponent_RVAc2b2d4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2B2E8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC33764UL /* metadata target: CustomGamepadProfileBank.LoadFromPlayerPrefs */);
        label_0xC2B2E8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.OnDestroyComponent` — RVA `0xc2b2f0`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GamepadManager_OnDestroyComponent_RVAc2b2f0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.OnEnableComponent` — RVA `0xc2b2f4`

- Lift status: **exact**; input span: 344 bytes; span to next metadata RVA: 344 bytes.
- Metadata signature: `protected override void OnEnableComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong GamepadManager_OnEnableComponent_RVAc2b2f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x100UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B324;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x100UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B324;
        label_0xC2B324:
        ;
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1DDUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B34C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1DDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B34C;
        label_0xC2B34C:
        ;
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = RuntimeMemory.ReadU64(x23);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B370;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B36CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B370;
        label_0xC2B370:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2B3C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B44CUL /* metadata target: GamepadManager.SetAsMain */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x30UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2B420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B3B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B3ACUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B3B0;
        label_0xC2B3B0:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1798C10UL /* metadata target: Object.DontDestroyOnLoad */);
        label_0xC2B3C8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1DDUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B3E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1DDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B3E4;
        label_0xC2B3E4:
        ;
        x8 = RuntimeMemory.ReadU64(x23);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B400;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B3FCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B400;
        label_0xC2B400:
        ;
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2B420;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC58364UL /* metadata target: CFUtils.get_editorStopped */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2B430;
        }
        else
        {
            goto label_0xC2B420;
        }
        label_0xC2B420:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC2B430:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */);
        return default(ulong);
    }
```

## `GamepadManager.SetAsMain` — RVA `0xc2b44c`

- Lift status: **exact**; input span: 432 bytes; span to next metadata RVA: 432 bytes.
- Metadata signature: `public void SetAsMain() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=71 (informational only).

```csharp
public static ulong GamepadManager_SetAsMain_RVAc2b44c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x102UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B4A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x102UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B4A0;
        label_0xC2B4A0:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2B4CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2B4CC:
        ;
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1DDUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B4EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1DDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B4EC;
        label_0xC2B4EC:
        ;
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x9 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(x21);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xD8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x9);
        x20 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B518;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B514UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2B518;
        label_0xC2B518:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2B55C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x1DDUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B548;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x1DDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B548;
        label_0xC2B548:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2B5F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B558UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2B68CUL /* metadata target: GamepadManager.RemoveAsMain */, x0, x1, x2, x3);
        goto label_0xC2B55C;
        label_0xC2B55C:
        ;
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1DEUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B57C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1DEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B57C;
        label_0xC2B57C:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x19);
        x8 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE8UL))));
        x1 = x19;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE0UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B5DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B5D8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B5DC;
        label_0xC2B5DC:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC2B7DCUL /* metadata target: CF2Input.add_onActiveRigChange */, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC2B8B8UL /* metadata target: GamepadManager.OnActiveRigChange */);
        label_0xC2B5F8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.IsMain` — RVA `0xc2b5fc`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `public bool IsMain() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong GamepadManager_IsMain_RVAc2b5fc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x101UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B628;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x101UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B628;
        label_0xC2B628:
        ;
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1DDUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B650;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1DDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B650;
        label_0xC2B650:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(x8);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B674;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B670UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B674;
        label_0xC2B674:
        ;
        x0 = x20;
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */);
        return default(ulong);
    }
```

## `GamepadManager.RemoveAsMain` — RVA `0xc2b68c`

- Lift status: **exact**; input span: 336 bytes; span to next metadata RVA: 336 bytes.
- Metadata signature: `public void RemoveAsMain() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=57 (informational only).

```csharp
public static ulong GamepadManager_RemoveAsMain_RVAc2b68c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x103UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B6E4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x103UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B6E4;
        label_0xC2B6E4:
        ;
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x1DDUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B70C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x1DDUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B70C;
        label_0xC2B70C:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(x22);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B730;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B72CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B730;
        label_0xC2B730:
        ;
        x24 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE0UL))));
        x0 = x20;
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2B798;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1DEUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B77C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1DEUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B77C;
        label_0xC2B77C:
        ;
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WritePtr(x8, 0x0UL);
        x8 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC2B798;
        label_0xC2B798:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = x19;
        x3 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x14E3EACUL /* metadata target: Action.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B7C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B7C0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B7C4;
        label_0xC2B7C4:
        ;
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC2BA9CUL /* metadata target: CF2Input.remove_onActiveRigChange */);
        return default(ulong);
    }
```

## `GamepadManager.OnActiveRigChange` — RVA `0xc2b8b8`

- Lift status: **exact**; input span: 484 bytes; span to next metadata RVA: 484 bytes.
- Metadata signature: `private void OnActiveRigChange() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=72 (informational only).

```csharp
public static ulong GamepadManager_OnActiveRigChange_RVAc2b8b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12761476 = default(uint);
        uint __arm64_flags_left_12761616 = default(uint);
        uint __arm64_flags_right_12761476 = default(uint);
        uint __arm64_flags_right_12761616 = default(uint);
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x105UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B90C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x105UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B90C;
        label_0xC2B90C:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B920;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B91CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2B920;
        label_0xC2B920:
        ;
        x23 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B940;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2B940;
        label_0xC2B940:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B954;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B94CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        goto label_0xC2B954;
        label_0xC2B954:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC2BA84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC2BD0CUL /* metadata target: GamepadManager.Gamepad.SetRig */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2BA84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xF8UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2B980;
        label_0xC2B980:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12761476 = unchecked((uint)(x21));
        __arm64_flags_right_12761476 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12761476) - (__arm64_flags_right_12761476))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12761476)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12761476)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12761476) - (__arm64_flags_right_12761476))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12761476)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2B9FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B9B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2B9B0;
        label_0xC2B9B0:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B9C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC2B9C4;
        label_0xC2B9C4:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2B9D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B9D0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        goto label_0xC2B9D8;
        label_0xC2B9D8:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC2BA84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x22;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC2BD0CUL /* metadata target: GamepadManager.Gamepad.SetRig */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x70UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2B980;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2B9F8UL);
        }
        goto label_0xC2BA84;
        label_0xC2B9FC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2BA84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2BA0C;
        label_0xC2BA0C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12761616 = unchecked((uint)(x21));
        __arm64_flags_right_12761616 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12761616) - (__arm64_flags_right_12761616))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12761616)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12761616)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12761616) - (__arm64_flags_right_12761616))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12761616)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2BA88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x22 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BA3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2BA3C;
        label_0xC2BA3C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BA50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x25)))));
        goto label_0xC2BA50;
        label_0xC2BA50:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BA64;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2BA5CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        goto label_0xC2BA64;
        label_0xC2BA64:
        ;
        if ((x22 == 0x0UL))
        {
            goto label_0xC2BA84;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x0 = x22;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC2BD0CUL /* metadata target: GamepadManager.Gamepad.SetRig */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2BA0C;
        }
        else
        {
            goto label_0xC2BA84;
        }
        label_0xC2BA84:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2BA88;
        label_0xC2BA88:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.GetCustomProfileBank` — RVA `0xc2bb78`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public CustomGamepadProfileBank GetCustomProfileBank() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_GetCustomProfileBank_RVAc2bb78(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.OnDisableComponent` — RVA `0xc2bb80`

- Lift status: **exact**; input span: 228 bytes; span to next metadata RVA: 228 bytes.
- Metadata signature: `protected override void OnDisableComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=36 (informational only).

```csharp
public static ulong GamepadManager_OnDisableComponent_RVAc2bb80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12762076 = default(uint);
        uint __arm64_flags_right_12762076 = default(uint);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x104UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BBC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x104UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2BBC4;
        label_0xC2BBC4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2BC10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF8UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2BBD8;
        label_0xC2BBD8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12762076 = unchecked((uint)(x20));
        __arm64_flags_right_12762076 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12762076) - (__arm64_flags_right_12762076))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12762076)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12762076)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12762076) - (__arm64_flags_right_12762076))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12762076)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2BC14;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2BC04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x2 = unchecked((ulong)(unchecked((uint)(0x3UL))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2BC64UL /* metadata target: GamepadManager.DisconnectGamepad */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2BC04;
        label_0xC2BC04:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2BBD8;
        }
        else
        {
            goto label_0xC2BC10;
        }
        label_0xC2BC10:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2BC14;
        label_0xC2BC14:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BC58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BC48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2BC48;
        label_0xC2BC48:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC2B68CUL /* metadata target: GamepadManager.RemoveAsMain */);
        label_0xC2BC58:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.DisconnectGamepad` — RVA `0xc2bc64`

- Lift status: **exact**; input span: 168 bytes; span to next metadata RVA: 168 bytes.
- Metadata signature: `private void DisconnectGamepad(GamepadManager.Gamepad g, GamepadManager.DisconnectionReason reason) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=27 (informational only).

```csharp
public static ulong GamepadManager_DisconnectGamepad_RVAc2bc64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10EUL))))))));
        x20 = unchecked((ulong)(unchecked((uint)(x2))));
        x19 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2BC9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x10EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2BC9C;
        label_0xC2BC9C:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC2BD08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BCB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x1 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0xC2CDF8UL /* metadata target: GamepadManager.DisactivateGamepad */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2BCB8;
        label_0xC2BCB8:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2BCF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2BCF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x19;
        x2 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2BCF4;
        label_0xC2BCF4:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC2CF0CUL /* metadata target: GamepadManager.Gamepad.OnDisconnect */);
        label_0xC2BD08:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `GamepadManager.Update` — RVA `0xc2c004`

- Lift status: **exact**; input span: 428 bytes; span to next metadata RVA: 428 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=63 (informational only).

```csharp
public static ulong GamepadManager_Update_RVAc2c004(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12763272 = default(uint);
        uint __arm64_flags_left_12763332 = default(uint);
        uint __arm64_flags_right_12763272 = default(uint);
        uint __arm64_flags_right_12763332 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x106UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C058;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x106UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2C058;
        label_0xC2C058:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2C1B0UL /* metadata target: GamepadManager.CheckJoystickConnections */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C1AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xF8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2C084;
        label_0xC2C084:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12763272 = unchecked((uint)(x20));
        __arm64_flags_right_12763272 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763272) - (__arm64_flags_right_12763272))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12763272)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12763272)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763272) - (__arm64_flags_right_12763272))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12763272)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C0B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C1AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C0A0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2C1FCUL /* metadata target: GamepadManager.Gamepad.Update */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2C084;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C0B0UL);
        }
        goto label_0xC2C1AC;
        label_0xC2C0B4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C1AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2C0C0;
        label_0xC2C0C0:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12763332 = unchecked((uint)(x20));
        __arm64_flags_right_12763332 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763332) - (__arm64_flags_right_12763332))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12763332)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12763332)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12763332) - (__arm64_flags_right_12763332))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12763332)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C104;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C0F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x22UL))))))));
        x1 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C0F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C1AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C0F0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2C304UL /* metadata target: GamepadManager.Gamepad.ApplyGamepadState */, x0, x1, x2, x3);
        goto label_0xC2C0F4;
        label_0xC2C0F4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2C0C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C100UL);
        }
        goto label_0xC2C1AC;
        label_0xC2C104:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x80UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C1AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C10CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC2C1FCUL /* metadata target: GamepadManager.Gamepad.Update */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C120;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C11CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2C120;
        label_0xC2C120:
        ;
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x1DFUL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C140;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE0UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x1DFUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2C140;
        label_0xC2C140:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C154;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C14CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xC2C154;
        label_0xC2C154:
        ;
        x8 = RuntimeMemory.ReadU64(x21);
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x18UL))));
        if ((unchecked((uint)(x10)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C170;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2C170;
        label_0xC2C170:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C19C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC2C42CUL /* metadata target: GamepadManager.ApplyToRig */);
        label_0xC2C19C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC2C1AC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.CheckJoystickConnections` — RVA `0xc2c1b0`

- Lift status: **exact**; input span: 76 bytes; span to next metadata RVA: 76 bytes.
- Metadata signature: `private void CheckJoystickConnections() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GamepadManager_CheckJoystickConnections_RVAc2c1b0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        float __arm64_float_flags_left_12763608 = default(float);
        float __arm64_float_flags_right_12763608 = default(float);
        ulong __arm64_load_address_12763624 = default(ulong);
        ulong __arm64_load_address_12763636 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2C564UL /* metadata target: GamepadManager.CheckUnactivatedGamepads */, x0, x1, x2, x3);
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x38UL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ADA8UL /* metadata target: Time.get_unscaledDeltaTime */, x0, x1, x2, x3);
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x34UL))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x38UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        __arm64_float_flags_left_12763608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0);
        __arm64_float_flags_right_12763608 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0);
        if ((__arm64_float_flags_left_12763608 < __arm64_float_flags_right_12763608))
        {
            goto label_0xC2C1F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12763624 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12763624)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12763624) + (0x20UL)));
        return RuntimeCalls.InvokeDirect(0xC2C690UL /* metadata target: GamepadManager.ConnectJoysticks */);
        label_0xC2C1F0:
        ;
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12763636 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12763636)), 0));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.ApplyToRig` — RVA `0xc2c42c`

- Lift status: **partial**; input span: 312 bytes; span to next metadata RVA: 312 bytes.
- Metadata signature: `private void ApplyToRig(InputRig rig) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=45 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc2c500; reason: Unsupported instruction 'b.ge' at 0xc2c504; reason: Unknown IR expression at 0xc2c504

```csharp
public static ulong GamepadManager_ApplyToRig_RVAc2c42c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_flags_left_12764364 = default(ulong);
        ulong __arm64_flags_left_12764424 = default(ulong);
        ulong __arm64_flags_right_12764364 = default(ulong);
        ulong __arm64_flags_right_12764424 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x107UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C480;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x107UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2C480;
        label_0xC2C480:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C490;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C48CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC2C490;
        label_0xC2C490:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C4B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2C4B4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF8UL))));
        x21 = 0x0UL;
        goto label_0xC2C4C8;
        label_0xC2C4C8:
        ;
        x8 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        __arm64_flags_left_12764364 = x21;
        __arm64_flags_right_12764364 = x8;
        if (((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12764364) - (__arm64_flags_right_12764364))))) < unchecked((long)0x0UL)) == (((unchecked((long)(__arm64_flags_left_12764364)) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_right_12764364)) < unchecked((long)0x0UL))) && ((unchecked((long)(unchecked((ulong)((__arm64_flags_left_12764364) - (__arm64_flags_right_12764364))))) < unchecked((long)0x0UL)) != (unchecked((long)(__arm64_flags_left_12764364)) < unchecked((long)0x0UL))))))
        {
            goto label_0xC2C538;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C528;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x22UL))))))));
        x1 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C528;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C4F0UL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC2C534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xE8UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        RuntimeCalls.Unsupported("cmp", 0xC2C500UL);
        RuntimeCalls.Unsupported("b.ge", 0xC2C504UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2C528;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C508UL);
        }
        __arm64_flags_left_12764424 = x21;
        __arm64_flags_right_12764424 = x9;
        if ((__arm64_flags_left_12764424 >= __arm64_flags_right_12764424))
        {
            goto label_0xC2C560;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = x19;
        x3 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3F9C0UL /* metadata target: InputRig.GamepadConfig.SyncGamepad */, x0, x1, x2, x3);
        goto label_0xC2C528;
        label_0xC2C528:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2C4C8;
        }
        else
        {
            goto label_0xC2C534;
        }
        label_0xC2C534:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2C538;
        label_0xC2C538:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC2C534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xF0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C534;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x80UL))));
        x2 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x3 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC3F9C0UL /* metadata target: InputRig.GamepadConfig.SyncGamepad */);
        label_0xC2C560:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.CheckUnactivatedGamepads` — RVA `0xc2c564`

- Lift status: **exact**; input span: 300 bytes; span to next metadata RVA: 300 bytes.
- Metadata signature: `private void CheckUnactivatedGamepads() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=46 (informational only).

```csharp
public static ulong GamepadManager_CheckUnactivatedGamepads_RVAc2c564(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12764616 = default(uint);
        uint __arm64_flags_right_12764616 = default(uint);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x110UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C5AC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x110UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2C5AC;
        label_0xC2C5AC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xF8UL))));
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2C5C4;
        label_0xC2C5C4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12764616 = unchecked((uint)(x20));
        __arm64_flags_right_12764616 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764616) - (__arm64_flags_right_12764616))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12764616)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12764616)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764616) - (__arm64_flags_right_12764616))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12764616)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C63C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        x21 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C62C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C62C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x22UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C62C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C62C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC2E278UL /* metadata target: GamepadManager.Gamepad.AnyInternalKeyPressed */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C61C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC2E2E4UL /* metadata target: GamepadManager.Gamepad.AnyInternalAxisPressed */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C62C;
        }
        else
        {
            goto label_0xC2C61C;
        }
        label_0xC2C61C:
        ;
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC2CB58UL /* metadata target: GamepadManager.ActivateGamepad */, x0, x1, x2, x3);
        x22 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2C62C;
        label_0xC2C62C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2C5C4;
        }
        else
        {
            goto label_0xC2C638;
        }
        label_0xC2C638:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2C63C;
        label_0xC2C63C:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) & (unchecked((uint)(x0)))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C680;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C680;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC2C680:
        ;
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

## `GamepadManager.ConnectJoysticks` — RVA `0xc2c690`

- Lift status: **exact**; input span: 552 bytes; span to next metadata RVA: 552 bytes.
- Metadata signature: `private void ConnectJoysticks() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=87 (informational only).

```csharp
public static ulong GamepadManager_ConnectJoysticks_RVAc2c690(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12764972 = default(uint);
        uint __arm64_flags_left_12765268 = default(uint);
        uint __arm64_flags_right_12764972 = default(uint);
        uint __arm64_flags_right_12765268 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x10FUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C6E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2C6E0;
        label_0xC2C6E0:
        ;
        x0 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x38UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0x17C7518UL /* metadata target: Input.GetJoystickNames */, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x90UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xFFFFFFFFFFFFFFE8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C79C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x23 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF8UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x28UL))));
        x25 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x24 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x26 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2C728;
        label_0xC2C728:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12764972 = unchecked((uint)(x20));
        __arm64_flags_right_12764972 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764972) - (__arm64_flags_right_12764972))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12764972)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12764972)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12764972) - (__arm64_flags_right_12764972))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12764972)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2C7A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C79C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        x21 = x0;
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C790;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x30UL))))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2C8B8UL /* metadata target: GamepadManager.GetConnectedDeviceName */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C77C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x30UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x26))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x24 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) | (unchecked((uint)(x24)))))));
        goto label_0xC2C790;
        label_0xC2C77C:
        ;
        x2 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC2BC64UL /* metadata target: GamepadManager.DisconnectGamepad */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2C790;
        label_0xC2C790:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2C728;
        }
        else
        {
            goto label_0xC2C79C;
        }
        label_0xC2C79C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2C7A0;
        label_0xC2C7A0:
        ;
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2C7A4;
        label_0xC2C7A4:
        ;
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0xC2C8B8UL /* metadata target: GamepadManager.GetConnectedDeviceName */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = 0x0UL;
        x22 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x13F6920UL /* metadata target: String.IsNullOrEmpty */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x24))) >> (int)(unchecked((int)(unchecked((uint)(x20)))))))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xC2CA60UL /* metadata target: GamepadManager.FindDisconnectedGamepad */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x0;
        if ((x0 != 0x0UL))
        {
            goto label_0xC2C7F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2C93CUL /* metadata target: GamepadManager.AddConnectedGamepad */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x21 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C850;
        }
        else
        {
            goto label_0xC2C7F0;
        }
        label_0xC2C7F0:
        ;
        x0 = x21;
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xC2CF60UL /* metadata target: GamepadManager.Gamepad.ConnectToJoy */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xC2D0A4UL /* metadata target: GamepadManager.GetProfileForDevice */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C81C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC2D0FCUL /* metadata target: GamepadManager.Gamepad.SetProfile */, x0, x1, x2, x3);
        goto label_0xC2C81C;
        label_0xC2C81C:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C84C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C84C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x21;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC2C84C;
        label_0xC2C84C:
        ;
        x25 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC2C850;
        label_0xC2C850:
        ;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_12765268 = unchecked((uint)(x20));
        __arm64_flags_right_12765268 = unchecked((uint)0x4UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12765268) - (__arm64_flags_right_12765268))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC2C7A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C85CUL);
        }
        if ((unchecked((uint)((unchecked((uint)(x25))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C8A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2C8A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C8A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC2C8A0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.GetConnectedDeviceName` — RVA `0xc2c8b8`

- Lift status: **partial**; input span: 132 bytes; span to next metadata RVA: 132 bytes.
- Metadata signature: `private string GetConnectedDeviceName(int internalJoyId) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=19 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ls' at 0xc2c900; reason: Unknown IR expression at 0xc2c900

```csharp
public static ulong GamepadManager_GetConnectedDeviceName_RVAc2c8b8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12765432 = default(uint);
        uint __arm64_flags_right_12765432 = default(uint);
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
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x108UL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C8E8;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x108UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2C8E8;
        label_0xC2C8E8:
        ;
        if ((unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C918;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2C918;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12765432 = unchecked((uint)(x9));
        __arm64_flags_right_12765432 = unchecked((uint)(x19));
        if (((unchecked((uint)((__arm64_flags_left_12765432) - (__arm64_flags_right_12765432))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12765432) - (__arm64_flags_right_12765432))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12765432)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12765432)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12765432) - (__arm64_flags_right_12765432))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12765432)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2C918;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2C900UL);
        }
        RuntimeCalls.Unsupported("b.ls", 0xC2C900UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC2C938;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2C918;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x10UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C92C;
        }
        else
        {
            goto label_0xC2C918;
        }
        label_0xC2C918:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x48UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        goto label_0xC2C92C;
        label_0xC2C92C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC2C938:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.AddConnectedGamepad` — RVA `0xc2c93c`

- Lift status: **exact**; input span: 292 bytes; span to next metadata RVA: 292 bytes.
- Metadata signature: `private GamepadManager.Gamepad AddConnectedGamepad() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=46 (informational only).

```csharp
public static ulong GamepadManager_AddConnectedGamepad_RVAc2c93c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12765592 = default(uint);
        uint __arm64_flags_left_12765704 = default(uint);
        uint __arm64_flags_result_12765592 = default(uint);
        uint __arm64_flags_right_12765592 = default(uint);
        uint __arm64_flags_right_12765704 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x109UL))))))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2C98C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x100UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x109UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2C98C;
        label_0xC2C98C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x70UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CA5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12765592 = unchecked((uint)(x8));
        __arm64_flags_right_12765592 = unchecked((uint)0x1UL);
        __arm64_flags_result_12765592 = unchecked((uint)((__arm64_flags_left_12765592) - (__arm64_flags_right_12765592)));
        x1 = unchecked((ulong)(__arm64_flags_result_12765592));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12765592) - (__arm64_flags_right_12765592))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12765592)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12765592)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12765592) - (__arm64_flags_right_12765592))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12765592)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2CA30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF8UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x70UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2CA5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x100UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x19 = x0;
        x0 = x8;
        x2 = RuntimeMemory.ReadU64(x9);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) - (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x10A48FCUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CA5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x78UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2CA5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12765704 = unchecked((uint)(x10));
        __arm64_flags_right_12765704 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12765704 >= __arm64_flags_right_12765704))
        {
            goto label_0xC2CA38;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x19);
        x0 = x8;
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC2CA4C;
        label_0xC2CA30:
        ;
        x19 = 0x0UL;
        goto label_0xC2CA4C;
        label_0xC2CA38:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3390UL, x0, x1, x2, x3);
        goto label_0xC2CA4C;
        label_0xC2CA4C:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2CA5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.FindDisconnectedGamepad` — RVA `0xc2ca60`

- Lift status: **partial**; input span: 248 bytes; span to next metadata RVA: 248 bytes.
- Metadata signature: `private GamepadManager.Gamepad FindDisconnectedGamepad(int internalJoyId, string deviceName) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=33 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xc2cb00; reason: Unknown IR expression at 0xc2cb00

```csharp
public static ulong GamepadManager_FindDisconnectedGamepad_RVAc2ca60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12765900 = default(uint);
        ulong __arm64_flags_left_12765940 = default(ulong);
        uint __arm64_flags_left_12765968 = default(uint);
        ulong __arm64_flags_left_12765976 = default(ulong);
        ulong __arm64_flags_left_12766000 = default(ulong);
        uint __arm64_flags_right_12765900 = default(uint);
        ulong __arm64_flags_right_12765940 = default(ulong);
        uint __arm64_flags_right_12765968 = default(uint);
        ulong __arm64_flags_right_12765976 = default(ulong);
        ulong __arm64_flags_right_12766000 = default(ulong);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x25 = default(ulong);
        ulong x26 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10AUL))))))));
        x19 = x2;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CAAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x10AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2CAAC;
        label_0xC2CAAC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CB2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xF8UL))));
        x24 = 0x0UL;
        x25 = 0x0UL;
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2CAC8;
        label_0xC2CAC8:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12765900 = unchecked((uint)(x22));
        __arm64_flags_right_12765900 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12765900) - (__arm64_flags_right_12765900))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12765900)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12765900)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12765900) - (__arm64_flags_right_12765900))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12765900)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2CB30;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x26);
        x1 = unchecked((ulong)(unchecked((uint)(x22))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CB2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x21UL))))))));
        x23 = x0;
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CB20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x28UL))));
        __arm64_flags_left_12765940 = x24;
        __arm64_flags_right_12765940 = 0x0UL;
        x1 = x19;
        x2 = 0x0UL;
        RuntimeCalls.Unsupported("csel", 0xC2CB00UL);
        x24 = (__Unsupported<bool>("Unknown IR expression") ? x23 : x24);
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CB20;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x23) + (0x30UL))))));
        __arm64_flags_left_12765968 = unchecked((uint)(x8));
        __arm64_flags_right_12765968 = unchecked((uint)(x20));
        if ((unchecked((uint)((__arm64_flags_left_12765968) - (__arm64_flags_right_12765968))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CB50;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2CB18UL);
        }
        __arm64_flags_left_12765976 = x25;
        __arm64_flags_right_12765976 = 0x0UL;
        x25 = ((unchecked((ulong)((__arm64_flags_left_12765976) - (__arm64_flags_right_12765976))) == 0x0UL) ? x23 : x25);
        goto label_0xC2CB20;
        label_0xC2CB20:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x78UL))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2CAC8;
        }
        else
        {
            goto label_0xC2CB2C;
        }
        label_0xC2CB2C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC2CB30;
        label_0xC2CB30:
        ;
        __arm64_flags_left_12766000 = x25;
        __arm64_flags_right_12766000 = 0x0UL;
        x0 = ((unchecked((ulong)((__arm64_flags_left_12766000) - (__arm64_flags_right_12766000))) == 0x0UL) ? x24 : x25);
        goto label_0xC2CB38;
        label_0xC2CB38:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2CB50:
        ;
        x0 = x23;
        goto label_0xC2CB38;
        return default(ulong);
    }
```

## `GamepadManager.ActivateGamepad` — RVA `0xc2cb58`

- Lift status: **exact**; input span: 508 bytes; span to next metadata RVA: 508 bytes.
- Metadata signature: `private void ActivateGamepad(GamepadManager.Gamepad g) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=76 (informational only).

```csharp
public static ulong GamepadManager_ActivateGamepad_RVAc2cb58(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12766172 = default(uint);
        uint __arm64_flags_left_12766212 = default(uint);
        uint __arm64_flags_left_12766332 = default(uint);
        uint __arm64_flags_right_12766172 = default(uint);
        uint __arm64_flags_right_12766212 = default(uint);
        uint __arm64_flags_right_12766332 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x10BUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CBBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x78UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x108UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x10BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2CBBC;
        label_0xC2CBBC:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC2CD44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x34UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xF8UL))));
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CBF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12766172 = unchecked((uint)(x21));
        __arm64_flags_right_12766172 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12766172) - (__arm64_flags_right_12766172))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12766172)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12766172)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12766172) - (__arm64_flags_right_12766172))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12766172)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2CBF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CCC4;
        }
        else
        {
            goto label_0xC2CBF4;
        }
        label_0xC2CBF4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2CC00;
        label_0xC2CC00:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12766212 = unchecked((uint)(x21));
        __arm64_flags_right_12766212 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12766212) - (__arm64_flags_right_12766212))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12766212)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12766212)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12766212) - (__arm64_flags_right_12766212))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12766212)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2CC58;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CC2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2CC00;
        }
        else
        {
            goto label_0xC2CC28;
        }
        label_0xC2CC28:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2CC2C;
        label_0xC2CC2C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x108UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = x19;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A3114UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CCE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CC28;
        }
        else
        {
            goto label_0xC2CC58;
        }
        label_0xC2CC58:
        ;
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x78UL))));
        x21 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x0) + (0x18UL)))) + (0x4UL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2CC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12766332 = unchecked((uint)(x21));
        __arm64_flags_right_12766332 = unchecked((uint)(x10));
        if ((__arm64_flags_left_12766332 >= __arm64_flags_right_12766332))
        {
            goto label_0xC2CCA8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((int)(unchecked((uint)(x21))))));
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x10)));
        x0 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x19);
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CCE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2CCA4UL);
        }
        goto label_0xC2CD44;
        label_0xC2CCA8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3390UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CCE4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC2CCC0UL);
        }
        goto label_0xC2CD44;
        label_0xC2CCC4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CC28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x108UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x2 = x19;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A3114UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2CCE4;
        label_0xC2CCE4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x34UL))), unchecked((uint)(x21)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x20UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0xC2DB9CUL /* metadata target: GamepadManager.Gamepad.Reset */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC2CD64UL /* metadata target: GamepadManager.CountActiveGamepads */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CD44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2CD44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC2CD44:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.CountActiveGamepads` — RVA `0xc2cd64`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `private void CountActiveGamepads() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=21 (informational only).

```csharp
public static ulong GamepadManager_CountActiveGamepads_RVAc2cd64(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12766648 = default(uint);
        uint __arm64_flags_right_12766648 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x10DUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CD9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x10DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2CD9C;
        label_0xC2CD9C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x88UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CDE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF8UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2CDB4;
        label_0xC2CDB4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12766648 = unchecked((uint)(x20));
        __arm64_flags_right_12766648 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12766648) - (__arm64_flags_right_12766648))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12766648)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12766648)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12766648) - (__arm64_flags_right_12766648))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12766648)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2CDEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CDDC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x88UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x88UL))), unchecked((uint)(x8)));
        goto label_0xC2CDDC;
        label_0xC2CDDC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2CDB4;
        }
        else
        {
            goto label_0xC2CDE8;
        }
        label_0xC2CDE8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC2CDEC;
        label_0xC2CDEC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.DisactivateGamepad` — RVA `0xc2cdf8`

- Lift status: **exact**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `private void DisactivateGamepad(GamepadManager.Gamepad g, GamepadManager.DisconnectionReason reason) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=43 (informational only).

```csharp
public static ulong GamepadManager_DisactivateGamepad_RVAc2cdf8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
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
        x22 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x10CUL))))))));
        x21 = unchecked((ulong)(unchecked((uint)(x2))));
        x20 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CE48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x110UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x108UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x10CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2CE48;
        label_0xC2CE48:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC2CEF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CEF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2CE90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2CE90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x1 = x20;
        x2 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2CE90;
        label_0xC2CE90:
        ;
        x0 = x20;
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x20UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC2DB9CUL /* metadata target: GamepadManager.Gamepad.Reset */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CF00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x110UL))));
        x1 = x20;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A3DC8UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2CEF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2CF00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x108UL))));
        x2 = 0x0UL;
        x3 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A3114UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xC2CD64UL /* metadata target: GamepadManager.CountActiveGamepads */);
        label_0xC2CEF0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC2CF00:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.GetProfileForDevice` — RVA `0xc2d0a4`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private GamepadProfile GetProfileForDevice(string joyDevice) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong GamepadManager_GetProfileForDevice_RVAc2d0a4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x19 = x1;
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D0C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2D4E8UL /* metadata target: CustomGamepadProfileBank.GetProfile */, x0, x1, x2, x3);
        if ((x0 != 0x0UL))
        {
            goto label_0xC2D0F4;
        }
        else
        {
            goto label_0xC2D0C0;
        }
        label_0xC2D0C0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC30B88UL /* metadata target: BuiltInGamepadProfileBank.Inst */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D0DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        if ((x0 != 0x0UL))
        {
            goto label_0xC2D0F4;
        }
        else
        {
            goto label_0xC2D0DC;
        }
        label_0xC2D0DC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xC30B88UL /* metadata target: BuiltInGamepadProfileBank.Inst */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D0F4;
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
        label_0xC2D0F4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.GetGamepadSlotCount` — RVA `0xc2d264`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public int GetGamepadSlotCount() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static uint GamepadManager_GetGamepadSlotCount_RVAc2d264(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x111UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x111UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2D290:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x8 == 0x0UL))
        {
            label_0xC2D2A8:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `GamepadManager.GetActiveGamepadCount` — RVA `0xc2d2ac`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public int GetActiveGamepadCount() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static uint GamepadManager_GetActiveGamepadCount_RVAc2d2ac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x88UL))))));
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `GamepadManager.GetGamepadAtSlot` — RVA `0xc2d2b4`

- Lift status: **exact**; input span: 132 bytes; span to next metadata RVA: 132 bytes.
- Metadata signature: `public GamepadManager.Gamepad GetGamepadAtSlot(int slot) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong GamepadManager_GetGamepadAtSlot_RVAc2d2b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12768000 = default(uint);
        uint __arm64_flags_right_12768000 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x112UL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2D2F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x112UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2D2F0;
        label_0xC2D2F0:
        ;
        if ((unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2D324;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D334;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12768000 = unchecked((uint)(x8));
        __arm64_flags_right_12768000 = unchecked((uint)(x19));
        if (((unchecked((uint)((__arm64_flags_left_12768000) - (__arm64_flags_right_12768000))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12768000) - (__arm64_flags_right_12768000))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12768000)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12768000)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12768000) - (__arm64_flags_right_12768000))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12768000)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2D324;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x10A30C0UL);
        label_0xC2D324:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC2D334:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.GetCombinedGamepad` — RVA `0xc2d338`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public GamepadManager.Gamepad GetCombinedGamepad() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GamepadManager_GetCombinedGamepad_RVAc2d338(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x80UL))));
        return x0;
        return default(ulong);
    }
```

## `GamepadManager.GetConnectedGamepadCount` — RVA `0xc2d340`

- Lift status: **exact**; input span: 72 bytes; span to next metadata RVA: 72 bytes.
- Metadata signature: `public int GetConnectedGamepadCount() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static uint GamepadManager_GetConnectedGamepadCount_RVAc2d340(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x113UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x113UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC2D36C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x78UL))));
        if ((x8 == 0x0UL))
        {
            label_0xC2D384:
            ;
            x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        }
        else
        {
            x0 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
            x30 = RuntimeMemory.ReadU64(sp);
            return unchecked((uint)(x0));
        }
        return default(uint);
    }
```

## `GamepadManager.GetConnectedGamepad` — RVA `0xc2d388`

- Lift status: **exact**; input span: 132 bytes; span to next metadata RVA: 132 bytes.
- Metadata signature: `public GamepadManager.Gamepad GetConnectedGamepad(int index) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong GamepadManager_GetConnectedGamepad_RVAc2d388(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12768212 = default(uint);
        uint __arm64_flags_right_12768212 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x114UL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2D3C4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x114UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2D3C4;
        label_0xC2D3C4:
        ;
        if ((unchecked((uint)((unchecked((uint)(x19))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x1FUL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2D3F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x78UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D408;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12768212 = unchecked((uint)(x8));
        __arm64_flags_right_12768212 = unchecked((uint)(x19));
        if (((unchecked((uint)((__arm64_flags_left_12768212) - (__arm64_flags_right_12768212))) == unchecked((uint)0x0UL)) || ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12768212) - (__arm64_flags_right_12768212))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12768212)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12768212)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12768212) - (__arm64_flags_right_12768212))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12768212)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC2D3F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xF8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(x19))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x10A30C0UL);
        label_0xC2D3F8:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC2D408:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `GamepadManager.DisactivateGamepads` — RVA `0xc2d40c`

- Lift status: **exact**; input span: 220 bytes; span to next metadata RVA: 220 bytes.
- Metadata signature: `public void DisactivateGamepads() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=35 (informational only).

```csharp
public static ulong GamepadManager_DisactivateGamepads_RVAc2d40c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12768360 = default(uint);
        uint __arm64_flags_right_12768360 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x115UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2D450;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x115UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2D450;
        label_0xC2D450:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D49C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xF8UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC2D464;
        label_0xC2D464:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12768360 = unchecked((uint)(x20));
        __arm64_flags_right_12768360 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12768360) - (__arm64_flags_right_12768360))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12768360)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12768360)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12768360) - (__arm64_flags_right_12768360))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12768360)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC2D4A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x21);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D490;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x0;
        x0 = x19;
        x2 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x0 = RuntimeCalls.InvokeDirect(0xC2CDF8UL /* metadata target: GamepadManager.DisactivateGamepad */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2D490;
        label_0xC2D490:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x68UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC2D464;
        }
        else
        {
            goto label_0xC2D49C;
        }
        label_0xC2D49C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC2D4A0;
        label_0xC2D4A0:
        ;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC2B5FCUL /* metadata target: GamepadManager.IsMain */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC2D4DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC2D4DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC2D4DC:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```
