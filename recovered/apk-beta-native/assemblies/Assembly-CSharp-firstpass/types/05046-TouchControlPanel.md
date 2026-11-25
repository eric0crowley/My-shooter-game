# `TouchControlPanel` — TypeDefIndex 5046

> **Reconstructed pseudocode only; not original C# source.** Synthetic ABI arguments, `ulong` return values, registers, `RuntimeMemory`/`RuntimeCalls` and control-flow labels come from the native lifter. `exact` is not proof of semantic equivalence or compilability. See [`README.md`](../../../README.md).

## Instance fields from metadata

| Offset | Type | Field |
|---:|---|---|
| `0x22` | `bool` | `autoConnectToRig` |
| `0x28` | `InputRig` | `rig` |
| `0x30` | `List<TouchControl>` | `controls` |
| `0x38` | `List<TouchControlPanel.SystemTouch>` | `touchList` |
| `0x40` | `TouchControl.HitPool` | `hitPool` |
| `0x48` | `float` | `fingerRadInPx` |

## `TouchControlPanel.RemoveControl` — RVA `0xc50478`

- Lift status: **exact**; input span: 136 bytes; span to next metadata RVA: 136 bytes.
- Metadata signature: `public void RemoveControl(TouchControl c) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=22 (informational only).

```csharp
public static ulong TouchControlPanel_RemoveControl_RVAc50478(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x266UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC504A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x628UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x266UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC504A8;
        label_0xC504A8:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x21UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC504BC;
        }
        else
        {
            goto label_0xC504B0;
        }
        label_0xC504B0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC504BC:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC504DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC504DC;
        label_0xC504DC:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC504B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x628UL))));
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x2 = RuntimeMemory.ReadU64(x8);
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x10A4650UL);
        return default(ulong);
    }
```

## `TouchControlPanel.AddControl` — RVA `0xc50500`

- Lift status: **exact**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `public void AddControl(TouchControl c) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=43 (informational only).

```csharp
public static ulong TouchControlPanel_AddControl_RVAc50500(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12912064 = default(uint);
        uint __arm64_flags_right_12912064 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x265UL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5053C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x620UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xCB8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x265UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5053C;
        label_0xC5053C:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x21UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50584;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC50564;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x20);
        x9 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x20UL))), unchecked((byte)(unchecked((uint)(x9)))));
        x0 = x20;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x178UL))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((x8) + (0x178UL)))) + (0x8UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, x3);
        goto label_0xC50564;
        label_0xC50564:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC50608;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xCB8UL))));
        x1 = x19;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0x10A36C0UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC50590;
        }
        else
        {
            goto label_0xC50584;
        }
        label_0xC50584:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC50590:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC50608;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = 0x1A8C000UL;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x9) + (0x620UL))));
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x9);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC50608;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12912064 = unchecked((uint)(x10));
        __arm64_flags_right_12912064 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12912064 >= __arm64_flags_right_12912064))
        {
            goto label_0xC505EC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x19);
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = x8;
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC505EC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x1 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0x10A3390UL);
        label_0xC50608:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControlPanel.ctor` — RVA `0xc53bdc`

- Lift status: **exact**; input span: 500 bytes; span to next metadata RVA: 500 bytes.
- Metadata signature: `public void .ctor() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=80 (informational only).

```csharp
public static ulong TouchControlPanel_ctor_RVAc53bdc(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12926328 = default(uint);
        uint __arm64_flags_left_12926388 = default(uint);
        uint __arm64_flags_result_12926388 = default(uint);
        uint __arm64_flags_right_12926328 = default(uint);
        uint __arm64_flags_right_12926388 = default(uint);
        ulong sp = default(ulong);
        ulong x10 = default(ulong);
        ulong x11 = default(ulong);
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
        x23 = 0x1BAB000UL;
        x22 = 0x1A8C000UL;
        x20 = 0x1A8C000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x23) + (0x262UL))))))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x4B0UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x4B8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xDF0UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53C78;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDF0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDF8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4B8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE00UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x4B0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE08UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDA8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE10UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x23) + (0x262UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC53C78;
        label_0xC53C78:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        x1 = 0x0UL;
        RuntimeMemory.WriteU8(unchecked((ulong)((x19) + (0x22UL))), unchecked((byte)(unchecked((uint)(x8)))));
        x0 = RuntimeCalls.InvokeDirect(0x1796274UL /* metadata target: MonoBehaviour.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x22);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x20);
        x1 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0x10A2BD4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x0) + (0x30UL))), x20);
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC534A4UL /* metadata target: TouchControl.HitPool.ctor */, x0, x1, x2, x3);
        x21 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x21) + (0x40UL))), x20);
        x0 = x21;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        if ((x0 == 0x0UL))
        {
            goto label_0xC53DCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xDA8UL))));
        x20 = 0x1A8C000UL;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE08UL))));
        x23 = 0x1A8C000UL;
        x2 = RuntimeMemory.ReadU64(x8);
        x21 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE00UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE10UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xDF8UL))));
        x1 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = RuntimeCalls.InvokeDirect(0x115EA34UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(x20);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x20 = x0;
        x23 = unchecked((ulong)(unchecked((uint)(0x10UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A2BD4UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x38UL))), x20);
        x0 = x19;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC53D40;
        label_0xC53D40:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x20 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC53DD0UL /* metadata target: TouchControlPanel.SystemTouch.ctor */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x19);
        if ((x0 == 0x0UL))
        {
            goto label_0xC53DCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x1CUL))))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x9 = RuntimeMemory.ReadU64(x22);
        x10 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x1CUL))), unchecked((uint)(x10)));
        if ((x8 == 0x0UL))
        {
            goto label_0xC53DCC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x10 = unchecked((ulong)(unchecked((long)(RuntimeMemory.ReadS32(unchecked((ulong)((x0) + (0x18UL))))))));
        x11 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        __arm64_flags_left_12926328 = unchecked((uint)(x10));
        __arm64_flags_right_12926328 = unchecked((uint)(x11));
        if ((__arm64_flags_left_12926328 >= __arm64_flags_right_12926328))
        {
            goto label_0xC53DA0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x10))) + (unchecked((uint)(0x1UL)))))));
        x8 = unchecked((ulong)((x8) + (unchecked((ulong)((x10) << (int)(unchecked((int)(0x3UL))))))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x0) + (0x18UL))), unchecked((uint)(x9)));
        RuntimeMemory.WriteU64(unchecked((ulong)((x8) + (0x20UL))), x20);
        x0 = x8;
        x1 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        goto label_0xC53DB4;
        label_0xC53DA0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)(unchecked((uint)(x9))))) + (0x20UL))));
        x1 = x20;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xC0UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x70UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3390UL, x0, x1, x2, x3);
        goto label_0xC53DB4;
        label_0xC53DB4:
        ;
        __arm64_flags_left_12926388 = unchecked((uint)(x23));
        __arm64_flags_right_12926388 = unchecked((uint)0x1UL);
        __arm64_flags_result_12926388 = unchecked((uint)((__arm64_flags_left_12926388) - (__arm64_flags_right_12926388)));
        x23 = unchecked((ulong)(__arm64_flags_result_12926388));
        if ((!((unchecked((uint)((__arm64_flags_left_12926388) - (__arm64_flags_right_12926388))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC53D40;
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
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC53DCC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControlPanel.OnInitComponent` — RVA `0xc53e40`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `protected override void OnInitComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControlPanel_OnInitComponent_RVAc53e40(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC53E44UL /* metadata target: TouchControlPanel.InvalidateHierarchy */);
        return default(ulong);
    }
```

## `TouchControlPanel.InvalidateHierarchy` — RVA `0xc53e44`

- Lift status: **exact**; input span: 260 bytes; span to next metadata RVA: 260 bytes.
- Metadata signature: `public void InvalidateHierarchy() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=42 (informational only).

```csharp
public static ulong TouchControlPanel_InvalidateHierarchy_RVAc53e44(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x264UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53E88;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE18UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD70UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x264UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC53E88;
        label_0xC53E88:
        ;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x22UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53EC0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x21);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53EAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC53EA8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC53EAC;
        label_0xC53EAC:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53F3C;
        }
        else
        {
            goto label_0xC53EC0;
        }
        label_0xC53EC0:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD70UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE31BC8UL, x0, x1, x2, x3);
        x20 = x19;
        RuntimeMemory.WriteU64(unchecked((ulong)((x20) + (0x28UL))), x0);
        x1 = x0;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB7D8D0UL, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(x20);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53EFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC53EF8UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC53EFC;
        label_0xC53EFC:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53F3C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE18UL))));
        x0 = x19;
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xE3204CUL, x0, x1, x2, x3);
        x1 = x0;
        RuntimeMemory.WriteU64(unchecked((ulong)((x19) + (0x28UL))), x0);
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xB7D8D0UL);
        label_0xC53F3C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControlPanel.OnDestroyComponent` — RVA `0xc53f48`

- Lift status: **exact**; input span: 416 bytes; span to next metadata RVA: 416 bytes.
- Metadata signature: `protected override void OnDestroyComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=63 (informational only).

```csharp
public static ulong TouchControlPanel_OnDestroyComponent_RVAc53f48(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12927096 = default(uint);
        uint __arm64_flags_right_12927096 = default(uint);
        ulong sp = default(ulong);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0x50UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x20UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x263UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC53FAC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE20UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE28UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE30UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE38UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x263UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC53FAC;
        label_0xC53FAC:
        ;
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = x19;
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x0UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((unchecked((ulong)((sp) + (0x8UL)))) + (0x8UL))), 0x0UL);
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x18UL))), 0x0UL);
        x0 = RuntimeCalls.InvokeDirect(0xC540E8UL /* metadata target: TouchControlPanel.ReleaseAll */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC5404C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE38UL))));
        x21 = 0x1A8C000UL;
        x22 = 0x1A8C000UL;
        x20 = 0x1A8C000UL;
        x1 = RuntimeMemory.ReadU64(x8);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE28UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xE20UL))));
        x0 = RuntimeCalls.InvokeDirect(0x10A3CF0UL, x0, x1, x2, x3);
        goto label_0xC53FF4;
        label_0xC53FF4:
        ;
        x1 = RuntimeMemory.ReadU64(x21);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA88UL, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54040;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(x22);
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54018;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC54014UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC54018;
        label_0xC54018:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC53FF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5402CUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC54060;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC50318UL /* metadata target: TouchControl.SetTouchControlPanel */, x0, x1, x2, x3);
        goto label_0xC53FF4;
        label_0xC54040:
        ;
        x1 = RuntimeMemory.ReadU64(x20);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        goto label_0xC5404C;
        label_0xC5404C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        return x0;
        label_0xC54060:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        goto label_0xC54074;
        label_0xC54074:
        ;
        x19 = x0;
        __arm64_flags_left_12927096 = unchecked((uint)(x1));
        __arm64_flags_right_12927096 = unchecked((uint)0x1UL);
        if ((!((unchecked((uint)((__arm64_flags_left_12927096) - (__arm64_flags_right_12927096))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC540B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0x19B0C00UL, x0, x1, x2, x3);
        x20 = RuntimeMemory.ReadU64(x0);
        x0 = RuntimeCalls.InvokeDirect(0x19B0C10UL, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE20UL))));
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x20 == 0x0UL))
        {
            goto label_0xC5404C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        goto label_0xC540B0;
        label_0xC540B0:
        ;
        x20 = 0x0UL;
        goto label_0xC540BC;
        label_0xC540BC:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE20UL))));
        x1 = RuntimeMemory.ReadU64(x8);
        x0 = unchecked((ulong)((sp) + (0x8UL)));
        x0 = RuntimeCalls.InvokeDirect(0xF0EA84UL, x0, x1, x2, x3);
        if ((x20 != 0x0UL))
        {
            goto label_0xC540DC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC26098UL, x0, x1, x2, x3);
        goto label_0xC540DC;
        label_0xC540DC:
        ;
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xB1BD40UL, x0, x1, x2, x3);
        x0 = RuntimeCalls.InvokeDirect(0xA29990UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControlPanel.ReleaseAll` — RVA `0xc540e8`

- Lift status: **exact**; input span: 164 bytes; span to next metadata RVA: 164 bytes.
- Metadata signature: `private void ReleaseAll(bool cancel) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=24 (informational only).

```csharp
public static ulong TouchControlPanel_ReleaseAll_RVAc540e8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12927300 = default(uint);
        uint __arm64_flags_right_12927300 = default(uint);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x26EUL))))))));
        x21 = unchecked((ulong)(unchecked((uint)(x1))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54128;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x26EUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC54128;
        label_0xC54128:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54178;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE48UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) & (unchecked((uint)(0x1UL)))))));
        goto label_0xC54140;
        label_0xC54140:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12927300 = unchecked((uint)(x20));
        __arm64_flags_right_12927300 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12927300) - (__arm64_flags_right_12927300))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12927300)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12927300)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12927300) - (__arm64_flags_right_12927300))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12927300)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC5417C;
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
            goto label_0xC54178;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54178;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0xC4D3BCUL /* metadata target: TouchObject.End */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC54140;
        }
        else
        {
            goto label_0xC54178;
        }
        label_0xC54178:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5417C;
        label_0xC5417C:
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

## `TouchControlPanel.OnEnableComponent` — RVA `0xc5418c`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `protected override void OnEnableComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControlPanel_OnEnableComponent_RVAc5418c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return x0;
        return default(ulong);
    }
```

## `TouchControlPanel.OnDisableComponent` — RVA `0xc54190`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `protected override void OnDisableComponent() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchControlPanel_OnDisableComponent_RVAc54190(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        return RuntimeCalls.InvokeDirect(0xC540E8UL /* metadata target: TouchControlPanel.ReleaseAll */);
        return default(ulong);
    }
```

## `TouchControlPanel.Update` — RVA `0xc54198`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `private void Update() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControlPanel_Update_RVAc54198(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC541A0UL /* metadata target: TouchControlPanel.UpdateTouches */);
        return default(ulong);
    }
```

## `TouchControlPanel.UpdatePanel` — RVA `0xc5419c`

- Lift status: **exact**; input span: 4 bytes; span to next metadata RVA: 4 bytes.
- Metadata signature: `public void UpdatePanel() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=0 (informational only).

```csharp
public static ulong TouchControlPanel_UpdatePanel_RVAc5419c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        return RuntimeCalls.InvokeDirect(0xC541A0UL /* metadata target: TouchControlPanel.UpdateTouches */);
        return default(ulong);
    }
```

## `TouchControlPanel.UpdateTouches` — RVA `0xc541a0`

- Lift status: **exact**; input span: 140 bytes; span to next metadata RVA: 140 bytes.
- Metadata signature: `public void UpdateTouches() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=20 (informational only).

```csharp
public static ulong TouchControlPanel_UpdateTouches_RVAc541a0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12927472 = default(uint);
        uint __arm64_flags_right_12927472 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x26DUL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC541D8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x26DUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC541D8;
        label_0xC541D8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54218;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = 0x1A8C000UL;
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xE48UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC541EC;
        label_0xC541EC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12927472 = unchecked((uint)(x20));
        __arm64_flags_right_12927472 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12927472) - (__arm64_flags_right_12927472))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12927472)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12927472)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12927472) - (__arm64_flags_right_12927472))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12927472)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC5421C;
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
            goto label_0xC54218;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC54208UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC54D50UL /* metadata target: TouchControlPanel.SystemTouch.Update */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC541EC;
        }
        else
        {
            goto label_0xC54218;
        }
        label_0xC54218:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC5421C;
        label_0xC5421C:
        ;
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC54DF0UL /* metadata target: TouchControlPanel.UpdateTouchPressure */);
        return default(ulong);
    }
```

## `TouchControlPanel.GetControlList` — RVA `0xc5422c`

- Lift status: **exact**; input span: 8 bytes; span to next metadata RVA: 8 bytes.
- Metadata signature: `public List<TouchControl> GetControlList() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=1 (informational only).

```csharp
public static ulong TouchControlPanel_GetControlList_RVAc5422c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x30UL))));
        return x0;
        return default(ulong);
    }
```

## `TouchControlPanel.Prepare` — RVA `0xc54234`

- Lift status: **exact**; input span: 192 bytes; span to next metadata RVA: 192 bytes.
- Metadata signature: `private void Prepare() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong TouchControlPanel_Prepare_RVAc54234(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12927720 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFD0UL)));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x19);
        x21 = 0x1BAB000UL;
        x20 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x267UL))))))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0xD8UL))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54278;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x490UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x267UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC54278;
        label_0xC54278:
        ;
        x0 = RuntimeMemory.ReadU64(x20);
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5428C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC54288UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5428C;
        label_0xC5428C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC542B0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC542F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC542A8UL);
        }
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x4CUL))))), 0));
        goto label_0xC542B8;
        label_0xC542B0:
        ;
        x8 = 0x432000UL;
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x8) + (0x3B8UL))))), 0));
        goto label_0xC542B8;
        label_0xC542B8:
        ;
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x490UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC542D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC542CCUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC542D0;
        label_0xC542D0:
        ;
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC38B44UL /* metadata target: CFScreen.get_dpcm */, x0, x1, x2, x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) * (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(unchecked((ulong)((x19) + (0x48UL))), global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        __arm64_load_address_12927720 = sp;
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12927720)), 0));
        return x0;
        label_0xC542F0:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(ulong);
    }
```

## `TouchControlPanel.Raycast` — RVA `0xc542f4`

- Lift status: **exact**; input span: 340 bytes; span to next metadata RVA: 340 bytes.
- Metadata signature: `public bool Raycast(Vector2 sp, Camera eventCamera) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=53 (informational only).

```csharp
public static uint TouchControlPanel_Raycast_RVAc542f4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        ulong __arm64_load_address_12927940 = default(ulong);
        ulong __arm64_load_address_12928060 = default(ulong);
        ulong __arm64_pair_address_12927736 = default(ulong);
        ulong __arm64_pair_address_12927936 = default(ulong);
        ulong __arm64_pair_address_12928052 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        RuntimeVector128 v9 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x22 = default(ulong);
        ulong x23 = default(ulong);
        ulong x24 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        ulong x9 = default(ulong);
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFB0UL)));
        __arm64_pair_address_12927736 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12927736, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12927736) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x19);
        x22 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x268UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        v8 = v1;
        v9 = v0;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5435C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE58UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x22) + (0x268UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5435C;
        label_0xC5435C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54370;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5436CUL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC54370;
        label_0xC54370:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC543CC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC54444;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x130UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5439C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC543B0;
        label_0xC5439C:
        ;
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x74UL))))))));
        if ((unchecked((uint)(x9)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC543AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x50UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC543CC;
        }
        else
        {
            goto label_0xC543AC;
        }
        label_0xC543AC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC543B0;
        label_0xC543B0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_12927936 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12927936)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12927936) + (0x8UL))))), 0));
        __arm64_load_address_12927940 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12927940)), 0));
        return unchecked((uint)(x0));
        label_0xC543CC:
        ;
        x23 = 0x1A8C000UL;
        x24 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE50UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xE58UL))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC54234UL /* metadata target: TouchControlPanel.Prepare */, x0, x1, x2, x3);
        x0 = RuntimeMemory.ReadU64(x23);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x40UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x30UL))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x20) + (0x48UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = x20;
        x23 = x0;
        x0 = RuntimeCalls.InvokeDirect(0xC53A78UL /* metadata target: TouchControl.HitPool.TouchControlFilterFunc.ctor */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC54444;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = x21;
        x1 = x22;
        v0 = v9;
        v1 = v8;
        x2 = x19;
        x3 = x23;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_12928052 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12928052)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12928052) + (0x8UL))))), 0));
        v2 = v10;
        __arm64_load_address_12928060 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12928060)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12928060) + (0x50UL)));
        return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC5352CUL /* metadata target: TouchControl.HitPool.HitTestAny */)));
        label_0xC54444:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, x3);
        return default(uint);
    }
```

## `TouchControlPanel.RaycastControlFilter` — RVA `0xc54448`

- Lift status: **exact**; input span: 144 bytes; span to next metadata RVA: 144 bytes.
- Metadata signature: `private bool RaycastControlFilter(TouchControl c) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=23 (informational only).

```csharp
public static uint TouchControlPanel_RaycastControlFilter_RVAc54448(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x20 = 0x1BAB000UL;
        x21 = 0x1A8C000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x269UL))))))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0xD8UL))));
        x19 = x1;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5447C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        // Likely IL2CPP class initialization helper (guarded call).
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x269UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC5447C;
        label_0xC5447C:
        ;
        x0 = RuntimeMemory.ReadU64(x21);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5448C;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC54488UL)));
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5448C;
        label_0xC5448C:
        ;
        x0 = x19;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC544C4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0xC544A0UL)));
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC544D4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(x19);
        x0 = x19;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = 0x0UL;
        x3 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x338UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x340UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(RuntimeCalls.InvokeIndirect(x3)));
        label_0xC544C4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return unchecked((uint)(x0));
        label_0xC544D4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        return default(uint);
    }
```

## `TouchControlPanel.OnSystemTouchStart` — RVA `0xc544d8`

- Lift status: **exact**; input span: 584 bytes; span to next metadata RVA: 584 bytes.
- Metadata signature: `public void OnSystemTouchStart(TouchControlPanel.SystemTouchEventData data) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=86 (informational only).

```csharp
public static ulong TouchControlPanel_OnSystemTouchStart_RVAc544d8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12928552 = default(uint);
        uint __arm64_flags_left_12928592 = default(uint);
        uint __arm64_flags_left_12928688 = default(uint);
        uint __arm64_flags_right_12928552 = default(uint);
        uint __arm64_flags_right_12928592 = default(uint);
        uint __arm64_flags_right_12928688 = default(uint);
        ulong __arm64_load_address_12928792 = default(ulong);
        ulong __arm64_pair_address_12928220 = default(ulong);
        ulong __arm64_pair_address_12928460 = default(ulong);
        ulong __arm64_pair_address_12928788 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v10 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v10.GetUInt64(0)))));
        sp = unchecked((ulong)((sp) + (0xFFFFFFFFFFFFFFA0UL)));
        __arm64_pair_address_12928220 = unchecked((ulong)((sp) + (0x8UL)));
        RuntimeMemory.WriteF64(__arm64_pair_address_12928220, global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v9.GetUInt64(0)))));
        RuntimeMemory.WriteF64(unchecked((ulong)((__arm64_pair_address_12928220) + (0x8UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((sp) + (0x18UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x0UL))), x26);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))), x25);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x0UL))), x24);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))), x23);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x0UL))), x22);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))), x19);
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x26AUL))))))));
        x21 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54558;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE50UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE60UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x26AUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC54558;
        label_0xC54558:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54700;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x26 = 0x1A8C000UL;
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((x26) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x26);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC5457C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC54578UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC5457C;
        label_0xC5457C:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC545A0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BCB8UL /* metadata target: InputRig.WakeTouchControlsUp */, x0, x1, x2, x3);
        goto label_0xC545A0;
        label_0xC545A0:
        ;
        x0 = x19;
        x1 = x21;
        x0 = RuntimeCalls.InvokeDirect(0xC54720UL /* metadata target: TouchControlPanel.StartNewTouch */, x0, x1, x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC54700;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC54234UL /* metadata target: TouchControlPanel.Prepare */, x0, x1, x2, x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        __arm64_pair_address_12928460 = unchecked((ulong)((x21) + (0x10UL)));
        v8 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12928460)), 0));
        v9 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12928460) + (0x4UL))))), 0));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        v10 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((x19) + (0x48UL))))), 0));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE50UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xB7DB70UL, x0, x1, x2, x3);
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xE60UL))));
        x1 = x25;
        x24 = x0;
        x2 = RuntimeMemory.ReadU64(x8);
        x0 = RuntimeCalls.InvokeDirect(0xC53A78UL /* metadata target: TouchControl.HitPool.TouchControlFilterFunc.ctor */, x0, x1, x2, x3);
        if ((x22 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x3 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x0 = x22;
        x1 = x23;
        v0 = v8;
        v1 = v9;
        x2 = x21;
        v2 = v10;
        x4 = x24;
        x0 = RuntimeCalls.InvokeDirect(0xC536F8UL /* metadata target: TouchControl.HitPool.HitTest */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_flags_left_12928552 = unchecked((uint)(x0));
        __arm64_flags_right_12928552 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928552) - (__arm64_flags_right_12928552))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12928552)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12928552)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928552) - (__arm64_flags_right_12928552))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12928552)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54700;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xDD8UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC54644;
        label_0xC54644:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12928592 = unchecked((uint)(x21));
        __arm64_flags_right_12928592 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928592) - (__arm64_flags_right_12928592))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12928592)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12928592)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928592) - (__arm64_flags_right_12928592))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12928592)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54700;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC546F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = x0;
        x0 = RuntimeMemory.ReadU64(x26);
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54680;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5467CUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC54680;
        label_0xC54680:
        ;
        x0 = x23;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x179568CUL /* metadata target: Object.op_Equality */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC546F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x25UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC546C0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC546ACUL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xC5486CUL /* metadata target: TouchObject.GetControlCount */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_flags_left_12928688 = unchecked((uint)(x0));
        __arm64_flags_right_12928688 = unchecked((uint)0x0UL);
        if (((!((unchecked((uint)((__arm64_flags_left_12928688) - (__arm64_flags_right_12928688))) == unchecked((uint)0x0UL)))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928688) - (__arm64_flags_right_12928688))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12928688)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12928688)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928688) - (__arm64_flags_right_12928688))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12928688)) < unchecked((int)0x0UL)))))))
        {
            goto label_0xC546F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            goto label_0xC546C0;
        }
        label_0xC546C0:
        ;
        x8 = RuntimeMemory.ReadU64(x0);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        x2 = 0x0UL;
        x3 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B8UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2C0UL))));
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC546F0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC546FC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x24UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54700;
        }
        else
        {
            goto label_0xC546F0;
        }
        label_0xC546F0:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC54644;
        }
        else
        {
            goto label_0xC546FC;
        }
        label_0xC546FC:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC54700;
        label_0xC54700:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x50UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x50UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x40UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x40UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x26 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x25 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x18UL))));
        __arm64_pair_address_12928788 = unchecked((ulong)((sp) + (0x8UL)));
        v9 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_pair_address_12928788)), 0));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((__arm64_pair_address_12928788) + (0x8UL))))), 0));
        __arm64_load_address_12928792 = sp;
        v10 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(__arm64_load_address_12928792)), 0));
        sp = unchecked((ulong)((__arm64_load_address_12928792) + (0x60UL)));
        return x0;
        return default(ulong);
    }
```

## `TouchControlPanel.StartNewTouch` — RVA `0xc54720`

- Lift status: **exact**; input span: 332 bytes; span to next metadata RVA: 332 bytes.
- Metadata signature: `private TouchControlPanel.SystemTouch StartNewTouch(TouchControlPanel.SystemTouchEventData data) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=46 (informational only).

```csharp
public static ulong TouchControlPanel_StartNewTouch_RVAc54720(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12928896 = default(uint);
        uint __arm64_flags_left_12928952 = default(uint);
        uint __arm64_flags_right_12928896 = default(uint);
        uint __arm64_flags_right_12928952 = default(uint);
        ulong __arm64_pair_address_12929068 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v4 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x270UL))))))));
        x19 = x1;
        x21 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54764;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x270UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC54764;
        label_0xC54764:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = 0x1A8C000UL;
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((x23) + (0xE48UL))));
        x20 = 0x0UL;
        x22 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC5477C;
        label_0xC5477C:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12928896 = unchecked((uint)(x22));
        __arm64_flags_right_12928896 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928896) - (__arm64_flags_right_12928896))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12928896)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12928896)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12928896) - (__arm64_flags_right_12928896))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12928896)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC547E0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x23);
        x1 = unchecked((ulong)(unchecked((uint)(x22))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC54868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x0) + (0x10UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC547CC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC547ACUL);
        }
        if ((x19 == 0x0UL))
        {
            goto label_0xC54868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x8) + (0x18UL))))));
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        __arm64_flags_left_12928952 = unchecked((uint)(x8));
        __arm64_flags_right_12928952 = unchecked((uint)(x9));
        if ((!((unchecked((uint)((__arm64_flags_left_12928952) - (__arm64_flags_right_12928952))) == unchecked((uint)0x0UL)))))
        {
            goto label_0xC547D0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        x0 = RuntimeCalls.InvokeDirect(0xC4D3BCUL /* metadata target: TouchObject.End */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC547D0;
        label_0xC547CC:
        ;
        x20 = unchecked((ulong)(unchecked((uint)(x8))));
        goto label_0xC547D0;
        label_0xC547D0:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x38UL))));
        x22 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x22))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC5477C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC547DCUL);
        }
        goto label_0xC54868;
        label_0xC547E0:
        ;
        if ((x20 == 0x0UL))
        {
            goto label_0xC54850;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC547E4UL);
        }
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((x19 == 0x0UL))
        {
            goto label_0xC54868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        x0 = 0x0UL;
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x18UL))), unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x179AEB8UL /* metadata target: Time.get_frameCount */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        RuntimeMemory.WriteU32(unchecked((ulong)((x20) + (0x20UL))), unchecked((uint)(x0)));
        RuntimeMemory.WriteU32(unchecked((ulong)((sp) + (0xCUL))), unchecked((uint)(x8)));
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x24UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54818;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC54824;
        label_0xC54818:
        ;
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x20) + (0x18UL))))));
        x2 = unchecked((ulong)((sp) + (0xCUL)));
        x0 = RuntimeCalls.InvokeDirect(0xC54EF8UL /* metadata target: TouchControlPanel.IsTouchPressureSensitive */, unchecked((ulong)(unchecked((uint)(x0)))), unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC54824;
        label_0xC54824:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC54868;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC5482CUL);
        }
        __arm64_pair_address_12929068 = unchecked((ulong)((x19) + (0x10UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12929068)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12929068) + (0x4UL))))), 0));
        v4 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((sp) + (0xCUL))))), 0));
        x2 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x24UL))))))));
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x18UL))));
        x3 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)(0x1UL)))))));
        x0 = x8;
        x0 = RuntimeCalls.InvokeDirect(0xC4DAC4UL /* metadata target: TouchObject.Start */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC54850;
        label_0xC54850:
        ;
        x0 = x20;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        return x0;
        label_0xC54868:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), unchecked((ulong)(unchecked((uint)(x3)))));
        return default(ulong);
    }
```

## `TouchControlPanel.OnSystemTouchEnd` — RVA `0xc548b4`

- Lift status: **exact**; input span: 180 bytes; span to next metadata RVA: 180 bytes.
- Metadata signature: `public void OnSystemTouchEnd(TouchControlPanel.SystemTouchEventData data) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=26 (informational only).

```csharp
public static ulong TouchControlPanel_OnSystemTouchEnd_RVAc548b4(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x26BUL))))))));
        x19 = x1;
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC548E4;
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
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x26BUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC548E4;
        label_0xC548E4:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54908;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC54904UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC54908;
        label_0xC54908:
        ;
        x0 = x21;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC5492C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54964;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BCB8UL /* metadata target: InputRig.WakeTouchControlsUp */, x0, x1, x2, x3);
        goto label_0xC5492C;
        label_0xC5492C:
        ;
        if ((x19 == 0x0UL))
        {
            goto label_0xC54964;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x19) + (0x20UL))))));
        x0 = x20;
        x0 = RuntimeCalls.InvokeDirect(0xC54968UL /* metadata target: TouchControlPanel.FindTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC54958;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54964;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x1 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return RuntimeCalls.InvokeDirect(0xC4D3BCUL /* metadata target: TouchObject.End */);
        label_0xC54958:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x8UL))));
        return x0;
        label_0xC54964:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        return default(ulong);
    }
```

## `TouchControlPanel.FindTouch` — RVA `0xc54968`

- Lift status: **exact**; input span: 176 bytes; span to next metadata RVA: 176 bytes.
- Metadata signature: `private TouchControlPanel.SystemTouch FindTouch(int hwId) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static ulong TouchControlPanel_FindTouch_RVAc54968(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12929472 = default(uint);
        uint __arm64_flags_left_12929516 = default(uint);
        uint __arm64_flags_right_12929472 = default(uint);
        uint __arm64_flags_right_12929516 = default(uint);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x21) + (0x26FUL))))))));
        x19 = unchecked((ulong)(unchecked((uint)(x1))));
        x20 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC549A8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x21) + (0x26FUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC549A8;
        label_0xC549A8:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54A00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE48UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC549BC;
        label_0xC549BC:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12929472 = unchecked((uint)(x21));
        __arm64_flags_right_12929472 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929472) - (__arm64_flags_right_12929472))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12929472)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12929472)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929472) - (__arm64_flags_right_12929472))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12929472)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54A04;
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
            goto label_0xC54A00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC54A00;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC549F4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12929516 = unchecked((uint)(x8));
        __arm64_flags_right_12929516 = unchecked((uint)(x19));
        if ((unchecked((uint)((__arm64_flags_left_12929516) - (__arm64_flags_right_12929516))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54A08;
        }
        else
        {
            goto label_0xC549F4;
        }
        label_0xC549F4:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x38UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC549BC;
        }
        else
        {
            goto label_0xC54A00;
        }
        label_0xC54A00:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC54A04;
        label_0xC54A04:
        ;
        x0 = 0x0UL;
        goto label_0xC54A08;
        label_0xC54A08:
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

## `TouchControlPanel.OnSystemTouchMove` — RVA `0xc54a18`

- Lift status: **exact**; input span: 520 bytes; span to next metadata RVA: 520 bytes.
- Metadata signature: `public void OnSystemTouchMove(TouchControlPanel.SystemTouchEventData data) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=73 (informational only).

```csharp
public static ulong TouchControlPanel_OnSystemTouchMove_RVAc54a18(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12929832 = default(uint);
        uint __arm64_flags_left_12929872 = default(uint);
        uint __arm64_flags_left_12929912 = default(uint);
        uint __arm64_flags_left_12929948 = default(uint);
        uint __arm64_flags_result_12929948 = default(uint);
        uint __arm64_flags_right_12929832 = default(uint);
        uint __arm64_flags_right_12929872 = default(uint);
        uint __arm64_flags_right_12929912 = default(uint);
        uint __arm64_flags_right_12929948 = default(uint);
        ulong __arm64_pair_address_12929776 = default(ulong);
        ulong __arm64_pair_address_12929852 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v1 = default(RuntimeVector128);
        RuntimeVector128 v2 = default(RuntimeVector128);
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
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x26CUL))))))));
        x21 = x1;
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54A80;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x5A0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xDE0UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xD8UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x26CUL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC54A80;
        label_0xC54A80:
        ;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x19) + (0x20UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54C0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = 0x1A8C000UL;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0xD8UL))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        x0 = RuntimeMemory.ReadU64(x8);
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0xE0UL))))));
        if ((unchecked((uint)(x8)) != unchecked((uint)0x0UL)))
        {
            goto label_0xC54AA4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0xC54AA0UL);
        }
        x0 = RuntimeCalls.InvokeDirect(0xB7DA5CUL, x0, x1, x2, x3);
        goto label_0xC54AA4;
        label_0xC54AA4:
        ;
        x0 = x20;
        x1 = 0x0UL;
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x1794AC8UL /* metadata target: Object.op_Inequality */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54AC8;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x28UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC3BCB8UL /* metadata target: InputRig.WakeTouchControlsUp */, x0, x1, x2, x3);
        goto label_0xC54AC8;
        label_0xC54AC8:
        ;
        if ((x21 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x21) + (0x20UL))))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC54968UL /* metadata target: TouchControlPanel.FindTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC54C0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = x0;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        RuntimeMemory.WritePtr(unchecked((ulong)((x20) + (0x1CUL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x21) + (0x18UL))));
        __arm64_pair_address_12929776 = unchecked((ulong)((x21) + (0x10UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12929776)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12929776) + (0x4UL))))), 0));
        x0 = RuntimeCalls.InvokeDirect(0xC54C28UL /* metadata target: TouchObject.Move */, x0, x1, x2, x3);
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x38UL))))))));
        if ((unchecked((uint)(x9)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54B18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x40UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC54B18;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC54B24;
        label_0xC54B18:
        ;
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x30UL))));
        if ((x1 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x23 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC54B24;
        label_0xC54B24:
        ;
        x9 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x1) + (0x18UL))))));
        __arm64_flags_left_12929832 = unchecked((uint)(x9));
        __arm64_flags_right_12929832 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929832) - (__arm64_flags_right_12929832))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12929832)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12929832)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929832) - (__arm64_flags_right_12929832))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12929832)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54C0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x30UL))));
        __arm64_pair_address_12929852 = unchecked((ulong)((x8) + (0x20UL)));
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(__arm64_pair_address_12929852)), 0));
        v1 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF32(unchecked((ulong)((__arm64_pair_address_12929852) + (0x4UL))))), 0));
        v2 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)0x0UL)), 0)), 0));
        x3 = unchecked((ulong)(unchecked((uint)(0x8UL))));
        x4 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0xC536F8UL /* metadata target: TouchControl.HitPool.HitTest */, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        __arm64_flags_left_12929872 = unchecked((uint)(x0));
        __arm64_flags_right_12929872 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929872) - (__arm64_flags_right_12929872))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12929872)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12929872)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929872) - (__arm64_flags_right_12929872))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12929872)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54C0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x24 = 0x1A8C000UL;
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((x24) + (0xDD8UL))));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC54B6C;
        label_0xC54B6C:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x10UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12929912 = unchecked((uint)(x21));
        __arm64_flags_right_12929912 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929912) - (__arm64_flags_right_12929912))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12929912)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12929912)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12929912) - (__arm64_flags_right_12929912))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12929912)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54C0C;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x2 = RuntimeMemory.ReadU64(x24);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x22 == 0x0UL))
        {
            goto label_0xC54C08;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x22) + (0x50UL))))));
        __arm64_flags_left_12929948 = unchecked((uint)(x8));
        __arm64_flags_right_12929948 = unchecked((uint)0xFFFFFFBFUL);
        __arm64_flags_result_12929948 = unchecked((uint)((__arm64_flags_left_12929948) & (__arm64_flags_right_12929948)));
        if ((!((__arm64_flags_result_12929948 == unchecked((uint)0x0UL)))))
        {
            goto label_0xC54BFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        x8 = RuntimeMemory.ReadU64(x22);
        if ((unchecked((uint)(x23)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54BBC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x308UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x310UL))));
        goto label_0xC54BC4;
        label_0xC54BBC:
        ;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x318UL))));
        x2 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x320UL))));
        goto label_0xC54BC4;
        label_0xC54BC4:
        ;
        x0 = x22;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54BFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = RuntimeMemory.ReadU64(x22);
        x1 = RuntimeMemory.ReadU64(unchecked((ulong)((x20) + (0x10UL))));
        x3 = unchecked((ulong)(unchecked((uint)(0x2UL))));
        x0 = x22;
        x9 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2B8UL))));
        x4 = RuntimeMemory.ReadU64(unchecked((ulong)((x8) + (0x2C0UL))));
        x2 = 0x0UL;
        x0 = RuntimeCalls.InvokeIndirect(x9, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54BFC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x22) + (0x24UL))))))));
        if ((unchecked((uint)(x8)) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54C0C;
        }
        else
        {
            goto label_0xC54BFC;
        }
        label_0xC54BFC:
        ;
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x40UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        if ((x8 != 0x0UL))
        {
            goto label_0xC54B6C;
        }
        else
        {
            goto label_0xC54C08;
        }
        label_0xC54C08:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, x2, unchecked((ulong)(unchecked((uint)(x3)))));
        goto label_0xC54C0C;
        label_0xC54C0C:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x30UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x30UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x24 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x23 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return x0;
        return default(ulong);
    }
```

## `TouchControlPanel.UpdateTouchPressure` — RVA `0xc54df0`

- Lift status: **exact**; input span: 264 bytes; span to next metadata RVA: 264 bytes.
- Metadata signature: `private void UpdateTouchPressure() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static ulong TouchControlPanel_UpdateTouchPressure_RVAc54df0(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12930600 = default(uint);
        uint __arm64_flags_left_12930656 = default(uint);
        uint __arm64_flags_left_12930676 = default(uint);
        uint __arm64_flags_left_12930776 = default(uint);
        uint __arm64_flags_right_12930600 = default(uint);
        uint __arm64_flags_right_12930656 = default(uint);
        uint __arm64_flags_right_12930676 = default(uint);
        uint __arm64_flags_right_12930776 = default(uint);
        ulong __arm64_pair_address_12930576 = default(ulong);
        ulong __arm64_pair_address_12930580 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xA0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        x19 = x0;
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x0 = 0x0UL;
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x90UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_12930576 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12930576, v0);
#else
        __WriteVector128(__arm64_pair_address_12930576, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12930576) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12930576) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12930580 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12930580, v0);
#else
        __WriteVector128(__arm64_pair_address_12930580, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12930580) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12930580) + (0x10UL))), v0);
#endif
        x0 = RuntimeCalls.InvokeDirect(0x17C7C6CUL /* metadata target: Input.get_touchPressureSupported */, x0, x1, x2, x3);
        if ((unchecked((uint)((unchecked((uint)(x0))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54EE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7C44UL /* metadata target: Input.get_touchCount */, x0, x1, x2, x3);
        __arm64_flags_left_12930600 = unchecked((uint)(x0));
        __arm64_flags_right_12930600 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12930600) - (__arm64_flags_right_12930600))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12930600)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12930600)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12930600) - (__arm64_flags_right_12930600))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12930600)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54EE0;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC54E34;
        label_0xC54E34:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7540UL /* metadata target: Input.GetTouch */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = unchecked((ulong)((sp) + (0x8UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x44UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F60UL /* metadata target: Touch.get_phase */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12930656 = unchecked((uint)(x0));
        __arm64_flags_right_12930656 = unchecked((uint)0x4UL);
        if ((unchecked((uint)((__arm64_flags_left_12930656) - (__arm64_flags_right_12930656))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54ECC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F60UL /* metadata target: Touch.get_phase */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12930676 = unchecked((uint)(x0));
        __arm64_flags_right_12930676 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_12930676) - (__arm64_flags_right_12930676))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54ECC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F18UL /* metadata target: Touch.get_fingerId */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x1 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = x19;
        x0 = RuntimeCalls.InvokeDirect(0xC54968UL /* metadata target: TouchControlPanel.FindTouch */, x0, unchecked((ulong)(unchecked((uint)(x1)))), unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC54ECC;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F68UL /* metadata target: Touch.get_pressure */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F70UL /* metadata target: Touch.get_maximumPossiblePressure */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        if ((x21 == 0x0UL))
        {
            goto label_0xC54EF4;
        }
        else
        {
            return RuntimeCalls.InvokeDirect(0x0UL);
        }
        x0 = x21;
        v0 = v8;
        x0 = RuntimeCalls.InvokeDirect(0xC55004UL /* metadata target: TouchObject.SetPressure */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        goto label_0xC54ECC;
        label_0xC54ECC:
        ;
        x0 = 0x0UL;
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x17C7C44UL /* metadata target: Input.get_touchCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12930776 = unchecked((uint)(x20));
        __arm64_flags_right_12930776 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12930776) - (__arm64_flags_right_12930776))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12930776)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12930776)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12930776) - (__arm64_flags_right_12930776))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12930776)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54E34;
        }
        else
        {
            goto label_0xC54EE0;
        }
        label_0xC54EE0:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0xA0UL))))), 0));
        return x0;
        label_0xC54EF4:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        return default(ulong);
    }
```

## `TouchControlPanel.IsTouchPressureSensitive` — RVA `0xc54ef8`

- Lift status: **exact**; input span: 268 bytes; span to next metadata RVA: 268 bytes.
- Metadata signature: `private bool IsTouchPressureSensitive(int touchId, out float pressureOut) { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=33 (informational only).

```csharp
public static uint TouchControlPanel_IsTouchPressureSensitive_RVAc54ef8(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12930884 = default(uint);
        uint __arm64_flags_left_12930940 = default(uint);
        uint __arm64_flags_left_12930960 = default(uint);
        uint __arm64_flags_left_12930980 = default(uint);
        uint __arm64_flags_left_12931000 = default(uint);
        uint __arm64_flags_right_12930884 = default(uint);
        uint __arm64_flags_right_12930940 = default(uint);
        uint __arm64_flags_right_12930960 = default(uint);
        uint __arm64_flags_right_12930980 = default(uint);
        uint __arm64_flags_right_12931000 = default(uint);
        ulong __arm64_pair_address_12930848 = default(ulong);
        ulong __arm64_pair_address_12930852 = default(ulong);
        ulong sp = default(ulong);
        RuntimeVector128 v0 = default(RuntimeVector128);
        RuntimeVector128 v8 = default(RuntimeVector128);
        ulong x19 = default(ulong);
        ulong x20 = default(ulong);
        ulong x21 = default(ulong);
        ulong x30 = default(ulong);
        ulong x8 = default(ulong);
        sp = unchecked((ulong)((sp) - (0xD0UL)));
        RuntimeMemory.WriteF64(unchecked((ulong)((sp) + (0xA0UL))), global::System.BitConverter.Int64BitsToDouble(unchecked((long)(v8.GetUInt64(0)))));
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x0UL))), x30);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))), x21);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x0UL))), x20);
        RuntimeMemory.WriteU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))), x19);
        v0 = (RuntimeVector128.Zero.WithUInt64(0, 0x0UL) | RuntimeVector128.Zero.WithUInt64(0, 0x0UL).ShiftLeftLogical(unchecked((int)0x40UL)));
        x8 = unchecked((ulong)(unchecked((uint)(0x3F800000UL))));
        x0 = 0x0UL;
        x19 = x2;
        x20 = unchecked((ulong)(unchecked((uint)(x1))));
        RuntimeMemory.WritePtr(unchecked((ulong)((sp) + (0x90UL))), unchecked((ulong)(unchecked((uint)0x0UL))));
        __arm64_pair_address_12930848 = unchecked((ulong)((sp) + (0x70UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12930848, v0);
#else
        __WriteVector128(__arm64_pair_address_12930848, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12930848) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12930848) + (0x10UL))), v0);
#endif
        __arm64_pair_address_12930852 = unchecked((ulong)((sp) + (0x50UL)));
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(__arm64_pair_address_12930852, v0);
#else
        __WriteVector128(__arm64_pair_address_12930852, v0);
#endif
#if IL2CPPREC_RUNTIME_VECTOR128
        RuntimeMemory.WriteVector128(unchecked((ulong)((__arm64_pair_address_12930852) + (0x10UL))), v0);
#else
        __WriteVector128(unchecked((ulong)((__arm64_pair_address_12930852) + (0x10UL))), v0);
#endif
        RuntimeMemory.WriteU32(x2, unchecked((uint)(x8)));
        x0 = RuntimeCalls.InvokeDirect(0x17C7C6CUL /* metadata target: Input.get_touchPressureSupported */, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(x0))));
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54FC4;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7C44UL /* metadata target: Input.get_touchCount */, x0, x1, x2, x3);
        __arm64_flags_left_12930884 = unchecked((uint)(x0));
        __arm64_flags_right_12930884 = unchecked((uint)0x1UL);
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12930884) - (__arm64_flags_right_12930884))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12930884)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12930884)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12930884) - (__arm64_flags_right_12930884))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12930884)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54FC0;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC54F50;
        label_0xC54F50:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x21))));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C7540UL /* metadata target: Input.GetTouch */, unchecked((ulong)(unchecked((uint)(x0)))), x1, x2, x3);
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = unchecked((ulong)((sp) + (0x8UL)));
        x2 = unchecked((ulong)(unchecked((uint)(0x44UL))));
        x0 = RuntimeCalls.InvokeDirect(0x19B0C40UL, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F60UL /* metadata target: Touch.get_phase */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12930940 = unchecked((uint)(x0));
        __arm64_flags_right_12930940 = unchecked((uint)0x4UL);
        if ((unchecked((uint)((__arm64_flags_left_12930940) - (__arm64_flags_right_12930940))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54FAC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F60UL /* metadata target: Touch.get_phase */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12930960 = unchecked((uint)(x0));
        __arm64_flags_right_12930960 = unchecked((uint)0x3UL);
        if ((unchecked((uint)((__arm64_flags_left_12930960) - (__arm64_flags_right_12930960))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54FAC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F18UL /* metadata target: Touch.get_fingerId */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12930980 = unchecked((uint)(x0));
        __arm64_flags_right_12930980 = unchecked((uint)(x20));
        if ((unchecked((uint)((__arm64_flags_left_12930980) - (__arm64_flags_right_12930980))) == unchecked((uint)0x0UL)))
        {
            goto label_0xC54FD8;
        }
        else
        {
            goto label_0xC54FAC;
        }
        label_0xC54FAC:
        ;
        x0 = 0x0UL;
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x0 = RuntimeCalls.InvokeDirect(0x17C7C44UL /* metadata target: Input.get_touchCount */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        __arm64_flags_left_12931000 = unchecked((uint)(x21));
        __arm64_flags_right_12931000 = unchecked((uint)(x0));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12931000) - (__arm64_flags_right_12931000))))) < unchecked((int)0x0UL)) != (((unchecked((int)(__arm64_flags_left_12931000)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12931000)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12931000) - (__arm64_flags_right_12931000))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12931000)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC54F50;
        }
        else
        {
            goto label_0xC54FC0;
        }
        label_0xC54FC0:
        ;
        x0 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC54FC4;
        label_0xC54FC4:
        ;
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xC0UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xC0UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0xB0UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0xB0UL)))) + (0x8UL))));
        v8 = RuntimeVector128.Zero.WithUInt64(0, global::System.BitConverter.ToUInt64(global::System.BitConverter.GetBytes(RuntimeMemory.ReadF64(unchecked((ulong)((sp) + (0xA0UL))))), 0));
        return unchecked((uint)(x0));
        label_0xC54FD8:
        ;
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F68UL /* metadata target: Touch.get_pressure */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        x0 = unchecked((ulong)((sp) + (0x50UL)));
        x1 = 0x0UL;
        v8 = v0;
        x0 = RuntimeCalls.InvokeDirect(0x17C6F70UL /* metadata target: Touch.get_maximumPossiblePressure */, x0, x1, unchecked((ulong)(unchecked((uint)(x2)))), x3);
        v0 = RuntimeVector128.Zero.WithUInt32(0, global::System.BitConverter.ToUInt32(global::System.BitConverter.GetBytes(unchecked((float)((global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v8.GetUInt64(0)))), 0)) / (global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0))))), 0));
        RuntimeMemory.WriteF32(x19, global::System.BitConverter.ToSingle(global::System.BitConverter.GetBytes(unchecked((uint)(v0.GetUInt64(0)))), 0));
        x0 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        goto label_0xC54FC4;
        return default(uint);
    }
```

## `TouchControlPanel.GetActiveTouchCount` — RVA `0xc5511c`

- Lift status: **exact**; input span: 164 bytes; span to next metadata RVA: 164 bytes.
- Metadata signature: `public int GetActiveTouchCount() { }`
- Structural verifier: suspect=0, unverifiable=0, unmapped-instructions=25 (informational only).

```csharp
public static uint TouchControlPanel_GetActiveTouchCount_RVAc5511c(ulong x0, ulong x1, ulong x2, ulong x3, ulong x4, ulong x5, ulong x6, ulong x7)
    {
        uint __arm64_flags_left_12931444 = default(uint);
        uint __arm64_flags_right_12931444 = default(uint);
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
        x20 = 0x1BAB000UL;
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x20) + (0x271UL))))))));
        x19 = x0;
        if ((unchecked((uint)((unchecked((uint)(x8))) & (unchecked((uint)((unchecked((uint)0x1UL)) << (int)(unchecked((int)(unchecked((uint)(0x0UL)))))))))) != unchecked((uint)0x0UL)))
        {
            goto label_0xC55158;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE40UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x0 = 0x1A8C000UL;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0xE48UL))));
        x0 = RuntimeCalls.InvokeDirect(0xB7D92CUL, x0, x1, x2, x3);
        x8 = unchecked((ulong)(unchecked((uint)(0x1UL))));
        RuntimeMemory.WriteU8(unchecked((ulong)((x20) + (0x271UL))), unchecked((byte)(unchecked((uint)(x8)))));
        goto label_0xC55158;
        label_0xC55158:
        ;
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        if ((x0 == 0x0UL))
        {
            goto label_0xC551A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x22 = 0x1A8C000UL;
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((x22) + (0xE48UL))));
        x20 = unchecked((ulong)(unchecked((uint)0x0UL)));
        x21 = unchecked((ulong)(unchecked((uint)0x0UL)));
        goto label_0xC55170;
        label_0xC55170:
        ;
        x8 = unchecked((ulong)(RuntimeMemory.ReadU32(unchecked((ulong)((x0) + (0x18UL))))));
        __arm64_flags_left_12931444 = unchecked((uint)(x21));
        __arm64_flags_right_12931444 = unchecked((uint)(x8));
        if (((unchecked((int)(unchecked((uint)((__arm64_flags_left_12931444) - (__arm64_flags_right_12931444))))) < unchecked((int)0x0UL)) == (((unchecked((int)(__arm64_flags_left_12931444)) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_right_12931444)) < unchecked((int)0x0UL))) && ((unchecked((int)(unchecked((uint)((__arm64_flags_left_12931444) - (__arm64_flags_right_12931444))))) < unchecked((int)0x0UL)) != (unchecked((int)(__arm64_flags_left_12931444)) < unchecked((int)0x0UL))))))
        {
            goto label_0xC551AC;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x2 = RuntimeMemory.ReadU64(x22);
        x1 = unchecked((ulong)(unchecked((uint)(x21))));
        x0 = RuntimeCalls.InvokeDirect(0x10A30C0UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        if ((x0 == 0x0UL))
        {
            goto label_0xC551A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = RuntimeMemory.ReadU64(unchecked((ulong)((x0) + (0x10UL))));
        if ((x8 == 0x0UL))
        {
            goto label_0xC551A8;
        }
        else
        {
            return unchecked((uint)(RuntimeCalls.InvokeDirect(0x0UL)));
        }
        x8 = unchecked((ulong)(unchecked((uint)(RuntimeMemory.ReadU8(unchecked((ulong)((x8) + (0x10UL))))))));
        x0 = RuntimeMemory.ReadU64(unchecked((ulong)((x19) + (0x38UL))));
        x21 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x21))) + (unchecked((uint)(0x1UL)))))));
        x20 = unchecked((ulong)(unchecked((uint)((unchecked((uint)(x20))) + (unchecked((uint)(x8)))))));
        if ((x0 != 0x0UL))
        {
            goto label_0xC55170;
        }
        else
        {
            goto label_0xC551A8;
        }
        label_0xC551A8:
        ;
        x0 = RuntimeCalls.InvokeDirect(0xB7DB74UL, x0, unchecked((ulong)(unchecked((uint)(x1)))), x2, x3);
        goto label_0xC551AC;
        label_0xC551AC:
        ;
        x0 = unchecked((ulong)(unchecked((uint)(x20))));
        x20 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x20UL))));
        x19 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x20UL)))) + (0x8UL))));
        x22 = RuntimeMemory.ReadU64(unchecked((ulong)((sp) + (0x10UL))));
        x21 = RuntimeMemory.ReadU64(unchecked((ulong)((unchecked((ulong)((sp) + (0x10UL)))) + (0x8UL))));
        x30 = RuntimeMemory.ReadU64(sp);
        return unchecked((uint)(x0));
        return default(uint);
    }
```
