# `MainMenu` — TypeDefIndex 3372

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `FPSPlayer` | `FPSPlayerComponent` |
| `0x28` | `bool` | `useMainMenu` |
| `0x29` | `bool` | `scaleWithScreenSize` |
| `0x30` | `GameObject[]` | `NpcGroups` |
| `0x38` | `Font` | `font` |
| `0x40` | `Color` | `GuiTint` |
| `0x50` | `Color` | `btnTextColor` |
| `0x60` | `Color` | `btnActiveTextColor` |
| `0x70` | `bool` | `initSyles` |
| `0x74` | `float` | `fontSizeScaled` |
| `0x78` | `float` | `titleFontSizeScaled` |
| `0x7C` | `int` | `fontSize` |
| `0x80` | `int` | `titleFontSize` |
| `0x84` | `float` | `menuPosV` |
| `0x88` | `float` | `menuPosH` |
| `0x8C` | `float` | `buttonHeight` |
| `0x90` | `float` | `buttonWidth` |
| `0x94` | `float` | `buttonHeightScaled` |
| `0x98` | `float` | `buttonWidthScaled` |
| `0x9C` | `float` | `buttonHeightAmt` |
| `0xA0` | `float` | `buttonWidthAmt` |
| `0xA4` | `float` | `buttonSpacing` |
| `0xA8` | `float` | `buttonV` |
| `0xAC` | `float` | `buttonH` |
| `0xB0` | `bool` | `menuDisplayed` |
| `0xB1` | `bool` | `resumePress` |
| `0xB2` | `bool` | `dzState` |
| `0xB3` | `bool` | `dzButtonState` |
| `0xB4` | `bool` | `invulButtonState` |
| `0xB5` | `bool` | `giveAllButtonState` |
| `0xB8` | `AudioSource` | `aSource` |
| `0xC0` | `AudioClip` | `buttonClickFx` |
| `0xC8` | `float` | `buttonFxVol` |
| `0xD0` | `AudioClip` | `invulClickFx` |
| `0xD8` | `float` | `invulFxVol` |
| `0xE0` | `AudioClip` | `giveAllClickFx` |
| `0xE8` | `float` | `giveAllFxVol` |
| `0xF0` | `AudioClip` | `beepClickFx` |
| `0xF8` | `float` | `beepFxVol` |
| `0x100` | `GUIStyleState` | `buttonActive` |
| `0x108` | `GUIStyleState` | `buttonInActive` |
| `0x110` | `GUIStyle` | `toggleButtonStyle1` |
| `0x118` | `GUIStyle` | `toggleButtonStyle2` |
| `0x120` | `GUIStyle` | `toggleButtonStyle3` |
| `0x128` | `GUIStyle` | `mainButtonSyle` |
| `0x130` | `GUIStyle` | `mapButtonStyle` |
| `0x138` | `bool` | `npcGoupsNull` |
| `0x140` | `GUIStyle` | `titleStyle` |
| `0x148` | `bool` | `hungerThirstActive` |

## `MainMenu.Start` — RVA `0xc9195c`

- Lift status: **exact**; input span: 664 bytes; span to next metadata RVA: 664 bytes.
- Metadata signature: `private void Start() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=94 (informational only).

```csharp
public static ulong MainMenu_Start_RVAc9195c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13179604 = default(uint);
        uint __arm64_flags_left_13179664 = default(uint);
        uint __arm64_flags_left_13179724 = default(uint);
        uint __arm64_flags_left_13179736 = default(uint);
        uint __arm64_flags_left_13179776 = default(uint);
        uint __arm64_flags_left_13179816 = default(uint);
        uint __arm64_flags_right_13179604 = default(uint);
        uint __arm64_flags_right_13179664 = default(uint);
        uint __arm64_flags_right_13179724 = default(uint);
        uint __arm64_flags_right_13179736 = default(uint);
        uint __arm64_flags_right_13179776 = default(uint);
        uint __arm64_flags_right_13179816 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x455UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC919B8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xAB0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x120UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x455UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC919B8;
        label_0xC919B8:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176F8DCUL /* metadata target: Camera.get_main */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCD8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5A0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE49224UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x20UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1792190UL /* metadata target: Component.get_gameObject */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xAB0UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE4913CUL, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0xB8UL))), x0);
        x1 = x0;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176AAA8UL /* metadata target: AudioSource.set_spatialBlend */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91A54UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176AB7CUL /* metadata target: AudioSource.set_playOnAwake */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        if ((x8 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x24CUL))))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x148UL))), unchecked((byte)(unchecked((uint)(x9)))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x18UL))));
        if ((x9 == 0x0UL))
        {
            goto label_0xC91BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91A94UL);
        }
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91BF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        x0 = RuntimeMemory.ReadU64(x21);
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC91AB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91AB0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC91AB4;
        label_0xC91AB4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13179604 = unchecked((uint)(x9));
        __arm64_flags_right_13179604 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13179604 >= __arm64_flags_right_13179604))) || (unchecked((uint)((__arm64_flags_left_13179604) - (__arm64_flags_right_13179604))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC91BF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x28UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC91AF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91AECUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC91AF0;
        label_0xC91AF0:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_13179664 = unchecked((uint)(x9));
        __arm64_flags_right_13179664 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13179664 >= __arm64_flags_right_13179664))) || (unchecked((uint)((__arm64_flags_left_13179664) - (__arm64_flags_right_13179664))) == unchecked((uint)0x0UL))))
        {
            goto label_0xC91BF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC91B2C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91B28UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC91B2C;
        label_0xC91B2C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91BCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13179724 = unchecked((uint)(x8));
        __arm64_flags_right_13179724 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13179724) - (__arm64_flags_right_13179724))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13179724)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13179724)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13179724) - (__arm64_flags_right_13179724))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13179724)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC91B88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC91B58;
        label_0xC91B58:
        ;
        __arm64_flags_left_13179736 = unchecked((uint)(x21));
        __arm64_flags_right_13179736 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13179736 >= __arm64_flags_right_13179736))
        {
            goto label_0xC91BF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        __arm64_flags_left_13179776 = unchecked((uint)(x21));
        __arm64_flags_right_13179776 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_13179776) - (__arm64_flags_right_13179776))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_13179776)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13179776)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13179776) - (__arm64_flags_right_13179776))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13179776)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC91B58;
        }
        else
        {
            goto label_0xC91B88;
        }
        label_0xC91B88:
        ;
        x8 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x120UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13179816 = unchecked((uint)(x0));
        __arm64_flags_right_13179816 = unchecked((uint)(x8));
        if ((__arm64_flags_left_13179816 >= __arm64_flags_right_13179816))
        {
            goto label_0xC91BF0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)((x20) + (unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) << (int)(unchecked((int)(unchecked((uint)(0x3UL))))))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x20UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC91BEC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC91BD4;
        label_0xC91BCC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x138UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC91BD4;
        label_0xC91BD4:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */);
        label_0xC91BEC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC91BF0;
        label_0xC91BF0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `MainMenu.Update` — RVA `0xc91bf4`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=10 (informational only).

```csharp
public static ulong MainMenu_Update_RVAc91bf4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0xB1UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91C40;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x20UL))));
        x19 = x0;
        if ((x8 == 0x0UL))
        {
            goto label_0xC91C48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91C0CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x46CUL))))), 0));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179AE80UL /* metadata target: Time.set_timeScale */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0xB1UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC91C48;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91C24UL);
        }
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x474UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x8) + (0x468UL))), unchecked((byte)(unchecked((uint)0x0UL))));
        x0 = x19;
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x2 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1791660UL /* metadata target: Behaviour.set_enabled */);
        label_0xC91C40:
        ;
        x30 = RuntimeMemory.ReadU64(sp);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC91C48:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `MainMenu.OnGUI` — RVA `0xc91c4c`

- Lift status: **partial**; input span: 2544 bytes; span to next metadata RVA: 2544 bytes.
- Metadata signature: `private void OnGUI() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=241 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'frintp' at 0xc92444; reason: Unsupported instruction 'frintm' at 0xc92450; reason: Unsupported instruction 'csel' at 0xc9246c; reason: Unknown IR expression at 0xc9246c; reason: Unsupported instruction 'frintp' at 0xc92570; reason: Unsupported instruction 'frintm' at 0xc9257c; reason: Unsupported instruction 'csel' at 0xc92598; reason: Unknown IR expression at 0xc92598

```csharp
public static ulong MainMenu_OnGUI_RVAc91c4c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        double __arm64_fcvtz_source_13181996 = default(double);
        double __arm64_fcvtz_source_13182048 = default(double);
        double __arm64_fcvtz_source_13182296 = default(double);
        double __arm64_fcvtz_source_13182348 = default(double);
        ulong __arm64_flags_left_13182004 = default(ulong);
        ulong __arm64_flags_left_13182304 = default(ulong);
        ulong __arm64_flags_result_13182004 = default(ulong);
        ulong __arm64_flags_result_13182304 = default(ulong);
        ulong __arm64_flags_right_13182004 = default(ulong);
        ulong __arm64_flags_right_13182304 = default(ulong);
        float __arm64_float_flags_left_13181820 = default(float);
        double __arm64_float_flags_left_13181832 = default(double);
        double __arm64_float_flags_left_13181980 = default(double);
        double __arm64_float_flags_left_13182052 = default(double);
        float __arm64_float_flags_left_13182244 = default(float);
        double __arm64_float_flags_left_13182256 = default(double);
        double __arm64_float_flags_left_13182280 = default(double);
        double __arm64_float_flags_left_13182352 = default(double);
        float __arm64_float_flags_right_13181820 = default(float);
        double __arm64_float_flags_right_13181832 = default(double);
        double __arm64_float_flags_right_13181980 = default(double);
        double __arm64_float_flags_right_13182052 = default(double);
        float __arm64_float_flags_right_13182244 = default(float);
        double __arm64_float_flags_right_13182256 = default(double);
        double __arm64_float_flags_right_13182280 = default(double);
        double __arm64_float_flags_right_13182352 = default(double);
        ulong __arm64_pair_address_13179980 = default(ulong);
        ulong __arm64_pair_address_13179984 = default(ulong);
        ulong __arm64_pair_address_13180068 = default(ulong);
        ulong __arm64_pair_address_13180072 = default(ulong);
        ulong __arm64_pair_address_13180704 = default(ulong);
        ulong __arm64_pair_address_13180708 = default(ulong);
        ulong __arm64_pair_address_13180740 = default(ulong);
        ulong __arm64_pair_address_13180744 = default(ulong);
        ulong __arm64_pair_address_13180876 = default(ulong);
        ulong __arm64_pair_address_13180880 = default(ulong);
        ulong __arm64_pair_address_13180912 = default(ulong);
        ulong __arm64_pair_address_13180916 = default(ulong);
        ulong __arm64_pair_address_13180948 = default(ulong);
        ulong __arm64_pair_address_13180952 = default(ulong);
        ulong __arm64_pair_address_13181120 = default(ulong);
        ulong __arm64_pair_address_13181124 = default(ulong);
        ulong __arm64_pair_address_13181156 = default(ulong);
        ulong __arm64_pair_address_13181160 = default(ulong);
        ulong __arm64_pair_address_13181192 = default(ulong);
        ulong __arm64_pair_address_13181196 = default(ulong);
        ulong __arm64_pair_address_13181348 = default(ulong);
        ulong __arm64_pair_address_13181352 = default(ulong);
        ulong __arm64_pair_address_13181384 = default(ulong);
        ulong __arm64_pair_address_13181388 = default(ulong);
        ulong __arm64_pair_address_13181420 = default(ulong);
        ulong __arm64_pair_address_13181424 = default(ulong);
        ulong __arm64_pair_address_13181576 = default(ulong);
        ulong __arm64_pair_address_13181580 = default(ulong);
        ulong __arm64_pair_address_13181612 = default(ulong);
        ulong __arm64_pair_address_13181616 = default(ulong);
        ulong __arm64_pair_address_13182432 = default(ulong);
        ulong __arm64_pair_address_13182508 = default(ulong);
        ulong __arm64_pair_address_13182512 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v11 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v3 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
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
        __arm64_pair_address_13179980 = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFF90UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13179980, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v11.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13179980) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = __arm64_pair_address_13179980;
        __arm64_pair_address_13179984 = unchecked((ulong)((sp) + (0x10UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_13179984, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_13179984) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x25 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x456UL))))))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x25) + (0xCE0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC91CA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x2A8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x456UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC91CA0;
        label_0xC91CA0:
        ;
        x0 = RuntimeMemory.ReadU64(x25);
        __arm64_pair_address_13180068 = unchecked((ulong)((x19) + (0x40UL)));
        v11 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180068)), 0));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180068) + (0x4UL))))), 0));
        __arm64_pair_address_13180072 = unchecked((ulong)((x19) + (0x48UL)));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180072)), 0));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180072) + (0x4UL))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC91CB8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91CB4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC91CB8;
        label_0xC91CB8:
        ;
        v0 = v11;
        v1 = v10;
        v2 = v9;
        v3 = v8;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B2DBCUL /* metadata target: GUI.set_color */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x70UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92274;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC91CE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91CE4UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC91CE8;
        label_0xC91CE8:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5514UL /* metadata target: GUISkin.get_button */, x0, x1, x2, x3);
        x26 = 0x1A8D000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0x2A8UL))));
        x20 = x0;
        x8 = RuntimeMemory.ReadU64(x26);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17BC4A8UL /* metadata target: GUIStyle.ctor */, x0, x1, x2, x3);
        x22 = unchecked((ulong)((x19) + (0x110UL)));
        x0 = x22;
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x110UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5514UL /* metadata target: GUISkin.get_button */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x20 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x20;
        x2 = 0x0UL;
        x21 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17BC4A8UL /* metadata target: GUIStyle.ctor */, x0, x1, x2, x3);
        x20 = unchecked((ulong)((x19) + (0x118UL)));
        x0 = x20;
        x1 = x21;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x118UL))), x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5514UL /* metadata target: GUISkin.get_button */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x21 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x21;
        x2 = 0x0UL;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17BC4A8UL /* metadata target: GUIStyle.ctor */, x0, x1, x2, x3);
        x21 = unchecked((ulong)((x19) + (0x120UL)));
        x0 = x21;
        x1 = x23;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x120UL))), x23);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5104UL /* metadata target: GUISkin.get_box */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x23 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x23;
        x2 = 0x0UL;
        x24 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17BC4A8UL /* metadata target: GUIStyle.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x140UL)));
        x1 = x24;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x140UL))), x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5514UL /* metadata target: GUISkin.get_button */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x23 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x23;
        x2 = 0x0UL;
        x24 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17BC4A8UL /* metadata target: GUIStyle.ctor */, x0, x1, x2, x3);
        x0 = unchecked((ulong)((x19) + (0x128UL)));
        x1 = x24;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x128UL))), x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B5514UL /* metadata target: GUISkin.get_button */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x26);
        x23 = x0;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = x23;
        x2 = 0x0UL;
        x24 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x17BC4A8UL /* metadata target: GUIStyle.ctor */, x0, x1, x2, x3);
        x23 = unchecked((ulong)((x19) + (0x130UL)));
        x0 = x23;
        x1 = x24;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x130UL))), x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x138UL))))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB5A8UL /* metadata target: GUIStyle.get_normal */, x0, x1, x2, x3);
        if ((unchecked((uint)(x24)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC91F1C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91EB0UL);
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91EB4UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91EE0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91F0CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        goto label_0xC91F74;
        label_0xC91F1C:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91F20UL);
        }
        __arm64_pair_address_13180704 = unchecked((ulong)((x19) + (0x58UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180704)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180704) + (0x4UL))))), 0));
        __arm64_pair_address_13180708 = unchecked((ulong)((x19) + (0x50UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180708)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180708) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91F44UL);
        }
        __arm64_pair_address_13180740 = unchecked((ulong)((x19) + (0x58UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180740)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180740) + (0x4UL))))), 0));
        __arm64_pair_address_13180744 = unchecked((ulong)((x19) + (0x50UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180744)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180744) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91F68UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC91F74;
        label_0xC91F74:
        ;
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x25);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC91F90;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91F8CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC91F90;
        label_0xC91F90:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17B388CUL /* metadata target: GUI.get_skin */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BA1F0UL /* metadata target: GUISkin.set_font */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x217UL))))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB5A8UL /* metadata target: GUIStyle.get_normal */, x0, x1, x2, x3);
        if ((unchecked((uint)(x23)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92020;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91FC8UL);
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91FCCUL);
        }
        __arm64_pair_address_13180876 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180876)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180876) + (0x4UL))))), 0));
        __arm64_pair_address_13180880 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180880)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180880) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC91FF0UL);
        }
        __arm64_pair_address_13180912 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180912)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180912) + (0x4UL))))), 0));
        __arm64_pair_address_13180916 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180916)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180916) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92014UL);
        }
        __arm64_pair_address_13180948 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180948)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180948) + (0x4UL))))), 0));
        __arm64_pair_address_13180952 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13180952)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13180952) + (0x4UL))))), 0));
        goto label_0xC9208C;
        label_0xC92020:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92024UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92050UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9207CUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC9208C;
        label_0xC9208C:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x90UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x6AUL))))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB5A8UL /* metadata target: GUIStyle.get_normal */, x0, x1, x2, x3);
        if ((unchecked((uint)(x22)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC92114;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC920BCUL);
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC920C0UL);
        }
        __arm64_pair_address_13181120 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181120)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181120) + (0x4UL))))), 0));
        __arm64_pair_address_13181124 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181124)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181124) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC920E4UL);
        }
        __arm64_pair_address_13181156 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181156)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181156) + (0x4UL))))), 0));
        __arm64_pair_address_13181160 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181160)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181160) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92108UL);
        }
        __arm64_pair_address_13181192 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181192)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181192) + (0x4UL))))), 0));
        __arm64_pair_address_13181196 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181196)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181196) + (0x4UL))))), 0));
        goto label_0xC92180;
        label_0xC92114:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92118UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92144UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92170UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC92180;
        label_0xC92180:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x148UL))))))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB5A8UL /* metadata target: GUIStyle.get_normal */, x0, x1, x2, x3);
        if ((unchecked((uint)(x21)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC921F8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC921A0UL);
        }
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC921A4UL);
        }
        __arm64_pair_address_13181348 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181348)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181348) + (0x4UL))))), 0));
        __arm64_pair_address_13181352 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181352)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181352) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC921C8UL);
        }
        __arm64_pair_address_13181384 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181384)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181384) + (0x4UL))))), 0));
        __arm64_pair_address_13181388 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181388)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181388) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC921ECUL);
        }
        __arm64_pair_address_13181420 = unchecked((ulong)((x19) + (0x68UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181420)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181420) + (0x4UL))))), 0));
        __arm64_pair_address_13181424 = unchecked((ulong)((x19) + (0x60UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181424)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181424) + (0x4UL))))), 0));
        goto label_0xC92264;
        label_0xC921F8:
        ;
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC921FCUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92228UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92254UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F000000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        goto label_0xC92264;
        label_0xC92264:
        ;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x70UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC92274;
        label_0xC92274:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB5A8UL /* metadata target: GUIStyle.get_normal */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92288UL);
        }
        __arm64_pair_address_13181576 = unchecked((ulong)((x19) + (0x58UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181576)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181576) + (0x4UL))))), 0));
        __arm64_pair_address_13181580 = unchecked((ulong)((x19) + (0x50UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181580)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181580) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC70CUL /* metadata target: GUIStyle.get_active */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC922ACUL);
        }
        __arm64_pair_address_13181612 = unchecked((ulong)((x19) + (0x58UL)));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181612)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181612) + (0x4UL))))), 0));
        __arm64_pair_address_13181616 = unchecked((ulong)((x19) + (0x50UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13181616)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13181616) + (0x4UL))))), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BC698UL /* metadata target: GUIStyle.get_hover */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC922D0UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x29UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC9239C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x94UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x9CUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x98UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        x0 = 0x0UL;
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xA0UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, x1, x2, x3);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x242UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x74UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92350;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC92350;
        label_0xC92350:
        ;
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xA60UL))));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        x0 = RuntimeMemory.ReadU64(x22);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC9236C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92368UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC9236C;
        label_0xC9236C:
        ;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x28UL)));
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, x1, x2, x3);
        __arm64_float_flags_left_13181820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13181820 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13181820 >= __arm64_float_flags_right_13181820))
        {
            goto label_0xC92418;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92384UL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13181832 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13181832 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13181832 != __arm64_float_flags_right_13181832) || ((__arm64_float_flags_left_13181832 != __arm64_float_flags_left_13181832) || (__arm64_float_flags_right_13181832 != __arm64_float_flags_right_13181832))))
        {
            goto label_0xC92440;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92390UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x28UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC9242C;
        label_0xC9239C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x19) + (0x8CUL))))), 0));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x9CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x7CUL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x7CUL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x7CUL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x7CUL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x7CUL))))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x80UL))))));
        goto label_0xC925A0;
        label_0xC92418:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13181980 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13181980 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13181980 != __arm64_float_flags_right_13181980) || ((__arm64_float_flags_left_13181980 != __arm64_float_flags_left_13181980) || (__arm64_float_flags_right_13181980 != __arm64_float_flags_right_13181980))))
        {
            goto label_0xC9244C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92424UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x28UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC9242C;
        label_0xC9242C:
        ;
        __arm64_fcvtz_source_13181996 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13181996 != __arm64_fcvtz_source_13181996) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13181996 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13181996 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13181996)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13182004 = x8;
        __arm64_flags_right_13182004 = 0x1UL;
        __arm64_flags_result_13182004 = unchecked((ulong)((__arm64_flags_left_13182004) & (__arm64_flags_right_13182004)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13182004 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC92454;
        label_0xC92440:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC92444UL);
        goto label_0xC92454;
        label_0xC9244C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC92450UL);
        goto label_0xC92454;
        label_0xC92454:
        ;
        x8 = 0x7FF0000000000000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x128UL))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13182048 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13182048 != __arm64_fcvtz_source_13182048) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13182048 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13182048 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13182048)))))))));
        __arm64_float_flags_left_13182052 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13182052 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC9246CUL);
        x20 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x130UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x110UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x118UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x120UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x20))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x242UL))))))));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x78UL))))), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92500;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA60UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x242UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC92500;
        label_0xC92500:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0))))), 0));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC92514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92510UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC92514;
        label_0xC92514:
        ;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0)))), 0));
        x0 = unchecked((ulong)((sp) + (0x28UL)));
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C60UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        __arm64_float_flags_left_13182244 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v9.GetUInt64(0)))), 0);
        __arm64_float_flags_right_13182244 = global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0);
        if ((__arm64_float_flags_left_13182244 >= __arm64_float_flags_right_13182244))
        {
            goto label_0xC92544;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC9252CUL);
        }
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFE0000000000000UL))), 0));
        __arm64_float_flags_left_13182256 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13182256 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13182256 != __arm64_float_flags_right_13182256) || ((__arm64_float_flags_left_13182256 != __arm64_float_flags_left_13182256) || (__arm64_float_flags_right_13182256 != __arm64_float_flags_right_13182256))))
        {
            goto label_0xC9256C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92538UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x28UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xBFF0000000000000UL))), 0));
        goto label_0xC92558;
        label_0xC92544:
        ;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FE0000000000000UL))), 0));
        __arm64_float_flags_left_13182280 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13182280 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        if (((__arm64_float_flags_left_13182280 != __arm64_float_flags_right_13182280) || ((__arm64_float_flags_left_13182280 != __arm64_float_flags_left_13182280) || (__arm64_float_flags_right_13182280 != __arm64_float_flags_right_13182280))))
        {
            goto label_0xC92578;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC92550UL);
        }
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0x28UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x3FF0000000000000UL))), 0));
        goto label_0xC92558;
        label_0xC92558:
        ;
        __arm64_fcvtz_source_13182296 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x8 = unchecked((ulong)(((__arm64_fcvtz_source_13182296 != __arm64_fcvtz_source_13182296) ? unchecked((long)0x0UL) : ((__arm64_fcvtz_source_13182296 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x43E0000000000000UL))) ? unchecked((long)0x7FFFFFFFFFFFFFFFUL) : ((__arm64_fcvtz_source_13182296 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC3E0000000000000UL))) ? unchecked((long)0x8000000000000000UL) : unchecked((long)(__arm64_fcvtz_source_13182296)))))));
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        __arm64_flags_left_13182304 = x8;
        __arm64_flags_right_13182304 = 0x1UL;
        __arm64_flags_result_13182304 = unchecked((ulong)((__arm64_flags_left_13182304) & (__arm64_flags_right_13182304)));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(((__arm64_flags_result_13182304 == 0x0UL) ? global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))) : global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))), 0));
        goto label_0xC92580;
        label_0xC9256C:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintp", 0xC92570UL);
        goto label_0xC92580;
        label_0xC92578:
        ;
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(unchecked((double)((global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0))))) + (global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0)))))))), 0));
        RuntimeCalls.Unsupported("frintm", 0xC9257CUL);
        goto label_0xC92580;
        label_0xC92580:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x7FF0000000000000UL;
        v1 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(global::System.BitConverter.Int64BitsToDouble(unchecked((long)(x8)))), 0));
        __arm64_fcvtz_source_13182348 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        x9 = unchecked((ulong)(unchecked((uint)(((__arm64_fcvtz_source_13182348 != __arm64_fcvtz_source_13182348) ? unchecked((int)0x0UL) : ((__arm64_fcvtz_source_13182348 >= global::System.BitConverter.Int64BitsToDouble(unchecked((long)0x41E0000000000000UL))) ? unchecked((int)0x7FFFFFFFUL) : ((__arm64_fcvtz_source_13182348 < global::System.BitConverter.Int64BitsToDouble(unchecked((long)0xC1E0000000000000UL))) ? unchecked((int)0x80000000UL) : unchecked((int)(__arm64_fcvtz_source_13182348)))))))));
        __arm64_float_flags_left_13182352 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0))));
        __arm64_float_flags_right_13182352 = global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v1.GetUInt64(0))));
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFF80000000UL))));
        RuntimeCalls.Unsupported("csel", 0xC92598UL);
        x1 = unchecked((ulong)((__Unsupported<bool>("Unknown IR expression") ? unchecked((uint)(x8)) : unchecked((uint)(x9)))));
        x0 = x20;
        goto label_0xC925A0;
        label_0xC925A0:
        ;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BBF28UL /* metadata target: GUIStyle.set_fontSize */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x140UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB5A8UL /* metadata target: GUIStyle.get_normal */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC92638;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC925BCUL);
        }
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x3F800000UL)), 0)), 0));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17BB61CUL /* metadata target: GUIStyleState.set_textColor */, x0, x1, x2, x3);
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1777C10UL /* metadata target: Screen.get_width */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x88UL))))), 0));
        __arm64_pair_address_13182432 = unchecked((ulong)((x19) + (0xA0UL)));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_13182432)), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_13182432) + (0x4UL))))), 0));
        v3 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0xBF000000UL)), 0)), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v3.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) - (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v2.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v4.GetUInt64(0)))), 0))))), 0));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) + (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        x0 = 0x0UL;
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xACUL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = RuntimeCalls.InvokeDirect(0x1777C38UL /* metadata target: Screen.get_height */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x84UL))))), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)(unchecked((int)(unchecked((uint)(x0))))))), 0));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v1.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0xA8UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x60UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x60UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        __arm64_pair_address_13182508 = unchecked((ulong)((sp) + (0x10UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13182508)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13182508) + (0x8UL))))), 0));
        __arm64_pair_address_13182512 = sp;
        v11 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_13182512)), 0));
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_13182512) + (0x8UL))))), 0));
        sp = unchecked((ulong)((__arm64_pair_address_13182512) + (0x70UL)));
        return x0;
        label_0xC92638:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `MainMenu.PlayButtonFx` — RVA `0xc9263c`

- Lift status: **exact**; input span: 80 bytes; span to next metadata RVA: 80 bytes.
- Metadata signature: `private void PlayButtonFx(AudioClip clip, float vol) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static ulong MainMenu_PlayButtonFx_RVAc9263c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92688;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x1;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A478UL /* metadata target: AudioSource.set_volume */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92688;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176A588UL /* metadata target: AudioSource.set_clip */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB8UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC92688;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x176A5CCUL /* metadata target: AudioSource.Play */);
        label_0xC92688:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `MainMenu.ctor` — RVA `0xc9268c`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong MainMenu_ctor_RVAc9268c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x8 = default(ulong);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)0xEUL)) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)0xEUL)).ShiftLeftLogical(unchecked((int)0x20UL)));
        RuntimeMemory.WriteU8(unchecked((ulong)((x0) + (0x28UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x8 = 0x431000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x7CUL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xF08UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0xCCCDUL))));
        x8 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x3CCCUL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x74UL))), unchecked((uint)(x8)));
        x8 = 0x431000UL;
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x84UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        v0 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((x8) + (0xF10UL))))), 0));
        x8 = unchecked((ulong)(unchecked((uint)(0x41200000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xA4UL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xC8UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xD8UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xE8UL))), unchecked((uint)(x8)));
        RuntimeMemory.WriteF64(unchecked((ulong)((x0) + (0x94UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0xF8UL))), unchecked((uint)(x8)));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```
