# `BuiltInGamepadProfileBank` — TypeDefIndex 4970

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `GamepadProfile[]` | `profiles` |
| `0x18` | `GamepadProfile` | `genericProfile` |

## `BuiltInGamepadProfileBank.GetProfile` — RVA `0xc2d590`

- Lift status: **exact**; input span: 44 bytes; span to next metadata RVA: 44 bytes.
- Metadata signature: `public static GamepadProfile GetProfile(string deviceName) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=6 (informational only).

```csharp
public static ulong BuiltInGamepadProfileBank_GetProfile_RVAc2d590(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC30B88UL /* metadata target: BuiltInGamepadProfileBank.Inst */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D5B4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = x19;
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x188UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x188UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeIndirect(x3);
        label_0xC2D5B4:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `BuiltInGamepadProfileBank.GetGenericProfile` — RVA `0xc2d5bc`

- Lift status: **exact**; input span: 36 bytes; span to next metadata RVA: 36 bytes.
- Metadata signature: `public static GamepadProfile GetGenericProfile() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=4 (informational only).

```csharp
public static ulong BuiltInGamepadProfileBank_GetGenericProfile_RVAc2d5bc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL))), x30);
        x0 = RuntimeCalls.InvokeDirect(0xC30B88UL /* metadata target: BuiltInGamepadProfileBank.Inst */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC2D5D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x0);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeIndirect(x2);
        label_0xC2D5D8:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `BuiltInGamepadProfileBank.ctor` — RVA `0xc30b80`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong BuiltInGamepadProfileBank_ctor_RVAc30b80(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */);
        return default(ulong);
    }
```

## `BuiltInGamepadProfileBank.Inst` — RVA `0xc30b88`

- Lift status: **exact**; input span: 440 bytes; span to next metadata RVA: 440 bytes.
- Metadata signature: `private static BuiltInGamepadProfileBank Inst() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=83 (informational only).

```csharp
public static ulong BuiltInGamepadProfileBank_Inst_RVAc30b88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12782652 = default(uint);
        uint __arm64_flags_left_12782744 = default(uint);
        uint __arm64_flags_right_12782652 = default(uint);
        uint __arm64_flags_right_12782744 = default(uint);
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
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x137UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x240UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC30C0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x248UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x250UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x258UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x260UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x268UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x270UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x278UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x240UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x137UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC30C0C;
        label_0xC30C0C:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        if ((x0 != 0x0UL))
        {
            goto label_0xC30D34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x248UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC30C34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30C30UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC30C34;
        label_0xC30C34:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176D5CCUL /* metadata target: Application.get_platform */, x0, x1, x2, x3);
        __arm64_flags_left_12782652 = unchecked((uint)(x0));
        __arm64_flags_right_12782652 = unchecked((uint)0x14UL);
        if (((__arm64_flags_left_12782652 >= __arm64_flags_right_12782652) && (!((unchecked((uint)((__arm64_flags_left_12782652) - (__arm64_flags_right_12782652))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xC30C98;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x432000UL;
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        x9 = unchecked((ulong)((x9) + (0x558UL)));
        x10 = 0xC30C60UL;
        x11 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)(x8))))))))))));
        x10 = unchecked((ulong)((x10) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x11))) << (int)(unchecked((int)(unchecked((uint)(0x2UL))))))))))));
        return RuntimeCalls.InvokeIndirect(x10);
        label_0xC30C98:
        ;
        __arm64_flags_left_12782744 = unchecked((uint)(x0));
        __arm64_flags_right_12782744 = unchecked((uint)0x1FUL);
        if ((!((unchecked((uint)((__arm64_flags_left_12782744) - (__arm64_flags_right_12782744))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC30D28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x258UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC32A68UL /* metadata target: BuiltInGamepadProfileBankIOS.ctor */, x0, x1, x2, x3);
        goto label_0xC30D0C;
        label_0xC30D0C:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x19);
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC30D28;
        label_0xC30D28:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        goto label_0xC30D34;
        label_0xC30D34:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `BuiltInGamepadProfileBank.GetInternalGenericProfile` — RVA `0xc30d40`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `protected virtual GamepadProfile GetInternalGenericProfile() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=16 (informational only).

```csharp
public static ulong BuiltInGamepadProfileBank_GetInternalGenericProfile_RVAc30d40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x136UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x280UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x136UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC30D6C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        if ((x0 != 0x0UL))
        {
        }
        else
        {
            x8 = 0x1A8C000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x280UL))));
            x0 = RuntimeMemory.ReadU64(x8);
            x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
            x20 = x0;
            x0 = RuntimeCalls.InvokeDirect(0xC30928UL /* metadata target: GamepadProfile.GenericProfile.ctor */, x0, x1, x2, x3);
            x0 = x19;
            x1 = x20;
            RuntimeMemory.WriteU64(x19, x20);
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
            x0 = RuntimeMemory.ReadU64(x19);
        }
        label_0xC30DA0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `BuiltInGamepadProfileBank.FindProfile` — RVA `0xc30dac`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `protected virtual GamepadProfile FindProfile(string deviceName) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong BuiltInGamepadProfileBank_FindProfile_RVAc30dac(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC30DB0UL /* metadata target: BuiltInGamepadProfileBank.FindInternalProfile */);
        return default(ulong);
    }
```

## `BuiltInGamepadProfileBank.FindInternalProfile` — RVA `0xc30db0`

- Lift status: **partial**; input span: 156 bytes; span to next metadata RVA: 156 bytes.
- Metadata signature: `protected GamepadProfile FindInternalProfile(string deviceName) { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=18 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'cmp' at 0xc30de0; reason: Unsupported instruction 'b.hs' at 0xc30de4; reason: Unknown IR expression at 0xc30de4; reason: Unsupported instruction 'cmp' at 0xc30e10; reason: Unsupported instruction 'b.lt' at 0xc30e14; reason: Unknown IR expression at 0xc30e14

```csharp
public static ulong BuiltInGamepadProfileBank_FindInternalProfile_RVAc30db0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12783056 = default(uint);
        uint __arm64_flags_left_12783152 = default(uint);
        uint __arm64_flags_right_12783056 = default(uint);
        uint __arm64_flags_right_12783152 = default(uint);
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
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC30E18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        x19 = x0;
        x0 = 0x0UL;
        if ((x9 == 0x0UL))
        {
            goto label_0xC30E1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30DD0UL);
        }
        __arm64_flags_left_12783056 = unchecked((uint)(x9));
        __arm64_flags_right_12783056 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12783056) - (__arm64_flags_right_12783056))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12783056)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12783056)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12783056) - (__arm64_flags_right_12783056))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12783056)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC30E1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x1;
        x21 = 0x0UL;
        goto label_0xC30DE0;
        label_0xC30DE0:
        ;
        RuntimeCalls.Unsupported("cmp", 0xC30DE0UL);
        RuntimeCalls.Unsupported("b.hs", 0xC30DE4UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC30E44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC30E08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC2FE74UL /* metadata target: GamepadProfile.IsCompatible */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC30E28;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC30E04UL);
        }
        if ((x8 == 0x0UL))
        {
            goto label_0xC30E48;
        }
        else
        {
            goto label_0xC30E08;
        }
        label_0xC30E08:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x21 = unchecked((ulong)((x21) + (0x1UL)));
        RuntimeCalls.Unsupported("cmp", 0xC30E10UL);
        RuntimeCalls.Unsupported("b.lt", 0xC30E14UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC30DE0;
        }
        else
        {
            goto label_0xC30E18;
        }
        label_0xC30E18:
        ;
        x0 = 0x0UL;
        goto label_0xC30E1C;
        label_0xC30E1C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC30E28:
        ;
        if ((x8 == 0x0UL))
        {
            goto label_0xC30E48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12783152 = unchecked((uint)(x21));
        __arm64_flags_right_12783152 = unchecked((uint)(x9));
        if ((__arm64_flags_left_12783152 >= __arm64_flags_right_12783152))
        {
            goto label_0xC30E44;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x21) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        goto label_0xC30E1C;
        label_0xC30E44:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xC30E48;
        label_0xC30E48:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
