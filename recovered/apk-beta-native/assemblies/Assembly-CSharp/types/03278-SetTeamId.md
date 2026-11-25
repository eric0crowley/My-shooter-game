# `SetTeamId` — TypeDefIndex 3278

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `int` | `myID` |
| `0x24` | `int` | `OpponentID` |
| `0x28` | `Text` | `RedCounter_Txt` |
| `0x30` | `Text` | `BlueCounter_Txt` |

## `SetTeamId.CountKill` — RVA `0xc6dd54`

- Lift status: **partial**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `public void CountKill() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=40 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'b.ne' at 0xc6de38; reason: Unknown IR expression at 0xc6de38; reason: Unsupported instruction 'cset' at 0xc6de44; reason: Unknown IR expression at 0xc6de44

```csharp
public static ulong SetTeamId_CountKill_RVAc6dd54(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13032856 = default(uint);
        uint __arm64_flags_left_13032864 = default(uint);
        uint __arm64_flags_left_13033000 = default(uint);
        uint __arm64_flags_left_13033008 = default(uint);
        uint __arm64_flags_left_13033020 = default(uint);
        uint __arm64_flags_right_13032856 = default(uint);
        uint __arm64_flags_right_13032864 = default(uint);
        uint __arm64_flags_right_13033000 = default(uint);
        uint __arm64_flags_right_13033008 = default(uint);
        uint __arm64_flags_right_13033020 = default(uint);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x36AUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC6DD8C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x510UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x428UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x36AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC6DD8C;
        label_0xC6DD8C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x510UL))));
        __arm64_flags_left_13032856 = unchecked((uint)(x8));
        __arm64_flags_right_13032856 = unchecked((uint)0x2UL);
        if ((unchecked((uint)((__arm64_flags_left_13032856) - (__arm64_flags_right_13032856))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6DDC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6DDA0UL);
        }
        __arm64_flags_left_13032864 = unchecked((uint)(x8));
        __arm64_flags_right_13032864 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13032864) - (__arm64_flags_right_13032864))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC6DE00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xCUL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(x0, unchecked((uint)(x8)));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        goto label_0xC6DDDC;
        label_0xC6DDC4:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x8UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(x0, unchecked((uint)(x8)));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        goto label_0xC6DDDC;
        label_0xC6DDDC:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x19 == 0x0UL))
        {
            goto label_0xC6DE5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x1 = x0;
        x0 = x19;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC6DE00;
        label_0xC6DE00:
        ;
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x428UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x8 = RuntimeMemory.ReadU64(x8);
        if ((x8 == 0x0UL))
        {
            goto label_0xC6DE5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(x20);
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x20UL))))));
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xB8UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x10) + (0x8UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x10) + (0x8UL)))) + (0x4UL))))));
        __arm64_flags_left_13033000 = unchecked((uint)(x9));
        __arm64_flags_right_13033000 = unchecked((uint)(x11));
        if ((unchecked((uint)((__arm64_flags_left_13033000) - (__arm64_flags_right_13033000))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC6DE3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC6DE30UL);
        }
        __arm64_flags_left_13033008 = unchecked((uint)(x10));
        __arm64_flags_right_13033008 = unchecked((uint)(x11));
        x10 = unchecked((ulong)(unchecked((uint)(x11))));
        RuntimeCalls.Unsupported("b.ne", 0xC6DE38UL);
        if (__Unsupported<bool>("Unknown IR expression"))
        {
            goto label_0xC6DE50;
        }
        else
        {
            goto label_0xC6DE3C;
        }
        label_0xC6DE3C:
        ;
        __arm64_flags_left_13033020 = unchecked((uint)(x9));
        __arm64_flags_right_13033020 = unchecked((uint)(x10));
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeCalls.Unsupported("cset", 0xC6DE44UL);
        x10 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x80UL))), unchecked((byte)(unchecked((uint)(x10)))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x108UL))), unchecked((byte)(unchecked((uint)(x9)))));
        goto label_0xC6DE50;
        label_0xC6DE50:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xC6DE5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `SetTeamId.DropGun` — RVA `0xc6de60`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public void DropGun() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong SetTeamId_DropGun_RVAc6de60(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `SetTeamId.Start` — RVA `0xc7247c`

- Lift status: **exact**; input span: 160 bytes; span to next metadata RVA: 160 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=27 (informational only).

```csharp
public static ulong SetTeamId_Start_RVAc7247c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
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
        x22 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x368UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x510UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x4F0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC724C8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x510UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x368UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC724C8;
        label_0xC724C8:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x8) + (0x8UL))), 0x0UL);
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x0);
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xC7251CUL /* metadata target: SetTeamId.SetIds */, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        return default(ulong);
    }
```

## `SetTeamId.SetIds` — RVA `0xc7251c`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private IEnumerator SetIds() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong SetTeamId_SetIds_RVAc7251c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x369UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x668UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x668UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x369UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xC7254C:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WritePtr(unchecked((ulong)((x19) + (0x10UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `SetTeamId.ctor` — RVA `0xc7259c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong SetTeamId_ctor_RVAc7259c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = 0x0UL;
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
