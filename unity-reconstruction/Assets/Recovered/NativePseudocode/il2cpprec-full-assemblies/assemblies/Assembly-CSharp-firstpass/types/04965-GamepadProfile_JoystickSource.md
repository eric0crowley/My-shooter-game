# `GamepadProfile.JoystickSource` — TypeDefIndex 4965

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `GamepadProfile.KeySource` | `keyU` |
| `0x18` | `GamepadProfile.KeySource` | `keyD` |
| `0x20` | `GamepadProfile.KeySource` | `keyR` |
| `0x28` | `GamepadProfile.KeySource` | `keyL` |

## `GamepadProfile.JoystickSource.ctor` — RVA `0xc2fcfc`

- Lift status: **exact**; input span: 276 bytes; span to next metadata RVA: 276 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=34 (informational only).

```csharp
public static ulong GamepadProfile_JoystickSource_ctor_RVAc2fcfc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x12AUL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x218UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC2FD34;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x218UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x12AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC2FD34;
        label_0xC2FD34:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL) | RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x22 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x18UL))), unchecked((byte)(unchecked((uint)(x22)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL) | RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = x19;
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x18UL))), unchecked((byte)(unchecked((uint)(x22)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x10UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL) | RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = x19;
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x18UL))), unchecked((byte)(unchecked((uint)(x22)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL) | RuntimeVector128.Zero.WithUInt64(0, 0xFFFFFFFFFFFFFFFFUL).ShiftLeftLogical(unchecked((int)0x40UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x20) + (0x10UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x18UL))), unchecked((byte)(unchecked((uint)(x22)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x20UL))), x20);
        x0 = x19;
        x1 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```

## `GamepadProfile.JoystickSource.IsDuplicateOf` — RVA `0xc3010c`

- Lift status: **exact**; input span: 124 bytes; span to next metadata RVA: 124 bytes.
- Metadata signature: `public bool IsDuplicateOf(GamepadProfile.JoystickSource a) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static uint GamepadProfile_JoystickSource_IsDuplicateOf_RVAc3010c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        if ((x1 == 0x0UL))
        {
            goto label_0xC30184;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC30184;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x19 = x1;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x1) + (0x18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC300C0UL /* metadata target: GamepadProfile.KeySource.IsDuplicateOf */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC30174;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC30184;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC300C0UL /* metadata target: GamepadProfile.KeySource.IsDuplicateOf */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC30174;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC30184;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC300C0UL /* metadata target: GamepadProfile.KeySource.IsDuplicateOf */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC30174;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC30184;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC300C0UL /* metadata target: GamepadProfile.KeySource.IsDuplicateOf */)));
        label_0xC30174:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        label_0xC30184:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `GamepadProfile.JoystickSource.Empty` — RVA `0xc3047c`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `public static GamepadProfile.JoystickSource Empty() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=12 (informational only).

```csharp
public static ulong GamepadProfile_JoystickSource_Empty_RVAc3047c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x12DUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x210UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x210UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x12DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC304AC:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2FCFCUL /* metadata target: GamepadProfile.JoystickSource.ctor */, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GamepadProfile.JoystickSource.Dpad` — RVA `0xc304f4`

- Lift status: **exact**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `public static GamepadProfile.JoystickSource Dpad(int keyU, int keyR, int keyD, int keyL) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong GamepadProfile_JoystickSource_Dpad_RVAc304f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        x21 = 0x1BAB000UL;
        x24 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x12BUL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x210UL))));
        x20 = unchecked((ulong)(unchecked((uint)(x3))));
        x23 = unchecked((ulong)(unchecked((uint)(x2))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x210UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x12BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC3053C:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2FCFCUL /* metadata target: GamepadProfile.JoystickSource.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
        }
        else
        {
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
            if ((x9 == 0x0UL))
            {
            }
            else
            {
                x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
                x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x23)));
                RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x8)));
                RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x18UL))), unchecked((byte)(unchecked((uint)(x10)))));
                x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
                if ((x9 == 0x0UL))
                {
                }
                else
                {
                    RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x22)));
                    RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x8)));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x18UL))), unchecked((byte)(unchecked((uint)(x10)))));
                    x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
                    if ((x9 == 0x0UL))
                    {
                    }
                    else
                    {
                        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
                        x10 = unchecked((ulong)(unchecked((uint)(0x1UL))));
                        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x20)));
                        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x8)));
                        RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x18UL))), unchecked((byte)(unchecked((uint)(x10)))));
                        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
                        if ((x9 == 0x0UL))
                        {
                        }
                        else
                        {
                            RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x19)));
                            RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x9) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x8)));
                            x0 = x21;
                            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
                            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
                            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
                            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
                            x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
                            RuntimeMemory.WriteU8(unchecked((ulong)((x9) + (0x18UL))), unchecked((byte)(unchecked((uint)(x10)))));
                            x30 = RuntimeMemory.ReadU64(sp);
                            return x0;
                        }
                    }
                }
            }
        }
        label_0xC305B8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GamepadProfile.JoystickSource.Axes` — RVA `0xc305d0`

- Lift status: **exact**; input span: 200 bytes; span to next metadata RVA: 200 bytes.
- Metadata signature: `public static GamepadProfile.JoystickSource Axes(int horzAxisId, bool horzPositiveRight, int vertAxisId, bool vertPositiveUp) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong GamepadProfile_JoystickSource_Axes_RVAc305d0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        x21 = 0x1BAB000UL;
        x24 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x12CUL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x210UL))));
        x20 = unchecked((ulong)(unchecked((uint)(x3))));
        x19 = unchecked((ulong)(unchecked((uint)(x2))));
        x23 = unchecked((ulong)(unchecked((uint)(x1))));
        x22 = unchecked((ulong)(unchecked((uint)(x0))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x210UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x12CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC30618:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC2FCFCUL /* metadata target: GamepadProfile.JoystickSource.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
        }
        else
        {
            x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x20UL))));
            if ((x10 == 0x0UL))
            {
            }
            else
            {
                x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x23))) & (unchecked((uint)(0x1UL)))))));
                x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
                RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x9)));
                RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x22)));
                RuntimeMemory.WriteU8(unchecked((ulong)((x10) + (0x18UL))), unchecked((byte)(unchecked((uint)(x8)))));
                x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x28UL))));
                if ((x10 == 0x0UL))
                {
                }
                else
                {
                    RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x9)));
                    RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x22)));
                    RuntimeMemory.WriteU8(unchecked((ulong)((x10) + (0x18UL))), unchecked((byte)(unchecked((uint)(x8)))));
                    x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x10UL))));
                    if ((x10 == 0x0UL))
                    {
                    }
                    else
                    {
                        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) & (unchecked((uint)(0x1UL)))))));
                        x9 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
                        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x9)));
                        RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x19)));
                        RuntimeMemory.WriteU8(unchecked((ulong)((x10) + (0x18UL))), unchecked((byte)(unchecked((uint)(x8)))));
                        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
                        if ((x10 == 0x0UL))
                        {
                        }
                        else
                        {
                            RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x0UL))), unchecked((uint)(x9)));
                            RuntimeMemory.WriteU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x10UL)))) + (0x4UL))), unchecked((uint)(x19)));
                            x0 = x21;
                            x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
                            x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
                            x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
                            x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
                            x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
                            x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
                            RuntimeMemory.WriteU8(unchecked((ulong)((x10) + (0x18UL))), unchecked((byte)(unchecked((uint)(x8)))));
                            x30 = RuntimeMemory.ReadU64(sp);
                            return x0;
                        }
                    }
                }
            }
        }
        label_0xC30694:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```
