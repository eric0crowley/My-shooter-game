# `bl_SnapShot` — TypeDefIndex 3487

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x20` | `int` | `resWidth` |
| `0x24` | `int` | `resHeight` |
| `0x28` | `int` | `msaa` |
| `0x30` | `string` | `m_TakeSnapShot` |

## `bl_SnapShot.get_FolderPath` — RVA `0xccaac4`

- Lift status: **exact**; input span: 88 bytes; span to next metadata RVA: 88 bytes.
- Metadata signature: `public static string get_FolderPath() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=14 (informational only).

```csharp
public static ulong bl_SnapShot_get_FolderPath_RVAccaac4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x19 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x57DUL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB38UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = 0x1A8E000UL;
            x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB38UL))));
            // Likely IL2CPP class initialization helper (guarded call).
            x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
            x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
            RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x57DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        }
        label_0xCCAAF4:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
        }
        else
        {
            x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
            x0 = RuntimeMemory.ReadU64(x19);
        }
        label_0xCCAB08:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `bl_SnapShot.SnapshotName` — RVA `0xccab1c`

- Lift status: **exact**; input span: 596 bytes; span to next metadata RVA: 596 bytes.
- Metadata signature: `private string SnapshotName(int width, int height) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=87 (informational only).

```csharp
public static ulong bl_SnapShot_SnapshotName_RVAccab1c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13413472 = default(uint);
        uint __arm64_flags_left_13413544 = default(uint);
        uint __arm64_flags_left_13413660 = default(uint);
        uint __arm64_flags_right_13413472 = default(uint);
        uint __arm64_flags_right_13413544 = default(uint);
        uint __arm64_flags_right_13413660 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x50UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x10UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x19 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x57EUL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x248UL))));
        x21 = unchecked((ulong)(unchecked((uint)(x2))));
        x22 = unchecked((ulong)(unchecked((uint)(x1))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCAB9C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x248UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x1C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3C0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x57EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCAB9C;
        label_0xCCAB9C:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x18UL))), 0x0UL);
        x20 = 0x1A8E000UL;
        x19 = 0x1A8D000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x3C0UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCABC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCABBCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCABC0;
        label_0xCCABC0:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176E1A8UL /* metadata target: Application.get_loadedLevelName */, x0, x1, x2, x3);
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xCCAD70UL /* metadata target: bl_SnapShot.GetFullFolderPath */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x20);
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x19);
        x19 = x0;
        x1 = unchecked((ulong)(unchecked((uint)(0x4UL))));
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7D9D4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAD6C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        if ((x23 == 0x0UL))
        {
            goto label_0xCCAC10;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x23;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAD60;
        }
        else
        {
            goto label_0xCCAC10;
        }
        label_0xCCAC10:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xCCAD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0x1C0UL))));
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x20UL))), x23);
        x1 = x23;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)((sp) + (0xCUL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x22)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x22 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAC5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x22;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAD60;
        }
        else
        {
            goto label_0xCCAC5C;
        }
        label_0xCCAC5C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13413472 = unchecked((uint)(x8));
        __arm64_flags_right_13413472 = unchecked((uint)0x1UL);
        if (((!((__arm64_flags_left_13413472 >= __arm64_flags_right_13413472))) || (unchecked((uint)((__arm64_flags_left_13413472) - (__arm64_flags_right_13413472))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCCAD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x28UL))), x22);
        x1 = x22;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0x8UL))), unchecked((uint)(x21)));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA64UL, x0, x1, x2, x3);
        x21 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCCACA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAD60;
        }
        else
        {
            goto label_0xCCACA4;
        }
        label_0xCCACA4:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13413544 = unchecked((uint)(x8));
        __arm64_flags_right_13413544 = unchecked((uint)0x2UL);
        if (((!((__arm64_flags_left_13413544 >= __arm64_flags_right_13413544))) || (unchecked((uint)((__arm64_flags_left_13413544) - (__arm64_flags_right_13413544))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCCAD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8D000UL;
        x22 = 0x1A8E000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x8C0UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xB48UL))));
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCACE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCACDCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCACE0;
        label_0xCCACE0:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x152BC60UL /* metadata target: DateTime.get_Now */, x0, x1, x2, x3);
        x1 = RuntimeMemory.ReadU64(x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x0);
        x0 = unchecked((ulong)((sp) + (0x18UL)));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x152C9A8UL /* metadata target: DateTime.ToString */, x0, x1, x2, x3);
        x21 = x0;
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAD18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x0 = x21;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7DA60UL, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xCCAD60;
        }
        else
        {
            goto label_0xCCAD18;
        }
        label_0xCCAD18:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        __arm64_flags_left_13413660 = unchecked((uint)(x8));
        __arm64_flags_right_13413660 = unchecked((uint)0x3UL);
        if (((!((__arm64_flags_left_13413660 >= __arm64_flags_right_13413660))) || (unchecked((uint)((__arm64_flags_left_13413660) - (__arm64_flags_right_13413660))) == unchecked((uint)0x0UL))))
        {
            goto label_0xCCAD5C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x38UL))), x21);
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x1 = x20;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x13F6DD4UL /* metadata target: String.Format */, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        return x0;
        label_0xCCAD5C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB7CUL, x0, x1, x2, x3);
        goto label_0xCCAD60;
        label_0xCCAD60:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB98UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        goto label_0xCCAD6C;
        label_0xCCAD6C:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `bl_SnapShot.GetFullFolderPath` — RVA `0xccad70`

- Lift status: **exact**; input span: 148 bytes; span to next metadata RVA: 148 bytes.
- Metadata signature: `private string GetFullFolderPath() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong bl_SnapShot_GetFullFolderPath_RVAccad70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x19 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x57FUL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x248UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCADAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x248UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x57FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCADAC;
        label_0xCCADAC:
        ;
        x0 = RuntimeMemory.ReadU64(x19);
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB38UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCADC4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xCCADC0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xCCADC4;
        label_0xCCADC4:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x176D540UL /* metadata target: Application.get_dataPath */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x19 = x0;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0xE0UL))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCADE8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        goto label_0xCCADE8;
        label_0xCCADE8:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = 0x0UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        return RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */);
        return default(ulong);
    }
```

## `bl_SnapShot.TakeSnapshot` — RVA `0xccae04`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public void TakeSnapshot() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong bl_SnapShot_TakeSnapshot_RVAccae04(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `bl_SnapShot.ctor` — RVA `0xccae08`

- Lift status: **exact**; input span: 104 bytes; span to next metadata RVA: 104 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=15 (informational only).

```csharp
public static ulong bl_SnapShot_ctor_RVAccae08(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x580UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x230UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCAE3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x580UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCAE3C;
        label_0xCCAE3C:
        ;
        v0 = (RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x8UL)) << (int)(unchecked((int)(unchecked((uint)0x8UL))))))) | RuntimeVector128.Zero.WithUInt32(0, unchecked((uint)((unchecked((uint)0x8UL)) << (int)(unchecked((int)(unchecked((uint)0x8UL))))))).ShiftLeftLogical(unchecked((int)0x20UL)));
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteF64(unchecked((ulong)((x19) + (0x20UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v0.GetUInt64(0)))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x28UL))), unchecked((uint)(x8)));
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x1);
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */);
        return default(ulong);
    }
```

## `bl_SnapShot.cctor` — RVA `0xccae70`

- Lift status: **exact**; input span: 108 bytes; span to next metadata RVA: 108 bytes.
- Metadata signature: `private static void .cctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=19 (informational only).

```csharp
public static ulong bl_SnapShot_cctor_RVAccae70(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x19 = 0x1A8E000UL;
        x20 = 0x1A8E000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x581UL))))))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0xB50UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xB38UL))));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCCAEB4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xB38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x581UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCCAEB4;
        label_0xCCAEB4:
        ;
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x19);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        RuntimeMemory.WriteU64(x8, x9);
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = RuntimeMemory.ReadU64(x19);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        return default(ulong);
    }
```
