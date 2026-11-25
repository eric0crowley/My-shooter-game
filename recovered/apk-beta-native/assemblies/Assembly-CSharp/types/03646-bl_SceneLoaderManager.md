# `bl_SceneLoaderManager` — TypeDefIndex 3646

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x18` | `List<bl_SceneLoaderInfo>` | `sceneList` |
| `0x20` | `List<string>` | `tipsList` |

## `bl_SceneLoaderManager.GetSceneInfo` — RVA `0xce8278`

- Lift status: **exact**; input span: 476 bytes; span to next metadata RVA: 476 bytes.
- Metadata signature: `public bl_SceneLoaderInfo GetSceneInfo(string scene) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=74 (informational only).

```csharp
public static ulong bl_SceneLoaderManager_GetSceneInfo_RVAce8278(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13534180 = default(uint);
        uint __arm64_flags_right_13534180 = default(uint);
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
        sp = unchecked((ulong)((sp) - (0x60UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x66DUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE82F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x398UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xBF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x66DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE82F0;
        label_0xCE82F0:
        ;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x18UL))), 0x0UL);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x18UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCE83D4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC00UL))));
        x24 = 0x1A8F000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xBF0UL))));
        x23 = 0x1A8F000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x22 = 0x1A8C000UL;
        x21 = 0x1A8F000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC08UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x398UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xBE8UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3CF0UL, x0, x1, x2, x3);
        goto label_0xCE8334;
        label_0xCE8334:
        ;
        x1 = RuntimeMemory.ReadU64(x24);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA88UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE8370;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        if ((x20 == 0x0UL))
        {
            goto label_0xCE83D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F610CUL /* metadata target: String.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCE8334;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        goto label_0xCE83B4;
        label_0xCE8370:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        goto label_0xCE837C;
        label_0xCE837C:
        ;
        x0 = RuntimeMemory.ReadU64(x23);
        x1 = x19;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE83A4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCE83A4;
        label_0xCE83A4:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1770B68UL /* metadata target: Debug.Log */, x0, x1, x2, x3);
        x20 = 0x0UL;
        goto label_0xCE83B4;
        label_0xCE83B4:
        ;
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        return x0;
        label_0xCE83D0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCE83D4;
        label_0xCE83D4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xCE83E0;
        label_0xCE83E0:
        ;
        x20 = x0;
        __arm64_flags_left_13534180 = unchecked((uint)(x1));
        __arm64_flags_right_13534180 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_13534180) - (__arm64_flags_right_13534180))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xCE841C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, x2, x3);
        x21 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBE8UL))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCE837C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        goto label_0xCE841C;
        label_0xCE841C:
        ;
        x21 = 0x0UL;
        goto label_0xCE8428;
        label_0xCE8428:
        ;
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xBE8UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x21 != 0x0UL))
        {
            goto label_0xCE8448;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, x2, x3);
        goto label_0xCE8448;
        label_0xCE8448:
        ;
        x0 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_SceneLoaderManager.get_HasTips` — RVA `0xce8454`

- Lift status: **exact**; input span: 84 bytes; span to next metadata RVA: 84 bytes.
- Metadata signature: `public bool get_HasTips() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=11 (informational only).

```csharp
public static uint bl_SceneLoaderManager_get_HasTips_RVAce8454(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13534348 = default(uint);
        uint __arm64_flags_right_13534348 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x66EUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA40UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x66EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCE8480:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        if ((x8 == 0x0UL))
        {
            label_0xCE8498:
            ;
            x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        }
        else
        {
            x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
            __arm64_flags_left_13534348 = unchecked((uint)(x8));
            __arm64_flags_right_13534348 = unchecked((uint)0x0UL);
            x0 = unchecked((ulong)((((!((unchecked((uint)((__arm64_flags_left_13534348) - (__arm64_flags_right_13534348))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13534348) - (__arm64_flags_right_13534348))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_13534348)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_13534348)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_13534348) - (__arm64_flags_right_13534348))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_13534348)) < unchecked((int)0x0UL)))))) ? unchecked((uint)0x1UL) : unchecked((uint)0x0UL))));
        }
        label_0xCE849C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```

## `bl_SceneLoaderManager.GetSceneNames` — RVA `0xce84a8`

- Lift status: **exact**; input span: 288 bytes; span to next metadata RVA: 288 bytes.
- Metadata signature: `public string[] GetSceneNames() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=50 (informational only).

```csharp
public static ulong bl_SceneLoaderManager_GetSceneNames_RVAce84a8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x22 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x66FUL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xC10UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE8514;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x66FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE8514;
        label_0xCE8514:
        ;
        x0 = RuntimeMemory.ReadU64(x22);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE852C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE8524UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xCE852C;
        label_0xCE852C:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x24 = 0x1A8F000UL;
        x23 = 0x1A8F000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xC18UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xC20UL))));
        if ((x20 != 0x0UL))
        {
            goto label_0xCE85A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE8558;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCE8550UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        goto label_0xCE8558;
        label_0xCE8558:
        ;
        x9 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC28UL))));
        x21 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeMemory.ReadU64(x9);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8F000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC30UL))));
        x1 = x21;
        x3 = 0x0UL;
        x20 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xFC1988UL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = x20;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x8UL))), x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xCE85A0;
        label_0xCE85A0:
        ;
        x2 = RuntimeMemory.ReadU64(x24);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xE3F3B4UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0xE41F30UL);
        return default(ulong);
    }
```

## `bl_SceneLoaderManager.AsyncLoadData` — RVA `0xce85c8`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public static IEnumerator AsyncLoadData() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=13 (informational only).

```csharp
public static ulong bl_SceneLoaderManager_AsyncLoadData_RVAce85c8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1A8F000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x670UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC38UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC38UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x670UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCE85F8:
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

## `bl_SceneLoaderManager.get_Instance` — RVA `0xce8648`

- Lift status: **exact**; input span: 220 bytes; span to next metadata RVA: 220 bytes.
- Metadata signature: `public static bl_SceneLoaderManager get_Instance() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=39 (informational only).

```csharp
public static ulong bl_SceneLoaderManager_get_Instance_RVAce8648(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x21 = 0x1BAB000UL;
        x20 = 0x1A8D000UL;
        x19 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x671UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xA10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xD8UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8C000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8F000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC40UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA00UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x0 = 0x1A8D000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xA10UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x671UL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCE86A4:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeMemory.ReadU64(x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x19 = RuntimeMemory.ReadU64(x8);
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        }
        label_0xCE86C0:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x8 = 0x1A8D000UL;
            x9 = 0x1A8F000UL;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xA00UL))));
            x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0xC40UL))));
            x0 = RuntimeMemory.ReadU64(x8);
            x1 = RuntimeMemory.ReadU64(x9);
            x0 = RuntimeCalls.InvokeDirect(0xD328ACUL, x0, x1, x2, x3);
            x8 = RuntimeMemory.ReadU64(x20);
            x1 = x0;
            x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            RuntimeMemory.WriteU64(x8, x0);
            x8 = RuntimeMemory.ReadU64(x20);
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
            x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        }
        label_0xCE870C:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `bl_SceneLoaderManager.ctor` — RVA `0xce8724`

- Lift status: **exact**; input span: 220 bytes; span to next metadata RVA: 220 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=36 (informational only).

```csharp
public static ulong bl_SceneLoaderManager_ctor_RVAce8724(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFC0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x23 = 0x1BAB000UL;
        x24 = 0x1A8F000UL;
        x20 = 0x1A8F000UL;
        x22 = 0x1A8D000UL;
        x21 = 0x1A8D000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x672UL))))))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xC48UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xC50UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x988UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x980UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCE879C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x980UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8F000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xC48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x988UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x672UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCE879C;
        label_0xCE879C:
        ;
        x0 = RuntimeMemory.ReadU64(x24);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2B64UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x18UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x21);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2B64UL, x0, x1, x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x179634CUL /* metadata target: ScriptableObject.ctor */);
        return default(ulong);
    }
```
