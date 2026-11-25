# `GameController.<SurvivalPanelFunc>d__93` — TypeDefIndex 3450

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x10` | `int` | `<>1__state` |
| `0x18` | `object` | `<>2__current` |
| `0x20` | `GameController` | `<>4__this` |

## `GameController.<SurvivalPanelFunc>d__93.ctor` — RVA `0xcc0c5c`

- Lift status: **exact**; input span: 40 bytes; span to next metadata RVA: 40 bytes.
- Metadata signature: `public void .ctor(int <>1__state) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=5 (informational only).

```csharp
public static ulong GameController_SurvivalPanelFunc_d__93_ctor_RVAcc0c5c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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

## `GameController.<SurvivalPanelFunc>d__93.Dispose` — RVA `0xcc2080`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void System.IDisposable.Dispose() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong GameController_SurvivalPanelFunc_d__93_Dispose_RVAcc2080(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `GameController.<SurvivalPanelFunc>d__93.MoveNext` — RVA `0xcc2084`

- Lift status: **partial**; input span: 628 bytes; span to next metadata RVA: 628 bytes.
- Metadata signature: `private bool MoveNext() { }`
- Structural verifier: suspect=1, unverifiable=0, unmapped-instructions=101 (informational only).
- Lift diagnostics: reason: Unsupported instruction 'csel' at 0xcc213c; reason: Unknown IR expression at 0xcc213c; reason: Unsupported instruction 'csel' at 0xcc2178; reason: Unknown IR expression at 0xcc2178; reason: Unsupported instruction 'csel' at 0xcc21c0; reason: Unknown IR expression at 0xcc21c0; reason: Unsupported instruction 'csel' at 0xcc21fc; reason: Unknown IR expression at 0xcc21fc

```csharp
public static uint GameController_SurvivalPanelFunc_d__93_MoveNext_RVAcc2084(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_13377764 = default(uint);
        ulong __arm64_flags_left_13377836 = default(ulong);
        ulong __arm64_flags_left_13377900 = default(ulong);
        ulong __arm64_flags_left_13377972 = default(ulong);
        ulong __arm64_flags_left_13378032 = default(ulong);
        ulong __arm64_flags_left_13378092 = default(ulong);
        uint __arm64_flags_right_13377764 = default(uint);
        ulong __arm64_flags_right_13377836 = default(ulong);
        ulong __arm64_flags_right_13377900 = default(ulong);
        ulong __arm64_flags_right_13377972 = default(ulong);
        ulong __arm64_flags_right_13378032 = default(ulong);
        ulong __arm64_flags_right_13378092 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x518UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC20DC;
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
        x0 = 0x1A8D000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE98UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x230UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x518UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xCC20DC;
        label_0xCC20DC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x10UL))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x20UL))));
        __arm64_flags_left_13377764 = unchecked((uint)(x8));
        __arm64_flags_right_13377764 = unchecked((uint)0x1UL);
        if ((unchecked((uint)((__arm64_flags_left_13377764) - (__arm64_flags_right_13377764))) == unchecked((uint)0x0UL)))
        {
            goto label_0xCC22B8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xCC20ECUL)));
        }
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xCC22DC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x22 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = 0x1A8D000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE18UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x1A0UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(x21);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x14UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x23 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(x20);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0x230UL))));
        __arm64_flags_left_13377836 = x0;
        __arm64_flags_right_13377836 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x9 = RuntimeMemory.ReadU64(x23);
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC213CUL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x228UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x18UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x23);
        __arm64_flags_left_13377900 = x0;
        __arm64_flags_right_13377900 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC2178UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x188UL))));
        x0 = unchecked((ulong)((sp) + (0xCUL)));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x14UL)))) + (0x4UL))))));
        x8 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x8))) + (unchecked((uint)(x9)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x23);
        __arm64_flags_left_13377972 = x0;
        __arm64_flags_right_13377972 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC21C0UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x220UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x10UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x23);
        __arm64_flags_left_13378032 = x0;
        __arm64_flags_right_13378032 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC21FCUL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x160UL))));
        x1 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x0 = unchecked((ulong)((x8) + (0x20UL)));
        x0 = RuntimeCalls.InvokeDirect(0x1545824UL /* metadata target: Int32.ToString */, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = RuntimeMemory.ReadU64(x23);
        __arm64_flags_left_13378092 = x0;
        __arm64_flags_right_13378092 = 0x0UL;
        x10 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5E8UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x5F0UL))));
        RuntimeCalls.Unsupported("csel", 0xCC2238UL);
        x1 = (__Unsupported<bool>("Unknown IR expression") ? x9 : x0);
        x0 = x20;
        x0 = RuntimeCalls.InvokeIndirect(x10, x0, x1, x2, x3);
        x20 = 0x1A8D000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE98UL))));
        x1 = 0x0UL;
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0x178FAB8UL /* metadata target: PlayerPrefs.GetInt */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(x21);
        x2 = 0x0UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xB8UL))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x14UL))))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((unchecked((ulong)((x8) + (0x14UL)))) + (0x4UL))))));
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x0)))))));
        x1 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x9))) + (unchecked((uint)(x10)))))));
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0x178F9E4UL /* metadata target: PlayerPrefs.SetInt */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = 0x1A8D000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x3E8UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
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
        goto label_0xCC22E0;
        label_0xCC22B8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0xFFFFFFFFFFFFFFFFUL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x19) + (0x10UL))), unchecked((uint)(x8)));
        if ((x22 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x58UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xCC22F4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794CD0UL /* metadata target: GameObject.SetActive */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xCC0820UL /* metadata target: GameController.ShowIntersititialAd */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xCC22DC;
        label_0xCC22DC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xCC22E0;
        label_0xCC22E0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        sp = unchecked((ulong)((sp) + (0x40UL)));
        return unchecked((uint)(x0));
        label_0xCC22F4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(uint);
    }
```

## `GameController.<SurvivalPanelFunc>d__93.get_Current` — RVA `0xcc22f8`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.Generic.IEnumerator<System.Object>.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GameController_SurvivalPanelFunc_d__93_get_Current_RVAcc22f8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```

## `GameController.<SurvivalPanelFunc>d__93.Reset` — RVA `0xcc2300`

- Lift status: **exact**; input span: 56 bytes; span to next metadata RVA: 56 bytes.
- Metadata signature: `private void System.Collections.IEnumerator.Reset() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=8 (informational only).

```csharp
public static ulong GameController_SurvivalPanelFunc_d__93_Reset_RVAcc2300(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x920UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D940UL, x0, x1, x2, x3);
        x1 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xB7DA4CUL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `GameController.<SurvivalPanelFunc>d__93.get_Current` — RVA `0xcc2338`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `private object System.Collections.IEnumerator.get_Current() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong GameController_SurvivalPanelFunc_d__93_get_Current_RVAcc2338(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x18UL))));
        return x0;
        return default(ulong);
    }
```
