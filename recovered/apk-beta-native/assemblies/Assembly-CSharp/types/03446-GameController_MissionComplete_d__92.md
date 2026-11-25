# `GameController.<MissionComplete>d__92` — TypeDefIndex 3446

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `GameController` | `<>4__this` |

## `GameController.<MissionComplete>d__92.ctor` — RVA `0xcc0bc8`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GameController_MissionComplete_d__92_ctor_RVAcc0bc8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFE0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x19);
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1589338UL /* metadata target: Object.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x10UL))), unchecked((uint)(x19)));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `GameController.<MissionComplete>d__92.Dispose` — RVA `0xcc173c`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GameController_MissionComplete_d__92_Dispose_RVAcc173c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `GameController.<MissionComplete>d__92.MoveNext` — RVA `0xcc1740`

- Lift status: **partial**; input span: 1044 bytes; span to next metadata RVA: 1044 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=168 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xcc183c; reason: Unknown IR expression at 0xcc183c; reason: Unsupported instruction 'csel' at 0xcc1880; reason: Unknown IR expression at 0xcc1880; reason: Unsupported instruction 'csel' at 0xcc18bc; reason: Unknown IR expression at 0xcc18bc; reason: Unsupported instruction 'csel' at 0xcc1908; reason: Unknown IR expression at 0xcc1908

```csharp
public static uint GameController_MissionComplete_d__92_MoveNext_RVAcc1740(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13375428 = default(uint);
        ulong __arm64_flags_left_13375532 = default(ulong);
        ulong __arm64_flags_left_13375604 = default(ulong);
        ulong __arm64_flags_left_13375664 = default(ulong);
        ulong __arm64_flags_left_13375740 = default(ulong);
        ulong __arm64_flags_left_13376008 = default(ulong);
        uint __arm64_flags_left_13376132 = default(uint);
        uint __arm64_flags_left_13376152 = default(uint);
        uint __arm64_flags_left_13376184 = default(uint);
        uint __arm64_flags_left_13376208 = default(uint);
        uint __arm64_flags_left_13376240 = default(uint);
        uint __arm64_flags_left_13376264 = default(uint);
        uint __arm64_flags_left_13376316 = default(uint);
        uint __arm64_flags_left_13376324 = default(uint);
        uint __arm64_flags_result_13376152 = default(uint);
        uint __arm64_flags_result_13376208 = default(uint);
        uint __arm64_flags_result_13376264 = default(uint);
        uint __arm64_flags_right_13375428 = default(uint);
        ulong __arm64_flags_right_13375532 = default(ulong);
        ulong __arm64_flags_right_13375604 = default(ulong);
        ulong __arm64_flags_right_13375664 = default(ulong);
        ulong __arm64_flags_right_13375740 = default(ulong);
        ulong __arm64_flags_right_13376008 = default(ulong);
        uint __arm64_flags_right_13376132 = default(uint);
        uint __arm64_flags_right_13376152 = default(uint);
        uint __arm64_flags_right_13376184 = default(uint);
        uint __arm64_flags_right_13376208 = default(uint);
        uint __arm64_flags_right_13376240 = default(uint);
        uint __arm64_flags_right_13376264 = default(uint);
        uint __arm64_flags_right_13376316 = default(uint);
        uint __arm64_flags_right_13376324 = default(uint);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        ulong x10 = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x40UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x514UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC17BC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3E8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x878UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x514UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC17BC;
        label_0xCC17BC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        __arm64_flags_left_13375428 = unchecked((uint)(x8));
        __arm64_flags_right_13375428 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13375428) - (__arm64_flags_right_13375428))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC1A5C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCC17CCUL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC1B24;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE28UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(0x1UL)))))));
        x2 = 0x0UL;
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x178F9E4UL /* metadata target: PlayerPrefs.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x178UL))));
        x8 = unchecked((ulong)(unchecked((uint)(0x1F4UL))));
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(x20);
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x230UL))));
        __arm64_flags_left_13375532 = x0;
        __arm64_flags_right_13375532 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x9 = RuntimeMemory.ReadU64(x22);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC183CUL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x23 = 0x1A8D000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE18UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x198UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x23);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x14UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x22);
        __arm64_flags_left_13375604 = x0;
        __arm64_flags_right_13375604 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC1880UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x158UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x18UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x22);
        __arm64_flags_left_13375664 = x0;
        __arm64_flags_right_13375664 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC18BCUL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x180UL))));
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x14UL)))) + (0x4UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x8)))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(0x1F4UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x22);
        __arm64_flags_left_13375740 = x0;
        __arm64_flags_right_13375740 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC1908UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE98UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x14UL)))) + (0x4UL))))));
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) + (unchecked((uint)(x9)))))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x10)))))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(0x1F4UL)))))));
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x178F9E4UL /* metadata target: PlayerPrefs.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = 0x1A8E000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x208UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x878UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x0)));
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        x8 = 0x1A8E000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x8F0UL))));
        x1 = x0;
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x8);
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x13ED2C8UL /* metadata target: String.Concat */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x210UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x10UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x1 = x0;
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x23);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x218UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x22);
        __arm64_flags_left_13376008 = x0;
        __arm64_flags_right_13376008 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC1A14UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x40400000UL)), 0)), 0));
        x1 = 0x0UL;
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1799B00UL /* metadata target: WaitForSeconds.ctor */, x0, x1, x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x18UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0xFFFFFFFFFFFFFFF8UL))), unchecked((uint)(x0)));
        goto label_0xCC1B28;
        label_0xCC1A5C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x21 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x90UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x19 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x20UL))))));
        __arm64_flags_left_13376132 = unchecked((uint)(x8));
        __arm64_flags_right_13376132 = unchecked((uint)0x1EUL);
        if (((__arm64_flags_left_13376132 >= __arm64_flags_right_13376132) && (!((unchecked((uint)((__arm64_flags_left_13376132) - (__arm64_flags_right_13376132))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xCC1AB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x10 = unchecked((ulong)(unchecked((uint)(0x9249UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x19))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x10 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x4924UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13376152 = unchecked((uint)(x9));
        __arm64_flags_right_13376152 = unchecked((uint)(x10));
        __arm64_flags_result_13376152 = unchecked((uint)((__arm64_flags_left_13376152) & (__arm64_flags_right_13376152)));
        if ((__arm64_flags_result_13376152 == unchecked((uint)0x0UL)))
        {
            goto label_0xCC1AB8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x20UL))))));
        goto label_0xCC1AB8;
        label_0xCC1AB8:
        ;
        __arm64_flags_left_13376184 = unchecked((uint)(x8));
        __arm64_flags_right_13376184 = unchecked((uint)0x1CUL);
        if (((__arm64_flags_left_13376184 >= __arm64_flags_right_13376184) && (!((unchecked((uint)((__arm64_flags_left_13376184) - (__arm64_flags_right_13376184))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xCC1AF0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x2492UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x10 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x1249UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13376208 = unchecked((uint)(x9));
        __arm64_flags_right_13376208 = unchecked((uint)(x10));
        __arm64_flags_result_13376208 = unchecked((uint)((__arm64_flags_left_13376208) & (__arm64_flags_right_13376208)));
        if ((__arm64_flags_result_13376208 == unchecked((uint)0x0UL)))
        {
            goto label_0xCC1AF0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x48UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x20UL))))));
        goto label_0xCC1AF0;
        label_0xCC1AF0:
        ;
        __arm64_flags_left_13376240 = unchecked((uint)(x8));
        __arm64_flags_right_13376240 = unchecked((uint)0x1DUL);
        if (((__arm64_flags_left_13376240 >= __arm64_flags_right_13376240) && (!((unchecked((uint)((__arm64_flags_left_13376240) - (__arm64_flags_right_13376240))) == unchecked((uint)0x0UL))))))
        {
            goto label_0xCC1B3C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x10 = unchecked((ulong)(unchecked((uint)(0x4124UL))));
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) << (int)(unchecked((int)(unchecked((uint)(x8)))))))));
        x10 = unchecked((ulong)(unchecked((uint)(unchecked((ulong)((unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) & (unchecked((uint)((~(0xFFFFUL)))))))))) | (unchecked((ulong)((unchecked((ulong)((0x2482UL) << (int)(unchecked((int)(0x10UL)))))) << (int)(unchecked((int)(0x0UL))))))))))));
        __arm64_flags_left_13376264 = unchecked((uint)(x9));
        __arm64_flags_right_13376264 = unchecked((uint)(x10));
        __arm64_flags_result_13376264 = unchecked((uint)((__arm64_flags_left_13376264) & (__arm64_flags_right_13376264)));
        if ((__arm64_flags_result_13376264 == unchecked((uint)0x0UL)))
        {
            goto label_0xCC1B3C;
        }
        else
        {
            goto label_0xCC1B10;
        }
        label_0xCC1B10:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x50UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC1B50;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC1B24;
        label_0xCC1B24:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCC1B28;
        label_0xCC1B28:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return unchecked((uint)(x0));
        label_0xCC1B3C:
        ;
        __arm64_flags_left_13376316 = unchecked((uint)(x8));
        __arm64_flags_right_13376316 = unchecked((uint)0x78UL);
        if ((unchecked((uint)((__arm64_flags_left_13376316) - (__arm64_flags_right_13376316))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC1B10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCC1B44UL)));
        }
        __arm64_flags_left_13376324 = unchecked((uint)(x8));
        __arm64_flags_right_13376324 = unchecked((uint)0x6FUL);
        if ((unchecked((uint)((__arm64_flags_left_13376324) - (__arm64_flags_right_13376324))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC1B10;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCC1B4CUL)));
        }
        goto label_0xCC1B24;
        label_0xCC1B50:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `GameController.<MissionComplete>d__92.get_Current` — RVA `0xcc1b54`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GameController_MissionComplete_d__92_get_Current_RVAcc1b54(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `GameController.<MissionComplete>d__92.Reset` — RVA `0xcc1b5c`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong GameController_MissionComplete_d__92_Reset_RVAcc1b5c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x30 = default(ulong);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFF0UL)))) + (0x8UL))), x19);
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x3F0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x1 = 0x0UL;
        x19 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x1549CD0UL /* metadata target: NotSupportedException.ctor */, x0, x1, x2, x3);
        x0 = 0x1A8E000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x8F8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GameController.<MissionComplete>d__92.get_Current` — RVA `0xcc1b94`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GameController_MissionComplete_d__92_get_Current_RVAcc1b94(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
