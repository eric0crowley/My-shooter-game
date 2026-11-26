# `LevelSelection` — TypeDefIndex 3455

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `Button[]` | `levelButton` |
| `0x28` | `GameObject[]` | `CompleteImg` |
| `0x30` | `GameObject[]` | `Z_levelButton` |
| `0x38` | `GameObject[]` | `Z_CompleteImg` |
| `0x40` | `int` | `levelNum` |
| `0x44` | `int` | `unlockLevelNum` |
| `0x48` | `GameObject` | `loading` |
| `0x50` | `GameObject` | `particles` |

## `LevelSelection.OnEnable` — RVA `0xcc272c`

- Lift status: **exact**; input span: 368 bytes; span to next metadata RVA: 368 bytes.
- Metadata signature: `private void OnEnable() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=55 (informational only).

```csharp
public static ulong LevelSelection_OnEnable_RVAcc272c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13379524 = default(uint);
        uint __arm64_flags_left_13379572 = default(uint);
        uint __arm64_flags_left_13379596 = default(uint);
        uint __arm64_flags_left_13379644 = default(uint);
        uint __arm64_flags_right_13379524 = default(uint);
        uint __arm64_flags_right_13379572 = default(uint);
        uint __arm64_flags_right_13379596 = default(uint);
        uint __arm64_flags_right_13379644 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x30UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x51EUL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x878UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC2770;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x870UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x878UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x51EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC2770;
        label_0xCC2770:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((unchecked((uint)(x0)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC2798;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x8;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178F9E4UL /* metadata target: PlayerPrefs.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        goto label_0xCC2798;
        label_0xCC2798:
        ;
        x0 = x8;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x44UL))), unchecked((uint)(x0)));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCC2870;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x870UL))));
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCC27C0;
        label_0xCC27C0:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13379524 = unchecked((uint)(x8));
        __arm64_flags_right_13379524 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13379524) - (__arm64_flags_right_13379524))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13379524)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13379524)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13379524) - (__arm64_flags_right_13379524))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13379524)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCC2874;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13379572 = unchecked((uint)(x0));
        __arm64_flags_right_13379572 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13379572) - (__arm64_flags_right_13379572))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCC285C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCC2870;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((sp) + (0xCUL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13379596 = unchecked((uint)(x9));
        __arm64_flags_right_13379596 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13379596 >= __arm64_flags_right_13379596))
        {
            goto label_0xCC2898;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2870;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCC2870;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((sp) + (0xCUL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13379644 = unchecked((uint)(x9));
        __arm64_flags_right_13379644 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13379644 >= __arm64_flags_right_13379644))
        {
            goto label_0xCC2898;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2870;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC285C;
        label_0xCC285C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0xCUL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x9 != 0x0UL))
        {
            goto label_0xCC27C0;
        }
        else
        {
            goto label_0xCC2870;
        }
        label_0xCC2870:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC2874;
        label_0xCC2874:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x44UL))))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x40UL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0xCC289CUL /* metadata target: LevelSelection.unlockLevels */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        label_0xCC2898:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `LevelSelection.unlockLevels` — RVA `0xcc289c`

- Lift status: **exact**; input span: 196 bytes; span to next metadata RVA: 196 bytes.
- Metadata signature: `private void unlockLevels(int num) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static ulong LevelSelection_unlockLevels_RVAcc289c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13379748 = default(uint);
        uint __arm64_flags_left_13379780 = default(uint);
        uint __arm64_flags_left_13379872 = default(uint);
        uint __arm64_flags_left_13379908 = default(uint);
        uint __arm64_flags_right_13379748 = default(uint);
        uint __arm64_flags_right_13379780 = default(uint);
        uint __arm64_flags_right_13379872 = default(uint);
        uint __arm64_flags_right_13379908 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
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
        __arm64_flags_left_13379748 = unchecked((uint)(x1));
        __arm64_flags_right_13379748 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13379748) - (__arm64_flags_right_13379748))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13379748)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13379748)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13379748) - (__arm64_flags_right_13379748))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13379748)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCC294C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCC28B8;
        label_0xCC28B8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCC2958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13379780 = unchecked((uint)(x21));
        __arm64_flags_right_13379780 = unchecked((uint)(x9));
        if ((__arm64_flags_left_13379780 >= __arm64_flags_right_13379780))
        {
            goto label_0xCC295C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792154UL /* metadata target: Component.get_transform */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179ED7CUL /* metadata target: Transform.GetChild */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((unchecked((uint)(x21)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC2940;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCC2958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) - (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13379872 = unchecked((uint)(x9));
        __arm64_flags_right_13379872 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13379872 >= __arm64_flags_right_13379872))
        {
            goto label_0xCC295C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC2940;
        label_0xCC2940:
        ;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13379908 = unchecked((uint)(x19));
        __arm64_flags_right_13379908 = unchecked((uint)(x21));
        if ((!((unchecked((uint)((__arm64_flags_left_13379908) - (__arm64_flags_right_13379908))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCC28B8;
        }
        else
        {
            goto label_0xCC294C;
        }
        label_0xCC294C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xCC2958:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC295C;
        label_0xCC295C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `LevelSelection.unlock_Zombie_Levels` — RVA `0xcc2960`

- Lift status: **exact**; input span: 272 bytes; span to next metadata RVA: 272 bytes.
- Metadata signature: `private void unlock_Zombie_Levels() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=37 (informational only).

```csharp
public static ulong LevelSelection_unlock_Zombie_Levels_RVAcc2960(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13380008 = default(uint);
        uint __arm64_flags_left_13380056 = default(uint);
        uint __arm64_flags_left_13380080 = default(uint);
        uint __arm64_flags_left_13380116 = default(uint);
        uint __arm64_flags_left_13380136 = default(uint);
        uint __arm64_flags_result_13380116 = default(uint);
        uint __arm64_flags_right_13380008 = default(uint);
        uint __arm64_flags_right_13380056 = default(uint);
        uint __arm64_flags_right_13380080 = default(uint);
        uint __arm64_flags_right_13380116 = default(uint);
        uint __arm64_flags_right_13380136 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x51FUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC298C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x870UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x51FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC298C;
        label_0xCC298C:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0xCUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCC2A5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x870UL))));
        x8 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCC29A4;
        label_0xCC29A4:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13380008 = unchecked((uint)(x8));
        __arm64_flags_right_13380008 = unchecked((uint)(x9));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13380008) - (__arm64_flags_right_13380008))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13380008)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13380008)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13380008) - (__arm64_flags_right_13380008))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13380008)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCC2A60;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        __arm64_flags_left_13380056 = unchecked((uint)(x0));
        __arm64_flags_right_13380056 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13380056) - (__arm64_flags_right_13380056))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCC2A10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xCC2A5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((sp) + (0xCUL))))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13380080 = unchecked((uint)(x9));
        __arm64_flags_right_13380080 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13380080 >= __arm64_flags_right_13380080))
        {
            goto label_0xCC2A6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x9) << (int)(unchecked((int)(0x3UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2A5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC2A10;
        label_0xCC2A10:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0xCUL))))));
        __arm64_flags_left_13380116 = unchecked((uint)(x9));
        __arm64_flags_right_13380116 = unchecked((uint)0x1UL);
        __arm64_flags_result_13380116 = unchecked((uint)((__arm64_flags_left_13380116) - (__arm64_flags_right_13380116)));
        x8 = unchecked((ulong)(__arm64_flags_result_13380116));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13380116) - (__arm64_flags_right_13380116))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13380116)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13380116)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13380116) - (__arm64_flags_right_13380116))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13380116)) < unchecked((int)0x0UL))))))
        {
            goto label_0xCC2A4C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xCC2A5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x9) + (0x18UL))))));
        __arm64_flags_left_13380136 = unchecked((uint)(x8));
        __arm64_flags_right_13380136 = unchecked((uint)(x10));
        if ((__arm64_flags_left_13380136 >= __arm64_flags_right_13380136))
        {
            goto label_0xCC2A6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x9) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x8))))) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2A5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((sp) + (0xCUL))))));
        goto label_0xCC2A4C;
        label_0xCC2A4C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x9 != 0x0UL))
        {
            goto label_0xCC29A4;
        }
        else
        {
            goto label_0xCC2A5C;
        }
        label_0xCC2A5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC2A60;
        label_0xCC2A60:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        label_0xCC2A6C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `LevelSelection.LevelCounter` — RVA `0xcc2a70`

- Lift status: **exact**; input span: 152 bytes; span to next metadata RVA: 152 bytes.
- Metadata signature: `public void LevelCounter(int levelNum) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=24 (informational only).

```csharp
public static ulong LevelSelection_LevelCounter_RVAcc2a70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x22 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x520UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE28UL))));
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC2AAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE28UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x520UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC2AAC;
        label_0xCC2AAC:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x178F9E4UL /* metadata target: PlayerPrefs.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2B04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC2B04;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xCC2B08UL /* metadata target: LevelSelection.WaitforLoading */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x1 = x0;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x1795D40UL /* metadata target: MonoBehaviour.StartCoroutine */);
        label_0xCC2B04:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `LevelSelection.WaitforLoading` — RVA `0xcc2b08`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private IEnumerator WaitforLoading() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong LevelSelection_WaitforLoading_RVAcc2b08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x521UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x930UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x930UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x521UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCC2B38:
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

## `LevelSelection.ctor` — RVA `0xcc2b88`

- Lift status: **exact**; input span: 16 bytes; span to next metadata RVA: 16 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=2 (informational only).

```csharp
public static ulong LevelSelection_ctor_RVAcc2b88(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x40UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
